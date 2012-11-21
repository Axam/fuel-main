# -*- coding: utf-8 -*-

import uuid
import logging
import itertools

import web

from nailgun.settings import settings
from nailgun.api.models import Cluster
from nailgun.api.models import Task
from nailgun.task.errors import DeploymentAlreadyStarted, WrongNodeStatus

from nailgun.task import task as original_tasks
from nailgun.task import fake as fake_tasks
tasks = settings.FAKE_TASKS and fake_tasks or original_tasks

logger = logging.getLogger(__name__)


class TaskManager(object):

    def __init__(self, cluster_id):
        self.cluster = web.ctx.orm.query(Cluster).get(cluster_id)


class DeploymentTaskManager(TaskManager):

    def execute(self):
        current_tasks = web.ctx.orm.query(Task).filter(
            Task.cluster == self.cluster,
            Task.name == "deploy"
        )
        for task in current_tasks:
            if task.status == "running":
                raise DeploymentAlreadyStarted()
            elif task.status in ("ready", "error"):
                for subtask in task.subtasks:
                    web.ctx.orm.delete(subtask)
                web.ctx.orm.delete(task)
                web.ctx.orm.commit()
        nodes_to_delete = filter(lambda n: n.pending_deletion,
                                 self.cluster.nodes)
        nodes_to_deploy = filter(lambda n: n.pending_addition,
                                 self.cluster.nodes)
        if not nodes_to_deploy and not nodes_to_delete:
            raise WrongNodeStatus("No changes to deploy")
        supertask = Task(
            name="deploy",
            cluster=self.cluster
        )
        web.ctx.orm.add(supertask)
        web.ctx.orm.commit()
        if nodes_to_delete:
            supertask.create_subtask("deletion")
        if nodes_to_deploy:
            supertask.create_subtask("deployment")
        for subtask in supertask.subtasks:
            subtask.execute({
                'deletion': tasks.DeletionTask,
                'deployment': tasks.DeploymentTask,
            }[subtask.name])
        return supertask


class VerifyNetworksTaskManager(TaskManager):

    def execute(self):
        task = Task(
            name="verify_networks",
            cluster=self.cluster
        )
        web.ctx.orm.add(task)
        web.ctx.orm.commit()
        task.execute(tasks.VerifyNetworksTask)
        return task

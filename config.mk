
BINARIES_DIR:=binaries
ifndef BOOTSTRAP_REBUILD
BOOTSTRAP_REDUILD:=0
endif

iso.path:=$(BUILD_DIR)/iso/nailgun-ubuntu-12.04-amd64.iso
image.centos.url=http://mc0n1-srt.srt.mirantis.net/centos63.qcow2

centos.packages=$(BUILD_DIR)/packages/centos
ubuntu.packages=$(BUILD_DIR)/packages/ubuntu

bootstrap.linux:=$(BUILD_DIR)/bootstrap/linux
bootstrap.initrd:=$(BUILD_DIR)/bootstrap/initrd.gz


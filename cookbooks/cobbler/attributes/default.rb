default_conf = Cobbler.default_conf(node)

default["cobbler"]["next_server"] = default_conf[:next_server]
default["cobbler"]["server"] = default_conf[:server]
default["cobbler"]["dhcp_range"] = default_conf[:dhcp_range]
default["cobbler"]["gateway"] = default_conf[:gateway]
default["cobbler"]["pxetimeout"] = "20" #10=1sec
default["cobbler"]["repoaddr"] = default_conf[:server]

default["cobbler"]["user"] = "cobbler"
default["cobbler"]["password"] = "cobbler"

default["cobbler"]["ks_mirror_dir"] = "/var/www/cobbler/ks_mirror" 
default["cobbler"]["preseed_dir"] = "/var/lib/cobbler/kickstarts"

default["cobbler"]["bootstrap_mnt"] = "/var/lib/mirror/bootstrap"

default["cobbler"]["precise-x86_64_iso"] = "/var/lib/mirror/netinst/precise-x86_64.iso"
default["cobbler"]["precise-x86_64_mnt"] = "/var/lib/mirror/netinst/precise-x86_64"

default["cobbler"]["centos-6.3-x86_64_iso"] = "/var/lib/mirror/netinst/CentOS-6.3-x86_64-netinstall.iso"
default["cobbler"]["centos-6.3-x86_64_mnt"] = "/var/lib/mirror/netinst/centos-6.3-x86_64"

 

"""pbench sysinfo commands"""
from pbench.agent.wrappers import base


class CollectSysinfo(base.BaseCommand):
    """pbench-collect-sysinfo"""

    def run(self):
        pass


class RemoteSysinfoDump(base.BaseCommand):
    """pbench-remote-sysinfo-dump"""

    def run(self):
        pass


class SysinfoDump(base.BaseCommand):
    """pbench-sysinfo-dump"""

    def run(self):
        pass

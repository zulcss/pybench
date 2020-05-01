"""pbench metric wrappers"""
from pbench.agent.wrappers import base


class MetricsIteration(base.BaseCommand):
    """pbench-get-iteration-metrics"""

    def run(self):
        pass


class MetricsData(base.BaseCommand):
    """pbench-get-metric-data"""

    def run(self):
        pass


class MetricsPrimary(base.BaseCommand):
    """pbench-get-primary-metric"""

    def run(self):
        pass

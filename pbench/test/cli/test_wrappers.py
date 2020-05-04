import pytest

from pbench.test.conftest import capture


PBENCH_WRAPPER = [
    "pbench-output-monitor",
    "pbench-postprocess-tools-cdm",
    "pbench-register-tool",
    "pbench-register-tool-set",
    "pbench-register-tool-trigger",
    "pbench-remote-sysinfo-dump",
    "pbench-sysinfo-dump",
    "pbench-test",
    "pbench-tool-data-sink",
    "pbench-tool-trigger",
    "cdm-get-iterations",
    "pbench-add-metalog-option",
    "pbench-agent-config-activate",
    "pbench-agent-config-ssh-key",
    "pbench-avg-stddev",
    "pbench-cleanup",
    "pbench-clear-tools",
    "pbench-collect-sysinfo",
    "pbench-copy-result-tb",
    "pbench-get-iteration-metrics",
    "pbench-get-metric-data",
    "pbench-get-primary-metric",
    "pbench-import-cdm",
    "pbench-list-tools",
    "pbench-list-triggers",
    "pbench-log-timestamp",
    "pbench-make-result-tb",
    "pbench-metadata-log",
    "pbench-move-results",
    "pbench-kill-tools",
    "pbench-start-tools",
    "pbench-stop-tools",
]


@pytest.mark.parametrize("cmd", PBENCH_WRAPPER)
def test_pbench_wrapper(cmd):
    command = [cmd, "--help"]
    out, err, exitcode = capture(command)
    assert b"help" in out
    assert b"" in err
    assert exitcode == 0

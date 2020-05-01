import os
import sys

import logging

import colorlog

LOG = logging.getLogger(os.path.basename(sys.argv[0]))
fh = logging.FileHandler("{}.log".format("pbench-agent"))
if os.environ.get("_PBENCH_BENCH_TESTS"):
    fmtstr = "%(levelname)s %(name)s %(funcName)s -- %(message)s"
else:
    fmtstr = (
        "%(asctime)s %(levelname)s %(process)s %(thread)s"
        " %(name)s %(funcName)s %(lineno)d -- %(message)s"
    )
fhf = logging.Formatter(fmtstr)
fh.setFormatter(fhf)
fh.setLevel(logging.INFO)
LOG.addHandler(fh)
LOG.setLevel(logging.INFO)

logger_formatter = colorlog.ColoredFormatter(
    "%(log_color)s %(levelname)s %(process)s %(thread)s"
    " %(name)s %(funcName)s %(lineno)d -- %(message)s",
    log_colors=dict(
        DEBUG="blue",
        INFO="green",
        WARNING="yellow",
        ERROR="red",
        CRITICAL="bold_red,bg_white",
    ),
)
# Create stream handler with debug level

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

# Add the logger_formatter to sh
sh.setFormatter(logger_formatter)

# Create logger and add handler to it
LOG.addHandler(sh)

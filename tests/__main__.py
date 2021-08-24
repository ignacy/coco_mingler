# pylint: skip-file

import os
import sys
from subprocess import check_call

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

os.putenv(
    "PATH", ":".join([os.path.join(REPO_ROOT, "bin"), os.getenv("PATH")])
)
os.putenv("COCO_MINGLER_HOME", REPO_ROOT)

opts = "-v --durations=0"
params = " ".join(sys.argv[1:])
cmd = f"{sys.executable} -m pytest {opts} {params}"
check_call(cmd, shell=True)

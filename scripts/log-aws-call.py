#!/usr/bin/env python3
"""PostToolUse hook — logs AWS CLI calls to logs/activity.log."""
import json
import sys
import os
from datetime import datetime

try:
    data = json.load(sys.stdin)
    cmd = data.get("tool_input", {}).get("command", "")
    if "aws " not in cmd:
        sys.exit(0)

    project_dir = data.get("cwd", os.getcwd())
    log_path = os.path.join(project_dir, "logs", "activity.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] {cmd[:300]}\n")

except Exception:
    pass

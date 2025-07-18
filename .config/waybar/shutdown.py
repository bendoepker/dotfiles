#! /usr/bin/env python3

import subprocess
import json
import os
from datetime import datetime


# NOTE: This command cannot fail, if it does, then you can just force shutdown anyways
workspaces_json_str = subprocess.run(["hyprctl", "workspaces", "-j"],
                                     capture_output=True, text=True)
workspaces_json = json.loads(workspaces_json_str.stdout)
windows = 0
for item in workspaces_json:
    for key, value in item.items():
        if key == "windows":
            windows += value


f = open("/home/ben/.config/waybar/poweroff.logs", "a")

# Base case, no windows are open
if windows == 0:
    os.system("systemctl poweroff")

else:
    f.write(f"Pressed at {datetime.now()} but could not power off because there are {windows} windows open.\n")
    # TODO: Create a popup allowing a user to close all windows peacefully or cancel

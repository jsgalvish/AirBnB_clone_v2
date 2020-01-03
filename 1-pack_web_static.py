#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder

from fabric.api import run, local, sudo
from datetime import datetime


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    local('mkdir -p versions')
    command = local("tar -cvzf " + file_name + " ./web_static/")
    if command.succeeded:
        return file_name
    return None

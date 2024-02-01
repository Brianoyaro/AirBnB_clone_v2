#!/usr/bin/python3
""" generates a .tgz archive from the contents of web_static"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """creates a tar file"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        time = time.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(time)
        local("tar -czvf {} web_static/".format(filename))
        return filename
    except:
        return None

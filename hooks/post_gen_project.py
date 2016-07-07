# -*- coding: utf-8 -*-
"""
Does the following:
    1. Remove docker files if docker won't be used.
"""
# System imports
import os
import shutil

# Third-party imports
from cookiecutter.main import cookiecutter


# Root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_docker_files(project_directory):
    """ Removes the files if docker isn't going to be used """
    docker_folder_location = os.path.join(
        project_directory,
        'docker'
    )
    shutil.rmtree(docker_folder_location)
    docker_compose_file_location = os.path.join(
        project_directory,
        'docker-compose.yml'
    )
    os.remove(docker_compose_file_location)
    docker_settings_file_location = os.path.join(
        project_directory,
        '{{ cookiecutter.project_slug }}/settings/docker.py'
    )
    os.remove(docker_settings_file_location)



# 1. Remove docker files
if '{{ cookiecutter.use_docker }}'.lower() == 'n':
    remove_docker_files(PROJECT_DIRECTORY)

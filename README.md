# Dockerfiles

This repository is the basis for my personal usage for Docker.  This repository 
includes a custom Docker image ([mergepdfs](images/mergepdfs)) and a few command
line [scripts](scripts) utilizing either my custom docker images or images that
exist already online.

## Installation

Docker is required to utilize the images in this repository.  Python is required
to utilize the command line scripts.  However, the scripts run utilizing only
the python standard library - no external dependencies/virtual environments are
required.

## Purpose

The purpose of this repository is to simplify the dependency management process
for a few command-line processes.  Because Docker runs all commands in a Virtual
Machine (including dependency installation) a user's machine is kept free from
excess dependencies.  Furthermore, dependency management is handled as part of
the commands, and cached for speed in future builds.

## Downsides

Utilizing Docker for this process has two downsides.
1.  Access to the internet is required for the initial run of the command.  To
    pull the required Docker image from Docker Hub, access to the internet is
    required.
2.  As a virtual machine must be run for each script, these commands are slower
    than they would be normally.

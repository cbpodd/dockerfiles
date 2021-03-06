#!/usr/bin/env python3

import os
import sys
from string import Template

IMAGE = 'cbpodd/ubuntu:20.04'
CC = 'zsh'

def main():
    commandArray = list()
    commandArray.append("docker run --rm -it") # Command and some parameters
    # commandArray.append("--net=none") # More parameters
    pwdTemplate = Template('-v $PWD:/root/repos') # Present working directory
    commandArray.append(pwdTemplate.substitute(PWD=getpwd()))
    commandArray.append(IMAGE) # Pull the requested docker image

    commandArray.append(CC) # Pass in chosen latex compiler
    commandArray.extend(sys.argv[1:]) # command line arguments passed into compiler

    # Run the command
    return os.system(' '.join(commandArray))

def getpwd():
    cwd = os.getcwd()
    if sys.platform.startswith('win32'):
        cwdArray = cwd.split('\\')
        outArray = ['/']
        driveLetter = cwdArray[0][0].lower()
        outArray.append(driveLetter)
        outArray.extend(cwdArray[1:])
        return '/'.join(outArray)
    return cwd

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

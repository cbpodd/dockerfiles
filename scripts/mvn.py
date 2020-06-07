#!/usr/bin/env python3

import os
import sys
from string import Template

IMAGE = 'maven:3.3-jdk-8'
CC = 'mvn'

def main():
    commandArray = list()
    commandArray.append("docker run --rm -i") # Command and some parameters
    # commandArray.append("--net=none") # More parameters
    pwdTemplate = Template('-v $PWD:/usr/repos/maven') # Present working directory
    commandArray.append(pwdTemplate.substitute(PWD=os.getcwd()))
    commandArray.append('-w /usr/repos/maven') # Present working directory
    commandArray.append(IMAGE) # Pull the requested docker image

    commandArray.append(CC) # Pass in chosen latex compiler
    commandArray.extend(sys.argv[1:]) # command line arguments passed into compiler

    # Run the command
    return os.system(' '.join(commandArray))

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

# Images

This folder holds various custom Docker images I have created to serve specific
purposes not available (to my knowledge) in the standard Docker library.

## [MergePDFs](./mergepdfs)

This image contains a python script for merging the pages of any number of PDFs
into one PDF.  It encapsulates the python pip dependency installation process,
as well as the script required to run the program.  It is available on my 
[Docker Hub](https://hub.docker.com) as image
[mergepdfs](https://hub.docker.com/r/cbpodd/mergepdfs).

TODO: See its [companion script](../scripts/mergepdfs.py) for usage of this 
image as a python command-line script.

## [PostgresQL](postgresql)

This image is a slight modification of the PostgresQL standard Docker image.  My
image allows for default user and password input, so that a user can enter a VM 
with postgresql installed and running.  

TODO: It is available on my [Docker Hub](https://docker.io) as image
[postgres](https://docker.io).

TODO:  See its [companion script](../scripts/postgres.py) for the usage of this
image as a python command-line script.

# Images

This folder holds various custom Docker images I have created to serve specific
purposes not available (to my knowledge) in the standard Docker library.

## [MergePDFs](./mergepdfs)

This image contains a python script for merging the pages of any number of PDFs
into one PDF.  It encapsulates the python pip dependency installation process,
as well as the script required to run the program.  It is available on my 
[Docker Hub](https://hub.docker.com) as image
[mergepdfs](https://hub.docker.com/r/cbpodd/mergepdfs).

See its [companion script](../scripts/mergepdfs.py) for usage of this 
image as a python command-line script.

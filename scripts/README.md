# Scripts

This folder contains various scripts I use to either replace existing
commands/command sets or to make my own command line tools.  The goal of using
these is to simplify the dependency process.  Each command is built in python,
using only the python 3 standard library - therefore, it requires python to run.
Each command also requires Docker to run, as the dependency management system is
run in a docker container.

## PdfLatex

This is a python script that compiles latex into a PDF.  The script is built off 
of the `blang/latex:ubuntu` Docker image, as well as the `pdflatex` compiler
It replaces pdflatex, except that you don't need latex installed (only Docker).

## Maven

This is a script to run maven in a docker container (`mvn.py`).
However, this script is just a starting point for running one-off maven
commands.  This is an in-progress project, and I have not tested running
commands including servers or networking - only one-off commands like compile,
test, package, etc.

## MergePDFs

This is a script to merge multiple PDFs into one PDF.  This script is built off
my `cbpodd/mergepdfs` Docker image, which installs the required dependency
(`pdfrw`) and runs a script to merge multiple pdfs into one.

Usage:
```
mergepdfs <pdf1> <pdf2> ... <pdfn> -o <outpdf>
```

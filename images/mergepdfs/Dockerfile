FROM python:3

WORKDIR /usr/repos/setup

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY mergepdfs.py /bin/mergepdfs

WORKDIR /usr/repos/python

# CMD [ "python3", "./mergepdfs.py" ]

FROM ubuntu:20.04

ENV TERM xterm-256color
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    gdb \
    git \
    python \
    ubuntu-server \
    sudo \
    zsh

RUN chsh -s /bin/zsh

WORKDIR /usr
RUN git clone https://github.com/cbpodd/dotfiles --recursive

WORKDIR /usr/dotfiles
RUN ./install.py

RUN vim +PluginInstall +qall

WORKDIR /root/repos

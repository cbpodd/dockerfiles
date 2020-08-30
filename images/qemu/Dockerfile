FROM cbpodd/ubuntu:20.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    binutils \
    build-essential \
    gcc-multilib \
    libsdl1.2-dev \
    libtool

WORKDIR /root/tmp

RUN git clone https://github.com/geofft/qemu.git -b 6.828-1.7.0

WORKDIR /root/tmp/qemu

RUN git submodule update --init pixman
RUN ./configure --disable-kvm --disable-werror --target-list="i386-softmmu x86_64-softmmu"
RUN make && make install

WORKDIR /root/repos/qemu

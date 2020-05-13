FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8

ENV HOME /root
ENV DEPLOY_DIR ${HOME}/mysite

RUN apt update

# Set locale
# https://stackoverflow.com/a/28406007
RUN apt install -y locales
RUN sed -i -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen \
    && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Python 3.7
RUN apt install -y wget \
    build-essential \
    zlib1g-dev \
    # https://stackoverflow.com/a/43923402
    libssl-dev \
    # https://stackoverflow.com/a/29862854
    libsqlite3-dev \
    libffi-dev
WORKDIR ${HOME}
RUN wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz \
    && tar zxf Python-3.7.1.tgz \
    && cd Python-3.7.1 \
    && ./configure --enable-optimizations \
    && make altinstall

# Set alias
RUN update-alternatives --install /usr/local/bin/python3 python3 /usr/local/bin/python3.7 1
RUN update-alternatives --install /usr/local/bin/pip3 pip3 /usr/local/bin/pip3.7 1
RUN pip3 install -U pip

WORKDIR ${DEPLOY_DIR}

CMD ["/bin/bash"]

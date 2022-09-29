FROM python:slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils build-essential \
    && apt-get upgrade -y --no-install-recommends

# Get gRPC repo
RUN apt-get install -y --no-install-recommends git
RUN git -c advice.detachedHead=false clone -b v1.46.0 https://github.com/grpc/grpc grpc.git
RUN cd grpc.git && git submodule update --init

# Get Bazel build tool, use bazelisk to enable build on arm64
RUN apt-get install -y --no-install-recommends curl gnupg unzip
RUN curl -sL https://deb.nodesource.com/setup_16.x  | bash -
RUN apt-get -y install nodejs && \
    npm install -g @bazel/bazelisk

# Build plugin binary for Python gRPC
RUN cd grpc.git \
    && CC=gcc bazel build //src/compiler:grpc_python_plugin \
    && cp /grpc.git/bazel-bin/src/compiler/grpc_python_plugin /bin/protoc-gen-python_grpc

# Set up container's user (override UID and GID for your host user)
ARG UNAME=iotics
ARG UID=1000
ARG GID=1000
RUN useradd -lm -u $UID -g $GID -s /bin/bash $UNAME

# Set up Golang
ENV GOROOT=/usr/local/go
COPY --from=golang:bullseye "$GOROOT" "$GOROOT"
ENV PATH="$PATH:$GOROOT/bin"
ENV GOPATH="/home/$UNAME/go"
ENV GOBIN="$GOPATH/bin"
ENV PATH="$PATH:$GOBIN"
RUN install -o $UID -g $GID -d "$GOPATH" "$GOBIN"

# Copy necessary project files to satisfy dependencies for the future runs in a container
ARG REPO_PATH=/iotics-grpc-client-py
ENV VENV_PATH=/docker-venv
RUN install -o $UID -g $GID -d "$REPO_PATH" "$REPO_PATH/src" "$VENV_PATH"
WORKDIR "$REPO_PATH"
COPY --chown=$UID:$GID iotics-api.git "$REPO_PATH/iotics-api.git"
COPY --chown=$UID:$GID \
  Makefile \
  buf.lock \
  buf.yaml \
  setup.cfg \
  setup.py \
  "$REPO_PATH"/

# Prepopulate dependencies
USER $UNAME
RUN make deps-py deps-go buf-list buf-lint
CMD ["make", "generate"]

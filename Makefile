SHELL := /bin/bash
BUF_VERSION ?= 1.6.0
PROTOC_VERSION ?= 21.2
VENV_PATH ?= ./env

GOBIN := $(shell go env GOPATH)/bin
BUF := $(GOBIN)/buf
PROTOC := $(GOBIN)/protoc
UNAME_S := $(shell uname -s)
UNAME_M := $(shell uname -m)
ifeq ($(UNAME_S), Darwin)
  PROTOC_ARCHIVE="protoc-$(PROTOC_VERSION)-osx-x86_64.zip"
else
  PROTOC_ARCHIVE="protoc-$(PROTOC_VERSION)-$(UNAME_S)-$(UNAME_M).zip"
endif
BUF_URL := "https://github.com/bufbuild/buf/releases/download/v$(BUF_VERSION)/buf-$(UNAME_S)-$(UNAME_M)"
PROTOC_URL := "https://github.com/protocolbuffers/protobuf/releases/download/v$(PROTOC_VERSION)/$(PROTOC_ARCHIVE)"

ifndef GIT_TAG
  GIT_TAG := main
else
  GIT_TAG ?= "tags/$(GIT_TAG)"
endif
GEN_FILES_DIR := src/iotics/api


########################
## High level targets ##
########################

build: deps-proto deps-docker
	docker run --rm -v ${PWD}:/iotics-grpc-client-py iotics-grpc-client-py-builder

clean:
	git clean -f -dX "$(VENV_PATH)" src/iotics_grpc_client.egg-info

buf-lint: deps-buf
	$(BUF) lint

buf-list:
	$(BUF) ls-files

generate: deps-proto deps-py deps-go buf-list buf-lint
	source "$(VENV_PATH)"/bin/activate \
	&& $(BUF) generate $(GEN_ARGS)

docker-shell:
	docker run --rm -it -v ${PWD}:/iotics-grpc-client-py iotics-grpc-client-py-builder /bin/bash


#######################
## Low level targets ##
#######################

deps-docker:
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -t iotics-grpc-client-py-builder .

deps-proto: iotics-api.git/.git
iotics-api.git/.git:
	git submodule update --init --recursive

deps-proto-update:
	cd iotics-api.git \
	&& git fetch --tags \
	&& git checkout "$(GIT_TAG)"

deps-go: $(BUF) $(PROTOC)
deps-go-update: deps-go-buf deps-go-protoc
deps-go-buf $(BUF):
ifneq ("$(shell ! test -e $(BUF) || $(BUF) --version 2>&1)", "$(BUF_VERSION)")
	curl -sSL $(BUF_URL) -o $(BUF) \
	&& chmod +x $(BUF)
endif
deps-go-protoc $(PROTOC):
ifneq ("$(shell ! test -e $(PROTOC) || $(PROTOC) --version 2>&1)", "libprotoc $(PROTOC_VERSION)")
	curl -sSLO $(PROTOC_URL) \
	&& unzip -p $(PROTOC_ARCHIVE) bin/protoc > $(PROTOC) \
	&& chmod +x $(PROTOC) \
	&& rm $(PROTOC_ARCHIVE)
endif

deps-buf: buf.lock
deps-buf-update buf.lock:
	$(BUF) mod update

deps-py: $(VENV_PATH)/bin
$(VENV_PATH)/bin:
	python3 -m venv "$(VENV_PATH)"
	source "$(VENV_PATH)"/bin/activate \
	&& pip install -U pip setuptools \
	&& pip install -e '.[dev]'
deps-py-update: clean deps-py


################
## CI helpers ##
################

verify-import: deps-py
	source "$(VENV_PATH)"/bin/activate \
	&& python -c 'from iotics.lib.grpc import IoticsApi'

run-examples: deps-py
	source "$(VENV_PATH)"/bin/activate \
	&& python examples/search_twin_models.py \
	&& python examples/search_location.py \
	&& python examples/sparql.py \
	&& python examples/create_edit_twins_feeds.py \
	&& python examples/follow_feed.py

SHELL := /bin/bash
BUF_VERSION := 0.52.0
PROTOC_VERSION := 3.17.3

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

build: deps-proto deps-go deps-buf deps-py buf-list buf-lint generate

clean:
	rm -rf env src/iotics_grpc_client.egg-info

buf-lint:
	$(BUF) lint

buf-list:
	$(BUF) ls-files

generate:
	source env/bin/activate \
	&& rm -rf $(GEN_FILES_DIR) \
	&& $(BUF) generate $(GEN_ARGS) \
	&& find $(GEN_FILES_DIR) -name \*_pb2_grpc.pyi -exec bash -c 'mv "$$0" "$${0/_pb2/}"' {} \;

update-iotics-api: deps-proto-update generate


#######################
## Low level targets ##
#######################

deps-proto:
	git submodule update --init --recursive

deps-proto-update:
	cd iotics-api.git \
	&& git fetch --tags \
	&& git checkout "$(GIT_TAG)"

deps-go: $(BUF) $(PROTOC)
$(BUF):
	curl -sSL $(BUF_URL) -o $(BUF) \
	&& chmod +x $(BUF)
$(PROTOC):
	curl -OL  $(PROTOC_URL) \
	&& unzip -p $(PROTOC_ARCHIVE) bin/protoc > $(PROTOC) \
	&& chmod +x $(PROTOC) \
	&& rm $(PROTOC_ARCHIVE)

deps-go-update:
ifneq ("$(shell ! test -e $(BUF) || $(BUF) --version 2>&1)", "$(BUF_VERSION)")
	curl -sSL $(BUF_URL) -o $(BUF) \
	&& chmod +x $(BUF)
endif
ifneq ("$(shell ! test -e $(PROTOC) || $(PROTOC) --version 2>&1)", "libprotoc $(PROTOC_VERSION)")
	curl -OL  $(PROTOC_URL) \
	&& unzip -p $(PROTOC_ARCHIVE) bin/protoc > $(PROTOC) \
	&& chmod +x $(PROTOC) \
	&& rm $(PROTOC_ARCHIVE)
endif

deps-buf: buf.lock
deps-buf-update buf.lock:
	$(BUF) mod update

deps-py: env
deps-py-update env:
	python3 -m venv env
	source env/bin/activate \
	&& pip install -U pip setuptools \
	&& pip install -e '.[dev]'

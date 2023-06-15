# Iotics gRPC Python Client
A Python library for interacting with Iotics API.


## Usage and Version Compatibility with Iotics host:

| iotics-grpc-client-py | iotics-host |
|----------------------| ----------- |
|      `pip install iotics-grpc-client~=4.0`       | `>= 6`       |
|      `pip install iotics-grpc-client~=3.0`       | `>= 6`       |
|      `pip install iotics-grpc-client~=2.0`       | `>= 5`       |
|      `pip install iotics-grpc-client~=0.10.0`      | `>= 4`     |



# Examples
## Configuring identity
To run examples, either set up required environment variables or create an `.env` file with the following values. For
more information on the meaning of these values and how to create them, consult https://docs.iotics.com/docs/identity-api-and-credentials
* __Required__:
  * `SPACE` - Domain name of the IOTICSpace with which to communicate. The scheme can be omitted, eg. examplecorp.
    iotics.space
  * `USER_DID` - Identity of the user
  * `AGENT_DID` - Identity of the agent authorised to operate on the user's behalf
  * `AGENT_KEY_NAME` - __secret__ value used to (re)create multiple key pairs
  * `AGENT_NAME` - registered identity name that can be used to e.g. identify public keys
  * `AGENT_SECRET` - __secret__ value, the agent's private key

* __Optional__:
  * `DID_RESOLVER_URL` - Where the database of identity documents is accessible, defaults to the one used by the given 
    space.
  * `TOKEN_TTL` - How long in seconds auth tokens will last if not specified in the method call, defaults to 30
## Running example scripts
Next, create and activate your virtual environment and run any of the scripts in the [examples](https://github.com/Iotic-Labs/iotics-grpc-client-py/tree/main/examples) directory, 
e.g.:
```bash
make deps-py
. env/bin/activate
python examples/search_twin_models.py
```


# FAQs

## Installing on Raspberry PI get: Import error GLIBC_2.33 not found

If you see this error running the exmaples on a Rapberry PI, the current workaround is to install Ubuntu for RPi which has a later version of glibc.

```bash
ImportError: /lib/arm-linux-gnueabihf/libc.so.6: version 'GLIBC_2.33' not found (required by /home/pi/work/starting/iotics-grpc-client-py/env/lib/python3.9/site-packages/grpc/_cython/cygrpc.cpython-39-arm-linux-gnueabihf.so)
```



# Contributing


## Installing dependencies and generating gRPC client
* To satisfy all dependencies, lint proto files and regenerate client files (inside a Docker container):
  ```shell
  make build
  ```
  * To generate gRPC Python files outside a Docker container the following command can be used: `make generate`.
    Currently, there is no official binary for Python gRPC plugin, but there is one built from the official repository
    inside the docker (the following will work on Linux machines):
    ```bash
    docker run --rm -dit --name iotics-grpc-client-py-builder iotics-grpc-client-py-builder /bin/bash
    docker cp iotics-grpc-client-py-builder:/bin/protoc-gen-python_grpc env/bin/protoc-gen-python_grpc
    docker stop iotics-grpc-client-py-builder
    make generate
    ```
* To update the Iotics API version and regenerate client  
  (proto files are submoduled in [./iotics-api.git/](./iotics-api.git)
  from [Iotics API](https://github.com/Iotic-Labs/api) repo):
  ```bash
  _ver=vX.X.X
  make GIT_TAG=$_ver deps-proto-update build
  # Address usages of the new client in `src`, update "Unreleased" section in CHANGELOG.md, then:
  git add CHANGELOG.md iotics-api.git src
  git commit -m "Update Iotics API to $_ver"
  # Push your branch and create a PR
  ```
* Other `make` commands:
  * `clean` - remove artifacts created inside the project.
  * `deps-*` - install specific requirements if missing.
  * `deps-*-update` - update specific requirements when applicable.


## PRs
Should contain a summary of the changes in [CHANGELOG.md](https://github.com/Iotic-Labs/iotics-grpc-client-py/blob/main/CHANGELOG.md) under the "Unreleased" section.


## Versioning

This package adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)


## Releasing
* Update package version in [setup.py](./setup.py) for the release:
* Update [CHANGELOG.md](https://github.com/Iotic-Labs/iotics-grpc-client-py/blob/main/CHANGELOG.md) (move notes from unreleased section, ensure right tags are used, etc.)
  and any other files as needed.
* Commit changes and create a [PR](https://github.com/Iotic-Labs/iotics-grpc-client-py/compare).
* Once PR is merged manually run the [Create Draft Release GitHub Action](https://github.com/Iotic-Labs/iotics-grpc-client-py/actions/workflows/draft_release.yml), this will create a tag with the version in setup.py and create a draft release in [releases](https://github.com/Iotic-Labs/iotics-grpc-client-py/releases).
* Update the release's information and press the publish button on the release to publish it.
* The [Publish GitHub Action](https://github.com/Iotic-Labs/iotics-grpc-client-ts/actions/workflows/publish.yml)
  will create a package and will publish it to [PyPI](https://pypi.org/project/iotics-grpc-client).


# License

Copyright © 2022 IOTIC LABS LTD. info@iotics.com. All rights reserved. Licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/Iotic-Labs/iotics-grpc-client-py/tree/main/LICENSE) in the project root for license information.


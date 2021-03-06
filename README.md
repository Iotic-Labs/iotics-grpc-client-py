# Iotics gRPC Python Client
![GHA check workflow](https://github.com/Iotic-Labs/iotics-grpc-client-py/actions/workflows/check.yml/badge.svg)

A Python library for interacting with Iotics API.


## Usage
```shell
pip install iotics-grpc-client
```


# Examples
## Configuring identity
To run examples, either set up required environment variables or create an `.env` file with the following values. For
more information on the meaning of these values and how to create them, consult https://docs.iotics.com/docs/identity-advanced
* __Required__:
  * `SPACE` - Domain name of the IOTICSpace with which to communicate. The scheme can be omitted, eg. examplecorp.
    iotics.space
  * `USER_SEED` - __secret__ value used to (re)create user public and private keys.
  * `AGENT_SEED` - __secret__ value used to (re)create agent public and private keys.

* __Optional__:
  * `DID_RESOLVER_URL` - Where the database of identity documents is accesible, defaults to the one used by the given 
    space.
  * `USER_KEY_NAME` - __secret__ value used to (re)create multiple key pairs, defaults to empty.
  * `USER_NAME` - used to create/identify public keys, defaults to `#user-0`.
  * `AGENT_KEY_NAME` - __secret__ value used to (re)create multiple key pairs, defaults to empty.
  * `AGENT_NAME` - registered identity name that can be used to e.g. identify public keys, defaults to 
   `#agent-0`.

## Running example scripts
Next, create and activate your virtual environment and run any of the scripts in the [examples](./examples) directory, 
e.g.:
```bash
make deps-py
. env/bin/activate
python examples/search_twin_models.py
```


## Contributing


### Installing dependencies and generating gRPC client
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


### PRs
Should contain a summary of the changes in [CHANGELOG.md](./CHANGELOG.md) under the "Unreleased" section.

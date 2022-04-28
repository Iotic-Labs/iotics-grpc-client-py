# Iotics gRPC Python Client
A Python library for interacting with Iotics API.


## Usage
```shell
pip install iotics-grpc-client
```


# Examples
* [ts-node](./examples/README.md) - example usages within Node.js runtime environment.


## Contributing


### Installing dependencies and generating gRPC client
* To satisfy all dependencies, lint proto files and regenerate client files:
  ```shell
  make build
  ```
* To update the Iotics API version and regenerate client  
  (proto files are submoduled in [./iotics-api.git/](./iotics-api.git)
  from [Iotics API](https://github.com/Iotic-Labs/api) repo):
  ```bash
  _ver=vX.X.X
  make update-iotics-api GIT_TAG=$_ver
  # Address usages of the new client in `src`, update "Unreleased" section in CHANGELOG.md, then:
  git add CHANGELOG.md iotics-api.git src
  git commit -m "Update Iotics API to $_ver"
  # Push your branch and create a PR
  ```
* Other `make` commands:
  * `clean` - remove artifacts created inside the project.
  * `generate` - regenerate client from proto files.
  * `deps-*` - install specific requirements if missing.
  * `deps-*-update` - update specific requirements when applicable.


### PRs
Should contain a summary of the changes in [CHANGELOG.md](./CHANGELOG.md) under the "Unreleased" section.

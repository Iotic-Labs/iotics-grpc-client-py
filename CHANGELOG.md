# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
- Rename allowlist allhost/nohost values to all/none


## [2.0.4] - 2023-01-24
- Updated the grpcio dependency to >=1.50.0

## [2.0.3] - 2022-12-13
- Fixed bug in the `update_channel` method of the `IoticsApi` Class. It now creates and initialises new instances of the APIs in order to correctly use an updated version of their methods.

## [2.0.2] - 2022-11-09
- different mandatory env vars for the IdentityAuth example, no user seed, user&agent pre-created

## [2.0.1] - 2022-10-31
- change to use tagged version 0.0.16 of api from PR of api

## [2.0.0] - 2022-10-07
- BREAKING CHANGE - Update to handle breaking changes in Iotics API, major change here is the change of TwinID Protobuf definition to include hostId (HostTwinDID)
- docker and makefile fixes for mac and changes in buf

[Unreleased]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v2.0.4...HEAD
[2.0.4]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v2.0.2...v2.0.4
[2.0.3]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v2.0.2...v2.0.3
[2.0.2]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/Iotic-Labs/iotics-grpc-client-py/compare/v0.10.0...v2.0.0

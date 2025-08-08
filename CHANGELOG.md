# Changelog

All notable changes to this project will be documented in this file.

This project aims to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
However, there will be an initial period of stabilisation where this is not adhered to
(releases with version numbers `0.0.x`).

## [0.3.0]

### New Features

- Added support for non-interactive commands via `qcrboxapiclient.commands.invoke_command`
- Added support for stopping long running non-interactive commands with `qcrbox.calculations.stop_running_calculation`

## Enhancements/changes

- Updated some model names related to interactive sessions `CreateInteractiveSession` ->
  `CreateInteractiveSessionParameters`, `CreateInteractiveSessionArguments` -> `CreateInteractiveSessionParametersArguments`

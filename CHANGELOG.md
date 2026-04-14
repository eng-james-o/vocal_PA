# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Comprehensive documentation suite (PRD, User Workflow, Data Models).
- Setup `CONTRIBUTING.md` and `TODO.md`.
- Initial Python core architecture.
- Mermaid diagrams for system flow and class structures.

## [0.1.0-alpha] - 2026-04-10

### Added

- Core YIN algorithm implementation for pitch detection.
- Movable-Do solfa conversion logic.
- Basic range tracking with outlier rejection.
- Preliminary UI wireframes using PyQt6.

### Fixed

- Issue with jittery pitch detection in the lower register by adding median filtering.

### Changed

- Refactored `NoteConverter` to allow dynamic A4 reference calibration.

---
*Note: This project is in active alpha development.*

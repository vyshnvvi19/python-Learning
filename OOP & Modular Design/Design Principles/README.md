# Design Principles

## Overview

This project demonstrates the process of identifying design problems in
deliberately bad Python code and refactoring it into a cleaner design.

The original application contains multiple responsibilities inside a single
class. The refactored version separates these responsibilities and applies
appropriate design principles.

## Objectives

- Identify common design problems.
- Understand the Single Responsibility Principle.
- Apply Dependency Inversion.
- Understand cohesion and coupling.
- Apply DRY where appropriate.
- Use pragmatic design decisions.
- Refactor code without changing its intended behavior.
- Handle invalid input.

## Concepts Covered

- Single Responsibility Principle (SRP)
- Dependency Inversion
- Abstraction
- DRY (Don't Repeat Yourself)
- Cohesion
- Coupling
- Pragmatic Design
- Refactoring

## Project Structure

```text
Design Principles/
├── bad_app.py
├── refactored_app.py
└── README.md
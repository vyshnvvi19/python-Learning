# Interfaces & Abstraction

## Overview

This project demonstrates interfaces and abstraction in Python using
abstract base classes, repository implementations, and a service layer.

The project uses two different repository implementations to show how
business logic can work independently of storage details.

## Objectives

- Understand abstract base classes.
- Define repository rules using abstract methods.
- Create multiple implementations of the same repository.
- Understand dependency boundaries.
- Use interchangeable implementations.
- Separate business logic from data storage.

## Concepts Covered

- Abstract Base Classes (ABC)
- Abstract Methods
- Interfaces
- Repository Pattern
- Service Layer
- Dependency Boundaries
- Interchangeable Implementations

## Project Structure

```text
Interfaces & Abstraction/
├── repository.py
├── memory_repository.py
├── file_repository.py
├── service.py
├── test.py
└── README.md
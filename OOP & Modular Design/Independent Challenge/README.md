# Independent Challenge - Order Management Service

## Overview

This project is a mini order-management service built using a layered
architecture.

The application separates the order domain, business logic, and data access
into different layers.

A mock repository is used so that the service can be tested without using a
real database.

## Objectives

- Build a small order-management service.
- Separate domain, service, and repository responsibilities.
- Apply validation to order creation.
- Use a repository abstraction.
- Create a mock repository for testing.
- Write automated tests.
- Handle valid and invalid input.
- Understand and explain the project architecture.

## Project Structure

```text
Independent Challenge/
├── domain/
│   └── order.py
│
├── repositories/
│   ├── order_repository.py
│   └── mock_order_repository.py
│
├── services/
│   └── order_service.py
│
├── tests/
│   └── test_order_service.py
│
├── app.py
└── README.md
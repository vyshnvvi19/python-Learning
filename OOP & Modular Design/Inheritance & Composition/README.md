# Inheritance & Composition

## Overview

This project demonstrates the use of inheritance and composition in Python
through practical examples involving notifications, payment processing, and
report generation.

The implementation also demonstrates abstract classes, abstract methods,
method overriding, and interchangeable implementations.

## Objectives

- Understand inheritance and its practical use cases.
- Implement method overriding using child classes.
- Define abstract behavior using abstract base classes.
- Apply composition to build flexible class relationships.
- Understand the difference between IS-A and HAS-A relationships.
- Use interchangeable implementations within a class.

## Concepts Covered

- Inheritance
- Method Overriding
- Abstract Classes
- Abstract Methods
- Composition
- Interchangeable Implementations
- IS-A Relationship
- HAS-A Relationship

## Implementation

### Notification

The `Notification` class is defined as an abstract base class with an
abstract `send()` method.

`EmailNotification` and `SMSNotification` inherit from the `Notification`
class and provide their own implementations of the `send()` method.

This demonstrates:

- Inheritance
- Abstract behavior
- Method overriding

### Payment

The payment example demonstrates composition through the `Checkout` class.

`Checkout` accepts a payment method object and uses it to process payments.
Different payment implementations such as `CardPayment` and
`PayPalPayment` can be supplied and switched at runtime.

This demonstrates how composition can provide flexible and interchangeable
implementations.

### Reporting

The reporting example demonstrates both inheritance and composition.

`SalesReport` and `InventoryReport` inherit from the abstract `Report` class
and implement their own `gather_data()` methods.

The `Report` class also uses a formatter object through composition.
`TextFormatter` and `HTMLFormatter` provide different ways of formatting
report data.

## Inheritance vs Composition

Inheritance is used when there is an **IS-A** relationship between classes.

Examples:

- `EmailNotification` IS-A `Notification`
- `SMSNotification` IS-A `Notification`
- `SalesReport` IS-A `Report`
- `InventoryReport` IS-A `Report`

Composition is used when a class **HAS-A** or **USES** another object.

Examples:

- `Checkout` USES a payment method.
- `Report` USES a formatter.

Composition allows different implementations to be supplied without changing
the main class.

## Project Structure

```text
Inheritance & Composition/
├── inheritance_composition.py
└── README.md
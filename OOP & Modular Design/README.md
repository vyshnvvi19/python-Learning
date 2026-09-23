# OOP & Modular Design

## Overview

This module focuses on applying Object-Oriented Programming (OOP) concepts
to design structured and maintainable Python programs.

The implementation models real-world entities such as customers, products,
orders, and invoices using classes and objects.

## Concepts Covered

- Classes and Objects
- Constructors
- Attributes and Methods
- The `self` keyword
- Object State and Behavior
- Object Relationships
- Basic OOP Design

## Implementation

The project includes the following classes:

### Customer

Represents a customer and stores basic information such as name and email.
It provides functionality to display customer details.

### Product

Represents a product with attributes such as name and price.

### Order

Represents a customer order by associating a customer with a product and
quantity. It also calculates the total order amount.

### Invoice

Represents an invoice associated with an order. It displays invoice details,
customer information, product information, quantity, and the total amount.

## Project Structure

```text
OOP & Modular Design/
├── classes_objects.py
└── README.md
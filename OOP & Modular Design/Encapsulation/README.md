# Encapsulation

## Overview

This task demonstrates encapsulation in Python by creating domain objects
with controlled access to their data.

The implementation uses properties, setters, and validation to prevent
objects from entering an invalid state.

## Concepts Covered

- Encapsulation
- Properties
- Property Setters
- Data Validation
- Controlled State Changes
- Invalid-State Prevention

## Implementation

### Product

The `Product` class stores a product name and price.

The price is controlled through a property setter that prevents zero or
negative values.

### Order

The `Order` class stores a product and quantity.

The quantity is controlled through a property setter that ensures the
quantity is greater than zero.

The class also calculates the total order amount.

## Validation

The program prevents invalid values such as:

- Negative or zero product price
- Negative or zero order quantity

Invalid values raise a `ValueError` instead of being stored in the object.

## Project Structure

```text
Encapsulation/
├── encapsulation.py
└── README.md
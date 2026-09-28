# Performance

## Overview

This module demonstrates common performance considerations when processing
larger datasets with Pandas.

The exercise compares a slow row-by-row transformation with a vectorized
transformation and also demonstrates memory awareness and chunking.

## Topics Covered

- Vectorization
- Avoiding unnecessary loops
- Performance measurement
- Memory awareness
- Chunking large datasets

## Dataset

A dataset containing 100,000 sales records was generated for the performance
comparison.

The dataset contains:

- Quantity
- Price

## Slow Transformation

The slow version processes the DataFrame one row at a time using a Python loop.

## Vectorized Transformation

The optimized version performs the calculation directly on Pandas columns:

```python
df["Total_Sales"] = df["Quantity"] * df["Price"]
\# Transformations



\## Overview



This module demonstrates data transformation techniques using Pandas.



The task uses sales and product datasets to perform filtering, sorting,

grouping, aggregation, merging, calculated columns, monthly summaries,

and pivot reports.



\## Topics Covered



\- Filter

\- Sort

\- Groupby

\- Aggregate

\- Merge / Join

\- Pivot

\- Calculated columns



\## Datasets



\### sales.csv



Contains:



\- Order ID

\- Date

\- Product

\- Category

\- Quantity

\- Price

\- City



\### products.csv



Contains:



\- Product

\- Category

\- Supplier



\## Transformations Performed



\### 1. Calculated Columns



A `Total\_Sales` column is calculated using:



```text

Quantity × Price


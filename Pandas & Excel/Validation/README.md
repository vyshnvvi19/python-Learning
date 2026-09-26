\# Excel Validation



\## Overview



This module demonstrates how to validate Excel data using Python and OpenPyXL.



The validation utility checks the Excel workbook for required columns,

required values, valid ranges, and duplicate Student IDs. It also creates

an error report containing actionable diagnostics.



\## Topics Covered



\- Schema checks

\- Required columns

\- Required values

\- Valid ranges

\- Duplicate keys

\- Error reporting

\- Reusable validation functions



\## Validation Rules



The utility checks:



\### Schema



The following columns must be present:



```text

Student\_ID

Name

Age

Marks


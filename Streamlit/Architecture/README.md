# Streamlit Architecture – Student Management

## Overview

This project demonstrates how to structure a Streamlit application by separating the user interface, application logic, domain model, and data storage responsibilities.

The project begins with a deliberately coupled Student Management application and refactors it into separate architectural layers.

The objective is to keep business logic out of the Streamlit UI and create a clearer, more maintainable application structure.

## Objectives

- Understand separation of responsibilities in a Streamlit application.
- Identify problems in a tightly coupled application.
- Refactor a coupled application into separate layers.
- Separate UI logic from business logic.
- Introduce a domain model for student data.
- Separate data storage using a repository.
- Keep the Streamlit page focused on user interaction.

## Architecture

The refactored application follows this flow:

```text
Streamlit Page
      ↓
   Service
      ↓
   Domain
      ↓
 Repository
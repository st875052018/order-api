# Order API

This is an API for order format checking and transformation, implemented using Flask and Docker.

## SOLID Principles and Design Patterns Used

### Single Responsibility Principle (SRP)
- **OrderValidator**: Responsible solely for validating order data.
- **OrderService**: Handles the processing and transformation of order data.

### Open/Closed Principle (OCP)
- The system is open for extension but closed for modification. New validation rules or transformations can be added by extending the validator or service classes without changing existing code.

### Liskov Substitution Principle (LSP)
- N/A

### Interface Segregation Principle (ISP)
- N/A

### Dependency Inversion Principle (DIP)
- High-level modules do not depend on low-level modules; both depend on abstractions. The app uses classes (`OrderValidator`, `OrderService`) rather than concrete implementations.

### Design Patterns
- **Strategy Pattern**: Validation methods in `OrderValidator` can be considered as different strategies for validation.

## Automating with Makefile

A `Makefile` is provided to automate common tasks.

### Build the Docker Image

```bash
make build
```

### Docker Image Unit Test

```bash
make test
```
# NET Mode - Software Engineering Directives & Code Guidelines

## 1. Architectural Integrity (Clean Architecture)
- **Strict Dependency Rule**: Dependencies point ONLY inwards (`Presentation -> Domain <- Data`).
- **Pure Domain**: The `domain/` layer must contain 0 external dependencies (NO Flutter widgets, NO database/HTTP/Android packages). Only Pure Dart.
- **UseCases**: Each business action must have a single UseCase class with one execution method (`call()` or `execute()`).

## 2. SOLID Principles Enforcement
- **Single Responsibility (SRP)**: Separate data models, database management, business rules, and UI widgets into isolated classes.
- **Open/Closed (OCP)**: Build systems using abstract contracts so new features (such as 5G SA/NSA, new bands, or carrier profiles) can be added without altering existing domain code.
- **Liskov Substitution (LSP)**: Subclasses or implementations must honor all base contracts without altering contract behaviors.
- **Interface Segregation (ISP)**: Create lightweight, role-focused interfaces rather than bloated monolithic interfaces.
- **Dependency Inversion (DIP)**: High-level modules must depend on Abstractions (abstract interfaces), never on concrete implementations.

## 3. Platform Boundaries & System Contracts
- **Domain Purity**: Network entities (`NetworkMode`, `SignalQuality`) must remain independent of Flutter or Android packages.
- **Radio Engine & Data Sources**: Android Native Code (`MethodChannel`, `TelephonyManager`, Intent calls) must reside strictly in `data/datasources/`.
- **Defensive Fallback**: Platform exceptions and OEM security locks must be caught in the data layer and mapped to domain-level `Failure` types.

## 4. Defensive Programming & Quality
- Validate parameters at entity boundaries.
- Strongly-typed immutable models with value equality (`operator ==` & `hashCode`).
- High testability with comprehensive unit test coverage.

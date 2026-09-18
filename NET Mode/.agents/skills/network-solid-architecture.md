
# Skill: NET Mode Architecture & System Contracts

## 1. Domain Purity
- Keep all network entities (`NetworkMode`, `SignalQuality`) independent of Flutter or Android packages.
- Platform-specific operations must strictly sit behind abstract interfaces (e.g., `abstract class NetworkRepository`).

## 2. SOLID Rules
- **SRP:** Separate telemetry/signal reading from network mode switching logic.
- **DIP:** Presentation and UseCases must depend on repository abstractions, never on Android method channels directly.

## 3. Platform Integration Boundaries
- Android Native Code (MethodChannels / Intent calls) must reside strictly in `data/datasources/`.
- Handle security and missing permission exceptions at the data layer and re-map them to domain-level `Failure` types.
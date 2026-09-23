# Gemini & Agent Directives: NET Mode

This project implements an offline-first Network Mode Management utility using Clean Architecture and SOLID principles.

## System Guidelines:
- **Domain Layer:** Pure Dart representations of network modes, signal status, and user preferences (strictly zero Flutter or Android UI imports).
- **Data Layer:** Platform channels for telephony and system settings, isolated with DAO/Repository patterns for preferences.
- **Presentation Layer:** Reactive UI applying UI/UX Pro-Max guidelines with clear state management.
- **Agent Directives:** Consult and follow all active skills located in `.agents/skills/` before generating solutions.
- **Defensive Design:** Explicitly handle missing permissions, airplane mode, and device incompatibilities.
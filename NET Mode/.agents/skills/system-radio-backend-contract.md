# Skill: System Radio Engine & Local Persistence Contract

## 1. Separation of Concerns (SRP & DIP)
- The application manages two distinct data sources behind abstract contracts:
  1. `RadioDeviceDataSource`: Interacts with Android platform channels (TelephonyManager / Radio state).
  2. `PreferencesLocalDataSource`: Interacts with local persistence (Drift / SQLite / SharedPreferences) for saved profiles and network history.
- Device radio commands must never be coupled with local storage state.

## 2. Radio Command Abstraction (OCP)
- Define a generic command interface for network mode switches:
  - New network modes (e.g., NR/5G Standalone, SA/NSA) must be extensible without modifying existing switch logic.

## 3. Platform Fault Isolation & Defensive Fallback
- When Android denies programmatic radio switching (due to OEM locks or security policies), the data layer must catch platform exceptions and return a fallback intent trigger (e.g., opening the system Radio Info testing menu) rather than crashing the Domain layer.
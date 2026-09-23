/// Pure Dart Domain Entity representing snapshot network telemetry.
class NetworkInfo {
  final String carrier;
  final String networkType;
  final bool hasSimCard;
  final bool isAirplaneMode;

  const NetworkInfo({
    required this.carrier,
    required this.networkType,
    required this.hasSimCard,
    this.isAirplaneMode = false,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is NetworkInfo &&
          carrier == other.carrier &&
          networkType == other.networkType &&
          hasSimCard == other.hasSimCard &&
          isAirplaneMode == other.isAirplaneMode;

  @override
  int get hashCode =>
      Object.hash(carrier, networkType, hasSimCard, isAirplaneMode);
}

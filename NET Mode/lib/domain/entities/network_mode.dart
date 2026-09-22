// Pure Dart Domain Entity - No Flutter or external framework dependencies.

/// Represents the network generation category of a cellular mode.
enum NetworkGeneration {
  /// 2G technologies (GSM, CDMA, GPRS, EDGE).
  twoG('2G'),

  /// 3G technologies (WCDMA, UMTS, HSPA, EVDO).
  threeG('3G'),

  /// 4G technologies (LTE, LTE-Advanced).
  fourG('4G / LTE'),

  /// 5G technologies (NR Standalone / Non-Standalone).
  fiveG('5G / NR'),

  /// Multi-mode automated switching between available generations.
  autoMultiMode('Auto / Multi-Mode');

  const NetworkGeneration(this.label);

  /// Human-readable label for the network generation.
  final String label;
}

/// Core domain entity representing a cellular radio network mode.
///
/// Adheres to Clean Architecture and Domain Purity rules:
/// - Pure Dart: Zero dependencies on Flutter, Android APIs, or 3rd-party libraries.
/// - Immutable: Thread-safe, predictable, and suitable for functional business logic.
/// - Value Object semantics: Implements structural equality and hashing.
/// - Open for extension: Supports standard presets as well as custom carrier-specific modes.
class NetworkMode {
  /// Unique business identifier for the network mode (e.g., 'lte_only', 'nr_only').
  final String id;

  /// Technical/display name for the network mode (e.g., 'LTE Only', 'NR/LTE/WCDMA').
  final String name;

  /// Standard radio engine / RIL (Radio Interface Layer) preferred network type code.
  final int networkTypeCode;

  /// The cellular generation category this mode belongs to.
  final NetworkGeneration generation;

  /// Indicates whether this mode strictly locks the device to a single technology
  /// without allowing dynamic radio fallback.
  final bool isLockMode;

  /// Detailed description explaining the behavior and trade-offs of this mode.
  final String description;

  /// Creates an immutable [NetworkMode] entity with parameter validation.
  const NetworkMode({
    required this.id,
    required this.name,
    required this.networkTypeCode,
    required this.generation,
    this.isLockMode = false,
    this.description = '',
  })  : assert(id.length > 0, 'NetworkMode id cannot be empty'),
        assert(name.length > 0, 'NetworkMode name cannot be empty'),
        assert(networkTypeCode >= 0, 'networkTypeCode must be non-negative');

  // --- Predefined Standard Presets (Open for Extension) ---

  /// Standard LTE Only mode (Force 4G).
  ///
  /// Android RIL preferred network type code: 11 (LTE_ONLY).
  static const NetworkMode lteOnly = NetworkMode(
    id: 'lte_only',
    name: 'LTE Only',
    networkTypeCode: 11,
    generation: NetworkGeneration.fourG,
    isLockMode: true,
    description: 'Forces connection to 4G LTE only. Prevents fallback to 3G or 2G.',
  );

  /// Standard NR (5G) Only mode (Force 5G Standalone).
  ///
  /// Android RIL preferred network type code: 20 (NR_ONLY).
  static const NetworkMode nrOnly = NetworkMode(
    id: 'nr_only',
    name: 'NR Only (5G)',
    networkTypeCode: 20,
    generation: NetworkGeneration.fiveG,
    isLockMode: true,
    description: 'Forces connection to 5G NR only. Requires 5G SA network availability.',
  );

  /// 5G / 4G / 3G Multi-mode Auto.
  ///
  /// Android RIL preferred network type code: 22 (NR_LTE_WCDMA_GSM).
  static const NetworkMode autoGlobal = NetworkMode(
    id: 'auto_global',
    name: '5G / LTE / 3G / 2G (Auto)',
    networkTypeCode: 22,
    generation: NetworkGeneration.autoMultiMode,
    isLockMode: false,
    description: 'Automatic switching between 5G, 4G, 3G, and 2G based on signal strength.',
  );

  /// Standard WCDMA (3G) Only mode.
  ///
  /// Android RIL preferred network type code: 2 (WCDMA_ONLY).
  static const NetworkMode wcdmaOnly = NetworkMode(
    id: 'wcdma_only',
    name: 'WCDMA Only (3G)',
    networkTypeCode: 2,
    generation: NetworkGeneration.threeG,
    isLockMode: true,
    description: 'Forces connection to 3G WCDMA network only.',
  );

  /// Standard GSM (2G) Only mode.
  ///
  /// Android RIL preferred network type code: 1 (GSM_ONLY).
  static const NetworkMode gsmOnly = NetworkMode(
    id: 'gsm_only',
    name: 'GSM Only (2G)',
    networkTypeCode: 1,
    generation: NetworkGeneration.twoG,
    isLockMode: true,
    description: 'Forces connection to 2G GSM network only (power saving mode).',
  );

  /// List of default available presets supported across standard devices.
  static const List<NetworkMode> standardPresets = [
    autoGlobal,
    nrOnly,
    lteOnly,
    wcdmaOnly,
    gsmOnly,
  ];

  // ─────────────────────────────────────────────────────────────────────────
  // Yemen Carrier-Specific Presets
  // مُصمَّمة لشبكات الاتصالات اليمنية بناءً على أكواد RIL الفعلية.
  // ─────────────────────────────────────────────────────────────────────────

  /// Yemen Mobile + 4G LTE Mode.
  ///
  /// يُثبِّت الجهاز على شبكة CDMA+LTE/EVDO (PRL) الخاصة بيمن موبايل.
  /// Android RIL code: 7 (LTE_CDMA_EVDO — preferred network type).
  static const NetworkMode yemenMobile4G = NetworkMode(
    id: 'yemen_mobile_4g',
    name: 'Yemen Mobile+4G',
    networkTypeCode: 7,
    generation: NetworkGeneration.fourG,
    isLockMode: false,
    description: 'CDMA+LTE/EVDO (PRL) — يمن موبايل 4G مع دعم EVDO.',
  );

  /// Yemen Mobile 3G Only Mode.
  ///
  /// يُثبِّت الجهاز على شبكة CDMA/EVDO Auto (PRL) الخاصة بيمن موبايل.
  /// Android RIL code: 4 (CDMA_EVDO_AUTO).
  static const NetworkMode yemenMobile3G = NetworkMode(
    id: 'yemen_mobile_3g',
    name: '3G Yemen Mobile فقط',
    networkTypeCode: 4,
    generation: NetworkGeneration.threeG,
    isLockMode: true,
    description: 'CDMA/EVDO Auto (PRL) — يمن موبايل 3G فقط.',
  );

  /// Sabafon + YOU (MTN) Mode.
  ///
  /// يُثبِّت الجهاز على شبكة GSM/WCDMA/LTE (PRL) لسبأفون وواي (يو).
  /// Android RIL code: 10 (LTE_GSM_WCDMA).
  static const NetworkMode sabafonYou = NetworkMode(
    id: 'sabafon_you',
    name: 'sabafon+you',
    networkTypeCode: 10,
    generation: NetworkGeneration.fourG,
    isLockMode: false,
    description: 'GSM/WCDMA/LTE (PRL) — مناسب لشبكات سبأفون وواي.',
  );

  /// VoLTE (Voice over LTE) Mode.
  ///
  /// يُثبِّت الاتصال على LTE Only لتفعيل مكالمات VoLTE.
  /// Android RIL code: 11 (LTE_ONLY).
  static const NetworkMode volte = NetworkMode(
    id: 'volte',
    name: 'VoLTE',
    networkTypeCode: 11,
    generation: NetworkGeneration.fourG,
    isLockMode: true,
    description: 'LTE Only — تفعيل مكالمات VoLTE عبر تثبيت الشبكة على 4G.',
  );

  /// Auto / Global Mode (تلقائي).
  ///
  /// يترك الهاتف يختار الشبكة تلقائياً حسب أفضل إشارة متاحة.
  /// Android RIL code: 0 (WCDMA_PREF / Auto-detect by modem).
  static const NetworkMode autoYemen = NetworkMode(
    id: 'auto_yemen',
    name: 'تلقائي',
    networkTypeCode: 0,
    generation: NetworkGeneration.autoMultiMode,
    isLockMode: false,
    description: 'Auto — الهاتف يختار الشبكة الأفضل تلقائياً.',
  );

  /// قائمة الأنماط اليمنية المخصصة للمشغلين المحليين.
  static const List<NetworkMode> yemenPresets = [
    yemenMobile4G,
    yemenMobile3G,
    sabafonYou,
    volte,
    autoYemen,
  ];

  /// Creates a copy of this [NetworkMode] with optional updated fields.
  NetworkMode copyWith({
    String? id,
    String? name,
    int? networkTypeCode,
    NetworkGeneration? generation,
    bool? isLockMode,
    String? description,
  }) {
    return NetworkMode(
      id: id ?? this.id,
      name: name ?? this.name,
      networkTypeCode: networkTypeCode ?? this.networkTypeCode,
      generation: generation ?? this.generation,
      isLockMode: isLockMode ?? this.isLockMode,
      description: description ?? this.description,
    );
  }

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;
    return other is NetworkMode &&
        other.id == id &&
        other.name == name &&
        other.networkTypeCode == networkTypeCode &&
        other.generation == generation &&
        other.isLockMode == isLockMode;
  }

  @override
  int get hashCode => Object.hash(
        id,
        name,
        networkTypeCode,
        generation,
        isLockMode,
      );

  @override
  String toString() =>
      'NetworkMode(id: $id, name: $name, code: $networkTypeCode, generation: ${generation.name}, isLockMode: $isLockMode)';
}

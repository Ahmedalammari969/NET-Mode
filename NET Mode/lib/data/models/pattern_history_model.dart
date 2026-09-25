/// نموذج بيانات يمثل سجل الأنماط السابقة للتطبيق مع دعم التحويل إلى ومن JSON.
class PatternHistoryModel {
  final String id;
  final int networkMode;
  final String modeName;
  final int? subId;
  final DateTime timestamp;
  final bool isSuccess;
  final Map<String, dynamic>? extraData;

  const PatternHistoryModel({
    required this.id,
    required this.networkMode,
    required this.modeName,
    this.subId,
    required this.timestamp,
    this.isSuccess = true,
    this.extraData,
  });

  /// إنشاء النموذج من خريطة JSON مع التحقق الصارم من سلامة الانعدام.
  factory PatternHistoryModel.fromJson(Map<String, dynamic> json) {
    return PatternHistoryModel(
      id: json['id'] as String? ?? '',
      networkMode: json['networkMode'] as int? ?? 0,
      modeName: json['modeName'] as String? ?? '',
      subId: json['subId'] as int?,
      timestamp: json['timestamp'] != null
          ? DateTime.tryParse(json['timestamp'] as String) ?? DateTime.now()
          : DateTime.now(),
      isSuccess: json['isSuccess'] as bool? ?? true,
      extraData: json['extraData'] != null
          ? Map<String, dynamic>.from(json['extraData'] as Map)
          : null,
    );
  }

  /// تحويل كائن النموذج إلى خريطة JSON لتسهيل الحفظ المحلي.
  Map<String, dynamic> toJson() {
    return <String, dynamic>{
      'id': id,
      'networkMode': networkMode,
      'modeName': modeName,
      'subId': subId,
      'timestamp': timestamp.toIso8601String(),
      'isSuccess': isSuccess,
      'extraData': extraData,
    };
  }

  PatternHistoryModel copyWith({
    String? id,
    int? networkMode,
    String? modeName,
    int? subId,
    DateTime? timestamp,
    bool? isSuccess,
    Map<String, dynamic>? extraData,
  }) {
    return PatternHistoryModel(
      id: id ?? this.id,
      networkMode: networkMode ?? this.networkMode,
      modeName: modeName ?? this.modeName,
      subId: subId ?? this.subId,
      timestamp: timestamp ?? this.timestamp,
      isSuccess: isSuccess ?? this.isSuccess,
      extraData: extraData ?? this.extraData,
    );
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is PatternHistoryModel &&
          runtimeType == other.runtimeType &&
          id == other.id &&
          networkMode == other.networkMode &&
          modeName == other.modeName &&
          subId == other.subId &&
          timestamp == other.timestamp &&
          isSuccess == other.isSuccess;

  @override
  int get hashCode =>
      id.hashCode ^
      networkMode.hashCode ^
      modeName.hashCode ^
      subId.hashCode ^
      timestamp.hashCode ^
      isSuccess.hashCode;

  @override
  String toString() {
    return 'PatternHistoryModel(id: $id, networkMode: $networkMode, modeName: $modeName, subId: $subId, timestamp: $timestamp, isSuccess: $isSuccess)';
  }
}

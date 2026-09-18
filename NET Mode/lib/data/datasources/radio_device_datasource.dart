import 'package:flutter/services.dart';

abstract class RadioDeviceDataSource {
  Future<Map<String, dynamic>> getInstantNetworkSnapshot();
  Future<bool> openRadioMenu();
}

class RadioDeviceDataSourceImpl implements RadioDeviceDataSource {
  static const _channel = MethodChannel('com.netmode.app/radio');

  @override
  Future<Map<String, dynamic>> getInstantNetworkSnapshot() async {
    try {
      final result = await _channel.invokeMapMethod<String, dynamic>(
        'getInstantNetworkSnapshot',
      );
      return result ??
          {
            'networkType': 'Unknown',
            'carrier': 'No Carrier',
            'simState': false,
          };
    } on PlatformException catch (_) {
      return {
        'networkType': 'Unknown',
        'carrier': 'No Carrier',
        'simState': false,
      };
    }
  }

  @override
  Future<bool> openRadioMenu() async {
    try {
      final bool? success = await _channel.invokeMethod<bool>(
        'openRadioSettings',
      );
      return success ?? false;
    } on PlatformException catch (_) {
      return false;
    }
  }
}

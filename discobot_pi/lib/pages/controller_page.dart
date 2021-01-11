import 'dart:async';

import 'package:flutter/material.dart';
import 'package:discobot_pi/components/remote_control_button.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:vector_math/vector_math.dart' as VectorMath;
import 'package:web_socket_channel/io.dart';
import 'package:google_fonts/google_fonts.dart';

String ip = "192.168.0.110";

IOWebSocketChannel _channel;
Function onMessage = (String message) {};

Color bgColor = Colors.black;
Color fgColor = Colors.white;
TextStyle style =
    GoogleFonts.robotoMono(fontSize: 30, fontWeight: FontWeight.w400);

IOWebSocketChannel getChannel() {
  if (_channel != null && _channel.closeCode == null) {
    return _channel;
  }
  if (_channel != null && _channel.closeCode != null) {
    print("Close reason: ${_channel.closeReason}");
    print("Close code: ${_channel.closeCode}");
  } else {
    print("Channel is null");
  }

  _channel = IOWebSocketChannel.connect(
    'ws://$ip:8765',
    pingInterval: Duration(seconds: 1),
  );

  _channel.stream.listen(
    (dynamic message) {
      print('Channel message $message');
      onMessage(message);
    },
    onDone: () {
      print('Channel closed');
      _channel = null;
      Timer(const Duration(seconds: 1), () => getChannel());
    },
    onError: (error) {
      print('Channel error $error');
      _channel = null;
      Timer(const Duration(seconds: 2), () => getChannel());
    },
  );

  return _channel;
}

class ControllerPage extends StatefulWidget {
  @override
  _ControllerPageState createState() => _ControllerPageState();
}

class _ControllerPageState extends State<ControllerPage> {
  TextEditingController ipController;

  @override
  void initState() {
    super.initState();

    Function loadIp = () async {
      SharedPreferences prefs = await SharedPreferences.getInstance();
      ip = prefs.getString("ip") ?? ip;
      ipController = TextEditingController(text: ip);

      getChannel();
    };

    loadIp();
  }

  @override
  void dispose() {
    super.dispose();
    ipController.dispose();
    onMessage = (String message) {};
    getChannel().sink.close();
  }

  void _send(String message) {
    getChannel().sink.add(message);
  }

  bool isOn = false;
  bool lightsOn = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: bgColor,
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('60%', style: style),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'Pop',
                  style: style,
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('30%', style: style),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'Rock',
                  style: style,
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('10%', style: style),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'R&B',
                  style: style,
                ),
              ],
            ),
            SizedBox(
              height: 64,
            ),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Column(
                  children: [
                    RemoteControlButton(
                        icon: Icons.power,
                        color: Colors.amber,
                        onPressed: () {
                          if (isOn) {
                            isOn = false;
                            _send('p');
                          } else if (!isOn) {
                            isOn = true;
                            _send('b');
                          }
                        }),
                    RemoteControlButton(
                        icon: lightsOn
                            ? Icons.lightbulb
                            : Icons.lightbulb_outline,
                        color: Colors.teal,
                        onPressed: () {
                          setState(() {
                            lightsOn ? lightsOn = false : lightsOn = true;
                          });
                        })
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

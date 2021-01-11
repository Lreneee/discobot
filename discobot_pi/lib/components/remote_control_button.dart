import 'package:flutter/material.dart';

class RemoteControlButton extends StatelessWidget {
  final IconData icon;
  final Color color;
  final Function onPressed;
  final bool noPadding;

  RemoteControlButton(
      {@required this.icon, @required this.color, @required this.onPressed, this.noPadding});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(noPadding ?? false ? 0 : 12),
      child: FlatButton(
        color: color,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(48),
        ),
        height: 96,
        minWidth: 96,
        onPressed: () {
          onPressed();
        },
        child: Icon(
          icon,
          size: 32,
        ),
      ),
    );
  }
}

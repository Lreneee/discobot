import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class MusicGenreText extends StatelessWidget {
  final String percentage;
  final String musicstyle;

  MusicGenreText({this.percentage, this.musicstyle});

  TextStyle style =
      GoogleFonts.robotoMono(fontSize: 30, fontWeight: FontWeight.w400);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(percentage, style: style),
        SizedBox(
          width: 10,
        ),
        Text(
          musicstyle,
          style: style,
        ),
      ],
    );
  }
}

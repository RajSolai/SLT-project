import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tflite/tflite.dart';
import 'package:image_picker/image_picker.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  File _imageFile;
  String _inferedValue = "";
  final picker = ImagePicker();

  void _loadModel() async {
    await Tflite.loadModel(
        model: 'assets/slt_model_tflt.tflite',
        labels: 'assets/labels.txt',
        isAsset: true);
  }

  void _inferenceTheModel() async {
    String prevWord = _inferedValue;
    var recognitions = await Tflite.runModelOnImage(
        path: _imageFile.path, numResults: 4, asynch: true);
    setState(() {
      _inferedValue = prevWord + recognitions[0]['label'];
    });
  }

  Future _openImageFile() async {
    final pickedFile = await picker.getImage(source: ImageSource.gallery);
    if (pickedFile.path == null) {
      return;
    }
    setState(() {
      _imageFile = File(pickedFile.path);
    });
    _inferenceTheModel();
  }

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        floatingActionButton: FloatingActionButton(
          onPressed: () => _openImageFile(),
          child: Icon(Icons.image_rounded),
        ),
        appBar: AppBar(
          elevation: 0.0,
          title: Text("Sign Language Translator"),
          actions: [
            IconButton(
              icon: Icon(Icons.clear_rounded),
              onPressed: () => {
                setState(() {
                  _inferedValue = "";
                })
              },
            )
          ],
        ),
        body: Center(
          child: Text(
            _inferedValue,
            style: TextStyle(fontSize: 42),
          ),
        ));
  }
}

import 'dart:io';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tflite/tflite.dart';

class HomeM extends StatefulWidget {
  HomeM({Key key}) : super(key: key);

  @override
  _HomeMState createState() => _HomeMState();
}

class _HomeMState extends State<HomeM> {
  List<File> images;
  File _imageFile;
  String _inferedValue = "";

  void _loadModel() async {
    await Tflite.loadModel(
        model: 'assets/slt_model_tflt.tflite',
        labels: 'assets/labels.txt',
        useGpuDelegate: true,
        isAsset: true);
  }

  void _inferenceTheModel(File image) async {
    String prevWord = _inferedValue;
    var recognitions = await Tflite.runModelOnImage(
        path: image.path, numResults: 4, asynch: false);
    setState(() {
      _inferedValue = prevWord + recognitions[0]['label'];
    });
  }

  void _runModel() {
    images.forEach((element) {
      _inferenceTheModel(element);
      //sleep(Duration(seconds: 1));
    });
  }

  Future _openImageFiles() async {
    List<File> files;
    FilePickerResult result =
        await FilePicker.platform.pickFiles(allowMultiple: true);
    if (result != null) {
      files = result.paths.map((path) => File(path)).toList();
    }
    setState(() {
      images = files;
    });
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
          onPressed: () => _openImageFiles(),
          child: Icon(Icons.image),
        ),
        body: Container(
          child: ListView(
            children: [
              CupertinoButton(
                  child: Text("Click me"), onPressed: () => _runModel()),
              Text(_inferedValue)
            ],
          ),
        ));
  }
}

# TCP_Python
Sending hand gesture data captured from webcamera(python TCP_Client), over tcp communication to esp8266 TCP server to controll LED brightness.

Library needed for python TCP client:
1) OpenCV ->  pip install opencv-python
2) Mediapipe -> pip install mediapipe


MediaPipe offers ready-to-use yet customizable Python solutions as a prebuilt Python package. MediaPipe Python package is available on PyPI for Linux, macOS and Windows. For more information: https://google.github.io/mediapipe/ 

Here i'm using 1W LED connected to GPIO2(D4) pin of the esp8266 NoseMCU, see the schematics below,
![Schematics](https://user-images.githubusercontent.com/35668660/129095362-c1b774fa-2c3f-48f0-be8b-40d8d51c4dc4.PNG)

https://user-images.githubusercontent.com/35668660/129095634-0add7f2d-1cb5-40fd-b28a-341eb2f55a5e.mp4


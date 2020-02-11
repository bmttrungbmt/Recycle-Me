# Recycle-Me
*This project was created for participate FPT Edu Hackathon 2019
This project contains two part: Server side and cilent side
- Server side(FlaskServer): base on Flask and ImageAI library. The server will receive image from client and using Object Detection module in ImageAI to detect type of trash appearing in the image, then send result to client as a String.
  *Folder FlaskSever is missing file Yolo.h5 because this file exceeds Github's file size limit of 100.0MB. You can download the file here https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/ and copy it to the folder.
- Client side(AndroidClient): created with Android Studio. The app will take image from camera and then send image to server to receive result.

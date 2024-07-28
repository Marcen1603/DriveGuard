# DriveGuard

The project "DriveGuard" develops a powerful program for processing traffic data using image analysis. It detects vehicles, license plates, pedestrians, road layouts, and traffic signs to enhance traffic safety and efficiency. DriveGuard also ensures data privacy by anonymizing sensitive information like individuals and license plates.

## Training

To detect different kinds of objects on images i am using currently YoloV10 (https://github.com/THU-MIG/yolov10). There are some different possible models available and the current instance is using the YOLOv10-N version. The model is trained on data which i recorded by myself to get high quality footage but i am using some good datasets from the internet also. It is possible to train also a model based on the other possible versions like YOLOv10-S, YOLOv10-M, YOLOv10-B, ... and so on, but currently i am limited by my hardware.

The basic idea what should be possible to detect by the DriveGuard are the following types:

- Vehicles (Car, Truck, Bus, Motorcycle, ...)
- License plates
- Persons
- Traffic signs (Speed, No passing, Town signs, ...) - Only which are relevant for vehicles
- Traffic lights

Planed for future releases:

- Street lines

To get the best results it should be a great idea if for each possible type a single model will be trained, but that increase the amount of work and this is not the focus in the first releases. The current version contains one single model which is learned information about all of the different types.

## Detection

The detection process is very simple. There are two different types of input data which can be used: photo and video. It is possible to get different results of the detection process. Here are the planed results:

- Based on the input data all possible types are tried to detect on the data and marked as their. If there is a vehicle, the vehicle is marked with a quarder and that for every car in each frame.
- If you do not want every type, you can select which types should be detected. If you only selected the vehicles, then no license plates or personens are marked in the output.
- Another option is to anonymize the data. So each detected thing will be blurred, this could be important if you want to preprocess some data and it is not allowed to see license plates or persons
- If you need a documentation about the behavior it will be possible to get a outfile which represents the detected behavior. In this file are information about the allowed speed or which/hor much vehicle are in front of your camera perspective
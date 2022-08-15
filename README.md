# Mahjong Tile Detection

## Quick Summary
This is a computer vision project using YOLOv7 aimed to detect and classify mahjong tiles in images, videos or as they appear on the webcam.

The scope of the project has been narrowed to detect only 3 types of tiles, namely honors-green ('qing fa'), honors-red ('hong zhong') and honors-white ('bai ban').

## Run this project

### Step 1
Clone this repository to the directory where you want the project

### Step 2
`
$ cd <path/to/project>
`

### Step 3
Pip install the required packages

`
$ pip install -r requirements.txt
`

`
$ pip install -r requirements_gpu.txt
`

### Step 4
Run the following commands to execute the detection on image, videos or webcam

Parameters:
* weights - the file which stores the trained weights for detection
* conf - confidence threshold
* img-size - set to 640; same as yolov7 test size 
* source - path to image/video

**For image:**

`
$ python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source demo_img.jpg --view-img --no-trace
`

*Place your image in the same directory and replace source path to your image*

**For video:**

`
$ python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source demo_vid.mp4 --view-img --no-trace
`

*Place your video in the same directory and replace source path to your video*

**For webcam:**

`
$ python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source 0 --view-img --no-trace
`

*Replace source path to your webcam name, use Ctrl + C on command prompt to kill the process*

### Step 5
The detection outcomes can be found under runs/detect/expXXX, where XXX is the run number 
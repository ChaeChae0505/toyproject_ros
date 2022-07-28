

$ docker load -i dope_realsensed435.tar
$ docker run --gpus all -it --ipc=host --net=host --privileged -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -e NVIDIA_DRIVER_CAPABILITIES=all -v /dev:/dev test2 

$ roslaunch realsense2_camera rs_camera.launch
$ roslaunch dope dope.launch
$ rosrun rviz rviz

# 작동관련
- $ roslaunch kobuki_node minimal.launch
- $ roslaunch kobuki_keyop safe_keyop.launch

## Kobuki with RPLidar slam, navigation
1. kobuki_noetic.sh install
- $ bash kobuki_noetic.sh

2. connect
- RPlidar usb를 먼저 꼽고 , kobuki
- 설정해서 사용해도 됨!
- $ ls -l /dev | grep ttyUSB # 잘 잡히나 확인해보기
- $ sudo chmod 666 /dev/ttyUSB0 # RPlidar 권한 주기





## [Reference]
- [wiki](http://wiki.ros.org/kobuki/Tutorials/Examine%20Kobuki)
- [turtlebot2 RPlidarA2](https://surfertas.github.io/ros/2020/07/11/turtlebot2-lidar.html)

sudo apt install liborocos-kdl-dev
sudo apt-get install ros-noetic-ecl-*
sudo apt-get install libusb-dev
sudo apt-get install libftdi-dev
sudo apt-get install ros-noetic-urg-node ros-noetic-gmapping ros-noetic-navigation

mkdir -p ~/kobuki_ws/src
cd ~/kobuki_ws/src

git clone https://github.com/yujinrobot/kobuki.git
git clone https://github.com/yujinrobot/yujin_ocs.git
git clone https://github.com/yujinrobot/kobuki_msgs.git
git clone https://github.com/yujinrobot/kobuki_core.git
git clone https://github.com/robopeak/rplidar_ros.git
git clone https://github.com/oroca/rosbook_kobuki.git


cd yujin_ocs
mkdir save 
mv yocs_cmd_vel_mux save
mv yocs_controllers save
mv yocs_velocity_smoother save
rm -rf yocs*
cd save 
mv * ..
cd .. && rmdir save
cd ~/kobuki_ws/
catkin_make

source ~/kobuki_ws/devel/setup.bash

rosrun kobuki_ftdi create_udev_rules # 유선 연결

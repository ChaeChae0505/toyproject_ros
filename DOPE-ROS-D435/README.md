
```
$ docker load -i dope_realsensed435.tar
$ docker run --gpus all -it --ipc=host --net=host --privileged -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -e NVIDIA_DRIVER_CAPABILITIES=all -v /dev:/dev test2 

$ roslaunch realsense2_camera rs_camera.launch
$ roslaunch dope dope.launch
$ rosrun rviz rviz
```

1. Docker 설치
2. NVIDIA Container Tookit
3. Docker file pull 
4. ROS install
5. Realsense , Realsense wrapper ros install
6. DOPE install

---
1. Docker 컨테이너 저장



## 1. Docker 설치 [1,2 참고](https://velog.io/@boom109/Nvidia-docker)
- 이전 버전 삭제
- sudo apt-get remove docker docker-engine docker.io containerd runc

- https를 통해 repository를 사용할 수 있도록 패키지 설치.
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
Stable repo로 설정
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
특정 버전을 설치 하고자 한다면 아래와 같이 버전을 확인하고 버전을 지정해서 설치 한다.
```
apt-cache madison docker-ce

# [print example]
# docker-ce | 5:20.10.12~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
# docker-ce | 5:20.10.11~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
# docker-ce | 5:20.10.10~3-0~ubuntu-focal | https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
# ...
```
### 설치 후 단계 (option)
- https://docs.docker.com/engine/install/linux-postinstall/
```
add docker group
# Create the docker group.
sudo groupadd docker

# Add your user to the docker group.
sudo usermod -aG docker $USER
sudo usermod -aG docker {other user}

# reboot or type below for activate new group
newgrp docker
docker test
docker run hello-world
```

## 2. NVIDA Container Tookit
- GPG key install
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```
- install nvidia-docker
```
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```
- restart docker daemon
```
sudo systemctl restart docker
```
- base CUDA container 테스트
```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```
### 3. DOCKER 환경
- [참고](https://hub.docker.com/r/celinachild/openvslam)
```
# Terminal #1
docker pull celinachild/openvslam


$ sudo apt-get install x11-xserver-utils
$ xhost +local:
$ docker pull celinachild/openvslam:latest
$ docker run --gpus all -it --ipc=host --net=host --privileged -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -e NVIDIA_DRIVER_CAPABILITIES=all dope docker run \
$VOLUMES \
$ENVS \
-v /dev:/dev \ 



# for mapping
$ ./run_video_slam -v ./orb_vocab/orb_vocab.dbow2 -m ./aist_living_lab_1/video.mp4 -c ./aist_living_lab_1/config.yaml --no-sleep --map-db map.msg

# for localization
$ ./run_video_localization -v ./orb_vocab/orb_vocab.dbow2 -m ./aist_living_lab_2/video.mp4 -c ./aist_living_lab_2/config.yaml --no-sleep --map-db map.msg

# terminal 설치
apt-get install tmux
tmux
# ctrl + b  -> " # 위아래로 나누기

# ctrl + b  -> % # 양옆으로 나누기

# openvslam remove
rm -rf openvslam # 죄송합니다.... 이러시려고 만드신건 아니겠지만
cat /etc/issue # ubuntu 18.04라는 걸 확인 가능

```

- Docker 참고
```
docker images # images 저장 되있는거 확인
docker ps # 실행중 docker 확인
docker commit <containner ID> <New_images_name>
docker rmi <IMAGE ID> # image 삭제
```

### 4. ROS install
```
apt-get install gedit
gedit install-ros-melodic.sh
```
- 아래내용을 입력 apt 앞에 sudo가 없는 이유는 sudo입력이 안해도 되도록 설정!했기 때문에 
- 안 했다면 [참고](https://github.com/ChaeChae0505/ubuntu-setup/blob/master/install-ros-melodic.sh)

```
#!/bin/bash

echo "[Add the ROS repository]"
if [ ! -e /etc/apt/sources.list.d/ros-latest.list ]; then
  sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list' 
fi

echo "[Set up the ROS keys]"
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

echo "[Update the package]"
apt update

echo "[Installing ROS and ROS Packages]"
apt install -y ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
apt-get install -y python-catkin-tools

echo "[rosdep init and python-rosinstall]"
apt install -y python-rosdep
rosdep init
rosdep update

echo "[Making the catkin workspace and testing the catkin_make]"
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws

catkin_make

echo "[Setting the ROS evironment]"
sh -c "echo \"source ~/catkin_ws/devel/setup.bash\" >> ~/.bashrc"
source ~/.bashrc


echo "[Install ROS packages]"

echo "[Complete!!!]"

exec bash

exit 0

```

```
chmod +x install-ros-melodic.sh
./install-ros-melodic.sh
```



- [NVIDIA docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
- [NVIDIA docker git](https://github.com/NVIDIA/nvidia-docker)

## 5. Realsense
```
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE

# ubuntu 16.04
sudo add-apt-repository "deb http://librealsense.intel.com/Debian/apt-repo xenial main" -u

# ubuntu 18.04
sudo add-apt-repository "deb http://librealsense.intel.com/Debian/apt-repo bionic main" -u

# ubuntu 20.04
sudo add-apt-repository "deb http://librealsense.intel.com/Debian/apt-repo focal main" -u


sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils
sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dbg

# test
realsense-viewer
```
```
# apt key error
sudo sed -i 's/http:\/\/realsense-hw-public.s3.amazonaws.com/https:\/\/librealsense.intel.com/' /etc/apt/sources.list
```


## 6. DOPE install
[1] DOPE install

```
cd ~/catkin_ws/src
git clone https://github.com/yehengchen/DOPE-ROS-D435.git
cd ~/catkin_ws/src/dope
apt-get install python-pip
pip install -r requirements.txt
cd ~/catkin_ws
apt-get install python-rosdep
rosdep init
rosdep update

rosdep install --from-paths src -i --rosdistro melodic -y
apt-get install ros-melodic-rosbash ros-melodic-ros-comm
Build

cd ~/catkin_ws
catkin_make

```

[2] weight file download 
- [cracker.pt](https://drive.google.com/file/d/1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p/view?usp=sharing)


- google drive file download in docker
- https://drive.google.com/file/d/1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p/view?usp=sharing

```
mkdir -p ~/catkin_ws/src/dope/weights 
cd ~/catkin_ws/src/dope/weights 
```

```bash
#!/bin/bash

FILEID=$1
FILENAME=$2

curl -sc ~/cookie.txt "https://drive.google.com/uc?export=download&id=${FILEID}" > /dev/null

curl -Lb ~/cookie.txt "https://drive.google.com/uc?export=download&confirm=`awk '/_warning_/ {print $NF}' ~/cookie.txt`&id=${FILEID}" -o ${FILENAME}

```
curl -sc ~/cookie.txt "https://drive.google.com/uc?export=download&id=1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p" > /dev/null

curl -Lb ~/cookie.txt "https://drive.google.com/uc?export=download&confirm=`awk '/_warning_/ {print $NF}' ~/cookie.txt`&id=1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p" -o cracker_60.pth
```
chmod u+x gdown.sh # 실행 권한 주기

./gdown.sh {FILEID} {FILENAME} # 1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p # cracker_60.pth
./gdown.sh 1eFl1WgC8i3SLPQ9GW8JQRhh3nKOmNK-p cracker_60.pth

curl -sc /tmp/cooke "
```
위 처럼 할바에 그냥 docker cp 해서 로컬 파일 옮기는 게 나음
DOPE 파일 안에 있는 ddynamic configure 파일은 지움 => apt install ros-melodic-ddynamic과 겹쳐서...에러 뜸


[3] 실행
- config / config_pose.yaml 파일에서  camera, camera info의 topic을 변경해 주시고
- roslaunch realsense2_camera rs_camera.launch
- roslaunch dope dope.launch
- rosrun rviz rviz를 해주시면 됩니다!
 
 
 
# 마주친 ERROR
-  DOPE 파일 안에 있는 ddynamic configure 파일은 지움 => apt install ros-melodic-ddynamic과 겹쳐서 look up symbol error 가 뜹니다!
- dope 파일은 nvlabs의 원 링크로 들어가서 Kinetic version을 다시 받아 오는 걸 추천드립니다!
 
 
# DOPE 한계점
- DOPE는 가로세로 비율과, 색깔에 민감한(?) 결과를 놓는다 그만큼 조금이라도 다르면 같은걸로 인식하지 않는다! 반대로 말하면 같은 물건인데 형상이나 색이 조금 달라지면 인식하기 어렵다!는 말도 될 것이다
출처: https://1ch0.tistory.com/124 [당근감자:티스토리]


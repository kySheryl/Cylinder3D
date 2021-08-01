```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

```bash
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

```bash
sudo apt update
```

```bash
sudo apt install ros-melodic-desktop-full
```

```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

```bash
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```

```bash
sudo apt-get install libpcap-dev
```

```bash
cd ～
mkdir -p catkin_ws/src
```

```bash
cd ~/catkin_ws/src
git clone https://github.com/RoboSense-LiDAR/ros_rslidar.git
```

```bash
cd ~/catkin_ws
catkin_make

```

Set the IP for the Personal Computer to be ``192.168.1.102`` and the Netmask to be ``255.255.255.0``

```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch rslidar_pointcloud rs_lidar_16.launch
```


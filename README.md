
# NavBot ROS 2 Project - Week 1

## Description
This project is part of a ROS 2 internship project.
The goal of Week 1 is to set up the development environment and create a first ROS 2 publisher/subscriber demo.

## Environment
- VMware Workstation Pro 17
- Ubuntu 22.04
- ROS 2 Humble
- Gazebo 11.10.2
- VS Code
- Python 3

## Workspace
Workspace name:

```bash
navbot_ws

## Week 2 - ROS 2 Communication

During Week 2, I worked on advanced ROS 2 communication concepts.

### Work completed

- Created a custom message `RobotStatus.msg`
- Created a publisher using the custom message
- Created a subscriber using the custom message
- Created a custom service `GetRobotStatus.srv`
- Created a service server
- Created a service client
- Added ROS 2 parameters to the publisher
- Created a launch file to run publisher and subscriber together
- Added pytest tests to verify project files

### Custom Message

The custom message `RobotStatus.msg` contains:

```text
string robot_name
float32 battery_level
string status

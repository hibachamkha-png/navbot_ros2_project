from pathlib import Path


def test_robot_status_publisher_exists():
    file_path = Path("src/navbot_bringup/navbot_bringup/robot_status_publisher.py")
    assert file_path.exists()


def test_robot_status_subscriber_exists():
    file_path = Path("src/navbot_bringup/navbot_bringup/robot_status_subscriber.py")
    assert file_path.exists()


def test_launch_file_exists():
    file_path = Path("src/navbot_bringup/launch/week2_demo.launch.py")
    assert file_path.exists()

import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/eaguiraud/ros2_ws/install/vision_rpi_bot'

import os
import sys
import threading

from python_qt_binding import loadUi
import rospkg
import rospy
from rqt_py_common.rqt_roscomm_util import RqtRoscommUtil
from rqt_topic.topic_widget import TopicWidget

class MonitorWidget(QWidget):
    def __init__(self, parent, plugin_context):
        super(MonitorWidget, self).__init__()
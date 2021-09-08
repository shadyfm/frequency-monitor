
from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
import sys
import yaml
import rospkg
from frequency_monitor import topic_monitor

config_file_location = "log_config.yaml"
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()

class Ui_Form(object):
    def setupUi(self, Form, required_topic_list):
        self.required_topics_monitor = []
        for item,topic_detail in required_topic_list.items():
            self.required_topics_monitor.append(topic_monitor(item, topic_detail.get("topic"), topic_detail.get("min_freq_hz")))
        Form.setObjectName("Form")
        Form.resize(1067, 779)
        self.Monitor = QtWidgets.QPushButton(Form)
        self.Monitor.setGeometry(200,150, 100, 100)
        self.Monitor.setStyleSheet("border-radius : 50; border: 2px rgb(0, 226, 0); background-color: rgb(0, 226, 0)")
        self.Monitor.setObjectName("Monitor")
        self.label = QtWidgets.QLabel(Form)
        self.label.move(100, 150)
        self.label.setObjectName("label")
        self.error_msg = ""
        self.ui_update_timer = rospy.Timer(rospy.Duration(secs=1.0), self.update_ui)

	
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Frequency Monitor"))
        self.label.setText(_translate("Form", "Loading Data"))
        self.label.adjustSize()
    def update_ui(self, timer):
        _translate = QtCore.QCoreApplication.translate

        now = rospy.get_rostime()

        if False in topic_monitor.works:
            #_translate = QtCore.QCoreApplication.translate
            self.Monitor.setStyleSheet("border-radius : 50; border: 2px rgb(255,0,0); background-color: rgb(255, 0, 0)")
            for topic in self.required_topics_monitor:
                if topic_monitor.works[topic.ind] == False:

                    if self.error_msg == "":
                        self.error_msg = self.error_msg + str(topic.topic_type)

                    else: 
                        self.error_msg = self.error_msg + " and " + str(topic.topic_type)

            if "and" in self.error_msg:
                self.error_msg = self.error_msg + " have not been logging data since last check."

            else:
                self.error_msg = self.error_msg + " has not been logging data since last check."
    
            self.label.setText(_translate("Form", self.error_msg))
            self.label.adjustSize()
            self.error_msg = ""

        else:
            self.Monitor.setStyleSheet("border-radius : 50; border: 2px rgb(0, 226, 0); background-color: rgb(0, 226, 0)")
            self.label.setText(_translate("Form", "All Sensors Working"))
            self.label.adjustSize()
        Form.update()
	


def main():
    rospy.init_node("data_freq_monitor", anonymous=True)

    pkg_path = rospkg.RosPack().get_path('sfm_topic_monitor')
    file = open(pkg_path + "/config/" + config_file_location)
    topic_list = yaml.load(file, Loader=yaml.Loader)
    required_topic_list = topic_list.get("required")


    ui = Ui_Form()
    ui.setupUi(Form, required_topic_list)
    Form.show()
    sys.exit(app.exec_())



    


if __name__ == "__main__":
    main()  
    
    

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
        _translate = QtCore.QCoreApplication.translate
        Form.setObjectName("Form")
        Form.resize(300, 0)
        Form.resize(Form.width(),Form.width())
        self.org_Formh = Form.width()
        self.org_Formw = Form.height()
        Form.setStyleSheet("border-radius: 100; border: 2px black; background-color: rgb(255,255,255)")
        
        self.Monitor = QtWidgets.QPushButton(Form)

        if Form.width()/2 <= Form.height():
            self.Monitor.setGeometry(0, 0, Form.width()/2, Form.width()/2)

        else:
            self.Monitor.setGeometry(0, 0, Form.height()/2, Form.height()/2)

        self.Monitor.move(Form.width()/2 - self.Monitor.width()/2, Form.height()/2 - self.Monitor.height()/2)
        self.Monitor.setStyleSheet("border-radius : " + str(self.Monitor.width()/2) + "; border: 2px rgb(0, 255, 0); background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(0, 100, 0), stop: 0.2 rgb(0,150,0), stop:0.9 rgb(0,200,0))")
        self.Monitor.setObjectName("Monitor")
        self.Centre = QtWidgets.QPushButton(Form)
        self.Centre.setGeometry(0, 0, self.Monitor.width() * 22/25, self.Monitor.width() * 22/25)
        self.Centre.move(Form.width()/2 - self.Centre.width()/2, Form.height()/2 - self.Centre.height()/2)
        self.Centre.setStyleSheet("border-radius : " + str(self.Centre.width()/2) + "; border: 2px rgb(0, 200, 0); background-color: rgb(255, 255, 255)")
        self.Centre.setObjectName("Centre")
        self.sensor_count = QtWidgets.QLabel(Form)
        self.sensor_count.setObjectName("sensor_count")
        #self.sensor_count.setStyleSheet("font-size: 200px")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.message = QtWidgets.QLabel(Form)
        self.message.setObjectName("message")
        self.message.setVisible(False)
        #self.message.setStyleSheet("font-size: " + str(self.message_size) + "px")
        self.logging_label = QtWidgets.QLabel(Form)
        self.logging_label.setObjectName("logginglabel")
        self.logging_label.setVisible(False)
        self.loading = QtWidgets.QLabel(Form)
        self.loading.setObjectName("loading")
        print(self.Monitor.width()*0.08)
        #self.loading.setStyleSheet("font-size: "+ str(20) + "px")
        self.currrent_error = ""
        
        self.error_msg = ""

        self.retranslateUi(Form)

        self.required_topics_monitor = []

        for item,topic_detail in required_topic_list.items():
            self.required_topics_monitor.append(topic_monitor(item, topic_detail.get("topic"), topic_detail.get("min_freq_hz")))
        
        
        self.ui_update_timer = rospy.Timer(rospy.Duration(secs=1.0), self.update_ui)
        
        #self.message_update_timer = rospy.Timer(rospy.Duration(secs=1.0), self.message_update)

        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Frequency Monitor"))
        self.sensor_count.setText(_translate("Form", ""))
        #self.sensor_count.setStyleSheet("font-size: 200px")
        self.sensor_count.setGeometry(0, 0, 0, self.Centre.height() * 2/5)
        #print(self.sensor_count.height())
        self.sensor_count.setStyleSheet("font-size: " + str(self.sensor_count.height()) + "px")
        self.sensor_count.adjustSize()
        self.sensor_count.move(self.org_Formw/2 - self.sensor_count.width()/2, self.org_Formh/2 - self.sensor_count.height()/2)
        self.label.setGeometry(0, 0, 0, self.Monitor.height() * 2/50)
        #print(self.label.height())
        self.label.setGeometry(0, 0, 0, self.Monitor.height()*3/50)
        self.label.setStyleSheet("font-size: " + str(self.label.height()) + "px")
        #self.label.setStyleSheet("font-size: " + str(self.label.height()) + "px")
        self.loading.setGeometry(0,0,0, self.Monitor.height() * 0.08)
        self.loading.setStyleSheet("font-size: "+ str(self.loading.height()) + "px")
        self.loading.setText(_translate("Form", "Loading Data"))
        self.loading.adjustSize()
        self.loading.move(self.org_Formw/2 - self.loading.width()/2, self.org_Formh/2 - self.loading.height()/2)
        self.logging_label.setGeometry(0, 0, 0, self.Monitor.height() * 0.08)
        self.logging_label.setStyleSheet("font-size: "+ str(self.logging_label.height()) + "px")
        self.message.setGeometry(0, 0, 0, self.Monitor.height() * 0.08)
        self.message.setStyleSheet("font-size: "+ str(self.message.height()) + "px")
    def update_ui(self, timer):
        _translate = QtCore.QCoreApplication.translate
        
        now = rospy.get_rostime()
        self.loading.setVisible(False)
        if False in topic_monitor.works:
            _translate = QtCore.QCoreApplication.translate
            self.Monitor.setStyleSheet("border-radius : " + str(self.Monitor.width()/2) + "; border: 2px rgb(200,0,0); background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(100, 0, 0), stop: 0.2 rgb(150, 0, 0), stop:0.9 rgb(200, 0, 0))")
            
            for topic in self.required_topics_monitor:
                if topic_monitor.works[topic.ind] == False:

                    if self.error_msg == "":
                        self.error_msg = self.error_msg + str(topic.topic_type)

                    else: 
                        self.error_msg = self.error_msg + " and " + str(topic.topic_type)

            if "and" in self.error_msg:
                self.logging_label.setText(_translate("Form", "have not been logging data since last check"))

            else:
                self.logging_label.setText(_translate("Form", "has not been logging data since last check."))
            self.error_msg = self.error_msg + "..."
            self.message.setVisible(True)
            self.logging_label.setVisible(True)
            self.message.setText(_translate("Form", self.error_msg))
            #self.sensor_count.move(Form.width()/2 - self.sensor_count.width()/2, Form.height()/2 - self.sensor_count.height()/2)
            
            #if len(self.error_msg) < len(self.currrent_error):
                #self.message_size = 30

            #self.currrent_error = self.error_msg
            self.error_msg = ""

        else:
            self.Monitor.setStyleSheet("border-radius : " + str(self.Monitor.width()/2) + "; border: 2px rgb(0, 200, 0); background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(0, 100, 0), stop: 0.2 rgb(0,150,0), stop:0.9 rgb(0,200,0))")
            self.message.setVisible(False)          
            self.logging_label.setVisible(False)

        #print(str(Form.width()) + " " + str(self.message.width()))
        self.message.adjustSize()
        self.message.move(self.org_Formw/2 - self.message.width()/2, self.org_Formh/2 - self.org_Formh*3/9)
        self.logging_label.adjustSize()
        self.logging_label.move(self.org_Formw/2 - self.logging_label.width()/2, self.org_Formh/2 + self.org_Formh*2/7)
        self.sensor_count.setText(_translate("Form", str(topic_monitor.works.count(True))))
        self.sensor_count.adjustSize()
        self.sensor_count.move(self.org_Formw/2 - self.sensor_count.width()/2, self.org_Formh/2 - self.sensor_count.height()/1.5)
        self.label.setText(_translate("Form", "of " + str(len(topic_monitor.works)) + " sensors active"))
        self.label.adjustSize()
        self.label.move(self.org_Formw/2 - self.label.width()/2, self.org_Formh * 4/7)

        #while self.message.width() > self.org_Formw and self.message_size > 1:

            #self.message.setStyleSheet("font-size: " + str(self.message_size - 1)+ "px")
            #self.message.adjustSize()
            #self.message.move(self.org_Formw/2 - self.message.width()/2, self.org_Formh/2 - self.org_Formh * 3/7)
            #self.message_size = self.message_size -1
            #Form.update()
   
        
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
  
    
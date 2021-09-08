#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
import sys
import yaml
import rospkg
from frequency_monitor import frequency_monitor

config_file_location = "log_config.yaml"
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()

class Ui_Form(object):
    def setupUi(self, Form, required_topic_list):
        _translate = QtCore.QCoreApplication.translate
       
        #parent widget
        Form.setObjectName("Form")
        self.FormSize = 300
        Form.resize(self.FormSize, self.FormSize)
        Form.setStyleSheet("border-radius: 100; border: 2px black; background-color: rgb(255,255,255)")
        
        #colour changing widget
        self.Monitor = QtWidgets.QPushButton(Form)
        self.Monitor.setGeometry(0, 0, self.FormSize/1.5, self.FormSize/1.5/2)
        self.Monitor.setStyleSheet("border-radius : " + str(self.Monitor.height()) + "; border: 2px rgb(0, 255, 0); background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(0, 100, 0), stop: 0.2 rgb(0,150,0), stop:0.9 rgb(0,200,0))")
        self.Monitor.setGeometry(0, 0, self.FormSize/1.5, self.FormSize/1.5)
        self.Monitor.move(Form.width()/2 - self.Monitor.width()/2, Form.height()/2 - self.Monitor.height()/2)
        self.Monitor.setObjectName("Monitor")
        
        #white circle in the middle
        self.Centre = QtWidgets.QPushButton(Form)
        self.Centre.setGeometry(0, 0, self.Monitor.width() * 22/25, self.Monitor.width()*22/25/2)
        self.Centre.setStyleSheet("border-radius : " + str(self.Centre.height()) + "; border: 2px rgb(0, 200, 0); background-color: rgb(255, 255, 255)")
        self.Centre.setGeometry(0, 0, self.Monitor.width() * 22/25, self.Monitor.width()*22/25)
        self.Centre.move(Form.width()/2 - self.Centre.width()/2, Form.height()/2 - self.Centre.height()/2)
        self.Centre.setObjectName("Centre")
        
        #displays the number of active sensors
        self.sensor_count = QtWidgets.QLabel(Form)
        self.sensor_count.setObjectName("sensor_count")

        #displays the total number of sensors
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label.setVisible(False)

        #displays the names of inactive sensors
        self.error = QtWidgets.QLabel(Form)
        self.error.setObjectName("error")
        self.error.setVisible(False)
        myFont=QtGui.QFont()
        myFont.setBold(True)
        self.error.setFont(myFont)

        #bottom half of error message
        self.logging_label = QtWidgets.QLabel(Form)
        self.logging_label.setObjectName("logginglabel")
        self.logging_label.setVisible(False)

        #loading message that appears at the start of program
        self.loading = QtWidgets.QLabel(Form)
        self.loading.setObjectName("loading")

        self.error_list = []
        self.error_msg = ""

        self.retranslateUi(Form)

        self.required_topics_monitor = []

        for item,topic_detail in required_topic_list.items():
            self.required_topics_monitor.append(frequency_monitor(item, topic_detail.get("topic"), topic_detail.get("min_freq_hz")))

        self.label.setText(_translate("Form", "of " + str(len(frequency_monitor.works)) + " sensors active"))
        self.label.adjustSize()
        self.label.move(self.FormSize/2 - self.label.width()/2, self.FormSize * 4/7)

        
        self.ui_update_timer = rospy.Timer(rospy.Duration(secs=1.0), self.update_ui)

        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Frequency Monitor"))

        self.sensor_count.setText(_translate("Form", ""))
        self.sensor_count.setGeometry(0, 0, 0, self.Centre.height() * 2/5)
        self.sensor_count.setStyleSheet("font-size: " + str(self.sensor_count.height()) + "px")
        self.sensor_count.adjustSize()
        self.sensor_count.move(self.FormSize/2 - self.sensor_count.width()/2, self.FormSize/2 - self.sensor_count.height()/2)

        self.label.setGeometry(0, 0, 0, self.Monitor.height() * 2/50)
        self.label.setGeometry(0, 0, 0, self.Monitor.height()*3/50)
        self.label.setStyleSheet("font-size: " + str(self.label.height()) + "px")

        self.loading.setGeometry(0,0,0, self.Monitor.height() * 0.08)
        self.loading.setStyleSheet("font-size: "+ str(self.loading.height()) + "px")
        self.loading.setText(_translate("Form", "Loading Data"))
        self.loading.adjustSize()
        self.loading.move(self.FormSize/2 - self.loading.width()/2, self.FormSize/2 - self.loading.height()/2)

        self.logging_label.setGeometry(0, 0, 0, self.Monitor.height() * 0.07)
        self.logging_label.setStyleSheet("font-size: "+ str(self.logging_label.height()) + "px")

        self.error.setGeometry(0, 0, 0, self.Monitor.height() * 0.07)
        self.error.setStyleSheet("font-size: "+ str(self.error.height()) + "px")

    def update_ui(self, timer):
        _translate = QtCore.QCoreApplication.translate

        self.loading.setVisible(False)
        self.label.setVisible(True)
        
        self.error_msg = ""
        self.error_list.clear()
        self.error.setText("")
        self.logging_label.setText("")

        if False in frequency_monitor.works:
           
            #creating error message
            for topic in self.required_topics_monitor:
                if frequency_monitor.works[topic.ind] == False:

                    if self.error_msg == "":
                        self.error_msg = str(topic.topic_type)

                    else: 
                        self.error_msg = self.error_msg + " and " + str(topic.topic_type)

            if "and" in self.error_msg:
                self.logging_label.setText(_translate("Form", "have not been logging data since last check."))
                self.error_list = self.error_msg.split("and")

            else:
                self.logging_label.setText(_translate("Form", "has not been logging data since last check."))
                self.error_list.append(self.error_msg)
            
            
            self.error.setText(_translate("Form", self.error_msg))

            self.error.adjustSize()

            excluded = 0

            #changing the error message so that it fits on the screen
            while self.error.width() > self.FormSize:
                if excluded > 1:
                    self.error.setText(_translate("Form", self.error.text().replace(" +" + str(excluded) + " others", "")))
                
                else:
                    self.error.setText(_translate("Form", self.error.text().replace(" +" + str(excluded) + " other", "")))

                self.error.setText(_translate("Form", self.error.text().replace(str(self.error_list[len(self.error_list) - 1]), "")))
                del self.error_list[len(self.error_list) -1]

                if len(self.error.text()) >= 3:
                    self.error.setText(self.error.text() [:len(self.error.text()) -3])
            
                
                excluded = excluded + 1

                if excluded > 1:
                    self.error.setText(_translate("Form", self.error.text() + " +" + str(excluded) + " others"))

                else:
                    self.error.setText(_translate("Form", self.error.text() + " +" + str(excluded) + " other"))
                
                self.error.adjustSize()

            self.error.move(self.FormSize/2 - self.error.width()/2, self.FormSize/2 - self.FormSize*3/7)

            self.logging_label.adjustSize()
            self.logging_label.move(self.FormSize/2 - self.logging_label.width()/2, self.FormSize/2 + self.FormSize*3/8)
                
            self.error.setVisible(True)
            self.logging_label.setVisible(True)
            
            #changing monitor colour to red
            self.Monitor.setStyleSheet(self.Monitor.styleSheet().replace("qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(0, 100, 0), stop: 0.2 rgb(0,150,0), stop:0.9 rgb(0,200,0)","qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(100, 0, 0), stop: 0.2 rgb(150, 0, 0), stop:0.9 rgb(200, 0, 0)"))

        else:
            #changing monitor colour to green
            self.Monitor.setStyleSheet(self.Monitor.styleSheet().replace("qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(100, 0, 0), stop: 0.2 rgb(150, 0, 0), stop:0.9 rgb(200, 0, 0)", "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0.1 rgb(0, 100, 0), stop: 0.2 rgb(0,150,0), stop:0.9 rgb(0,200,0)"))
            
            self.error.setVisible(False)          
            self.logging_label.setVisible(False)
        
            #self.error.setText(_translate("Form", self.error_msg))
            self.error.adjustSize()
            

        #changing active sensor count value

        self.sensor_count.setText(_translate("Form", str(frequency_monitor.works.count(True))))
        self.sensor_count.adjustSize()
        self.sensor_count.move(self.FormSize/2 - self.sensor_count.width()/2, self.FormSize/2 - self.sensor_count.height()/1.5)
        
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
  
    

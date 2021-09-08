#!/usr/bin/env python3

import rospy
import yaml
import rospkg


config_file_location = "log_config.yaml"

class frequency_monitor:
    works = []
    
    def __init__(self, topic_type, topic, min_freq):
        self.topic_type = topic_type
        self.msg_count = 0
        self.count_list = []
        self.working = True
        self.works.append(self.working)
        self.ind = len(self.works) - 1
        self.sub = rospy.Subscriber(name=topic, data_class=rospy.AnyMsg, callback=self.msg_counter)
        self.min_freq = min_freq
        self.add = rospy.Timer(rospy.Duration(secs=1.0), self.add_count)
        self.checker = rospy.Timer(rospy.Duration(secs=1.0), self.freq_monitor)
        self.avg = 0
        
        
    def msg_counter(self, msg):
        self.msg_count = self.msg_count + 1

    def add_count(self, timer):
        if len(self.count_list) == 5:
            del self.count_list[0]
            self.count_list.append(self.msg_count)
        else:
            self.count_list.append(self.msg_count)

        self.msg_count = 0
    
    def freq_monitor(self, timer):
        if len(self.count_list) == 5:
            #print(str(self.topic_type) + str(self.count_list))
            #print(sum(self.count_list)/5)
            
            self.avg = sum(self.count_list)/5

            if self.avg < self.min_freq:
                #msg = self.topic_type + " has not been logging data since last check."
                #rospy.logwarn(msg)
                self.working = False

            else:
                self.working = True

        self.works[self.ind] = self.working
            

        
def main():
    # Wait for 1 second for everything to get up and running
    rospy.sleep(1.0)

    rospy.init_node("logging_monitor", anonymous=True)
    pkg_path = rospkg.RosPack().get_path('sfm_topic_monitor')
    file = open(pkg_path + "/config/" + config_file_location)
    topic_list = yaml.load(file, Loader=yaml.Loader)
    required_topic_list = topic_list.get("required")
    required_topics_monitor = []
    for item,topic_detail in required_topic_list.items():
        required_topics_monitor.append(frequency_monitor(item, topic_detail.get("topic"), topic_detail.get("min_freq_hz")))
   
  
    rospy.spin()


if __name__ == '__main__':
    main()

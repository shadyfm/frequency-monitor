#!/usr/bin/env python

import rospy
import yaml
import rospkg

config_file_location = "log_config.yaml"

class topic_monitor:
    def __init__(self, topic_type, topic, min_freq):
        self.topic_type = topic_type
        self.msg_count = 0
        self.msg_count_last_check = 0
        self.sub = rospy.Subscriber(name=topic, data_class=rospy.AnyMsg, callback=self.msg_counter)
        self.checker = rospy.Timer(rospy.Duration(secs=1.0/min_freq), self.freq_monitor)

    def msg_counter(self, msg):
        self.msg_count = self.msg_count + 1
        #print("message" + str(self.msg_count))

    def freq_monitor(self, timer):
        if self.msg_count_last_check >= self.msg_count:
            print(str(self.topic_type) + " " + str(self.msg_count))
            print(str(self.topic_type) + " " + str(self.msg_count_last_check))
            msg = self.topic_type + " is not logging data since last check."
            rospy.logwarn(msg)
        self.msg_count_last_check = self.msg_count


def main():
    # Wait for 10 seconds for everything to get up and running
    rospy.sleep(1.0)

    rospy.init_node("logging_monitor", anonymous=False)
    pkg_path = rospkg.RosPack().get_path('sfm_topic_monitor')
    file = open(pkg_path + "/config/" + config_file_location)
    topic_list = yaml.load(file, Loader=yaml.Loader)
    required_topic_list = topic_list.get("required")
    required_topics_monitor = []
    for item,topic_detail in required_topic_list.items():
        required_topics_monitor.append(topic_monitor(item, topic_detail.get("topic"), topic_detail.get("min_freq_hz")))

    rospy.spin()


if __name__ == '__main__':
    main()

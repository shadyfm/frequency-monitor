execute_process(COMMAND "/home/shadida/catkin_ws/build/rqt_freq_monitor/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/shadida/catkin_ws/build/rqt_freq_monitor/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

Troubleshooting
===============

Node-RED
--------

* This Code Pattern uses [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)  
* Whie installing Raspbian on Raspberry Pi make sure you installed the correct version.  
  The version used in this IBMCode pattern can be found [here](http://downloads.raspberrypi.org/raspbian/images/raspbian-2017-08-17/)  
* You can refer to a complete list of Raspberry Pi OS archives [here](http://downloads.raspberrypi.org/raspbian/images/)  
* Make sure the import of Node-RED ran correctly. Ensure each flow works correctly in the  
  sequence of data flow before moving on to the next. 
* All the flows depend on the outputs from previous flows and also the connectivity.  
  If there is an issue in any stage stop and resolve the issue before moving further.  
  Start from the beginning when troubleshooting. Examine the outputs in the debug window in  
  Node-RED editor thorougly at each stage.    
* The flow relies on service credentials from IBM Cloud.  
  Make sure to add your service credentials correctly.  

  
IBM IoT Platform
----------------
* Make sure data is received and transmitted correctly between Raspberry Pi  
  and IBM IoT Platform on the cloud.  
* Specifically ensure the Region in which your Service is created in IBM Cloud  
  is consistent  
* Also pay special attention to the unique ``Device ID`` you set on the Raspberry Pi  
  Node-RED flow as well as the Node-RED flow in IBM Cloud. These must be same and unique  
  to ensure seamless data transfer.  

# 1 Edge communication using Predictive and Change Point models in Watson IoT and IBM DSX (IoT)

Internet of Things (IoT) have evolved tremendously in all spheres of our daily lives like Industrial  
applications, Social interactions, Remote management of facilities and equipment to name a few.  

In general application areas, IoT data collected mainly by use of Sensors can be for Monitoring as  
well as predicting the outcomes. If any deviation from the norm is detected, corrective action can be  
prescribed either manually or by an automated process. Such actions may come out of Rule based anomaly  
detection or a Statistical Change point detection or a Predictive model that predicts a faulty  
condition ahead of time.  

The Process steps for applying Analytics on IoT data can be broadly classified as below
1.	Collect IoT data from sensor
2.	Change Point detection using IoT Sensor data
3.	Predicting Equipment failure using IoT Sensor data
4.	Sending Decisions based on Analytics insights to the edge for Automated Action

This IBM Code Pattern is a composite pattern that brings together the end to end flow of IoT Analytics systems.

![png](doc/images/iea_aainiot_arch.png)  
Image courtesy from blog [Advanced Analytics Applications in IoT](https://developer.ibm.com/code/?p=25889)


While Rule based anomaly detection uses point in time data, which may be sudden spike in some parameters  
with a possibility of getting back to normal ranges, statistical Change point detection can differentiate  
and identify a Change in operating parameters that might not return to normal by itself. And so a more  
reliable corrective action can be initiated.  

The Statistical method and flow for detecting change points in IoT Sensor data and related steps are  
covered in the IBM Code pattern below:  
* [Statistical Change point detection - Overview](https://developer.ibm.com/code/journey/detect-change-points-in-iot-sensor-data/)  
* [Statistical Change point detection - Code and HowTo](https://github.com/IBM/detect-timeseriesdata-change)  


One step further, using Advanced Analytics, predictive models can be built that could predict a failure  
condition in an equipment or a system like say a Compressor in a refrigeration unit well ahead of time.  
   
This approach goes a long way in implementing Predictive maintenance which is more prudent approach   
than Scheduled Preventive maintenance which is periodic in nature.  
Predictive Analytics on IoT is covered in the journey below:  
* [Equipment failure Prediction using IoT Sensor data - Overview](https://github.com/IBM/iot-predictive-analytics)
* [Equipment failure Prediction using IoT Sensor data - Code and HowTo](https://github.ibm.com/developer-journeys/si-journey-iot-predictive-analytics)  
 
Also, by using multivariate data collected from different sensors mounted on an equipment, more   
sophisticated Predictive models can be built that can pinpoint upcoming failure of a specific   
equipment or subsystem.  
  
Once an anomaly is detected, a prescriptive action needs to be taken.  
This journey in specific covers, “Detecting the need for any corrective action and then  
communicating “Decisions based on Analytics insights to the edge for Automated Action”  


#### Prerequisites:  
Users who want to implement this IBM Code pattern are expected to have the below knowledge as  
Pre-requisites. Before proceeding, it is strongly suggested to familiarize yourself with the  
below pre-requisites.  
1.	[Node-RED]( https://nodered.org/):  
    a.	[Creating your first sample flow](https://nodered.org/docs/getting-started/first-flow)  
    b.	[Creating your second sample flow](https://nodered.org/docs/getting-started/second-flow)  
2.	Node-RED in IBM Cloud (previously IBM Bluemix):  
    a.	[Running Node-RED on IBM blue mix](https://nodered.org/docs/platforms/bluemix)  
    b.	[Deploying IoT platform starter on IBMcloud]( https://developer.ibm.com/recipes/tutorials/deploy-internet-of-things-platform-starter-service-on-bluemix/)  
3.	Node-RED on Raspberry Pi:  
    a.	[Running Node-RED on Raspberry Pi](https://nodered.org/docs/hardware/raspberrypi)  
4.	[Configure a Raspberry Pi with Watson IoT Platform and connect it to the cloud](https://www.youtube.com/watch?v=nlvAFwifU9c&feature=youtu.be)  
  

# 2 Flow
![png](doc/images/iea_arch_flow.png)

1.	Temperature Data is read from a sensor attached to an edge device, in our case a Raspberry Pi  
2.	.json files will be imported to create the Node-RED flows in the Edge layer  
3.	Node-Red running on Raspberry Pi will collect the Sensor data and dispatches to the  
    IBM IoT service in Cloud. Node-RDE flows in Raspberry Pi will also receive commands for  
	action from IoT platform in IBM Cloud and triggers action  
4.	IBM Internet of Things (IoT) platform running on IBM Cloud will receive the data from Raspberry Pi  
    and Analyzes the data to detect if any action needs to be taken at the edge  
5.	.json files will be imported to create the Node-RED flows in the IBM Cloud – IoT service  
6.	Node-RED flows running on IBM IoT platform will once again run the logic on the data and then  
    translate it into a action and communicate the action to be taken back to the edge layer, Raspberry Pi  
7.	Analytics logic to detecting the action to be taken at the Edge will be embedded in the Node-RED  
    flow in IBM Cloud – IoT service  
  
# 3 Included Components 
* [IBM Cloud](https://console.bluemix.net/catalog/): IBM's innovative cloud computing platform or IBM Cloud (formerly Bluemix) combines   
  platform as a service (PaaS) with infrastructure as a service (IaaS) and includes a rich catalog of  
  cloud services that can be easily integrated with PaaS and IaaS to build business applications rapidly.  
* [IBM Watson IoT Platform](https://internetofthings.ibmcloud.com/): IBM Watson™ IoT Platform for IBM Cloud gives you a versatile  
  toolkit that includes gateway devices, device management, and powerful application access. By using  
  Watson IoT Platform, you can collect connected device data and perform analytics on real-time data  
  from your organization.  
* [IBM Data Science Experience](https://www.ibm.com/bs-en/marketplace/data-science-experience): Analyze data using Python, Jupyter Notebook  
  and RStudio in a configured, collaborative environment that includes IBM value-adds, such as managed Spark.  

# 4	Featured Technologies

* [Analytics](https://developer.ibm.com/code/technologies/analytics?cm=IBMCode-_--_-featured_technologies-_-analytics): Finding patterns in data to derive information.  
* [Data Science](https://developer.ibm.com/code/technologies/data-science?cm=IBMCode-_--_-featured_technologies-_-data-science): Systems and scientific methods to analyze structured and unstructured data in  
  order to extract knowledge and insights.  

# 5	Watch the Video  
* [Video](Video - WIP)
 

# 6	Steps  

1.	User sets up Node-RED in Raspberry Pi and connect to Network
2.	User imports Node-RED flows in Raspberry Pi
3.	User configures Emitter,Receiver Node-RED flows in Raspberry Pi
4.	User signs up for IBM Internet of Things Starter service on IBM Cloud
5.	User imports Node-RED flows in IBM IoT Cloud service
6.	User configures Emitter Node-RED flows in IBM IoT Cloud service
7.	User checks the CPU temperature from Raspberry Pi transported to IBM IoT service
8.	User checks the action received at the Raspberry Pi Edge node from IBM IoT service

## 6.1	User sets up Node-RED in Raspberry Pi and connect to Network  
Follow this [Video]( https://www.youtube.com/watch?v=nlvAFwifU9c&feature=youtu.be) which will walk you through the below steps.  
1.	Setup and Connect Raspberry Pi to Local Wifi Network with Internet  
2.	Connect the Raspberry Pi to the same WiFi network as your Laptop  
3.	Login to Raspberry Pi from your Laptop using putty or any other SSH  
4.	Start Node-RED service on Raspberry Pi  
5.	Start IoT service in Raspberry Pi if not started already  
6.	On your laptop /desktop web browser, open the Node-RED web editor running on Raspberry by entering the URL  
    ”raspberrypi ip address:1880”. In the example shown below the IP address for Raspberry Pi is 192.168.1.26.  
	You can check your WiFi router (or horspot) configuration for the finding the Raspberry Pi IP address.  

## 6.2  User imports Node-RED flows in Raspberry Pi  

Import “Emitter” Node-RED flow “Rpi2BMX” in Raspberry Pi from [RPi2BMX.json](/configuration/RPi/RPi2BMX.json)  

![png](doc/images/iea_rpi2bmx_flow.png)  
  
Set the Device ID in the “event” IoT output node to “kpedgetobmx20171207”  
  
Import “Collector” Node-RED flow “BMX2RPi” on Raspberry Pi from [BMX2RPi.json](/configuration/RPi/BMX2RPi.json)  

![png](doc/images/iea_bmx2rpi_flow.png)  
  
## 6.3	User configures Emitter,Receiver Node-RED flows in Raspberry Pi  

In “BMX2RPi” flow, set the “Device ID” in the “Receive IBM IoT BMX command to Edge” node to “kpbmxtoedge20171207”  
Note that, this ID must be the same as the Device ID that will be set later in Node–RED flow in IBM Cloud  
  
## 6.4	User signs up for IBM Internet of Things Starter service on IBM Cloud  

Go to [IBM Cloud Catalog]( https://console.bluemix.net/catalog/) and type “node-red” in the search box.  
This displays a list of components that match the search criteria in IBM Cloud.  
Select the “Node-RED starter” Service  

![png](doc/images/iea_nodered_bmx.png)  
  
Fill in the details in the Node-RED service creation page  
![png](doc/images/iea_nodered_bmx_form.png)   
  
Select the 30 days trial plan and click “Create”  

![png](doc/images/iea_nodered_bmx_plan.png)    
The Node-RED service will be created under “Cloud Foundry App” and the service will be started by default.  
Click on “Visit App URL” in the Service status page.  
You will be asked for a User ID and password. This is for accessing the Node-RED flows that will be created by you in future.  
Enter a UserID and password and make a note of it. You will need it later when you relogin and work on your Node-RED flows.  
In the next page, you will be provided with options for browsing “Available Bluemix nodes”.  
Select “node-red-contrib-ibm-wiotp-device-ops”and click “Next”  

![png](doc/images/iea_nodered_bmx_iotp.png)   
![png](doc/images/iea_nodered_bmx_edlaunch.png)   

“Go to Node-RED flow editor”  
You will be presented with a blank Node-RED flow tab  
 
![png](doc/images/iea_nodered_bmx_blank.png)   
As a sample trial, drag and drop the input node that says “ibmiot” into the blank tab “Flow 1”.  
You can see a description of the functions of this node. You can experiment further to get yourself comfortable with  
the flow. Discard or Save any flow you might have created, we will be using from pre-built flows that are made available  
in the git repo.  


## 6.5	User imports Node-RED flows in IBM IoT Cloud service  
Import  the Node-RED flow  “BMXReceiveIoTTemp” from [BMXReceiveProcessIoTTemp.json](/configuration/BMX/BMXReceiveProcessIoTTemp.json)
 
![png](doc/images/iea_bmxreceiveiottemp_bmx_flow.png)   
  

## 6.6	User configures Emitter Node-RED flows in IBM IoT Cloud service  

Set the “Device ID” in the “ibmiot” node to “kpbmxtoedge20171207”   

![png](doc/images/iea_bmxreceiveiottemp_bmx_devid.png)    
  
# 7	Run the Node-RED flows and View the Results
* On RPi: Inject In ``RPi2BMX`` flow and see results in debug screen  
  ![png](doc/images/iea_rpi2bmx_results.png)   
* On BMX: Inject in ``BMXReceiveIoTTemp`` flow and see results in debug screen  
  ![png](doc/images/iea_bmxreceiveiottemp_results.png)   
* On RPi: Inject ``BMX2RPi`` flow and see results in debug screen  
  ![png](doc/images/iea_bmx2rpi_results.png)   
* Confirm the ouputs  

# 8	Troubleshooting  
See [Debugging.md](https://github.com/IBM/iot-edge-predictive-models-dsx/blob/master/DEBUGGING.md)  
  
# 9	License  
[Apache 2.0](https://github.com/IBM/iot-edge-predictive-models-dsx/blob/master/LICENSE)  
    
# 10	Further enhancements  

The following areas are suggested as further enhancement areas for a User to explore by self.  
These are consciously been omitted from this IBM Code pattern as thse will require additional  
hardware and knowledge of basic electronics   

* Inputs from Raspberry Pi GPIO pins can be used for reading temperature from a external Temperature sensor attached  
* Outputs to Raspberry Pi GPIO pins can be used for triggering action by external actuators  

  
  
  
#### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<End>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
  
  
  
  
# 5 Steps

Follow these steps to setup and run this developer journey. The steps are described in detail below.
1. [Sign up for the Data Science Experience](#1-sign-up-for-the-data-science-experience)
2. [Create Bluemix services](#2-create-bluemix-services)
3. [Create the Jupyter notebook](#3-create-jupyter-notebook)
4. [Add the data and configuraton file](#4-add-data-config-file)
5. [Run the notebook](#5-run-notebook)
6. [Download the results](#6-download-results)

## 5.1	Sign up for the Data Science Experience

Sign up for IBM's [Data Science Experience](http://datascience.ibm.com/). By signing up for the Data Science Experience, two services: ``DSX-Spark`` and ``DSX-ObjectStore`` will be created in your Bluemix account.  

## 5.2	Create Bluemix services
Create the Bluemix services by following the links below.
[Object Storage in Bluemix](https://console.ng.bluemix.net/catalog/services/object-storage)

  i.	Choose an appropriate name for the DB2 Warehouse ``Service Name`` and choose  ``Free`` Pricing Plan. Click on Create.
  
![png](doc/images/ipredict_db2_service_create.png)  
  
  ii.	Click on Object Storage service instance on ``Bluemix Dashboard``. Choose the ``region`` and create a Container unit using ``Add a container`` link.  
![png](doc/images/ipredict_db2_object_storage.png)
  
  iii.	Upload the [sample data file](https://github.com/IBM/iot-predictive-analytics/blob/master/data/iot_sensor_dataset.csv) in Object storage Container.

  
* [DB2 Warehouse on Cloud](https://console.bluemix.net/catalog/services/db2-warehouse-on-cloud)  
![png](doc/images/ipredict_db2_whse_oncloud.png)  
  
    i.	Once service is created, click on ``DB2 Warehouse on Cloud`` service instance on Bluemix Dashboard. Click ``Open`` to launch the Dashboard.
    ii.	``Load data`` into the DB2 Warehouse by selecting the sample data from ``My Computer -> browse files``.
    ![png](doc/images/ipredict_db2_browse_file.png)
    iii.	Click on ``Next`` from the panel, choose schema and then create a ``New Table``.
    ![png](doc/images/ipredict_db2_create_table1.png)

* [**Data Science Experience**](https://console.bluemix.net/catalog/services/data-science-experience)  
![png](doc/images/ipredict_dsx_experience_create.png)  

## 5.3	Create the Python Jupyter Notebook
Use the menu on the left to select ``My Projects`` and then ``Default Project``. Click on Add notebooks (upper right) to create a notebook.
*	Select the ``From URL`` tab.
*	Enter a name for the notebook.
*	Optionally, enter a description for the notebook.
*	Enter this Notebook URL:
https://github.com/IBM/iot-predictive-analytics/blob/master/notebook/watson_iotfailure_prediction.ipynb
*	Click the ``Create Notebook`` button.
    ![png](doc/images/ipredict_dsx_notebook_create.png)
* Upload the sample .json DSX configuration file to Object storage from URL:
    https://github.com/IBM/iot-predictive-analytics/blob/master/configuration/iotpredict_config.json

## 5.4	Add the configuration and data access details
Fix-up configuration parameter .json file name and values
Once the files have been uploaded into ``DSX-ObjectStore`` you need to update the variables that refer to the .json configuration files in the R - Jupyter Notebook.
In the notebook, update the DSX configuration .json file name in section 3.1.1 
  
![png](doc/images/ipredict_set_json_filename.png)
  
Edit the [DSX configuration .json file](https://github.com/IBM/iot-predictive-analytics/blob/master/configuration/iotpredict_config.json)
Update the ``paramvalue`` ONLY to suit your requirements and save the .json file
Retain the rest of the format and composition of the .json file
  
![png](doc/images/ipredict_json_file_sample.png)
    
The descriptions of the parameters that can be configured are as below.

i.	features: List of variable names that are independent ‘x’ variables for Prediction  
ii.	target: Target variable name that needs to be predicted ‘y’ with values in binary 1 or 0 form with 1 indicating a failure  
iii.	data_size: Percentage of sample data to be reserved for Testing in decimal form.
      Example: 0.7 indicates 70% of the data will be used for Training the model and 30% will be used as Test  data

* In section 3.1.2 of DSX notebook, Insert (replace) your own Object storage file credentials to read the .json configuration file
* Also replace the function name in the block that Read json configuration file in section 3.2

![png](doc/images/ipredict_insert_jsonconn.png)
![png](doc/images/ipredict_insert_filecreds.png)

#### Add the data and configuration to the notebook
Use ``Find and Add Data`` (look for the ``10/01`` icon) and its ``Connections`` tab. You must be able to see your database connection created earlier. From there you can click ``Insert to Code`` under the 'Data connection' list and add ibm DBR code with connection credentials to the flow.

![png](doc/images/ipredict_insert_dataconn.png)

Note: If you don't have your own data and configuration files, you can reuse our example in the "Read IoT Sensor data from database" section. Look in the /data/iot_sensor_dataset.csv directory for data file.
  
![png](doc/images/ipredict_insert_read_data_func.png)
  

# 6	Run the notebook
When a notebook is executed, what is actually happening is that each code cell in
the notebook is executed, in order, from top to bottom.

Each code cell is selectable and is preceded by a tag in the left margin. The tag
format is `In [x]:`. Depending on the state of the notebook, the `x` can be:

* A blank, this indicates that the cell has never been executed.
* A number, this number represents the relative order this code step was executed.
* A `*`, this indicates that the cell is currently executing.

There are several ways to execute the code cells in your notebook:

* One cell at a time.
  * Select the cell, and then press the `Play` button in the toolbar.
* Batch mode, in sequential order.
  * From the `Cell` menu bar, there are several options available. For example, you
    can `Run All` cells in your notebook, or you can `Run All Below`, that will
    start executing from the first cell under the currently selected cell, and then
    continue executing all cells that follow.
* At a scheduled time.
  * Press the `Schedule` button located in the top right section of your notebook
    panel. Here you can schedule your notebook to be executed once at some future
    time, or repeatedly at your specified interval.

# 7	View the results
The notebook outputs the results in the Notebook which can be copied to clipboard
The Training model Prediction accuracy is output in section 5.2
The overall prediction accuracy is output as a percentage

![png](doc/images/ipredict_train_model.png)  

If you are satisfied with the Training model accuracy, you can proceed further for scoring the Test data using the Trained model and analyze the results  
The Confusion matrix is computed on the results of the Testing for a dep dive understanding of the Model performance  

![png](doc/images/ipredict_confusion_matrix.png)  

Overall accuracy percentage gives the overall Prediction performance of the model.  
Sensitivity and Specificity of the model is also calculated along with absolute values of False positives and False Negatives to give the Data Scientist / Analyst an idea of predictive accuracy in the model.  
It can be checked if these are within thresholds for the specific application of the model or IoT equipment.  
  
# 8 Troubleshooting

[See DEBUGGING.md](DEBUGGING.md)
  
# 9 License

[Apache 2.0](LICENSE)

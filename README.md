# IoTMaintenance

## Motive ##
The purpose of this project is to predict the time until an internet of things (IoT) device will require maintenance or replacement so this can be prepared in advance.
I'll be using the 'Turbofan Engine Degradation Simulation Data Set' from NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/tech/dash/pcoe/prognostic-data-repository/).

## The Data ##
The data schema is as follows
![image](https://github.com/chrismcgale/IoTMaintenance/assets/56483395/76b44dcf-832f-4fe9-a6b8-4aefdb9ec9eb)

The original data source has input data is spread across 3 files "train_FD001.txt", "test_FD001.txt", and "RUL_FD001.txt". 
The ith line of the "RUL" data represents the number of cycles remaining for the test device with id i. We'll have to join these tables when the time comes.

## Selected features ## 
I'll be using all given features except the id and cycle# as input variables for my models.

## Aggregate features ##
To see a degredation in sensor data over time, I'll be aggregating sensor values into a weighted average over the past 5 cycles. Hopefully this will allow my model to forecast an imprending breakdown.

## Labels ##
I'll be using 2 types of labels 1. Number of cycles remaining and 2. Whether the number of cycles remaining is below some threshold.

## Models ##
For the number of cycles remaing I'll be using a random forest regression. For whether or not the machine is below some threshold I'll be using a logistic regression.

# Results #
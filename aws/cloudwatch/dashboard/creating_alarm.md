# How to create a cpu usage alarm

1. Go to CloudWatch console
2. In the navigation pane, select **Alarms**, then **All Alarms**  
   <img height="180" src="images/all_alarms.png"/>
3. Choose **Create Alarm**  
![](images/create_alarm.png)
4. Choose **Select metric**  
   <img height="160" src="images/select_metric.png"/>
5. In the **All metrics**
   1. Select the **EC2** tab  
![](images/ec2.png)
   2. Select **Per-Instance Metrics**  
![](images/per_instance.png)
   3. In the search bar paste in the id of your instance
   4. Scroll to find the metric named **CPUUtilization**  
![](images/cpu_usage.png)
   5. Select Metric
6. In Specify metric and conditions
![](images/metric_conditions.png)
![](images/conditions.png)
   1. **Metric** - **Statistic** check that it is set to average.
   2. **Conditions** - **Threshold type** keep that as static
   3. Select the threshold you require for your alarm, the number value as well as the condition.
   4. Select **Next**
7. Notifications
![](images/notifications.png)
   1. Select **In Alarm**
   2. **Create new topic**
   3. Enter topic name
   4. Enter email to notify
   5. Next
8. Name and Description
![](images/name_desc.png)
   1. Enter the name of your alarm
   2. Enter a description explaining what the alarm is for
9. Confirm subscription for the alarm SNS topic by going to your email you should find an email that looks the same as below.
![](images/notification_confirm_email.png)
10. Receiving alarms once the threshold is met, you will recieve another email that will look like:
![](images/alarm_email.png)


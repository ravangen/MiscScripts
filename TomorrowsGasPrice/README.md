Tomorrows Gas Prices
==============

There are multiple gas price prediction services available online and for mobile applications, but accessing this information from "dumb" cell phones is difficult, especially on the go without a data plan. To address this problem, use [SmsGasPrices.py] to daily send a sms message to your cell phone with tomorrow's gas price prediction.

### Script Requirements ###

* To send text messages, we use [Twilio](https://www.twilio.com/). You can get a trial/test or paid account
* To easily interact with Twilio, install the [Twilio Python helper library](https://www.twilio.com/docs/python/install)
    * ``` pip install twilio ```
* To retrieve prediction data from online services, install [requests](https://pypi.python.org/pypi/requests)
    * ``` pip install requests ```
* To parse prediction data, install [Beautiful Soup 3](http://www.crummy.com/software/BeautifulSoup/)
    * ``` pip install BeautifulSoup ```

### Script Setup ###
* Update the script with your Twilio credentials associated phone number
* Update ```users``` array to contain the cell numbers to receive text messages and cities of interest to include in each message

### Automating a Daily SMS ###

To make the most of [SmsGasPrices.py], schedule the script to run in Task Scheduler. For example, [SampleTaskSchedulerDefinition.xml] is a Task Scheduler definition to run the python script every day at 5pm. Just modify the user from *laptop\Robert* to *<computer_name>\<user_name>* and the executed command to be the local path to SmsGasPrices.py.

[SmsGasPrices.py]:SmsGasPrices.py
[SampleTaskSchedulerDefinition.xml]:SampleTaskSchedulerDefinition.xml

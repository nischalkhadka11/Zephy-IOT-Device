Project implementation
Requirements: 
Powerbank
Raspbeeri Pi
Roboloq Qoopers
6 AA batteries

Actators:
Fan
Heater
Ventilator
Humidifier
Mini Fan

Sensors:
SGP30 sensiron sensor
DHT11 Sensor
Grove pi Dust sensor
Grove pi Air quality sensor

STEP by Step guide
STEP 1.Connect IOT SENSORS in RASPBERRI PI
1) DHT11 sensor on Digital Port 1
2) SGP30 sensor on I2C port 2
3) LCD grab sensor on I2c Port 1
4) Dust sensor on Digital Port D7
5) Mini fan on Digital Port 8
6) Green LED on DIgital port 4
7) Light Sensor on Analog port 2
8) Air quality Sensor on Analog Port 1 
 STEP 2:MAKe Robobloq Qoopers using the guidelines by the user manual

STEP 3: Connect LED SCREEN and Ultra sensor of Robot on PORT 5 and 7 in QArduino on Robobloq

STEP 4: Mount Raspberri pi on top of Robot and connect it to portable powerbank for power supply

Step 5: Connect actuators as fan , heater , vetilators using the Kasa Plug and Wyze Plug

Step 6: Start node res using node-red-start and start grafana and influxDB

Step 7: Turn on  Robobloq

Step 8: See the actuators change its state in the grafana Dashboard 

PLATFORM USED: 
Node-red
QOBO - robot movement
grafana
influxDB

API USED: Kasa plug API/ Wyze API

Cloud Platform services used: Wyze/ Kasa authentication
Grafana Dashboards

Scripts:
Pytho nscripts for Wyze connection

Functionality: node-red flows

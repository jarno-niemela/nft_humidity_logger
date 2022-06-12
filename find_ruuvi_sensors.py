from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from pprint import pprint
import json

counter = 10
# RunFlag for stopping execution at desired time
run_flag = RunFlag()

found_sensors=dict()

def handle_data(found_data):
    global counter
    counter = counter - 1
    if counter < 0:
        run_flag.running = False

    if found_data[0] not in found_sensors:
        found_sensors[found_data[0]]=found_data[1]
        print('MAC ' + found_data[0])
        print(found_data)

# List of macs of sensors which will execute callback function
RuuviTagSensor.get_datas(handle_data, run_flag=run_flag)


sensor_count=0
for sensor in found_sensors :
    sensor_count+=1
    with open("found_sensor_%d.json"%sensor_count,"w") as output:
        sensor_data=dict()
        sensor_data["type"] = "ruuvitag"
        sensor_data["id"] = sensor
        sensor_data["name"] = "sensor name"
        json.dump(sensor_data,output)


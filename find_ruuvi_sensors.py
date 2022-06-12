from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from pprint import pprint

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

pprint(found_sensors)
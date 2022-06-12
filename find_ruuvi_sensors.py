    from ruuvitag_sensor.ruuvi import RuuviTagSensor

    def handle_data(found_data):
        print('MAC ' + found_data[0])
        print(found_data[1])

    if __name__ == '__main__':
        print("Scanning devices")
        RuuviTagSensor.get_datas(handle_data)

import menteepybind.pyCandle as pyCandle
from doorman.doorman import Doorman
from doorman.motors_list import MotorsList as ML
from doorman.utils import show
import os

"""
This is the main file of the project.

1. It connects to the CANDLE

2. It builds a motors dictionary from the ping

3. It starts a Doorman thread that communicates with the CANDLE
** The CANDLE requires some info like impedance params, watchdog params, etc. Write it in the yaml files (added for example) **

4. It gets user input and sends it to the Doorman thread


 You can now activate the motors from the command line by typing the motor's id and the desired position

"""


def main(): 
    # Connect to CANDLE 
    candle = pyCandle.CandleHandler(pyCandle.CANdleBaudrate_E.CAN_BAUD_1M, pyCandle.BusType_E.USB, "", False)

    # Build motors dictionary from ping
    motors_dict = ML(candle.ping(pyCandle.CANdleBaudrate_E.CAN_BAUD_1M)).motors_dict 

    # Start Doorman thread
    Doorman(candle, motors_dict)

    # Gets user input (Motor id and desired position) and sends it to the Doorman thread, 0 to exit
    show(motors_dict)
    motor_input = input("Enter motor id (0 to exit): ")
    if motor_input == "0":
        print("Exiting...")
        os._exit(1)
    id = int(motor_input)
    show(motors_dict)
    while True:
        position_input = input("Enter desired position (e to exit):)")
        if motor_input == "e" or motor_input == "E":
            print("Exiting...")
            os._exit(1)
        desired_pos = float(position_input)
        if desired_pos > -80.0 and desired_pos < 80:          # Hard limits
            motors_dict[id].desired_pos = desired_pos
            show(motors_dict)

if __name__ == "__main__":
    main()

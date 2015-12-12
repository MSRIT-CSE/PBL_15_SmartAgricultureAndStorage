import RPi.GPIO as GPIO
import dht11
import time
from ubidots import ApiClient

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(19,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.IN)
#Create an "API" object

api = ApiClient("f0aee71e9c7d1ca8e792c1b39cb90448d734d76c")

#Create a "Variable" object

test_variable = api.get_variable("5669177d76254278e8150f21")
test1_variable = api.get_variable("56695d66762542112ed97c2b")
test2_variable = api.get_variable("56695d56762542128eb5dbfb")
test3_variable = api.get_variable("566973c876254243f3602899")


# read data using pin 8
instance = dht11.DHT11(pin = 8)
result = instance.read()
result1= GPIO.input(19)
time.sleep(0.1)
current_state = GPIO.input(7)

if result.is_valid():
        test_variable.save_value({'value':result.temperature})
        test2_variable.save_value({'value':result.humidity})
       
else:
    print("Error: %d" % result.error_code)

while True:
	 test1_variable.save_value({'value':result1})
         test3_variable.save_value({'value':current_state})
~
~

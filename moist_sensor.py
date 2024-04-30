# Moist sensor. 
# Bruger MCP302 klassen.

# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-soil-moisture-sensor


# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-soil-moisture-sensor


import time
import ADC_MCP302

# Create an ADS1115 ADC object
adc = ADC_MCP302.MCP3021



# Set the gain to ±4.096V (adjust if needed)
GAIN = 1

# Main loop to read the analog value from the soil moisture sensor and print the raw ADC value
try:
    while True:
        raw_value = adc.readRaw()
        # Print the raw ADC value
        print("Raw Value: {}".format(raw_value))

        # Add a delay between readings (adjust as needed)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting the program.")

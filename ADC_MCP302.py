import smbus2
import time

class MCP3021:
    bus = smbus2.SMBus(1)
    
    def __init__(self, address = 0x49):
        self.address = address
        
    def readRaw(self):
        # Reads word (16 bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # Exchanges high and low bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # Ignores two least significiant bits
        return data >> 2
    
adc = MCP3021()

# while True:
#     raw = adc.readRaw()
#     print("Raw :", raw)
#     time.sleep(1)
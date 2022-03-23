import pymeasure
import pymeasure

v = pymeasure.__version__
print(v)

dmm = Agilent34450A("USB0::...")
dmm.reset()
dmm.configure_voltage()
print(dmm.voltage)
dmm.shutdown()
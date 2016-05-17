import sys
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4

humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperatura, humedad))

sys.exit(1)

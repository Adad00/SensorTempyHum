import sys

import Adafruit_DHT


sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('uso: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('ejemplo: sudo ./Adafruit_DHT.py 2302 4 - Lee de un sensor AM2302 conectado al GPIO #4')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


if humidity is not None and temperature is not None:
    print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity))
else:
    print('Fallo al leer los datos. Intentalo nuevamente!')
    sys.exit(1)

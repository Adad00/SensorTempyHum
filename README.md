Libreria para sensor Temp  y Humedad Adafruit Python DHT 
===========================================================

Archivos necesarios para la instalacion de la libreria para usar el senso de Temperatura y Humedad en Raspberry Pi y script de python para hacer uso del sensor impriendo en pantalla los resultados.

Para instalar la libreria es con el comando: 
````
sudo python setup.py install
````

Para correr el script en el directorio ejemplo es con el comando:
```` 
sudo python tempyhum.py 
````




Libreria tomada de Adafruit*
***************************************************************************
Python library to read the DHT series of humidity and temperature sensors on a Raspberry Pi or Beaglebone Black.

Designed specifically to work with the Adafruit DHT series sensors ----> https://www.adafruit.com/products/385

Currently the library is only tested with Python 2.6/2.7.

For all platforms (Raspberry Pi and Beaglebone Black) make sure your system is able to compile Python extensions.  On Raspbian or Beaglebone Black's Debian/Ubuntu image you can ensure your system is ready by executing:

````
sudo apt-get update
sudo apt-get install build-essential python-dev
````

Install the library by downloading with the download link on the right, unzipping the archive, and executing:

````
sudo python setup.py install
````

See example of usage in the examples folder.

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution

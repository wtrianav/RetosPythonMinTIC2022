# IoT
Una **smart-home** es una casa que tiene una serie de dispositivos IoT que permiten el manejo de diferentes dispositivos del hogar como: electricos (luces, toma corrientes, etc.), sensores (humedad, temperatura, etc.) y alarmas (movimiento, apertura, etc.)

Cada smart-home envía un reporte de los estados de sus dispositivos IoT para que sean procesados en un servidor central; estos datos son enviados en una cadena de caracteres con el siguiente formato:

*"tipo_dispositivo1,identificador1,estado1@tipo_dispositivo2,identificador2,estado2@..."*

*  Los tipos de dispositivos pueden ser: electricos, sensor y alarma
*  El identificador puede ser: luces, tomas, entre otros, para los dispositivos de tipo electrico. humedad, temperatura entre otros para sensores y finalmente movimiento, apertura entre otros para alarmas.
*  El estado solo tiene dos valores ON y OFF

## ¿Que debo hacer?
El primer proceso que debe hacerse es separar los elementos que vienen en la cadena, para ello se deben utilizar namedtuples. Luego debe sacar un reporte de la cantidad de sensores que están en estado ON y los que están en estado OFF.

## Algunos tips
* Para separar la cadena puede utilizar la función [split()](https://www.w3schools.com/python/ref_string_split.asp)
* En el archivo smarth_home.py esta la línea base para el desarrollo de la aplicación-








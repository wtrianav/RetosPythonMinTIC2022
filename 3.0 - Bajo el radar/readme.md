# El radar
El funcionamiento de los radares de velocidad se basa en un principio básico de la cinetica que establece

`velocidad = espacio/tiempo`

El radar envía dos haces de luz en un lapso de tiempo (en segundos) y obtiene la distancia del vehículo al radar en cada haz de luz enviado, así puede calcular la velocidad del vehículo y establecer si está en los límites permitidos o por el contrario debe ser multado. El radar toma estos datos en metros 

## ¿Que debo hacer?
Utilizar el método IDEAL para 
implementar un programa que: 

### Multa velocidad 
Dadas las dos distancias obtenidas del vehículo y el lapso de tiempo, calcular si debe pagar una multa de acuerdo a la siguiente tabla  
  
| Velocidad (Km/h) |Multa | 
| :---: | :---: | 
| de 1 a 20 | llamado de atención por baja velocidad |
| de 21 a 60 | Normal |
| de 61 a 80 | llamado de atención por alta velocidad |
| de 81 a 120 |multa tipo I |
| masd de 120 | multa tipo II e inmovilización del vehículo |


### Multa alcoholemia 

En caso de multa por velocidad se le practica un examen de alcoholemia al conductor que acarrea multas adicionales de acuerdo a la siguiente norma


*   Entre	 20	 y	 39	 mg	 de	 etanol/l00	 ml	 de	sangre	 total,	 además	 de	 las	 sanciones	
previstas	en	la	presente	ley,	se	decretará	la	suspensión	de	la	licencia	de	conducción	
entre	seis	(6)	y	doce	(12)	meses.


*  Primer	 grado	 de	 embriaguez	 entre	 40	 y	 99	 mg	 de	 etanol/100	 ml	 de	 sangre	 total,	
adicionalmente	 a	 la	 sanción	 multa,	 se	 decretará	 la	 suspensión	 de	 la	 Licencia	 de	
Conducción	entre	uno	(1)	y	tres	(3)	años.


*  Segundo	grado	de	embriaguez	entre	100	y	149	mg	de	etanol/100	ml	de	sangre	total,	
adicionalmente	 a	 la	 sanción	 multa,	 se	 decretará	 la	 suspensión	 de	 la	 Licencia	 de	
Conducción	 entre	 tres	 (3)	 y	 cinco	 (5)	 años,	 y	 la	 obligación	 de	 realizar	 curso	 de	
sensibilización,	conocimientos	y	consecuencias	de	la	alcoholemia	y	drogadicción	en	
centros	de	rehabilitación	debidamente	autorizados,	por	un	mínimo	de	cuarenta	(40)	
horas.


* Tercer	 grado	 de	 embriaguez,	 desde	 150	 mg	 de	 etanol/100	 ml	 de	 sangre	 total	 en	
adelante,	 adicionalmente	 a	 la	 sanción	 de	 la	 sanción	 de	 multa,	 se	 decretará	 la	
suspensión	 entre	 cinco	 (5)	 y	 diez	 (10)	 años	 de	 la	 Licencia	 de	 Conducción,	 y	 la	
obligación	de	realizar	curso	de	sensibilización,	conocimientos	y	consecuencias	de	la	
alcoholemia	 y	drogadicción	en	 centros	de	 rehabilitación	debidamente	autorizados,	
por	un	mínimo	de	ochenta	(80)	horas.

---
# IMPORTANTE
---
*   Implementar la solución aplicando el método IDEAL
*   Las funciones deben ir en el módulo `multas.py`
*   El punto de entrada a la aplicación debe estar en el archivo `main.py` 
*  En la implementación de la función que calcula la multa de velocidad debe hacer un llamado a la función de la función que calcula la multa de alcoholemia.  

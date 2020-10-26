# DC4-D1

## Problema 🚀

El  objetivo  del  presente  reto  es  atacar  una  condición  recurrente  de  compromiso  de usuarios, que, como eslabón más débil de la cadena puede desembocar en daños irreparables para una  empresa,  nos  referimos  al  Phishing  y  su  particularidad  que  es  la  de  robo  de  credenciales, específicamente mediante un formulario web.
### Requerimientos 📋
Python 3.0
```
pip install scapy
```
### Uso 📋
```
python algoritmo.py -p file.pcap -d dominio.com
```
## Estado 🚀
Actualmente se encuentra en estado de PoC, se logro determinar si el usuario ingresa a un sitio web, sin certificado o con certificado SSL/TLS, para la verificación de datos ingresados se lo identifica observando la respuesta de la api de google (checkgooglepasswordlist), petición que es enviada al momento de realizar un POST en cualquier formulario

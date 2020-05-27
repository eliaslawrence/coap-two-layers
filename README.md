# coap-server
PhD Work for IoT Class (2020).
## Requisitos

- [Python 2.7.16](https://www.python.org/download/releases/2.7/)
- [CoAPthon](https://github.com/Tanganelli/CoAPthon)
- [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)

## Instalação

PIP no Debian/Ubuntu
```
$ sudo apt-get install python-pip   #python 2
```

CoAPthon no Debian/Ubuntu
```
$ sudo pip install CoAPthon
```

## Operação

<p align="center">
  <img src="/imgs/diagram.png" width="100%">  
</p>
<p align="center">
  <em>Diagrama de operação da aplicação com CoAP</em>
</p>

### Cliente ([client.py](https://github.com/eliaslawrence/coap-server/blob/master/client.py))

As aplicações CLIENTE acessam o servidor enviando os valores de threshold de temperatura e pressão.

- POST
```
$ python client.py -P POST -p coap://<server-ip-here>:<server-port-here>/<resource> -P <payload>
```

- GET
```
$ python client.py -P GET -p coap://<server-ip-here>:<server-port-here>/<resource>
```

### Servidor ([server.py](https://github.com/eliaslawrence/coap-server/blob/master/server.py))

O servidor é inicializado com apenas 2 recursos disponíveis: threshold para temperatura e threshold pra pressão.

Através de um método POST para o resource **/temp** do servidor, passando como payload um valor de temperatura, o cliente altera o threshold de temperatura.

Através de um método POST para o resource **/pres** do servidor, passando como payload um valor de pressão, o cliente altera o threshold de pressão.

<p align="center">
  <img src="/imgs/sensehat.png" width="300">  
</p>
<p align="center">
  <em>Servidor em estado IDLE</em>
</p>

Caso os valores do emulador de temperatura e pressão ultrapassem os limiares determinados pelas aplicações CLIENTE, os LEDs se acendem na cor vermelha, conforme imagem abaixo.

<p align="center">
  <img src="/imgs/sensehat1.png" width="300">  
</p>
<p align="center">
  <em>Valores de temperatura e/ou pressão acima do THRESHOLD</em>
</p>

- Inicializar

Antes de inicializar o programa, o emulador [Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) deve estar rodando na máquina. 

```
$ python server.py <server-ip-here> <server-port-here>
```

## Exemplo

- IP do servidor: 192.168.25.4
- Porta do servidor: 5683

- Inicialize o Sense HAT Emulator 
- Inicializa servidor

```
$ python server.py 192.168.25.4 5683
```

- A temperatura e pressão podem ser alteradas pelo emulador

### Cliente

- Sete threshold de temperatura: 50

```
$ python client.py -P POST -p coap://192.168.25.4:5683/temp -P 50
```

- Sete threshold de pressão: 1100

```
$ python client.py -P POST -p coap://192.168.25.4:5683/pres -P 1100
```

- Os limiares de temperatura e pressão podem ser alteradas pelo método POST.

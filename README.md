# Escáner de Puertos TCP en Python

## Descripción

Este proyecto consiste en el desarrollo de un escáner de puertos TCP utilizando Python y la biblioteca `socket`. El programa permite ingresar una dirección IP y un rango de puertos para identificar cuáles se encuentran abiertos.

El escáner fue desarrollado con fines académicos y debe utilizarse únicamente en equipos y redes propias o expresamente autorizadas.

## Objetivo

Desarrollar una herramienta básica en Python que permita comprobar el estado de puertos TCP de una dirección IP mediante conexiones de red utilizando sockets.

## Requisitos

- Python 3
- Visual Studio Code
- Biblioteca `socket` incluida en Python
- Sistema operativo Windows

## Funcionamiento

El programa solicita al usuario:

1. Dirección IP que desea analizar.
2. Puerto inicial.
3. Puerto final.

La dirección IP ingresada es validada antes de iniciar el proceso. También se verifica que el rango de puertos sea válido.

Para cada puerto se crea un socket TCP mediante:

`socket.AF_INET` y `socket.SOCK_STREAM`

El método `connect_ex()` intenta establecer la conexión. Cuando devuelve el valor `0`, el puerto se identifica como abierto.

## Ejecución

Ejecutar el archivo:

`scanner_puertos.py`

Ejemplo de datos utilizados durante las pruebas:

- IP: `127.0.0.1`
- Puerto inicial: `8075`
- Puerto final: `8085`

Para comprobar el funcionamiento del escáner se habilitó temporalmente un servidor HTTP local en el puerto `8080`.

El escáner detectó correctamente:

`Puerto 8080 ABIERTO`

## Resultados

El programa presenta al finalizar:

- IP analizada.
- Rango de puertos analizado.
- Total de puertos abiertos.
- Lista de puertos abiertos encontrados.

## Seguridad

El escaneo de puertos debe realizarse únicamente sobre sistemas propios o cuando exista autorización. Esta herramienta fue implementada como práctica académica para comprender el funcionamiento de los puertos TCP, sockets y técnicas básicas de análisis de red.

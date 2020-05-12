import requests
import json
import os

#Para realizar este ejercicio he optado por elegir la siguiente página: https://date.nager.at/
#Esta página proporciona información sobre las diferentes fiestas nacionales de diferentes paises y de diferentes años
#La verdad es que de primeras me ha costado cogerlo, pero lo voy entendiendo, pero faltan conocimientos, como a la hora
#de querer realizar un recuento de todas fiestas que puede haber en una año en país determinado, pero he intendado
#hacerlo como tu, para ir entendiendolo mejor a la hora de hacerlo yo solo

try:

    def mostrar_fiestas():
        url="https://date.nager.at/api/v2/publicholidays/2019/ES"

        response = requests.get(url)

        if response.status_code == 200:
            datos = json.loads(response.content)
            contador=1
            for json_data in datos:
                print ("Nombre Fiesta : ",json_data['localName'],"\tTipo :",json_data['type'],"\tPrimer anyo de celebración : ",json_data['launchYear'])
                contador=1+contador
                if contador>6:
                    break

    def mostrar_anyo():
        anyo = int(input("Introduce un año: "))

        url="https://date.nager.at/api/v2/publicholidays/%s/ES"%anyo

        response = requests.get(url)

        if response.status_code == 200:
            datos = json.loads(response.content)
            contador=1
            for json_data in datos:
                print ("Nombre Fiesta : ",json_data['localName'],"\tTipo :",json_data['type'],"\tPrimer anyo de celebración : ",json_data['launchYear'])
                contador=1+contador
                if contador>6:
                    break

    def mostrar_otro():
        print("Indique sus siglas, ejemplo: España = ES")
        pais = int(input("Seleccione el País que desee: "))

        url="https://date.nager.at/api/v2/publicholidays/2019/%s"%pais

        print(url)

        response = requests.get(url)

        if response.status_code == 200:
            datos = json.loads(response.content)
            contador=1
            for json_data in datos:
                print ("Nombre Fiesta : ",json_data['localName'],"\tTipo :",json_data['type'],"\tPrimer anyo de celebración : ",json_data['launchYear'])
                contador=1+contador
                if contador>6:
                    break



    while True:
        os.system('cls')
        print("1. Mostrar fiestas de España de 2019")
        print("2. Mostrar fiestas de España de un año determinado")
        print("3. Mostrar fiestas de un país determinado")
        print("4. Salir")
        opc=int(input("Seleccione una opción: "))

        if opc == 1:
            mostrar_fiestas()
        elif opc == 2:
            mostrar_anyo()
        elif  opc == 3:
            mostrar_otro()
        elif opc == 4:
            print("Gracias por su visita")
            break
        else:
            print("Opción no disponible")
            input("Pulse para continuar")

except:
    print("Se ha producido un error")
            
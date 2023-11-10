# code meteo
import requests


import json


from datetime import datetime

 


api_key = '7c0285446e8bff2402e8c943c46e26ef' 


city = 'Montpellier'


url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  

 

response = requests.get(url)


data = response.json() #mettre les données dans un dictionnaire

 

print("Bienvenue dans l'application météo !\nVoulez vous ajouter la méteo Actuelle (Tapez 1) ou prévoir la météo des prochains jours (Tapez 2) ?")


leChoix = int(input("Votre choix :"))

 
# partie peut-être inutile mais pour l'instant on la garde
if leChoix == 1:


       


   

 

    if response.status_code == 200:


       


        weather_description = data['weather'][0]['description']


        temperature = data['main']['temp']


        humidity = data['main']['humidity']


        wind_speed = data['wind']['speed']

 

        print(f'Météo à {city}:')


        print(f'Description: {weather_description}')


        print(f'Température: {temperature}°C')


        print(f'Humidité: {humidity}%')


        print(f'Vitesse du vent: {wind_speed} m/s')


       


        # Obtenir date et heure actuelles


        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

 

        # Charger les données existantes à partir du fichier JSON


        try:


            with open('/Users/jeanne/Desktop/meteo/testgithubdesktop/meteo.json', 'r') as file: 


                meteo_data = json.load(file)


        except FileNotFoundError:


            meteo_data = []

 

        # Ajouter les nouvelles données à la liste des données météorologiques


        meteo_data.append({


            'city': city,


            'description': weather_description,


            'temperature': temperature,


            'humidity': humidity,


            'wind_speed': wind_speed,


            'timestamp': current_time,  # Ajoutez la date et l'heure


            'prevision': False


        })

 

        # Enregistrer les données dans le fichier JSON


        with open('/Users/jeanne/Desktop/meteo/testgithubdesktop/meteo.json', 'w') as outfile:#A REMPLACER


            json.dump(meteo_data, outfile, indent=4)


    else:


        print('Impossible de récupérer les données météorologiques.')











 
elif leChoix == 2:


     # Code pour l'option 2 (prévisions des prochains jours)


    # Endpoint pour obtenir les prévisions des prochains jours


    url = f'http://api.openweathermap.org/data/2.5/ChaquePrevision?q={city}&appid={api_key}&units=metric'


    response = requests.get(url)


    data = response.json()

 

    if response.status_code == 200:


        ListeDePrevision = data['list']

 

        print(f'Prévisions météorologiques pour les prochains jours à {city}:')


        for ChaquePrevision in ListeDePrevision:


            date = ChaquePrevision['dt_txt']  # Date de la prévision


            weather_description = ChaquePrevision['weather'][0]['description']


            temperature = ChaquePrevision['main']['temp']


            humidity = ChaquePrevision['main']['humidity']


            wind_speed = ChaquePrevision['wind']['speed']

 

            print(f'Date: {date}')


            print(f'Description: {weather_description}')


            print(f'Température: {temperature}°C')


            print(f'Humidité: {humidity}%')


            print(f'Vitesse du vent: {wind_speed} m/s')


            print('---')

 

            # Obtenir la date actuelle


            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

 

            # Charger les données existantes à partir du fichier JSON


            try:


                with open('/Users/jeanne/Desktop/meteo/testgithubdesktop/meteo.json', 'r') as file:


                    meteo_data = json.load(file)


            except FileNotFoundError:


                meteo_data = []

 

            # Ajouter les nouvelles données à la liste des données météorologiques


            meteo_data.append({


                'city': city,


                'description': weather_description,


                'temperature': temperature,


                'humidity': humidity,


                'wind_speed': wind_speed,


                'timestamp': date,  # Utilisez la date de la prévision


                'prevision': True


            })

 

            # Enregistrer les données dans le fichier JSON


            with open('/Users/jeanne/Desktop/meteo/testgithubdesktop/meteo.json', 'w') as outfile:


                json.dump(meteo_data, outfile, indent=4)


    else:


        print('Impossible de récupérer les données météorologiques.')








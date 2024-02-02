import requests





def place(city):
    url = f'https://goweather.herokuapp.com/weather/{city}'
    
    req = requests.get(url)
    data = req.json()
    text = f"""{city}
Temperature : {data['temperature']}
Wind : {data['wind']}
Today : {data['description']}
    """
    return text

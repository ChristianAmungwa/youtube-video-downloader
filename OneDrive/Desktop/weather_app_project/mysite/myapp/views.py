from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # api key might be expired use your own api_key
        #    place api_key in place of appid ="your_api_key_here "  
  
        # source contain JSON data from API


  
        source = urllib.request.urlopen(('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4a4652418a4c8dbc54ba6088988d87e5&units=metric').replace(' ', '%20')).read()

        

        #updated_source = source.replace(' ', '')

  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        #list_of_data = json.loads(updated_source)
  
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
        #print(data.replace(' ', ''))


    else:
        data ={}
    return render(request, 'myapp/index.html', data)

    


'''

def index2(request):
    if request.method == 'POST':
        city = request.POST['city']
        # api key might be expired use your own api_key
        #    place api_key in place of appid ="your_api_key_here "  
  
        # source contain JSON data from API


  
        source = urllib.request.urlopen(('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4a4652418a4c8dbc54ba6088988d87e5&units=metric').replace(' ', '%20')).read()

        

        #updated_source = source.replace(' ', '')

  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        #list_of_data = json.loads(updated_source)
  
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
        #print(data.replace(' ', ''))


    else:
        data ={}
    return render(request, 'myapp/index.html', data)    

'''
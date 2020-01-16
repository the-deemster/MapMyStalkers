import requests 
import GeoScriptAPIKey
def findAndPrint(result, response):
	str="" 
	num = 10
	 
	for element in range(result , len(response.text)):
		
		if(response.text[element] == '\"'):
			break;
		str+=response.text[element]
	return str
def geoLocationScript(text): 
	 
	lines = []
	num = 0
	for line in text:
		string = ""
		url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
		
		str1 = str(line.strip())
		querystring = {"ip":str1}
		headers = {
			'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
			'x-rapidapi-key': GeoScriptAPIKey.getAPIKey()
			} 
		response = requests.request("GET", url, headers=headers,params=querystring)
		state = "region\":\""
		latitude = "\"latitude\":\""
		longitude = "\"longitude\":\""
		city = "city\":\""
		country = "country\":\""
		if(response.text.find(country)== -1):
			return "404"
		result = response.text.find(latitude) + len(latitude) 
		string +="var marker = new H.map.Marker({lat:" + findAndPrint(result, response)
		result = response.text.find(longitude) + len(longitude)
		string +=", lng:" + findAndPrint(result, response)
		string += "});map.addObject(marker);"
		 
		 
		#num+=1
		lines.append(string)
		 
		if(num >=2):
			break
	return lines
     
	return lines
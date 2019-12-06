import requests 

def findAndPrint(result, response):
	str="" 
	num = 10
	 
	for element in range(result , len(response.text)):
		
		if(response.text[element] == '\"'):
			break;
		str+=response.text[element]
	return str
def geoLocationScript(text): 
	print("your in")
	lines = []
	num = 0
	for line in text:
		string = ""
		url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
		
		str1 = str(line.strip())
		querystring = {"ip":str1}
		headers = {
			'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
			'x-rapidapi-key': "686f776c45msh6cdb33dd9424ad1p15ed09jsnb6c766735c05"
			} 
		response = requests.request("GET", url, headers=headers,params=querystring)
		state = "region\":\""
		city = "city\":\""
		country = "country\":\""
		
		string += "***********************************************<br>"
		string +="ip address:\t"+str1+"<br>"
		
		if(response.text.find(country)== -1):
			return "404"
		result = response.text.find(country) + len(country)
		string +="county: " + findAndPrint(result, response)+"<br>"
		result = response.text.find(state) + len(state)
		if(findAndPrint(result, response).find("\\")== -1): 
			string +="region: " + findAndPrint(result, response)+"<br>"
		result = response.text.find(city) + len(city)
		if(findAndPrint(result, response).find("\\")== -1):
			string +="city: " + findAndPrint(result, response)+"<br>"
		num+=1
		lines.append(string+"<br>")
		if(num >=10):
			break
	return lines
     
	return lines
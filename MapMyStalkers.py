from flask import Flask, request, render_template
import sudonFindIPScript
import apiGeoScriptLatLng
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('submitIP.php')
@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	processed_text = text.upper()
	lines = sudonFindIPScript.sudanFunction(text.strip())
	if(lines == "545"):
		string = "the ip addres you sumbmited was wrong <br>"
		string += render_template('submitIP.php')
		return string
	result = apiGeoScriptLatLng.geoLocationScript(lines)
	 
	string = ""
	if(result == "404"):
		string = "sudan database does not contain any connecting ip address with the ip adress provided<br>"
		string += render_template('submitIP.php')
		
	else:
		string = render_template('submitIP.php')
		string +="<br>"
		string += render_template('MapOpen.html')
		for line in result:
			string+=line
		string+=render_template('MapClose.html')
 
	return string
	
if __name__ == '__main__':
    app.run(debug=True)
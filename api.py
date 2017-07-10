from flask import Flask, request, jsonify
from google.cloud import translate
app = Flask(__name__)

@app.route('/')
def index():
	return __name__

@app.route('/API/translate', methods=['POST'])
def translator():
	translate_client = translate.Client()
	if 'source' in request.form:
		translation = translate_client.translate(
			request.form['query'],
			target_language=request.form['target'],
			source_language=request.form['source']
		)
	else:
		translation = translate_client.translate(
			request.form['query'],
			target_language=request.form['target']
		)			

	return jsonify(translation)

@app.route('/API/rpg/character_sheet', methods=['POST'])
def character_sheet():
	return 'character_sheet'

@app.route('/API/rpg/get_next_rpg_session')
def get_next_rpg_session():
	return 'get next gathering'

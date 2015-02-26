# This is a program for that manages TTS for jarvis
# This is a new API for Google TTS for python

import sqlite3
import os

_FOLDER = "./sounds/"

def tts(string):
	if string is None:
		return None
	# CHecking database if the sound already exists
	conn = sqlite3.connect(_FOLDER+"sounds.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS sounds(
    	id INTEGER PRIMARY KEY AUTOINCREMENT,
    	query TEXT NOT NULL,
    	path TEXT NOT NULL
    	);''')
	conn.commit()
	cursor.execute('''SELECT path FROM sounds WHERE query="%s";''' % string)
	data = cursor.fetchone()
	if data is None:
		# Downlading text to speech from google server
		cursor.execute('''SELECT * FROM sounds;''')
		num = len(cursor.fetchall())
		if(num==0):
			numbering = '1'
		else:
			numbering = str(num+1)
		new_string = string.replace(" ","+")
		r = os.system("wget -q -U Mozilla -O "+_FOLDER+numbering+".mp3 \"http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q="+new_string+"\"")
		if r==0:
	        # Adding the latest sound download to database
			cursor.execute('''INSERT INTO sounds(query,path) VALUES("%s","%s");''' % (string,_FOLDER+numbering+'.mp3'))
			conn.commit()
			conn.close()
			return "./sounds/"+str(numbering)+".mp3"
		if r != 0:
			#os.remove("./sounds/"+numbering+".mp3")
			return "Not connected to the internet."
	else:
		pass

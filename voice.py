import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voice_id)
engine.runAndWait()

def speak(text):
	print('[Delancy] : ' + text)
	engine.say(text)
	engine.runAndWait()

def wish_me():
	hour = int(datetime.datetime.now().hour)
	
	greeting = ''
	if hour>=0 and hour<12:
		greeting = 'Good Morning !'
	elif hour>=12 and hour<18:
		greeting = 'Good Afternoon !'
	else:
		greeting = 'Good Evening !'

	speak(greeting + 'I am Delancy, How can I help you today ?')

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening......')
		audio = r.listen(source)
		print('Recognizing......')
		query = r.recognize_google(audio, language='en-in')
		print('[Me] : ' + query)

	return query



wish_me()
while True:
	command = takeCommand().lower()

	if 'how are you' in command:
		speak('I am good, Thank you')

	elif 'open youtube' in command:
		speak('opening youtube...')
		webbrowser.open('https://www.youtube.com/')

	elif 'open google' in command:
		speak('opening google...')
		webbrowser.open('https://www.google.com/')

	elif 'what' in command and 'time' in command:
		strTime = datetime.datetime.now().strftime("%H:%M:%S")
		speak('The time is ' + strTime)

	elif 'wikipedia' in command:
		speak('Searching wikipedia...')
		command = command.replace('Delancy','') 
		command = command.replace('wikipedia','')
		command = command.replace('search','')
		command = command.replace('for','')
		command = command.replace('about','')
		results = wikipedia.summary(command, sentences = 1)
		speak('According to wikipedia' + results)

	elif 'bye' in command:
		speak('bye..signing off')
		break

	else:
		speak('I am sorry, could you please ask another question ?')

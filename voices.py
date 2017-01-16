import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[11].id) #change index to change voices
engine.say('I m a little teapot...')

engine.runAndWait()
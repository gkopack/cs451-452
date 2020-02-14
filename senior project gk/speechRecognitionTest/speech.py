import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak the word friend and enter : ')
    audio = r.listen(source)

    #currently ends after it registers one message, need to tweak how long it waits between sentences
    #also seems slow to process

    try:
        text = r.recognize_google(audio)
        print('You have spoken : {}'.format(text))
    except:
        print('I have no idea what you have said')
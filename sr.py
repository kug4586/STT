import speech_recognition as sr

def stt():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("말해봐!")
        audio = r.listen(source)

    try:
        print("Google Speech Recognition thinks you said : " + r.recognize_google(audio, language='ko'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
while(1):
    stt()
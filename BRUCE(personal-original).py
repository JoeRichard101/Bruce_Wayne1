import webbrowser
import socket as s
import playsound
import sys
import pywhatkit.sendwhatmsg as ps
import winsound
from win10toast import ToastNotifier
import os
import datetime
import psutil
import pyttsx3
import speech_recognition as sr
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import auto_py_to_exe

asus = s.gethostname()
gt750= s.gethostbyname(asus)
HEIGHT, WIDTH = 350, 250
X_POS, Y_POS = '500', '0'

battery=psutil.sensors_battery()
percentage=battery

now=datetime.datetime.now()
date=(now.strftime("%d-%m-%y"))
currenthour=int(datetime.datetime.now().hour)
currentmin=now.minute

py = pyttsx3
pys=py.init()
py.speak('hello, if you are Mr Richard please say the secret code')
r=sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)
    try:
        voice = r.recognize_google(audio);
        if voice == '1101' and currenthour >=00 and currenthour <12 :
            py.speak('welcome back sir, good morning')
        elif voice =='1101' and currenthour>=12 and currenthour<16:
            py.speak('welcome back sir, good afternoon')
        elif voice=='1101' and currenthour>=16 and currenthour !=00:
            py.speak('welcome back sir, good evening')
        else:
            print(voice)
            py.speak('sorry strangers are not allowed')
            exit()
    except sr.UnknownValueError:
        exit()

def voice():
    try:
     while True:
      r = sr.Recognizer()
      with sr.Microphone() as source:
       audio = r.listen(source)
      voice = r.recognize_google(audio);
      new_text=Label(text=voice, fg="red",bg= "yellow")

      if voice == 'how are you':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('i am fine sir')
         userText.set("Wayne:" + 'i am fine sir')
         screen.update()
      elif voice == 'shutdown':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('see you soon sir!,have a nice day')
         userText.set("Wayne:" +'see you soon sir!,have a nice day' )
         os.system("shutdown/s /t 10")
         exit()
      elif voice == 'restart the system':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('Hold on sir, Wayne will be back in a minute')
         userText.set("Wayne:" + 'Hold on sir, Wayne will be back in a minute')
         os.system("shutdown/r /t 10")
         exit()
      elif voice == 'motivate me':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('dont give up sir')
         userText.set("Wayne:" +'dont give up sir')

      elif voice == 'what is your name':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('my name is bruce wayne')
         userText.set("Wayne:" + 'my name is bruce wayne')
      elif voice == 'who created you':
         userText.set("USER:" + voice)
         screen.update()
         py.speak('Mr Joe Richard started to create me on 19th september and completed it on 14th october!')
         userText.set("Wayne:" + 'Mr Joe Richard started to create me on 19th september and completed it on 14th october')
         print(voice)
      elif voice == 'what is my laptop password':
         print(voice)
         userText.set("USER:" + voice)
         screen.update()
         py.speak('to know your laptop password answer me a question, What is your Pet dog''s name?')
         userText.set('Wayne:' + 'to know your laptop password answer me a question, What is your Pet dog''s name?')
         screen.update()
         answer = input('to know your laptop password answer me a question ')
         userText.set("USER:" + answer)
         screen.update()
         if answer == 'Mani':
             py.speak('your laptop password is jamm1101')
             userText.set("Wayne:" + 'your laptop password is jamm1101')
             screen.update()
         else:
             py.speak('sorry sir wrong answer try again')
             userText.set("Wayne:" + 'sorry sir wrong answer try again')
      elif voice == 'who is Minu Ananya':
         py.speak('Miss minu annanya is sisterof my creator Joe Richard')
      elif voice == 'open Google':
         print(voice)
         webbrowser.open('https://www.google.co.in/')
      elif voice == 'sunset Salem':
         print(voice)
         webbrowser.open('https://www.timeanddate.com/sun/india/salem')
      elif voice == 'open YouTube':
         print(voice)
         webbrowser.open('https://www.youtube.com/')
      elif voice == '1101':
         py.speak('')
      elif voice == 'what is my IP address':
         print(gt750)
         py.speak(f'sir your IP adress is {gt750}')
      elif voice == 'exit':
         print(voice)
         py.speak('see you soon sir, Have a nice day')
         sys.exit()
      elif voice == 'Google search':
         py.speak('please say what to search sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         speak = r.recognize_google(audio)
         webbrowser.open('https://www.google.com/search?q=' + speak)
      elif voice == 'message to mum':
         print(voice)
         py.speak('please say the message sir, i will deliver it to her')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg('+918610227291', voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'message to dad':
         print(voice)
         py.speak('please say the message sir, i will deliver it to him')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg('+919842695466', voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'message to Meenu':
         print(voice)
         py.speak('please say the message sir, i will deliver it to her')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg('+919659591424', voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'send WhatsApp message to Naveen':
         print(voice)
         py.speak('please say the message sir, i will deliver it to him')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg('+918940540339', voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'send WhatsApp message to Devesh':
         print(voice)
         py.speak('please say the message sir, i will deliver it to him')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg('+919182865876', voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'send WhatsApp message':
         print(voice)
         py.speak('please say the number sir...Remember you should say the number without any gap')
         print('number should start with +91')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         pn = r.recognize_google(audio)
         number = '+91' + pn
         print(number)
         py.speak('listened sucessfully sir')
         py.speak('please say the message sir, i will deliver it to him')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg(number, voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'send WhatsApp message':
         print(voice)
         py.speak('please enter the number sir remember the number should start with country code +91')
         numb = input('please enter th number sir: ')
         py.speak('please say the message sir, i will deliver it to him')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         ps.sendwhatmsg(numb, voice, currenthour, currentmin + 2, )
         py.speak('message sent sucesfully sir')
      elif voice == 'set me a alarm':
         def timer(seconds):
             notification = ToastNotifier()
             notification.show_toast("remainder", f'alarm will go off in {seconds} seconds', duration=seconds)
             notification.show_toast(f'remainder:', duration=1)

             frequency = 2000
             duration = 20000
             winsound.Beep(frequency, duration)

         if __name__ == "__main__":
             py.speak('please say from now on how many seconds sir')
             r = sr.Recognizer()
             with sr.Microphone() as source:
                 audio = r.listen(source)
             voice = r.recognize_google(audio)
             sec = int(voice)
             py.speak('your alarm is sucesfully set sir!')
             timer(sec)
      elif voice == 'set me an reminder':
         py.speak('please say the remainder sir')

         def timer(remainder, seconds):
             notification = ToastNotifier()
             notification.show_toast("remainder", f'will be shown in {seconds} seconds', duration=seconds)
             notification.show_toast(f'remainder:', remainder, duration=5)

         if __name__ == "__main__":
             r = sr.Recognizer()
             with sr.Microphone() as source:
                 audio = r.listen(source)
             voice = r.recognize_google(audio)
             remainder = voice
             py.speak('remainder listened sir')
             py.speak('please say the seconds sir')
             r = sr.Recognizer()
             with sr.Microphone() as source:
                 audio = r.listen(source)
             voice = r.recognize_google(audio)
             second = int(voice)
             print(voice, 'seconds')
             py.speak('your remainder is sucessfully set sir')
             timer(remainder, second)

      elif voice == 'play songs from YouTube':
         py.speak('which song do you want me to play sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         songs = r.recognize_google(audio)
         webbrowser.open('https://www.youtube.com/results?search_query=' + songs)
      elif voice == "what is today's date":
         print(date)
         py.speak(date)
      elif voice == 'what is the time now':
         print(currenthour - 12, ':', currentmin)
         py.speak(f' sir the time is {currenthour - 12}hour and {currentmin}minutes')
      elif voice == 'play me a song':
         playsound.playsound("C:\\Users\\joe10\\Music\\")
      elif voice == 'close':
         print(voice)
         os.system("taskkill /im chrome.exe /f")
      elif voice == 'addition':
         def add(num1, num2, num3, num4, num5):
             return num1 + num2 + num3 + num4 + num5

         num1 = int(input('please enter the first number'))
         num2 = int(input('please enter the second number'))
         num3 = int(input('please enter the third number, else enter "0"'))
         num4 = int(input('please enter the fourth number,else enter "0"'))
         num5 = int(input('please enter the fifth number,else enter "0"'))
         py.speak('your answer will be displayed below sir')
         print(num1, '+', num2, '+', num3, '+', num4, '+', num5, '=', add(num1, num2, num3, num4, num5))
      elif voice == 'subtraction':
         def sub(num1, num2, num3, num4, num5):
             return num1 - num2 - num3 - num4 - num5

         num1 = int(input('please enter the first number'))
         num2 = int(input('please enter the second number'))
         num3 = int(input('please enter the third number, else enter "0"'))
         num4 = int(input('please enter the fourth number,else enter "0"'))
         num5 = int(input('please enter the fifth number,else enter "0"'))
         py.speak('your answer will be displayed below sir')
         print(num1, '-', num2, '-', num3, '-', num4, '-', num5, '=', sub(num1, num2, num3, num4, num5))
      elif voice == 'multiplication':
         def mul(num1, num2, num3, num4, num5):
             return num1 * num2 * num3 * num4 * num5

         num1 = int(input('please enter the first number'))
         num2 = int(input('please enter the second number'))
         num3 = int(input('please enter the third number, else enter "1"'))
         num4 = int(input('please enter the fourth number,else enter "1"'))
         num5 = int(input('please enter the fifth number,else enter "1"'))
         py.speak('your answer will be displayed below sir')
         print(num1, '*', num2, '*', num3, '*', num4, '*', num5, '=', mul(num1, num2, num3, num4, num5))
      elif voice == 'divide':
         def Div(num1, num2, num3, num4, num5):
             return num1 // num2 // num3 // num4 // num5

         num1 = int(input('please enter the first number'))
         num2 = int(input('please enter the second number'))
         num3 = int(input('please enter the third number, else enter "1"'))
         num4 = int(input('please enter the fourth number,else enter "1"'))
         num5 = int(input('please enter the fifth number,else enter "1"'))
         py.speak('your answer will be displayed below sir')
         print(num1, '//', num2, '//', num3, '//', num4, '//', num5, '=', Div(num1, num2, num3, num4, num5))
      elif voice == 'addition through voice':
         userText.set("USER:" + voice)
         screen.update()
         def add(num1, num2, num3, num4, num5):
             return num1 + num2 + num3 + num4 + num5

         py.speak('please say the first value sir') # 1
         userText.set("Wayne:" + 'please say the first value sir')
         screen.update()
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         userText.set("USER:" + voice)
         screen.update()
         num1 = int(voice)
         print(voice)
         userText.set("Wayne:" + 'vaule listened sir')
         screen.update()
         py.speak('value listened sir')
         py.speak('please say the second value sir')  # 2
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         print(voice)
         num2 = int(voice)

         userText.set("Wayne:" + 'vaule listened sir')
         screen.update()
         py.speak('value listened sir')
         py.speak('please say the third value sir, if there is not third vaule please say 0')# 3
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         userText.set("USER:" + voice)
         screen.update()
         if voice=='result':
             print(num1+num2)
             userText.set(num1+num2)
             screen.update()
         else:
             pass
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num3 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fourth value sir,else say 0 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num4 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fifth value sir,else say 0 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num5 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('your answer will be displayed below sir')
         print(num1, '+', num2, '+', num3, '+', num4, '+', num5, '=', add(num1, num2, num3, num4, num5))
      elif voice == 'subtraction through voice':
         def sub(num1, num2, num3, num4, num5):
             return num1 - num2 - num3 - num4 - num5

         py.speak('please say the first value sir')  # 1
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num1 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the second value sir')  # 2
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         print(voice)
         num2 = int(voice)
         py.speak('value listened sir')
         py.speak('please say the third value sir, if there is not third vaule please say 0')  # 3
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num3 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fourth value sir,else say 0 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num4 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fifth value sir,else say 0 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num5 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('your answer will be displayed below sir')
         print(num1, '-', num2, '-', num3, '-', num4, '-', num5, '=', sub(num1, num2, num3, num4, num5))
      elif voice == 'multiplication through voice':
         def mul(num1, num2, num3, num4, num5):
             return num1 * num2 * num3 * num4 * num5

         py.speak('please say the first value sir')  # 1
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num1 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the second value sir')  # 2
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         print(voice)
         num2 = int(voice)
         py.speak('value listened sir')
         py.speak('please say the third value sir, if there is not third vaule please say 1')  # 3
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num3 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fourth value sir,else say 1 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num4 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fifth value sir,else say 1 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num5 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('your answer will be displayed below sir')
         print(num1, '*', num2, '*', num3, '*', num4, '*', num5, '=', mul(num1, num2, num3, num4, num5))
      elif voice == 'division through voice':
         def div(num1, num2, num3, num4, num5):
             return num1 // num2 // num3 // num4 // num5

         py.speak('please say the first value sir')  # 1
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num1 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the second value sir')  # 2
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         print(voice)
         num2 = int(voice)
         py.speak('value listened sir')
         py.speak('please say the third value sir, if there is not third vaule please say 1')  # 3
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num3 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fourth value sir,else say 1 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num4 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('please say the fifth value sir,else say 1 sir')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         voice = r.recognize_google(audio)
         num5 = int(voice)
         print(voice)
         py.speak('value listened sir')
         py.speak('your answer will be displayed below sir')
         print(num1, '/', num2, '/', num3, '/', num4, '/', num5, '=', div(num1, num2, num3, num4, num5))

      elif voice == '1101' and currenthour >= 00 and currenthour < 12:
         py.speak('')
      elif voice == '1101' and currenthour >= 3 and currenthour < 16:
         py.speak('')
      elif voice == '1101' and currenthour > 16 and currenthour != 00:
         py.speak('')
      elif voice == 'what is my laptop battery':
         print(percentage)
         py.speak(percentage)
      else:
         print(voice)
         py.speak("sorry sir you haven't programmed me for this command")
    except sr.UnknownValueError:
        print('', end='')


screen = Tk()
screen.title("BRUCE WAYNE")
screen.geometry('{}x{}+{}+{}'.format(HEIGHT, WIDTH, X_POS, Y_POS))
canvas=Canvas(screen,width=1500,height=1500)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\joe10\\Pictures\\197277.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack(side=RIGHT,fill=BOTH,expand=1)
welcome_text = Label(text='Hello',width=5,height=5,bd=2 ,fg="red", bg="black")
welcome_text.pack()
click_me = Button(text="click me to speak", fg='black', bg='yellow', command=voice)
click_me.pack()
userText = StringVar()
userText.set('Click on speak to me button to Give commands! ')

userFrame = LabelFrame(screen, text="MR:Wayne", font=('Black ops one', 25, 'bold'))
userFrame.pack(fill="y", expand="yes", side='left')

User_Message = Message(userFrame, textvariable=userText, bg='gray24', fg='white')
User_Message.config(font=("Comic Sans MS", 10, 'bold'))
User_Message.pack(fill='y', expand='yes', )

screen.mainloop()


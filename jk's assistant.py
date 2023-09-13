#help of jesus
import tkinter as tk
from tkinter import ttk
import pyttsx3 as pt
import speech_recognition as sr
import threading
import webbrowser
import keyboard
import os
import wikipedia
from pytube import YouTube

from datetime import datetime

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        
        self.root.configure(bg="#279EFF")  
        
        self.label = ttk.Label(root, text="JK'S VOICE ASSISTANT--LUCAS", font=("Berlin Sans FB Demi", 23))
        self.label.pack(pady=20, anchor="w")
        
        self.main_frame = ttk.Frame(root, borderwidth=20, relief="raised")  # Add border and relief
        self.main_frame.pack(padx=10, pady=(67, 10))
        
        self.text_display = tk.Text(self.main_frame, height=3, width=20, font=("Sitka Display Semibold", 17), fg="#000000", bg="#CAEDFF")
        self.text_display.pack(side="left", padx=1, pady=1)
        
        self.microphone_img = tk.PhotoImage(file="assets/microphone.png").subsample(3, 3)
        self.microphone_button = ttk.Button(self.main_frame, image=self.microphone_img, command=self.process_input)
        self.microphone_button.pack(side="left", padx=7)
        
        self.system_text = tk.Text(root, height=10, width=80,font=("Arial Narrow",12) ,bg="#CAEDFF",state=tk.DISABLED)
        self.system_text.pack(pady=10)
        
        self.exit_button = ttk.Button(root, text="Exit",command=root.destroy)
        self.exit_button.pack(pady=20, side="bottom")
        
        self.is_listening = False
        
        
    def center_elements(self):
        
        for widget in self.main_frame.winfo_children():
            widget.grid_configure(sticky="ew")

        # Center the exit button horizontally
        self.exit_button.grid_configure(sticky="ew")
        
        # Center the label horizontally in the response_frame
        self.label.pack_forget()  # Unpack the label from the main_frame
        self.label.pack(in_=self.response_frame, pady=20, fill="both", expand=True)  # Pack it into the response_frame
    
    

    def process_input(self):
        if self.is_listening:
            return
        
        self.is_listening = True
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, "Yes Iam listening.....")
        self.microphone_button.config(image="")
        threading.Thread(target=self.listen_and_respond).start()
    
    def get_user_input(self):
        try:
            text = self.assistant()
            return text
        except sr.UnknownValueError:
            return None
         
    def perform_calculation(self, a, b, operation):
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            result = a / b
        else:
            result = None

        return result

    # (Your existing code here...)

    def listen_and_respond(self):
        try:
            text = self.assistant()
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, "YOU: " + text)
            self.append_system_text("YOU: " + text)

            # ... (Your existing response logic)

            if "calculator" in text:
                self.say_response("Sure! Please provide the first value.")
                a = float(input(self.assistant()))

                self.say_response("Got it! Now, provide the second value")
                b =float(input(self.assistant()))

                self.say_response("Understood! Now, which operation would you like to perform? (add, subtract, multiply, divide)")
                operation = self.assistant()

                result = self.perform_calculation(a, b, operation)

                if result is not None:
                    self.say_response(f"The result is {result}.")
                else:
                    self.say_response("Sorry, I couldn't understand the operation.")

        except sr.UnknownValueError:
            response = "Sorry, I couldn't understand what you said. Please try again."
            self.say_response(response)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, "Try again or ask something else.")

            self.is_listening = False
            self.microphone_button.config(image=self.microphone_img)

        if  "hello" in text:
            response = "YES hello how can i assist you... "
            self.say_response(response)
            
        
            
        elif "parents" in text:
            response="Yes sure!! Jk's father name is lakshmana rao and his mother name is babyrani"
            self.say_response(response)
            
        elif "do you like your boss" in text:
            response="definitely i really  respected him when the time of creation he is very simple and very active person thats why i like him a lot"
            self.say_response(response)
            
        elif "who invented you" in text:
            response="JK sir invented me by the help of jesus and ..! i will help you if u want to open browsers or social media too"
            self.say_response(response)
            
        elif "favourite food" in text:
            response="I dont have any favourite foods because iam a machine so im not an foodie but my favourite one is Electrical power !!and onething but my jk sir loves prawns he told me in the time of my creation"
            self.say_response(response)
            
        elif "are you male or female" in text:
            response="sorry iam an machine iam not human but i am invented by human intilligence and i created by jk sir" 
            self.say_response(response)
            
        elif "your name" in text:
            response="my name is lucas!! and what is your name"
            self.say_response(response)
            
        elif "my name is jk" in text:
            response="i was impressed because my boss name is also jk"
            self.say_response(response)
        
        elif "iam your boss" == text:
            response="hoo boss! are you really!!  welcome boss...i miss u "
            
        elif "my name is " in text:
            response="cool i like your name my friend"
            self.say_response(response)
        
        elif "calculator" in text:
                self.say_response("Sure! Please provide the first number (a).")
                a = float(self.assistant())

                self.say_response("Got it! Now, provide the second number (b).")
                b = float(self.assistant())

                self.say_response("Understood! Now, which operation would you like to perform? (add, subtract, multiply, divide)")
                operation = self.assistant()

                result = self.perform_calculation(a, b, operation)

                if result is not None:
                    self.say_response(f"The result is {result}.")
                else:
                    self.say_response("Sorry, I couldn't understand the operation.")

        elif "google" in text:
            self.say_response("Opening Google.")
            self.open_google()
       
        elif "open youtube" in text:
            self.say_response("Opening YouTube.")
            self.open_youtube()
        
        elif "open dev town" == text:
            self.say_response("opening Devtown please wait")
            self.open_devtown()
            
        elif " my college portal" in text:
            self.say_response("opening college portal please wait")
            self.open_kietportal()
        
        elif "camera" in text:
                self.say_response("Opening Camera.")
                self.open_camera()

        elif "open visual studio" in text:
            self.say_response("Opening Visual Studio Code.")
            self.open_visual_studio()
            
        elif "linkedin" in text:
            self.say_response("opening linked in please wait")
            self.open_linkedin()
            
        elif "open github" == text :
            self.say_response("opening github in please wait")
            self.open_github()
        
        elif "open whatsapp" in text:
            self.say_response("opening whatsapp in please wait")
            self.open_whatsapp()
            
        elif "male voice" in text:
            self.say_response("converting into male voice")
            self.convert_male()
            
        elif "female voice" in text:
            self.say_response("converting into female voice")
            self.convert_female()
            

        elif "file manager" in text:
            self.say_response("Opening File Manager.")
            self.open_file_manager()
            
        elif "close google" == text:
            self.say_response("Closing Google.")
            self.close_google()
            
        elif "close youtube" == text:
            self.say_response("Closing YouTube.")
            self.close_youtube()
            
        elif "time" in text:
            self.say_response("now the current time is " + self.get_current_time())
            
        elif "date" in text:
            self.say_response("Today the current date in india is "+self.get_current_datetime()) 
            
        elif "thank you " in text:
            response="yes your welcome and if you have any queries regarding anything  or if u want any help or need visit me again. Have a good day!!"
            self.say_response(response)
            
        else:
            response = "Sorry, I didn't understand what you said. Please try again."
            self.say_response(response)
            
        self.is_listening = False
        self.microphone_button.config(image=self.microphone_img)
    
    def assistant(self):
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Please say something...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print("You have said:\n" + text)
                 
        return text.lower()

    def open_google(self):
        webbrowser.open("https://www.google.com")
    
    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")
    
    def open_devtown(self):
        webbrowser.open("https://www.student-platform.devtown.in/programs")
        
    def open_kietportal(self):
        webbrowser.open("https://www.kietgroup.info/Account/Login")
        
    def open_linkedin(self):
        webbrowser.open("https://in.linkedin.com/")
        
    def open_github(self):
        webbrowser.open("https://github.com/")
        
    def open_whatsapp(self):
        webbrowser.open("https://web.whatsapp.com")
    
    def close_google(self):
        keyboard.press_and_release("ctrl+w")  # Simulate Ctrl+w to close tab
    
    def close_youtube(self):
        keyboard.press_and_release("ctrl+w")  # Simulate Ctrl+w to close tab
    
    def get_current_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        return current_time
    
    def open_camera(self):
        os.system("start microsoft.windows.camera:")

    def open_visual_studio(self):
        os.system("code")
    
    def open_file_manager(self):
        os.system("explorer")
        
    def get_current_datetime(self):
        current_datetime = datetime.now().strftime("%B %d, %Y")  
        return current_datetime
    
    def say_response(self, text):
        pyobj = pt.init()
        
        pyobj.setProperty("rate", 91)
        pyobj.say(text)
        pyobj.runAndWait()
    
    def append_system_text(self, text):
        self.system_text.config(state=tk.NORMAL)
        self.system_text.insert(tk.END, text + "\n")
        self.system_text.config(state=tk.DISABLED)
        self.system_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()

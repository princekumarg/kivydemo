import kivy
from kivy.app import App
from kivy.uix.label import Label 
class MyFirstKivyApp(App):
    def build(self):
        return Label(text ="Hello World !")    
MyFirstKivyApp().run()
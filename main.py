
from kivy. app import App
from kivy.uix.image import Image



class MainApp(App):
    def build(self):
        img = Image(source='img0.png')

        return img




MainApp().run()

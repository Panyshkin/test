from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class BoxApp(App):
    def build(self):

        self.bl = BoxLayout(orientation="vertical",padding = 100,spacing=10)
        self.bl.add_widget((Image(source='kd_logo2.png')))
        self.bl.add_widget(Label(text="Отсканируй QR для входа", color=[.12,.71,.47,1], font_size='30'))
        self.bl.add_widget(TextInput(font_size='30'))
        self.bl.add_widget(Button(text="Войти",
                                  background_color=[.12,.71,.47,1],
                                  background_normal = "",
                                  on_press = self.btn_press,
                                  font_size='30'))


        self.blqr = BoxLayout(orientation = "vertical")
        self.blqr.add_widget(TextInput())


        return self.bl

    def btn_press(self, instance):
        print(instance.text)





        ##return self.al




if __name__ =="__main__":
    BoxApp().run()
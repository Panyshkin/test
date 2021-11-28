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
        al = AnchorLayout()

        gl = GridLayout(cols=3, size_hint = [.7,.7])
        gl.add_widget(Image(source='KD.png',size_hint_x=None, width=50))
        gl.add_widget(Label(text="Авторизация", color="ff3333",font_size='30sp'))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Label(text="Логин:",color="ff3333",font_size='30sp'))
        gl.add_widget(TextInput())
        gl.add_widget(Widget())
        gl.add_widget(Label(text="Пароль:",color="ff3333",font_size='30sp'))
        gl.add_widget(TextInput())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text="Войти",
                             background_color=[.88,.88,.05,1],
                             background_normal = ""))
        al.add_widget(gl)

        return al
if __name__ =="__main__":
    BoxApp().run()
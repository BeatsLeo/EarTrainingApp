from kivy.app import App
from utils import ReturnPopup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import LabelBase

from settings import *

Window.size = (300, 600)  # 宽度大于高度

class MyApp(App):
    
    lang = 'zh'
    content = CONTENT
    
    def show_input_popup(self):
        # 创建弹窗
        popup = ReturnPopup()
        popup.open()

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        open_popup_button = Button(text="打开对话框")
        open_popup_button.bind(on_release=lambda x: self.show_input_popup())
        main_layout.add_widget(open_popup_button)
        return main_layout

if __name__ == '__main__':
    LabelBase.register(name="Roboto", fn_regular="NotoSansSC-VF.ttf")
    MyApp().run()

    

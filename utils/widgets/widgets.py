import os
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from utils import ReturnPopup


# 显式加载 .kv 文件
kv_file = os.path.join(os.path.dirname(__file__), 'widgets.kv')
Builder.load_file(kv_file)


class BackButton(Button):
    last_screen = StringProperty('')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        popup = ReturnPopup(self.last_screen)
        popup.open()
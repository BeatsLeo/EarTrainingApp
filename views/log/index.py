import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

# 显式加载 .kv 文件
kv_file = os.path.join(os.path.dirname(__file__), 'index.kv')
Builder.load_file(kv_file)

class LOGScreen(Screen):
    back_text = StringProperty('')
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
        
    def refresh(self):
        lang_map = self.app.content[self.app.lang]

        self.back_text = lang_map['BACK']
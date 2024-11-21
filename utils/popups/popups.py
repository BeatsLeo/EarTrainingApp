import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty


# 显式加载 .kv 文件
kv_file = os.path.join(os.path.dirname(__file__), 'popups.kv')
Builder.load_file(kv_file)


class BasePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
    
    def refresh(self):
        lang_map = self.app.content[self.app.lang]
        # get all variables that end with '_text' and set their value to the corresponding language key
        for var in filter(lambda x: not x.startswith('__'), dir(self)):
            if var.endswith('_text'):
                lang_name = var.split('_')[0].upper()
                setattr(self, var, lang_map.get(lang_name, 'Not Registered'))


class ReturnPopup(BasePopup):
    return_text = StringProperty('')
    sure_text = StringProperty('')
    cancel_text = StringProperty('')
    
    def __init__(self, last_screen, **kwargs):
        super().__init__(**kwargs)
        self.last_screen = last_screen
        self.refresh()
        
    def sure_return(self):
        self.app.sm.current = self.last_screen
        self.dismiss()
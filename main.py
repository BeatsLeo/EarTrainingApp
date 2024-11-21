from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager

from settings import *
from utils import BaseScreen
from views import ETScreen, SSScreen, LOGScreen

Window.size = (300, 600)  # 宽度大于高度

class Index(BaseScreen):
    title_text = StringProperty('')
    ss_text = StringProperty('')
    et_text = StringProperty('')
    log_text = StringProperty('')
    lang_text = StringProperty('')
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()


class MTAApp(App):
    lang = 'zh'
    content = CONTENT
    
    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()
        self.screens = [
            Index(name='Index'),
            ETScreen(name='ET Screen'),
            SSScreen(name='SS Screen'),
            LOGScreen(name='LOG Screen')
        ]
        for screen in self.screens:
            self.sm.add_widget(screen)
        self.sm.current = 'Index'
        
        self.refresh()

        return self.sm

    def refresh(self):
        for screen in self.screens:
            screen.refresh()

    def change_lang(self):
        self.lang = 'en' if self.lang == 'zh' else 'zh'
        self.refresh()

if __name__ == '__main__':
    LabelBase.register(name="Roboto", fn_regular="NotoSansSC-VF.ttf")
    MTAApp().run()
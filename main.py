from kivy.app import App
from kivy.properties import StringProperty
from views import ETScreen, SSScreen, LOGScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from settings import *

Window.size = (300, 600)  # 宽度大于高度

class Index(Screen):
    title = StringProperty('')
    ss_text = StringProperty('')
    et_text = StringProperty('')
    log_text = StringProperty('')
    lang_text = StringProperty('')
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
    
    def refresh(self):
        lang_map = self.app.content[self.app.lang]
        
        self.title = lang_map['TITLE']
        self.ss_text = lang_map['SS']
        self.et_text = lang_map['ET']
        self.log_text = lang_map['LOG']
        self.lang_text = lang_map['LANG']


class MTAApp(App):
    lang = 'zh'
    content = CONTENT
    
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        self.screens = [
            Index(name='Index'),
            ETScreen(name='ET Screen'),
            SSScreen(name='SS Screen'),
            LOGScreen(name='LOG Screen')
        ]
        for screen in self.screens:
            sm.add_widget(screen)
        sm.current = 'Index'
        
        self.refresh()

        return sm

    def refresh(self):
        for screen in self.screens:
            screen.refresh()

    def change_lang(self):
        self.lang = 'en' if self.lang == 'zh' else 'zh'
        self.refresh()

if __name__ == '__main__':
    MTAApp().run()
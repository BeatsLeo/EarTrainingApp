import os
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

from utils import BaseScreen, ReturnPopup

# 显式加载 .kv 文件
kv_file = os.path.join(os.path.dirname(__file__), 'index.kv')
Builder.load_file(kv_file)

class ETScreen(BaseScreen):
    score = NumericProperty(0)
    total = NumericProperty(0)
    et_text = StringProperty('')
    back_text = StringProperty('')
    et_question_text = StringProperty('')
    replay_text = StringProperty('')
    submit_text = StringProperty('')
    standard_text = StringProperty('')
    return_popup = ReturnPopup
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
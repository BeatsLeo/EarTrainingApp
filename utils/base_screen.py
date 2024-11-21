from kivy.app import App
from kivy.uix.screenmanager import Screen


# Override the base screen class to add language support
# The text under the controlable variables should be named in the format of:
# {lang_key}_text
# For example:
# title_text, et_text, etc. Corresponding to the language keys: TITLE, ET, etc.

class BaseScreen(Screen):    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = App.get_running_app()
    
    def refresh(self):
        lang_map = self.app.content[self.app.lang]
        # get all variables that end with '_text' and set their value to the corresponding language key
        for var in filter(lambda x: not x.startswith('__'), dir(self)):
            if var.endswith('_text'):
                lang_name = var.rsplit('_', 1)[0].upper()
                setattr(self, var, lang_map.get(lang_name, 'Not Registered'))
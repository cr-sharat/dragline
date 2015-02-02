import global_settings


class Settings(object):
    def __init__(self, settings_module):
        self.update(global_settings)
        self.update(settings_module)

    def update(self, module):
        for setting in dir(module):
            if setting.isupper():
                setting_value = getattr(module, setting)
                setattr(self, setting, setting_value)

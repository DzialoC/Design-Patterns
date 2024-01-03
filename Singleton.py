
class ConfigurationManager:
    _instance = None # private class variable to store the instance
    volume = 100
    mouse_sensitivity = 100


    def __init__(self):
        self.volume = ConfigurationManager.volume
        self.mouse_sensitivity = ConfigurationManager.mouse_sensitivity

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


conf1 = ConfigurationManager.get_instance()
conf2 = ConfigurationManager.get_instance()

# Checks if both conf1 and conf2 refers to the same object
print(conf1 is conf2)
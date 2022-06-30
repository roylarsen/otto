from pathlib import Path
from os import path

class ConfigFile:
    def __init__(self):
        self.conffile = str(Path.home()) + "/.otto.conf"

    def check(self):
        return path.isfile(self.conffile)

    def create(self):
        if self.check():
            #shouldn't ever happen
            print("How did we get here? Please check existance of {0}".format(self.conffile))
            return
        
        file = open(self.conffile, 'w', encoding="utf-8")
        from .config import Config
        otconf = Config()
        file.write(otconf.generate())
        file.close()
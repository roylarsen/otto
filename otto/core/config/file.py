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
    
    def getvaluefromfile(self, value):
        """Takes a dotted notation variable reference: module.variable"""
        valuelist = value.split(".")

        from .config import Config
        otconf = Config()

        with open(self.conffile) as conffile:
            configctx = conffile.read()

        return otconf.getvaluefromconfig(configctx, valuelist)

    def update(self):
        """Handles opening the config for writing"""

        with open(self.conffile) as conffile:
            configctx = conffile.read()
        print("Updating old config content:\n{0}".format(configctx))

        from .config import Config
        otconf = Config()

        conffile = open(self.conffile, 'w', encoding="utf-8")
        updatedconf = otconf.update(configctx)
        print("Updated config content:\n {0}".format(updatedconf))
        conffile.write(updatedconf)
        conffile.close()

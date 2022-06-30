import tomlkit
from pkgutil import walk_packages
from importlib import import_module

class Config:
    def printmods(self):
        import otto.utils
        packages = {}
        for sub in walk_packages(otto.utils.__path__, otto.utils.__name__ + "."):
            if sub.name.endswith(".config"):
                utilconfig = getattr(import_module(sub.name), "Config")
                if hasattr(utilconfig, "CONFIGURATION"):
                    packages.update(utilconfig.CONFIGURATION)
        print(packages)
        return packages
    
    def generate(self):
        utilconfigs = self.printmods()
        configdoc = tomlkit.document()
        for tableheader, tablevalue in utilconfigs.items():
            table = tomlkit.table()
            for value in tablevalue:
                table.add(value, "")
            configdoc.add(tableheader, table)
        return tomlkit.dumps(configdoc)
from abc import ABC, abstractmethod 

# Product class
class Desktop():
    def __init__(self):
        self._monitor = None
        self._keyboard = None
        self._mouse = None
        self._speaker = None
        self._ram = None
        self._processor = None
        self._motherBoard = None
    
    def setMonitor():
        pass
    
    def setKeyboard():
        pass
    
    def setMouse():
        pass
    
    def setSpeaker():
        pass
    
    def setRam():
        pass
    
    def setProcessor():
        pass
    
    def setMotherBoard():
        pass
    
    def showSpecs():
        pass
    
# Buidler class (Abstract / Interface)
class DesktopBuilder(ABC):
    def __init__(self):
        # protected variable
        self._desktop = Desktop()
    
    @abstractmethod
    def buildMonitor(): pass
    
    @abstractmethod
    def buildKeyboard(): pass
    
    @abstractmethod
    def buildMouse(): pass
    
    @abstractmethod
    def buildSpeaker(): pass

    @abstractmethod
    def buildRam(): pass

    @abstractmethod
    def buildProcessor(): pass
    
    @abstractmethod
    def buildMotherBoard(): pass
    
    @abstractmethod
    def getDesktop() -> Desktop:
        return self._desktop

# ConcreteBuilder classes (implements interface)
# In these the implemented set methods return self 
# so that we can chain the set methods
class Dell_DesktopBuilder(DesktopBuilder):
    ...

class HP_DesktopBuilder(DesktopBuilder):
    ...
    
class Asus_DesktopBuilder(DesktopBuilder):
    ...
    

# Director Class
class Director():
    
    def __init__(self, arg_DesktopBuilder: DesktopBuilder):
        # private variable
        self.__desktop_builder = arg_DesktopBuilder
    
    # calling all the builders of whatever concrete builder
    # to make process of building the desktops
    def buildDesktop() -> Desktop:
        pass


if __name__ == "__main__":
    hp_desktop_build = HP_DesktopBuilder()
    dell_desktop_build = Dell_DesktopBuilder()
    asus_desktop_build = Asus_DesktopBuilder()
    
    dir1 = Director(hp_desktop_build)
    dir2 = Director(dell_desktop_build)
    dir3 = Director(asus_desktop_build)
    
    desktop1 = dir1.buildDesktop()
    desktop2 = dir2.buildDesktop()
    desktop3 = dir3.buildDesktop()
    
    desktop1.showSpecs()
    desktop2.showSpecs()
    desktop3.showSpecs()
    
    return
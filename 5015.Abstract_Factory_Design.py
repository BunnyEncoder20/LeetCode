from abc import ABC, abstractmethod

# interface for button
class IButton(ABC):
    @abstractmethod
    def press(self): pass

# interface for textarea
class ITextarea(ABC):
    @abstractmethod
    def showText(self): pass

# abstract factory
class GUI_AbstractFactory(ABC):
    @staticmethod
    def createFactory(osType):
        
    
    
    
    
# client side 
if __name__ == "__main__":
    osType = input("Enter OS Type (windows / mac):")

    # making OS factory from static method
    factory = GUI_AbstractFactory.createFactory(osType)

    # make GUI elements 
    button = factory.createButton()
    button.press()

    textarea = factory.createTextarea()
    textarea.showText()

    return
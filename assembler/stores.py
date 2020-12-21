import SingeltonMeta as singleton

class SymbolStore(metaclass=singleton.SingletonMeta):
    symbols = {}

    def getSymbol(self, key):
        return self.symbols[key]
    
    def setSymbol(self, key, value, position):
        self.symbols[key] = {
            'value': value,
            'position': position,
        }

class LabelStore(metaclass=singleton.SingletonMeta):
    labels = {}

    def getLabel(self, key):
        return self.labels[key]
    
    def setLabel(self, label_name, label_offset):
        self.labels[label_name] = label_offset

import SingeltonMeta as singleton

class SymbolStore(metaclass=singleton.SingletonMeta):
    symbols = {}

    def getSymbol(self, key):
        return self.symbols[key]
    
    def setSymbol(self, key, value, position):
        self.symbols[key] = {
            'value': int(value),
            'position': position,
        }
        print(f"Symbol stored : {self.symbols[key]}")

class LabelStore(metaclass=singleton.SingletonMeta):
    labels = {}

    def getLabel(self, key):
        return self.labels[key]
    
    def setLabel(self, label_name, label_offset):
        self.labels[label_name] = label_offset
        print(f"Label stored : {label_name} => {self.labels[label_name]}")

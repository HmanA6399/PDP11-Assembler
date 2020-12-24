from enum import Enum
import constants
import stores

class Token():
    """
    Generic Representation of token information
    """
    code : int = None
    
    def __str__(self):
        return str(oct(self.code))
        pass
    
    def getCode(self):
        return self.code;
        pass

    pass

class OpcodeToken(Token):
    """
    Represents tokens for opcode
    """
    typ : constants.OpcodeType = constants.OpcodeType.DEFAULT;
    
    def __init__(self, code, typ) :
        
        self.code = code
        self.typ = typ 
        
        pass
    
    pass

class OperandToken(Token):
    """
    Represents first word of operand code
    """
    reg = 0
    mode = 0
    is_indirect = 0
    def __init__(self, reg, mode, is_indirect) :
        self.reg = reg
        self.mode = mode
        self.code = ( (mode + is_indirect * constants.MODES_COUNT) << (constants.REG_BIT_COUNT)) | reg
        pass

    pass

class ImmediateValueToken(Token):
    """
    Represents immediate value stored in secoond word of operand code
    """
    def __init__(self, code) :
        self.code = code
        pass
    pass

class LabelToken(Token):
    """
    Represents label
    """
    label_name = ""

    def __init__(self, label_name) :
        self.label_name = label_name
    
    def __str__(self) :
        lbl_tbl = stores.LabelStore()
        self.code = lbl_tbl.getLabel(self.label_name)
        return Token.__str__(self)

class SymbolToken(Token):
    """
    Represents a symbol define by the Define statement
    """

    symbol_name = ""

    def __init__(self, name, value):
        self.symbol_name = name
        self.code = value

class SymbolAbsoluteReferenceToken(Token):
    """
    Represents the absolute reference to a stored symbol
    """

    symbol_name = ""

    def __init__(self, symbol_name):
        self.symbol_name = symbol_name
    
    def __str__(self):
        sym_tbl = stores.SymbolStore()
        symbol = sym_tbl.getSymbol(self.symbol_name)
        
        self.code = symbol['position']
        return Token.__str__(self)

class SymbolRelativeReferenceToken(Token):
    """
    Represents the relative reference to a stored symbol (symbol_position - self_position)
    """
    
    symbol_name = ""
    position = 0

    def __init__(self, symbol_name, position):
        self.symbol_name = symbol_name
        self.position = position
    
    def __str__(self):
        sym_tbl = stores.SymbolStore()
        symbol = sym_tbl.getSymbol(self.symbol_name)
        self.code = symbol['position'] - self.position
        return Token.__str__(self)

class LineBreakToken(Token):

    def __str__(self):
        return '\n';

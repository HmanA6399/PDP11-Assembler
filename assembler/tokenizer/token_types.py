from enum import Enum
import constants

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
    def __init__(self, reg, mode) :
        self.reg = reg
        self.mode = mode
        self.code = (mode << (constants.REG_BIT_COUNT)) | reg
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
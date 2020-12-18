from enum import Enum

class TokenType(Enum):
    OPCODE  = 0
    OPERAND = 1
    OFFSET  = 2
    NUMBER  = 3
    pass

class Token():
    """
    Representation of token information
    """
    code : int = None
    type : TokenType = None
    
    def __str__(self):
        return self.code
        pass
    
    pass
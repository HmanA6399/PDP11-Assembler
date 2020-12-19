import SingeltonMeta
import constants
import tokenizer.token_types
import re

class Tokenizer(metaclass=SingeltonMeta.SingletonMeta) :
    def getOpcodeToken(self, assem_str) :
        """
        Given assembly operation string, create a new token with the proper code and type
        """
        
        # Translate to code
        code = constants.OPCODES_DICT[assem_str]

        # Determine type of operation
        typ = constants.OPCODE_TYPE[code >> 3]
        
        return token_types.OpcodeToken(code, typ)
        pass

    def getOperandToken(self, assem_str) :
        """
        Given assembly string of operand, return array of tokens with the appropriate code for output and immediate value
        """
        reg = None
        mode = None
        reg_match = re.search(constants.REG_REGEX, assem_str)
        
        # Handeling indirect modes bit
        if ( re.search(constants.INDIRECT_REGEX, assem_str) ) :
            assem_str = assem_str[1:]
            mode += 4
        
        reg = int( reg_match.group()[1] if reg_match else constants.PC_REG )
        modes = constants.NON_PC_MODES if reg_match else constants.PC_MODES

        for mode_name in modes :
            if ( re.search(constants.MODE_REGEX[mode_name], assem_str) ) :
                print(f"Matched mode {mode_name}")
                if (mode == None) : mode = 0
                mode += constants.MODE_CODE[mode_name]

        if (mode == None) :
            raise "MODE UNDETECTED!"

        
        return token_types.OperandToken(reg, mode)
        pass
    
    pass
import SingletonMeta
import constants
import tokenizer.token_types
import re
import stores

class Tokenizer(metaclass=SingletonMeta.SingletonMeta):
    def createOpcodeToken(self, assem_str):
        """
        Given assembly operation string, create a new token with the proper code and type
        """
        
        # Translate to code
        code = constants.OPCODES_DICT[assem_str.upper()]

        # Determine type of operation
        typ = constants.OPCODE_TYPE[code & 0x0F]
        
        return token_types.OpcodeToken(code, typ)
        pass

    def createOperandToken(self, assem_str):
        """
        Given assembly string of operand, return array of tokens with the appropriate code for output and immediate value
        """
        reg = None
        mode = 0
        is_indirect = 0
        reg_match = re.search(constants.REG_REGEX, assem_str)
        
        # Handeling indirect modes bit
        if ( re.search(constants.INDIRECT_REGEX, assem_str) ):
            assem_str = assem_str[1:]
            is_indirect = 1
        
        reg = int( reg_match.group()[1] if reg_match else constants.PC_REG )
        modes = constants.NON_PC_MODES if reg_match else constants.PC_MODES

        for mode_name in modes:
            if ( re.search(constants.MODE_REGEX[mode_name], assem_str) ) :
                # print(f"Matched mode {mode_name}")
                mode = constants.MODE_CODE[mode_name]

        if (mode == None):
            raise "MODE UNDETECTED!"

        
        return token_types.OperandToken(reg, mode, is_indirect)
        pass

    def createOperandTokens(self, assem_str, position):
        """
        Get all tokens requires to build operand
        """
        operand_first_token = self.createOperandToken(assem_str);
        operand_extra_token = None
        
        # Needs extra token (INDEXED or RELATIVE)
        if (operand_first_token.mode == constants.MODE_CODE["INDEXED"]) :
            # PC (RELATIVE)
            if (operand_first_token.reg == constants.PC_REG):
                symbol_name = re.search(constants.SYMBOL_NAME_REGEX, assem_str).group()
                operand_extra_token = token_types.SymbolRelativeReferenceToken(symbol_name, position+1)
            
            # Non PC
            else:
                imm_val = int(re.search(constants.INDEX_MATCHER, assem_str).group())
                operand_extra_token = token_types.ImmediateValueToken(imm_val)
        
        # IMMDIATE
        if (operand_first_token.mode == constants.MODE_CODE["AUTO_INC"] and operand_first_token.reg == 7):
            imm_val = int(re.search(constants.IMMEDIATE_VALUE_MATCHER, assem_str).group())
            operand_extra_token = token_types.ImmediateValueToken(imm_val)
        
        return operand_first_token, operand_extra_token
    
    def tokenizeStatement(self, statement, position):
        primary_tokens = []
        extra_tokens = []

        if (len(statement) == 0) : return primary_tokens, extra_tokens  # Handle empty sentence case
        
        # Assignment
        if (re.match(constants.DEFINE_REGEX, statement[0], flags=re.IGNORECASE)):
            sym_store = stores.SymbolStore()
            sym_store.setSymbol(statement[1], statement[2], position)
            primary_tokens.append(token_types.SymbolToken(statement[1], statement[2]))
            primary_tokens.append(token_types.LineBreakToken())
        
        # Operation
        else:
            opcode_token = self.createOpcodeToken(statement[0])
            primary_tokens.append(opcode_token)
            
            # SINGLE
            if (opcode_token.typ == constants.OpcodeType.SINGLE):
                opd_token, ext_token = self.createOperandTokens(statement[1], position)
                primary_tokens.append(opd_token)
                if (ext_token):
                    [extra_tokens.append(t) for t in [ext_token, token_types.LineBreakToken()]]
            
            # DOUBLE
            elif (opcode_token.typ == constants.OpcodeType.DOUBLE):
                for i in range(1,3) :
                    opd_token, ext_token = self.createOperandTokens(statement[i], position)
                    primary_tokens.append(opd_token)
                    if (ext_token):
                        [extra_tokens.append(t) for t in [ext_token, token_types.LineBreakToken()]]
            
            # BRANCH
            elif (opcode_token.typ == constants.OpcodeType.BRANCH):
                primary_tokens.append(token_types.LabelToken(statement[1]))
            
            # JUMP
            elif (opcode_token.typ == constants.OpcodeType.JUMP):
                [extra_tokens.append(t) for t in [token_types.SymbolAbsoluteReferenceToken(statement[1]), token_types.LineBreakToken()]]
        
        primary_tokens.append(token_types.LineBreakToken())
        return primary_tokens, extra_tokens
    pass
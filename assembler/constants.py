from enum import Enum

class OpcodeType(Enum) :
    NO_OPD = 0,
    BRANCH = 1,
    SINGLE = 2,
    DOUBLE = 3,
    JUMP = 4,
    DEFAULT = -1
    pass


OPCODES_DICT = {
    # 2 OPERAND => At most 4 bits
    'MOV'   : 0b0000,
    'ADD'   : 0b0001,
    'ADC'   : 0b0010,
    'SUB'   : 0b0011,
    'SBC'   : 0b0100,
    'AND'   : 0b0101,
    'OR'    : 0b0110,
    'XOR'   : 0b0111,
    'CMP'   : 0b1000,
    # I'll leave the rest of 0o5x if any 2 operand is intended to be added

    # SINGLE OPERAND
    'INC'   : 0b00001001,
    'DEC'   : 0b00011001,
    'CLR'   : 0b00101001,
    'INV'   : 0b00111001,
    'LSR'   : 0b01001001,
    'ROR'   : 0b01011001,
    'ASR'   : 0b01101001,
    'LSL'   : 0b01111001,
    # I'll leave the rest of 0o3x if any single operand is intended to be added

    # NO OPERAND
    'HLT'  :  0b001010,
    'NOP'   : 0b011010,
    'RESET' : 0b101010,
    
    # BRANCH
    'BR'    : 0b0001011,
    'BEQ'   : 0b0011011,
    'BNE'   : 0b0101011,
    'BLO'   : 0b0111011,
    'BLS'   : 0b1001011,
    'BHI'   : 0b1011011,
    'BHS'   : 0b1101011,


    # JUMP INSTRUCTIONS
    'JSR'   : 0b001100,
    'RTS'   : 0b011100,
'INTERRUPT' : 0b101100,
    'IRET'  : 0b111100,
}

OPCODE_TYPE = [
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
    OpcodeType.SINGLE,
    OpcodeType.NO_OPD,
    OpcodeType.BRANCH,
    OpcodeType.JUMP
]
REG_COUNT = 7
REG_BIT_COUNT = 3
PC_REG = 7
MODES_COUNT = 4 # Direct or indirect

INDIRECT_BIT = 5 # From starting of operand code
REG_SUBREGEX = f"[Rr][0-{REG_COUNT}]"
REG_REGEX = f"(?<!\w)({REG_SUBREGEX})(?!\w)"
SYMBOL_NAME_REGEX = "[A-Za-z_]{1}[A-Za-z0-9_]*"
INDIRECT_REGEX= r'^@'
DEFINE_REGEX = r'^define$'
INDEX_MATCHER = r'[0-9]{1,}(?=\()'
IMMEDIATE_VALUE_MATCHER = r'(?<=#)[0-9]{1,}'
COMMENT_REGEX = r';.*'
SEGMENT_REGEX = r'[A-Za-z0-9@\(\)#\+\-]+'
LABEL_DELIMETER_REGEX = r'[\s]*:[\s]*'

NON_PC_MODES = ["REGISTER", "AUTO_INC", "AUTO_DEC", "INDEXED"]
PC_MODES = ["IMMEDIATE", "RELATIVE"]

MODE_CODE = {
    "REGISTER" : 0,
    "AUTO_INC" : 1,
    "AUTO_DEC" : 2,
    "INDEXED"  : 3,
    "IMMEDIATE": 1, # Same as AUTO_INC
    "RELATIVE" : 3, # Same as INDEXED
}

MODE_REGEX = {
    "REGISTER" : f"^{REG_SUBREGEX}$",
    "AUTO_INC" : f"^\({REG_SUBREGEX}\)\+$",
    "AUTO_DEC" : f"^-\({REG_SUBREGEX}\)$",
    "INDEXED"  : f"^\(?[0-9].*\({REG_SUBREGEX}\)\)?$",
    "IMMEDIATE": r"^#[0-9].*$",
    "RELATIVE" : f"^{SYMBOL_NAME_REGEX}$"
}
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
    'MOV'   : 0b0000,   # 0x00
    'ADD'   : 0b0001,   # 0x01
    'ADC'   : 0b0010,   # 0x02
    'SUB'   : 0b0011,   # 0x03
    'SBC'   : 0b0100,   # 0x04
    'AND'   : 0b0101,   # 0x05
    'OR'    : 0b0110,   # 0x06
    'XOR'   : 0b0111,   # 0x07
    'CMP'   : 0b1000,   # 0x08
    # I'll leave the rest of 0o5x if any 2 operand is intended to be added

    # SINGLE OPERAND
    'INC'   : 0b00001001,   # 0x009
    'DEC'   : 0b00011001,   # 0x019
    'CLR'   : 0b00101001,   # 0x029
    'INV'   : 0b00111001,   # 0x039
    'LSR'   : 0b01001001,   # 0x049
    'ROR'   : 0b01011001,   # 0x059
    'ASR'   : 0b01101001,   # 0x069
    'LSL'   : 0b01111001,   # 0x079
    # I'll leave the rest of 0o3x if any single operand is intended to be added

    # NO OPERAND
    'HLT'  :  0b001010,     # 0x00a
    'NOP'   : 0b011010,     # 0x01a
    'RESET' : 0b101010,     # 0x02a
    
    # BRANCH
    'BR'    : 0b0001011,    # 0x00b
    'BEQ'   : 0b0011011,    # 0x01b
    'BNE'   : 0b0101011,    # 0x02b
    'BLO'   : 0b0111011,    # 0x03b
    'BLS'   : 0b1001011,    # 0x04b
    'BHI'   : 0b1011011,    # 0x05b
    'BHS'   : 0b1101011,    # 0x06b


    # JUMP INSTRUCTIONS
    'JSR'   : 0b001100,     # 0x00c
    'RTS'   : 0b011100,     # 0x01c
'INTERRUPT' : 0b101100,     # 0x02c
    'IRET'  : 0b111100,     # 0x03c
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
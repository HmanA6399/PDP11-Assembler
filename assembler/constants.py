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
    # NO OPERAND
    'HALT'  : 0o00,
    'NOP'   : 0o01,
    'RESET' : 0o02,
    
    # BRANCH
    'BR'    : 0o10,
    'BEQ'   : 0o11,
    'BNE'   : 0o12,
    'BLO'   : 0o13,
    'BLS'   : 0o14,
    'BHI'   : 0o15,

    # SINGLE OPERAND
    'INC'   : 0o20,
    'DEC'   : 0o22,
    'CLR'   : 0o23,
    'INV'   : 0o24,
    'LSR'   : 0o25,
    'ROR'   : 0o26,
    'ASR'   : 0o27,
    'LSL'   : 0o30,
    # I'll leave the rest of 0o3x if any single operand is intended to be added

    # 2 OPERAND
    'MOV'   : 0o40,
    'ADD'   : 0o41,
    'ADC'   : 0o42,
    'SUB'   : 0o43,
    'SBC'   : 0o44,
    'AND'   : 0o45,
    'OR'    : 0o46,
    'XOR'   : 0o47,
    'CMP'   : 0o50,
    # I'll leave the rest of 0o5x if any 2 operand is intended to be added

    # JUMP INSTRUCTIONS
    'JSR'   : 0o60,
    'RTS'   : 0o61,
'INTERRUPT' : 0o62,
    'IRET'  : 0o63,
}

OPCODE_TYPE = [
    OpcodeType.NO_OPD,
    OpcodeType.BRANCH,
    OpcodeType.SINGLE,
    OpcodeType.SINGLE,
    OpcodeType.DOUBLE,
    OpcodeType.DOUBLE,
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
INDIRECT_REGEX= "^@"
DEFINE_REGEX = "^define$"
INDEX_MATCHER = "[0-9]{1,}(?=\()"
IMMEDIATE_VALUE_MATCHER = "(?<=#)[0-9]{1,}"

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
    "IMMEDIATE": "^#[0-9].*$",
    "RELATIVE" : f"^{SYMBOL_NAME_REGEX}$"
}
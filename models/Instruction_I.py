from .Instruction import Instruction


class Instruction_I(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 31),
    ]
    sliceNames = ["opcode", "rd", "funct3", "rs1", "imm"]

from .Instruction import Instruction


class Instruction_R(Instruction):

    bitRanges = [
        (0, 7),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 24),
        (25, 31),
    ]
    sliceNames = ["opcode", "rd", "funct3", "rs1", "rs2", "funct7"]

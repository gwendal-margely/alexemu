from .Instruction import Instruction


class Instruction_U(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 31),
    ]
    sliceNames = ["opcode", "rd", "imm"]

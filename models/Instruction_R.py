from .Instruction import Instruction

class Instruction_R(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 24),
        (25, 31),
    ]
    sliceNames = ["opcode", "rd", "funct3", "rs1", "rs2", "funct7"]

    def __str__(self):
        return ", ".join(
            [
                hex(int(self.rd, 2))[1:],
                hex(int(self.rs1, 2))[1:],
                hex(int(self.rs2, 2))[1:],
            ]
        )

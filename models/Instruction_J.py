from .Instruction import Instruction

class Instruction_J(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 19),
        (20, 30),
        (31, 31),
    ]
    sliceNames = ["opcode", "rd", "imm1", "imm2", "imm3"]

    def __str__(self):
        imm1 = int(self.imm1, 2)
        imm2 = int(self.imm2, 2)
        imm3 = int(self.imm3, 2)
        imm = (imm3 << 20) | (imm2 << 1) | (imm1 << 11) | (imm3 << 19)
        if imm & (1 << 20):  # Sign extend
            imm |= 0xFFE00000
        return (
            ", ".join(
                [
                    hex(int(self.rd, 2))[1:],
                    str(imm),
                ]
            ).ljust(20)
            + f"// {hex(imm)}"
        )

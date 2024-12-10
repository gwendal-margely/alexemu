from .Instruction import Instruction

class Instruction_B(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 24),
        (25, 30),
        (31, 31),
    ]
    sliceNames = ["opcode", "imm1", "funct3", "rs1", "rs2", "imm2", "imm3"]

    def __str__(self):
        imm1 = int(self.imm1, 2)
        imm2 = int(self.imm2, 2)
        imm3 = int(self.imm3, 2)
        imm = (imm3 << 12) | (imm2 << 5) | (imm1 << 1)
        if imm & (1 << 12):  # Sign extend
            imm |= 0xFFFFF000
        return (
            ", ".join(
                [
                    hex(int(self.rs1, 2))[1:],
                    hex(int(self.rs2, 2))[1:],
                    str(imm),
                ]
            ).ljust(20)
            + f"// {hex(imm)}"
        )

from .Instruction import Instruction

class Instruction_S(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 24),
        (25, 31),
    ]
    sliceNames = ["opcode", "imm1", "funct3", "rs1", "rs2", "imm2"]

    def __str__(self):
        imm1 = int(self.imm1, 2)
        imm2 = int(self.imm2, 2)
        imm = (imm2 << 5) | imm1
        if imm & (1 << 11):  # Sign extend
            imm |= 0xFFFFF000
        return (
            ", ".join(
                [
                    str(imm1),
                    hex(int(self.rs1, 2))[1:],
                    hex(int(self.rs2, 2))[1:],
                    str(imm2),
                ]
            ).ljust(20)
            + f"// {hex(imm1)}, {hex(imm2)}"
        )

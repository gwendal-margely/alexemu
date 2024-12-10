from .Instruction import Instruction


class Instruction_S(Instruction):

    bitRanges = [
        (0, 7),
        (7, 11),
        (12, 14),
        (15, 19),
        (20, 24),
        (25, 31),
    ]
    sliceNames = ["opcode", "imm1", "funct3", "rs1", "rs2", "imm2"]

    def __str__(self):
        return (
            ", ".join(
                [
                    str(int(self.imm1, 2)),
                    hex(int(self.rs1, 2))[1:],
                    hex(int(self.rs2, 2))[1:],
                    str(int(self.imm2, 2)),
                ]
            ).ljust(20)
            + f"// {hex(int(self.imm1, 2))}, {hex(int(self.imm2, 2))}"
        )

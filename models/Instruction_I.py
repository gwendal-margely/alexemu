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

    def __str__(self):
        return (
            ", ".join(
                [
                    hex(int(self.rd, 2))[1:],
                    hex(int(self.rs1, 2))[1:],
                    str(int(self.imm, 2)),
                ]
            ).ljust(20)
            + f"// {hex(int(self.imm, 2))}"
        )

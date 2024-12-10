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
        imm = int(self.imm, 2)
        if imm & (1 << 11):  # Sign extend
            imm |= 0xFFFFF000
        return (
            ", ".join(
                [
                    hex(int(self.rd, 2))[1:],
                    hex(int(self.rs1, 2))[1:],
                    str(imm),
                ]
            ).ljust(20)
            + f"// {hex(imm)}"
        )

from .Instruction import Instruction

class Instruction_U(Instruction):

    bitRanges = [
        (0, 6),
        (7, 11),
        (12, 31),
    ]
    sliceNames = ["opcode", "rd", "imm"]

    def __str__(self):
        imm = int(self.imm, 2)
        imm <<= 12
        return (
            ", ".join(
                [
                    hex(int(self.rd, 2))[1:],
                    str(imm),
                ]
            ).ljust(20)
            + f"// {hex(imm)}"
        )

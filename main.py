from models import Instruction
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "FICHIER_BIN",
    help="Un fichier au format binaire contenant les instructions à décoder",
    type=str,
)
args = parser.parse_args()

df = pd.read_csv(
    "res/instructions.csv",
    dtype={i: str for i in ["opcode_value", "funct3", "funct7", "funct1"]},
)
buffer_size = 4  # en 'bytes' (octets)

i_type_to_class = {c.__name__[0]: c for c in Instruction.__subclasses__()}

offset = 0
with open(args.FICHIER_BIN, "rb") as f:
    while dword := f.read(buffer_size):  # walrus operator 🤩
        hex_str = dword.hex()
        bin_str = bin(int(hex_str, 16))[2:].zfill(32)

        opcode = bin_str[-7:]

        rows = df[df["opcode_value"] == opcode]
        if rows.shape[0] == 1:
            row = rows.iloc[0]
        else:
            funct3 = bin_str[12:15]
            row = rows[rows["funct3"] == funct3].iloc[0]

        i_type = row["type_encodage"][0]
        print(
            hex(offset * 4)[2:].zfill(8) + ":",
            row["instruction"],
            sep=" ",
        )

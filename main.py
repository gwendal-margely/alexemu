from models import Instruction_I, Instruction_R, Instruction_S, Instruction_U, Instruction_B, Instruction_J
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
    dtype={i: str for i in ["opcode_value", "funct3", "funct7", "funct12"]},
)
buffer_size = 4  # en 'bytes' (octets)

i_type_to_class = {
    "I": Instruction_I,
    "R": Instruction_R,
    "S": Instruction_S,
    "U": Instruction_U,
    "B": Instruction_B,
    "J": Instruction_J,
}

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
            rows_funct3 = rows[rows["funct3"] == funct3]
            if rows_funct3.shape[0] == 1:
                row = rows_funct3.iloc[0]
            else:
                print(f"Erreur: Combinaison opcode {opcode} et funct3 {funct3} non trouvée dans le fichier CSV.")
                continue  # Passe à l'instruction suivante

        i_type = row["type_encodage"][0]
        instruction = i_type_to_class[i_type](bin_str)

        print(
            hex(offset * 4)[2:].zfill(8) + ":",
            row["instruction"].ljust(10),
            sep=" ",
            end=" ",
        )
        print(instruction)
        offset += 1

import argparse, json, sys

parser = argparse.ArgumentParser()

parser.add_argument(
    "FICHIER_BIN",
    help="Un fichier au format binaire contenant les instructions à décoder",
    type=str,
)

args = parser.parse_args()
buffer_size = 4  # en 'bytes' (octets)
instructions = json.load(open("res/instructions.json"))

offset = 0
print("offset,valeur,opcode,encoding")
with open(args.FICHIER_BIN, "rb") as f:
    while dword := f.read(buffer_size):  # walrus operator 🤩
        opcode = bin(dword[3] & 0x7F)[2:].zfill(7)
        instruction_type, encoding = instructions[opcode]
        print(
            hex(offset)[2:].zfill(8),
            dword.hex().replace("0x", ""),
            instruction_type,
            encoding,
            sep=",",
        )
        offset += 1

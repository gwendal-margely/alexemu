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
        hex_str = dword.hex().replace("0x", "")
        opcode = bin(int(hex_str, 16))[2:].zfill(buffer_size * 8)[-7:]
        instruction_type, encoding = instructions[opcode]
        print(
            hex(offset)[2:].zfill(8),
            hex_str,
            instruction_type,
            encoding,
            sep=",",
        )
        offset += 1

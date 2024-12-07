import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "FICHIER_BIN",
    help="Un fichier au format binaire contenant les instructions à décoder",
    type=str,
)
args = parser.parse_args()

buffer_size = 4 # en 'bytes' (octets)

offset = 0
with open(args.FICHIER_BIN, "rb") as f:
    while (dword := f.read(buffer_size)): # walrus operator 🤩
        print(
            str(offset).zfill(8),
            dword.hex(),
            sep=" ",
        )
        offset += 1

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--file",
    help="Chemin du fichier binaire à décoder",
    type=str,
    required=True
)
args = parser.parse_args()
print(args.file)
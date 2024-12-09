from models import Instruction_I, Instruction_R, Instruction_S, Instruction_U
import csv
from string import ascii_lowercase, digits

x = Instruction_I(ascii_lowercase + digits)
print(x)

# with open("res/instructions.csv", "r") as f:
#     reader = csv.DictReader(f)
#     headers = next(reader)
#     for row in reader:
#         print(row)

import json


class Instruction:

    bitRanges = []
    sliceNames = []

    def __init__(self, bits):
        for name, [start, end] in zip(self.sliceNames, self.bitRanges):
            setattr(self, name, bits[start : end + 1])

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def __repr__(self):
        return self.__str__()
`docker run --rm -it $(docker build -q -f livrables/Dockerfile.l1 .) tests/test_file_1.bin`

```
.
├── livrables
│   └── Dockerfile.l1
├── main.py
├── models
│   ├── __init__.py
│   ├── Instruction_I.py
│   ├── Instruction.py
│   ├── Instruction_R.py
│   ├── Instruction_S.py
│   ├── Instruction_U.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       ├── Instruction.cpython-312.pyc
│       ├── Instruction_I.cpython-312.pyc
│       ├── Instruction_R.cpython-312.pyc
│       ├── Instruction_S.cpython-312.pyc
│       └── Instruction_U.cpython-312.pyc
├── Pipfile
├── Pipfile.lock
├── README.md
├── res
│   └── instructions.csv
└── tests
    ├── test_b_type.bin
    ├── test_file_1.bin
    ├── test_file_2.bin
    ├── test_i_type.bin
    ├── test_j_type.bin
    ├── test_r_type.bin
    ├── test_s_type.bin
    └── test_u_type.bin
```
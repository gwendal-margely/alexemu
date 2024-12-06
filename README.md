# Projet RISC-V Emulateur

Ce projet est un émulateur pour l'architecture RISC-V RV32I écrit en Go.

## Structure du Projet

```
project/
│ 
├── res/
│   ├── opcodes.json
│   ├── instructions.json
│
├── src/
│   ├── main.go
│   ├── decoder.go
│   ├── disassembler.go
│   └── utils.go
│
├── rendus/
│   ├── Dockerfile.l1
│   ├── Dockerfile.l2
│
├── README.md
└── go.mod
```

## Instructions

### Livrable 1

Pour construire et exécuter le livrable 1 (décodage des instructions):

```sh
docker build -t livrable1 -f rendus/Dockerfile.l1 .
docker run -it --rm livrable1 <fichier_binaire>
```

Pour tester :

```sh
docker build -t livrable1 --build-arg MODE=TEST -f rendus/Dockerfile.l1 .
docker run -it --rm livrable1
```

### Livrable 2

Pour construire et exécuter le livrable 2 (désassemblage des instructions):

```sh
docker build -t livrable2 -f rendus/Dockerfile.l2 .
docker run -it --rm livrable2 <fichier_binaire>
```

Pour tester :

```sh
docker build -t livrable2 --build-arg MODE=TEST -f rendus/Dockerfile.l2 .
docker run -it --rm livrable2

```
### Fichiers JSON

Les fichiers JSON contiennent les opcodes et les instructions nécessaires pour le décodage et le désassemblage. Ils sont situés dans le répertoire res/.
Licence

*Ce projet est sous licence Creative Commons CC-BY-NC-SA 4.0*
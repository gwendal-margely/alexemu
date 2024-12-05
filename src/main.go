package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	flag.Parse()
	if flag.NArg() < 1 {
		fmt.Println("Veuillez fournir un fichier binaire en argument.")
		os.Exit(1)
	}

	filepath := flag.Arg(0)
	err := DecodeFile(filepath)
	if err != nil {
		fmt.Printf("Erreur lors du décodage du fichier: %v\n", err)
		os.Exit(1)
	}
}

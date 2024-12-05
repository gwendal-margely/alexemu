package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

var opcodes map[string]string
var instructions map[string]map[string]string

func init() {
	data, err := ioutil.ReadFile("res/opcodes.json")
	if err != nil {
		fmt.Printf("Erreur lors de la lecture du fichier opcodes.json: %v\n", err)
		os.Exit(1)
	}
	json.Unmarshal(data, &opcodes)

	data, err = ioutil.ReadFile("res/instructions.json")
	if err != nil {
		fmt.Printf("Erreur lors de la lecture du fichier instructions.json: %v\n", err)
		os.Exit(1)
	}
	json.Unmarshal(data, &instructions)
}

func DecodeFile(filepath string) error {
	file, err := os.Open(filepath)
	if err != nil {
		return err
	}
	defer file.Close()

	fmt.Println("offset,valeur,opcode,encoding")
	offset := 0
	buffer := make([]byte, 4)
	for {
		_, err := file.Read(buffer)
		if err != nil {
			break
		}
		instruction := uint32(buffer[0]) | uint32(buffer[1])<<8 | uint32(buffer[2])<<16 | uint32(buffer[3])<<24
		opcode := instruction & 0x7F
		encoding := ""
		for key, value := range opcodes {
			if value == fmt.Sprintf("%02x", opcode) {
				encoding = key
				break
			}
		}
		fmt.Printf("%08x,%08x,%s,%s\n", offset, instruction, encoding, opcodes[encoding])
		offset += 4
	}
	return nil
}

package main

import (
	"fmt"
	"os"
)

func DisassembleFile(filepath string) error {
	file, err := os.Open(filepath)
	if err != nil {
		return err
	}
	defer file.Close()

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
		inst := instructions[encoding]
		fmt.Printf("%08x: %s\n", offset, inst["nom"])
		offset += 4
	}
	return nil
}

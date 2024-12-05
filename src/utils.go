package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
)

func LoadJSON(filepath string, data interface{}) error {
	file, err := os.Open(filepath)
	if err != nil {
		return err
	}
	defer file.Close()

	byteValue, err := ioutil.ReadAll(file)
	if err != nil {
		return err
	}

	err = json.Unmarshal(byteValue, data)
	if err != nil {
		return err
	}

	return nil
}

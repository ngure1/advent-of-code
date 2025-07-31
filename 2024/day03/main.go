package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

const (
	filePath = "input.txt"
	fileBufferSize = 18798
)


func GetRegex () (*regexp.Regexp) {
	reg:= regexp.MustCompile(`mul\(\d+,\d+\)`)
	return reg
}

func part1(corruptedMem []byte){
	reg := GetRegex()
	res := reg.FindAllString(string(corruptedMem),-1)

	var muls int
	
	for _,instruction := range res {

		validInstruction := string([]byte(instruction[4:len(instruction)-1]))

		nums := strings.Split(validInstruction,",")
		
		num1,err := strconv.Atoi(nums[0])
		if err != nil {
			log.Fatalf("Failed to convert num1 to int %s \n",err)
		}

		num2,err := strconv.Atoi(nums[len(nums)-1])
		if err != nil {
			log.Fatalf("Failed to convert num2 to int %s \n",err)
		}

		muls += num1 * num2
	}

	fmt.Println(muls)
}


func part2(corruptedMem string) {

}

func main () {
	bytes,err := os.ReadFile(filePath)
	if err != nil {
		log.Fatalf("Error reading file %s \n",err)
	}

	part1(bytes)

}


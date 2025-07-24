package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const filePath = "input.txt"

func main() {
	fd,err := os.OpenFile(filePath,os.O_RDONLY,0677)
	if err != nil {
		log.Fatalf("could not open file %s\n",err)
	}
	defer fd.Close()

	scanner := bufio.NewScanner(fd)

	var left []uint
	right := make(map[uint]int)
	for  scanner.Scan() {
		line := strings.Split(scanner.Text(),"   ")
		
		leftInt,err := strconv.Atoi(line[0])
		if err != nil {
			log.Printf("error converting %s %s\n",line[0],err)
		}

		rightInt,err := strconv.Atoi(line[1])
		if err != nil {
			log.Printf("error converting %s %s\n",line[0],err)
		}

		left = append(left, uint(leftInt))

		right[uint(rightInt)] += 1

		if err = scanner.Err(); err != nil {
			log.Fatalf("error reading text %s\n",err)
		}
	}

	var totalDistance uint

	for _,val := range left {
		if count,ok := right[val] ; ok {
			totalDistance += val * uint(count)
		}
	}
		
	fmt.Printf("Solution: %d\n",uint(totalDistance))
	
}
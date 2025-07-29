package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

const (
	maxDiff  = 3
	minDiff  = 1
	filePath = "input.txt"
)

func checkIsSafe(report []int) bool {
	j := 1
	// check if is increasing/decreasing
	isIncreasing := report[0] < report[j]

	for i := range report {
		// check if j is in range
		if j > len(report)-1 {
			break
		}

		diff := report[j] - report[i]
		if isIncreasing && (diff > maxDiff || diff < minDiff) {
			return false
		} else if !isIncreasing && (diff < -maxDiff || diff > -minDiff) {
			return false
		}

		j++
	}

	return true
}

func part1(fd io.ReadCloser) int {
	defer fd.Close()

	scanner := bufio.NewScanner(fd)

	var safeCount int

	for scanner.Scan() {
		stringReport := strings.Split(scanner.Text(), " ")
		var report []int
		for _, str := range stringReport {
			num, err := strconv.Atoi(str)
			if err != nil {
				log.Printf("Error parsing string to int %s \n", err)
			} else {
				report = append(report, num)
			}
		}

		if checkIsSafe(report) {
			safeCount++
		}

	}

	return safeCount
}

func part2(fd io.ReadCloser) int {
	defer fd.Close()

	scanner := bufio.NewScanner(fd)

	var safeCount int

	for scanner.Scan() {
		stringReport := strings.Split(scanner.Text(), " ")
		var report []int
		for _, str := range stringReport {
			num, err := strconv.Atoi(str)
			if err != nil {
				log.Printf("Error parsing string to int %s \n", err)
			} else {
				report = append(report, num)
			}
		}

		if checkIsSafe(report) {
			safeCount++
		} else {
			for i := range report {
				var modifiedLevel []int
				modifiedLevel = append(modifiedLevel,report[:i]...)
				modifiedLevel = append(modifiedLevel, report[i+1:]...)
				if checkIsSafe(modifiedLevel) {
					safeCount ++
					break
				}
			}
		}

	}

	return safeCount
}

func main() {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Could not open file : %s\n", err)
	}

	safe := part2(file)
	fmt.Printf("Safe count is : %d\n", safe)
}

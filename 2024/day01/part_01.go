package main

// import (
// 	"bufio"
// 	"fmt"
// 	"log"
// 	"math"
// 	"os"
// 	"slices"
// 	"strconv"
// 	"strings"
// 	"sync"
// )

// const filePath = "input.txt"

// func main() {
// 	fd,err := os.OpenFile(filePath,os.O_RDONLY,0677)
// 	if err != nil {
// 		log.Fatalf("could not open file %s\n",err)
// 	}
// 	defer fd.Close()

// 	scanner := bufio.NewScanner(fd)

// 	var left []uint
// 	var right []uint
// 	for  scanner.Scan() {
// 		line := strings.Split(scanner.Text(),"   ")
		
// 		leftInt,err := strconv.Atoi(line[0])
// 		if err != nil {
// 			log.Printf("error converting %s %s\n",line[0],err)
// 		}

// 		rightInt,err := strconv.Atoi(line[1])
// 		if err != nil {
// 			log.Printf("error converting %s %s\n",line[0],err)
// 		}

// 		left = append(left, uint(leftInt))
// 		right = append(right, uint(rightInt))

// 		if err = scanner.Err(); err != nil {
// 			log.Fatalf("error reading text %s\n",err)
// 		}
// 	}

// 	var wg sync.WaitGroup

// 	wg.Add(2)
// 	go func () {
// 		slices.Sort(left)
// 		defer wg.Done()
// 	}()

// 	go func () {
// 		slices.Sort(right)
// 		defer wg.Done()
// 	}()


// 	wg.Wait()

// 	var totalDistance float64

// 	for i := range left {
// 			totalDistance += math.Abs(float64(left[i]) - float64(right[i]))
// 		}
		
// 	fmt.Printf("Solution: %d\n",uint(totalDistance))
	
// }
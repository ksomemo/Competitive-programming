package main

import (
	"fmt"
	"math"
	"time"
)
import "github.com/dustin/go-humanize"

func main() {
	for i := 4; i <= 9; i++ {
		benchmark_op(int(math.Pow10(i)))
	}
}

/*
 * 複数行コメントは使われていない?
 */
func benchmark_op(N int) {
	humanized := humanize.Comma(int64(N))
	fmt.Printf("benchmark, N:%s\n", humanized)
	var a int
	a = 0

	d := time.Now()
	for i := 0; i <= N; i++ {
		// nothing
	}
	fmt.Println("for", time.Now().Sub(d))

	d = time.Now()
	for i := 1; i <= N; i++ {
		a += i + 10000000
	}
	fmt.Println("add", time.Now().Sub(d))

	d = time.Now()
	for i := 1; i <= N; i++ {
		a += i - 10000000
	}
	fmt.Println("Sub", time.Now().Sub(d))

	d = time.Now()
	for i := 1; i <= N; i++ {
		a += i * i
	}
	fmt.Println("mul", time.Now().Sub(d))

	d = time.Now()
	for i := 1; i <= N; i++ {
		a += 10000000 / i
	}
	fmt.Println("div", time.Now().Sub(d))

	fmt.Println("")
}

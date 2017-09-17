package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// http://qiita.com/tnoda_/items/b503a72eac82862d30c6
	var N int
	fmt.Scan(&N)

	// make 2 dimension slice
	a := make([][]int, N)
	for i := 0; i < N; i++ {
		a[i] = make([]int, N)
	}

	// 行取得からの分割/Int
	var sc = bufio.NewScanner(os.Stdin)
	total := 0
	for i := 0; i < N; i++ {
		sc.Scan()
		line := sc.Text()
		values := strings.Split(line, " ")
		for j, v := range values {
			vInt, _ := strconv.Atoi(v)
			a[i][j] = vInt
			total += vInt
		}
	}

	no_need := 0
	for k := 0; k < N; k++ {
		// from
		for i := 0; i < N; i++ {
			// to
			for j := 0; j < N; j++ {
				// compare from-to / from-経由地点-to
				if i == k || j == k {
					continue
				}
				d := a[i][k] + a[k][j]
				if a[i][j] > d {
					fmt.Println(-1)
					return
				} else if a[i][j] == d {
					// 経由して同じであれば必要ない
					no_need += d
				}
			}
		}
	}
	//  対称なので半分にする
	fmt.Println((total - no_need) / 2)
}

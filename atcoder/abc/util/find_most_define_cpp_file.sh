#!/bin/bash
for f in `find ../../ -name "*.cpp"`; do
  echo `grep define $f | wc -l ` $f;
done | sort -nr | head -n 1

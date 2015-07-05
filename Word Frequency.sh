#!/bin/bash
# Write a bash script to calculate the frequency of each word in a text file
# words.txt.
# https://leetcode.com/problems/word-frequency/

awk '{ for (i=1; i<=NF; i++) f[$i]++ } END { for (w in f) printf "%d %s\n", f[w], w }' words.txt | sort -gr | awk '{print $2" "$1}' 

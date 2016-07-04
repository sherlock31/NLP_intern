awk 'BEGIN { FS = OFS = "," }
     NR != 1 { y[$1] += $2; $2 = y[$1]; x[$1] = $0; }
     END { for (i in x) { print x[i]; } }' dic2.txt > dic3.txt


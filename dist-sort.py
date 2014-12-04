#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=';')

#Ovo je promena

For line in reader:
    #Try to interpret 3rd column as a float. Ignore line on error.
    try:
        power = float(line[2])
    except:
        continue
    # Key = power, value = entire line
    print power, "\t", writer.writerow(line)


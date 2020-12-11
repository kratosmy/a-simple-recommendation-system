#!/bin/bash

for n in {a..x};
do
	cat /home/1155148594/CMSC5741_Project/updated_data/outputphase1_parts/newfilea$n | python3 MapperC.py | sort | python3 ReducerC_new.py > outputphase3_$n.txt
done

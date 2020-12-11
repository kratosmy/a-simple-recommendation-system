#!/bin/bash

#for n in {a..x};
for n in {a};
do
	hdfs dfs -rm -r outputphase3

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=8192 \
	-D mapreduce.reduce.memory.mb=8192 \
	-D mapred.map.tasks=20 \
	-D mapred.reduce.tasks=10 \
	-input input/newfilea$n \
	-output outputphase3 \
	-file MapperC.py -mapper MapperC.py \
	-file ReducerC_new.py -reducer ReducerC_new.py \
	-file outputphase2_final.txt \
	
	hadoop fs -getmerge outputphase3/* outputphase3$n.txt

	cat outputphase3$n.txt >> outputphase3_final.txt
	
	hdfs dfs -rm -r outputphase3
done
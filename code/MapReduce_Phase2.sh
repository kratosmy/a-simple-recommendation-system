#!/bin/bash

for n in {a};
do
	hdfs dfs -rm -r outputphase2

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.map.tasks=30 \
	-D mapred.reduce.tasks=10 \
	-input input/newfilea$n \
	-output outputphase2 \
	-file MapperB.py -mapper MapperB.py \
	-file ReducerB.py -reducer ReducerB.py \

	hadoop fs -getmerge outputphase2/* output_pairs.txt
done

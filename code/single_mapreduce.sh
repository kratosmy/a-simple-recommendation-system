#!/bin/bash

for n in {a};
do
	chmod +x single_mapreduce.sh
	
	hdfs dfs -rm -r outputphase_single

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.map.tasks=30 \
	-D mapred.reduce.tasks=10 \
	-input input/newfilea$n \
	-output outputphase_single \
	-file single_mapper.py -mapper single_mapper.py \
	-file single_reducer.py -reducer single_reducer.py \

	hadoop fs -getmerge outputphase_single/* output_single.txt
done

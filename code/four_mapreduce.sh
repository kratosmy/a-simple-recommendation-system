#!/bin/bash

#for n in {a..x};
for n in {a};
do
	hdfs dfs -rm -r four_mapreduce

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=8192 \
	-D mapreduce.reduce.memory.mb=8192 \
	-D mapred.map.tasks=30 \
	-D mapred.reduce.tasks=10 \
	-input input/newa$n \
	-output four_mapreduce \
	-file four_mapper.py -mapper four_mapper.py \
	-file four_reducer.py -reducer four_reducer.py \
	-file output_pairs.txt \

	hadoop fs -getmerge four_mapreduce/* output_four.txt
done

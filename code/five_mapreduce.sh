#!/bin/bash

#for n in {a..x};
for n in {a};
do
	hdfs dfs -rm -r five_mapreduce

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapreduce.map.memory.mb=15000 \
	-D mapreduce.reduce.memory.mb=15000 \
	-D mapred.map.tasks=50 \
	-D mapred.reduce.tasks=10 \
	-input input/newa$n \
	-output five_mapreduce \
	-file five_mapper.py -mapper five_mapper.py \
	-file five_reducer.py -reducer five_reducer.py \
	-file output_pairs.txt \

	hadoop fs -getmerge five_mapreduce/* output_five.txt
done

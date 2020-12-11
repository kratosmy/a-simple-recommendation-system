#!/bin/bash

#for n in {a..x};
for n in {a};
do
	hdfs dfs -rm -r triple_mapreduce

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.map.tasks=30 \
	-D mapred.reduce.tasks=10 \
	-input input/newfilea$n \
	-output triple_mapreduce \
	-file triple_mapper.py -mapper triple_mapper.py \
	-file triple_reducer.py -reducer triple_reducer.py \
	-file output_pairs.txt \

	hadoop fs -getmerge triple_mapreduce/* output_triple.txt
done

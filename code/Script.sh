# unzip all compressed files
unzip *.zip

# aggregate all .csv files into a whole .csv file
cat *.csv > wholedata.csv

# sort this file according to the userId
sort -t "," -k3 wholedata.csv > wholedata_sorted.csv

# put the .csv file into HDFS
hdfs dfs -put wholedata_sorted.csv input

# first round MapReduce
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -files MapperA_new.py,ReducerA.py -mapper MapperA_new.py -reducer ReducerA.py -input input/wholedata_sorted.csv -output outputphase1

# check the first round output
hdfs dfs -getmerge outputphase1/* outputphase1.txt
cat outputphase1.txt

# check the lines
wc -l outputphase1.txt
(7984920 outputphase1.txt)

# second round MapReduce, I have to split the file into 10 parts
split -b 100m outputphase1.txt newfile

# then run the following bash scripts

#!/bin/bash

for n in {a..x};
do
	hdfs dfs -rm -r outputphase2

	hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.map.tasks=30 \
	-D mapred.reduce.tasks=10 \
	-input input/newfilea$n \
	-output outputphase2 \
	-file MapperB.py -mapper MapperB.py \
	-file ReducerB.py -reducer ReducerB.py \

	hadoop fs -getmerge outputphase2/* outputphase2$n.txt

	cat outputphase2$n.txt >> outputphase2_final.txt
	
	hdfs dfs -rm -r outputphase2
done

# normally we should run MapReduce in Hadoop, but failed, this is the bash script
#!/bin/bash

for n in {a..x};
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

# due to memory issue, I have to run MapReduce round 3 locally
#!/bin/bash

for n in {a..x};
do
	cat /home/1155148594/CMSC5741_Project/updated_data/outputphase1_parts/newfilea$n | python3 MapperC.py | sort | python3 ReducerC_new.py > outputphase3_$n.txt
done

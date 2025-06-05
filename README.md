# Air Traffic MapReduce Analysis (2024)

##  Objective
Use Hadoop MapReduce (Python Streaming) to analyze European air traffic data and find the top 5 busiest countries by number of flights in 2024.

##  Files Included
- `mapper.py`: Mapper for extracting (country, flights) from the dataset
- `reducer.py`: Reducer for aggregating and sorting top 5
- `plot_top5.py`: Python script to plot final result using matplotlib
- `flights_by_country_2024.csv`: Input dataset
- `top5countries.txt`: Output result from MapReduce

##  How to Run (Brief)
1. Put CSV into HDFS:
```bash
hdfs dfs -mkdir -p /user/hdoop/input
hdfs dfs -put flights_by_country_2024.csv /user/hdoop/input/
```
2.Run Hadoop job:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/hdoop/input/flights_by_country_2024.csv \
  -output /user/hdoop/output/top5countries \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```
3.Get result:
```
hdfs dfs -cat /user/hdoop/output/top5countries/part-00000 > top5countries.txt
```
4.Visualize:
```
python plot_top5.py

```


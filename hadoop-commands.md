1. To load the file to hadoop env<br/>
```$ hadoop fs -put $filename```

2. To run MapReduce code<br/>
```$ hs code/mapper.py code/reducer.py $data_file $output_dir```

3. List the files in hadoop filesystem<br/>
```$ hadoop fs -ls```

4. Check the output file after a MapReduce job is finished<br/>
```$ hadoop fs -cat output_dir/part-00000```

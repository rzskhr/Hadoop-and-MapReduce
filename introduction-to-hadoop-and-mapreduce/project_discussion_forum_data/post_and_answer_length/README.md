Write a MapReduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click [here](https://www.udacity.com/wiki/ud617/local-testing-instructions) to access the instructions to use it.

##### Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.

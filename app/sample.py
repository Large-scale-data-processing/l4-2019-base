from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('appName').setMaster('local')
sc = SparkContext(conf=conf)

data = range(1000)
dist_data = sc.parallelize(data)

large_data = dist_data.flatMap(lambda a: range(1000000000))

add = lambda x, y: x + y

print(large_data.reduce(add))
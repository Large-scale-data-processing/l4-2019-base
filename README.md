# L4 - 2019

## Scope
1. pySpark
2. Linear regression
3. Binary classification
4. Multi-class  classification

## Tasks
Implement the third stage of the following architecture:
![Architecture](assets/stage-3.png)
Detailed information about components can be found in the further tasks.

For each task make sure that `tox` passes.

**Please do not modify the provided tox manifest!**

0. **Preparation** Copy appropriate source code from the previous task into this repository in order to be able to access gathered data
1. **Start questions**
    - [Guide](https://spark.apache.org/docs/latest/ml-guide.html)
    - why do we need to install Java, how pySpark works?
    - do we need to use Java 8
    - can we conntect to external cluster from python code
    - can we deploy our python code to spark cluster
    - how can we observe spark jobs progress (spark HTTP UI)
    - logistic regression vs linear regression
    - multi-class vs multi-label
2. Update Dockerfile and docker-compose:
    - download and instal spark
    - run code using pyspark command
3. Read data from mongodb using SparkSQL and appropriate connector. 
    - You need to add jar to spark runtime, use --packages flag for pyspark
    - mongodb need to be a separate service in docker-compose, utilize apropriate directives in order to get connections
4. Divide data into trainign and testing sets using some criterion (date of acquisition, first n items)
    - you can use apropriate ready to use class from spark
5. Create regression pipeline:
    - select a submission attribute that we want to be our dependant variable
    - map data to contain dependant variable and features vector columns
    - create ML pipeline
    - evluate your regressor using RMSE on train and test sets
6. Create binary classification pipeline:
    - select a submission attribute that we want to be our class
    - map data to contain class and features vector columns
    - create ML pipeline
    - evluate your classifier computing F1 mettric
6. Create multi-class classification pipeline:
    - select a submission attribute that we want to be our class (multi-class)
    - map data to contain class and features vector columns
    - create ML pipeline
    - evluate your classifier using MulticlassClassificationEvaluator
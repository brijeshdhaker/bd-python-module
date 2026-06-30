#
# /home/brijeshdhaker/.ipython/profile_default/startup
#

import os
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from delta import *

# Set absolute path for new metastore
metastore_path = os.path.abspath('/apps/sandbox/metastore')
metastore_url = f"jdbc:derby:;databaseName={metastore_path};create=true"

# mysqluser = os.getenv('MYSQL_ADMIN_USER')
# mysqlpass = os.getenv('MYSQL_ADMIN_PASSWORD')
# metastore_url = f"jdbc:mysql://mysqlserver.sandbox.net:3306/METASTORE?user={mysqluser}&password={mysqlpass}&createDatabaseIfNotExist=true"

#
# com.mysql.cj.jdbc.Driver
#


# Adding AWS S3 Minio configs
sparkConf = (
    SparkConf()
    .set("spark.jars.ivy","/home/brijeshdhaker/.ivy2")
    .set("spark.jars.packages","org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.797,io.delta:delta-spark_2.12:3.3.2,io.unitycatalog:unitycatalog-spark_2.12:0.2.1")
    .set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .set("spark.sql.catalogImplementation", "hive")
    .set("spark.sql.catalog.spark_catalog.warehouse","s3a://warehouse/default")
    .set("spark.sql.warehouse.dir", "s3a://warehouse/default/spark")
    .set("javax.jdo.option.ConnectionURL", metastore_url)
    .set("spark.executor.heartbeatInterval", "300000")
    .set("spark.network.timeout", "400000")
    .set("spark.hadoop.fs.defaultFS", "s3a://defaultfs/")
    .set("spark.hadoop.fs.s3a.endpoint", "http://minio.sandbox.net:9010")
    .set("spark.hadoop.fs.s3a.access.key", "pgm2H2bR7a5kMc5XCYdO")
    .set("spark.hadoop.fs.s3a.secret.key", "zjd8T0hXFGtfemVQ6AH3yBAPASJNXNbVSx5iddqG")
    .set("spark.hadoop.fs.s3a.path.style.access", "true")
    .set("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
    .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .set("spark.hadoop.delta.enableFastS3AListFrom", "true")
    # 
    #.set("spark.eventLog.enabled", "true")
    #.set("spark.eventLog.dir", "file:///apps/var/logs/spark-events")
    #
    # Unity Catalog Configuration
    #.set("spark.sql.catalog.unitycatalog", "io.unitycatalog.spark.UCSingleCatalog")
    #.set("spark.sql.catalog.unitycatalog.uri", "http://ucserver.sandbox.net:8080")
    #.set("spark.sql.catalog.unitycatalog.token", "")
    #.set("spark.sql.defaultCatalog", "unitycatalog")

)

# configure the SparkSession with the configure_spark_with_delta_pip() utility function in Delta Lake:
builder = SparkSession.builder.appName("jupyter-pyspark").master("local[*]").config(conf=sparkConf)
spark = configure_spark_with_delta_pip(builder, extra_packages=["org.apache.hadoop:hadoop-aws:3.3.4,io.unitycatalog:unitycatalog-spark_2.12:0.2.1"]).getOrCreate()

#
sc = spark.sparkContext
sc.setLogLevel('ERROR')

#
#
#
def display(df):
    df.show(truncate=False)

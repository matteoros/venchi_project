from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, to_date

def main():
    spark = SparkSession.builder \
        .appName("VenchiDataLoading") \
        .getOrCreate()

    print("Hello from my-spark-project!")


if __name__ == "__main__":
    main()

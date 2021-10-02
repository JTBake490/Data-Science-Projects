from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import NaiveBayes, RandomForestClassifier, LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

SEED = 10

spark = SparkSession.builder.appName('Zoo_Classification').getOrCreate()

col_names = (
    'animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne',
    'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous',
    'fins', 'legs', 'tail', 'domestic', 'catsize', 'label'
)

df = spark.read.csv('../../ML Datasets/zoo/zoo.data', inferSchema=True)
df = df.toDF(*col_names)

# This is lumps all desired features into one "column"
feature_assembler = VectorAssembler(inputCols=df.columns[1:-1], outputCol='features')
df_output = feature_assembler.transform(df)
df_final = df_output.select('features', 'label')

algos = {
    'rfc' : RandomForestClassifier(featuresCol='features', labelCol='label', seed=SEED),
    'log_reg' : LogisticRegression(featuresCol='features', labelCol='label', family='multinomial')
    }

# PySpark's CrossValidator does not provide more than one metric, therefore a loop is necessary for all desired metrics
metrics = ('accuracy', 'weightedPrecision', 'weightedRecall', 'f1')
def fit_model(algo, dataframe, labelCol='label', predictionCol='prediction', metrics=metrics):
    scores = {}
    for metric in metrics:
        evaluator = MulticlassClassificationEvaluator(labelCol=labelCol, predictionCol=predictionCol, metricName=metric)
        pipeline = Pipeline(stages=[algo])
        param_grid = ParamGridBuilder().build()
        cross_val = CrossValidator(estimator=pipeline,
                                estimatorParamMaps=param_grid,
                                evaluator=evaluator,
                                numFolds=3,
                                collectSubModels=True)

        model = cross_val.fit(dataframe)
        scores[metric] = model.avgMetrics[0]
    return scores

if __name__ == '__main__':
    models = {}
    for name, algo in algos.items():
        models[name] = fit_model(algo, df_final)
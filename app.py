import pandas as pd
import preprocess


df=preprocess.read_csv('data/agaricus-lepiota.data')
df=preprocess.give_column_name(df)
df=preprocess.convert_to_csv(df)

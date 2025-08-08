import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dataset_banco.csv")
print(data.shape)
data.info()
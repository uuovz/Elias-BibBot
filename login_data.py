import pandas as pd

df = pd.read_csv("user.csv")

peopleArray = df[['username', 'password', 'place']].values.tolist()


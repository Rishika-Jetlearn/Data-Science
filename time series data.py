import pandas as pd
covid_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\WHO-COVID-19-global-data.csv")
print(covid_df.isna().sum())
covid_df.info()
covid_df["DateReported"]=pd.to_datetime(covid_df["DateReported"])
covid_df.info()
covid_df["year"]=covid_df["DateReported"].dt.year
print(covid_df)
covid_df["month_name"]=covid_df["DateReported"].dt.month_name()
print(covid_df)
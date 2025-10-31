import pandas as pd
import matplotlib.pyplot as plt
books_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\books.csv")
print(books_df)
print(books_df.isna().sum())
print(books_df.info())
#1.How many book are published by Scholastic?
print(books_df[books_df["publisher"]=="Scholastic Inc."]["title"].count())

#2.average rating
print(books_df["average_rating"].mean())

"""#3 author who has written the most books
authors=books_df["authors"].value_counts().head(10)
plt.bar(authors.index,authors.values)
plt.show()

#5.Which publishers released the most books?
publishers=books_df["publisher"].value_counts().head(10)
plt.bar(publishers.index,publishers.values)
plt.show()"""

#6.Highest rated books
books=books_df.sort_values(by="average_rating",ascending=False).head(20)
print(books[["title","average_rating"]])
plt.bar(books["title"],books["average_rating"])
plt.show()
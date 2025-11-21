import pandas as pd
import matplotlib.pyplot as plt
books_df=pd.read_csv(r"C:\Users\Manisha\Desktop\Jetlearn-python-rishika\Data-Science\books.csv")
print(books_df)
books_df["publication_date"]=pd.to_datetime(books_df["publication_date"],format="%m/%d/%Y",errors="coerce")#change format to YY/MM/DD
print(books_df.info())
books_df=books_df[books_df["publication_date"].isna()==False]

books_df=books_df[pd.to_numeric(books_df["text_reviews_count"],errors="coerce").notna()]#picking the numeric values
books_df["text_reviews_count"]=books_df["text_reviews_count"].astype(int)#turning the numeric values to integers(eg.like the date)
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
"""books=books_df.sort_values(by="average_rating",ascending=False).head(20)
print(books[["title","average_rating"]])
plt.bar(books["title"],books["average_rating"])
plt.show()"""
#Find the 10 authors with highest average rating for all their books combined.
author_avg = books_df.groupby(by="authors")["average_rating"].mean()
top_authors = author_avg.sort_values (ascending=False).head(10)
top_authors=top_authors.iloc[1:]
print(top_authors)

plt.bar(top_authors.index, top_authors)
plt.xticks(rotation=90)
plt.xlabel('Author')
plt.ylabel('Average Rating')
plt.title('Top 10 Authors by Average Book Rating')
plt.show()
#top 20 authors with most books
top_20=books_df['authors'].value_counts().head(20)
plt.bar(top_20.index,top_20)
plt.show()
#top 5 shortest books
shortest=books_df.sort_values(by="num_pages").loc[books_df["num_pages"]>0].head(5)
plt.bar(shortest["title"],shortest["num_pages"])
print(shortest[["title","num_pages"]])
plt.show()
#5 languages with the most number of books
lang_5=books_df.groupby(by="language_code").count().sort_values(by="title",ascending=False).head(5)
plt.pie(lang_5["title"],labels=lang_5.index,autopct='%1.0f%%')
plt.show()
#Create a pie chart for the number of books by top 5 publishers.
top_5_publishers=books_df.groupby(by="publisher").count().sort_index(ascending=False).head(5)
print(top_5_publishers)
plt.pie(top_5_publishers["title"],autopct='%1.0f%%',labels=top_5_publishers.index)
plt.show()
#Create a bar graph for the 10 books with most number of text reviews.
most_text_reviews=books_df.sort_values(by="text_reviews_count",ascending=False).head(5)
print(most_text_reviews)
plt.bar(most_text_reviews["title"],most_text_reviews["text_reviews_count"])
plt.xticks(rotation=90)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
# Our main focus will be to find out that is the netflix movie's duration is getting shorter with respect to time
# Providing the path to the data and reading it
netflix_data = pd.read_csv("C:/Users/JHF-PC/Downloads/netflix_data.csv", index_col=0)
# Subsetting the netflix_data for type movie and selecting only column of interest
netflix_data_movies_only = netflix_data[netflix_data["type"] == "Movie"]
netflix_movies_col_subset = netflix_data_movies_only[['title', 'country', 'genre', "release_year", "duration"]]
# Visualizing the data and for inspection
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]])
# Creating the Title and providing the Labels to the plot
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Movie Duration (min)")
# Creating plot
plt.show()
# As we can see from the plot that some of the movie's duration is less than 60 minutes
# Let's find out which movie genre's duration is 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]
print(short_movies[['genre']].head(20))
# We can see from the result that movies with genre Children, Documentaries and Stand-Up are most of the having
# duration less than 60 minutes
# Let's give these short movies genre unique colors
colors = []
for lab, row in netflix_movies_col_subset.iterrows():
    if row["genre"] == "Children":
        colors.append("red")
    elif row["genre"] == "Documentaries":
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
# Let's get this done
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]], c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Movie Duration (min)")
plt.show()

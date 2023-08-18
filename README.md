# Netflix-Movies-Duration-Analysis-Verses-Time
This project uses matplotlib.pyplot and pandas libraries from python and read csv file to perform insights. Our main focus is to visualize the changes in netflix movie's duration verses time.

First we convert the csv data in to pandas dataframe by using command pd.read_csv("path/to/csv/file") and then filter out only the type "Movies" from the given data. We also select only our columns of intrest

Now we visualize the data and we see that as time passes by the duration of the netflix movies is getting shorter but there is also some other intresting information. We can see from the scatter plot that sime of the movie's duration is less than 60 minutes.

We have to find out which movie's genre has movie duration less than 60 minutes and we apply some filtering methods and came up with the result that movies with genre "Children", "Documentaries" and "Stand-Up" have movies duration less than 60 minutes and our observation is true because such movies are made with duration less than 60 minutes

Now let's give these shorter movies genre,s a unique look by assigning them unique colors and make our scatter plot more colorful

And the scatter plot shows the result exactly we were expecting as most of the colorful area is below the 60 minutes duratiion.

Thank you very much for viewing my small project and feel free for contacting me. I'll be honoured if I remove all of the confusion

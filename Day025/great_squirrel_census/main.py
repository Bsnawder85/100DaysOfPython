# TODO create a table with the total amount of
#  grey, black, and cinnamon colored squirrels from the census data.
#  You will only need two columns: Fur Color and Count.
#  Use Pandas to figure out how to get the counts into a new CSV table.

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]['Unique Squirrel ID'].count()
grey_squirrels = data[data['Primary Fur Color'] == 'Gray']['Unique Squirrel ID'].count()
black_squirrels = data[data['Primary Fur Color'] == 'Black']['Unique Squirrel ID'].count()

squirrel_data = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}
squirrel_counts = pandas.DataFrame(squirrel_data)
squirrel_counts.to_csv("squirrel_count.csv")


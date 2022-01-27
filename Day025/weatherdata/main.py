# import csv
import pandas

# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if not row[1] == "temp":
#             print(row)
#             temperatures.append(int(row[1]))
#     for t in temperatures:
#         print(t)

data = pandas.read_csv("weather_data.csv")
temperatures = data['temp'].tolist()

# find the average temperature from the 'temp' data series
average = sum(temperatures) / len(temperatures)
print(average)

# using Pandas is also way faster
avg = data['temp'].mean()
print(avg)

# find the max temp value using Pandas

mx = data['temp'].max()
print(mx)

print(data.condition)

# Get data in a Row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

print(data[data.day == 'Monday'].condition)

monday = data[data.day == 'Monday']
far = monday.temp * (9/5) + 32
print(far)

# Create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('students.csv')


# FILE_NAME="weather_data.csv"

# # with open(FILE_NAME) as file:
# #     data=file.readlines()

# # print(data)

# # with open(FILE_NAME) as file:
# #     data = csv.reader(file)

# #     export_data=[]
# #     for row in data:
# #         export_data.append(row)

# # headers=export_data[0]
# # export_data.pop(0)

# # temperatures=[]
# # for row in export_data:
# #     temperatures.append(int(row[1]))

# # print(temperatures)

# import pandas

# data = pandas.read_csv(FILE_NAME)


# # max_temp=data['temp'].max()

# # print(data[data.temp == max_temp])

# monday=data[data.day == "Monday"]

# md_temp=int(monday.temp)
# md_temp_fahrenheit=md_temp*9/5 + 32
# print(md_temp_fahrenheit)

import pandas
FILE_NAME="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(FILE_NAME)

#print(data['Primary Fur Color'])

squirrel_types = ['Gray', 'Cinnamon', 'Black']

sq_counts=[]

for tp in squirrel_types:
    tmp=data[data['Primary Fur Color'] == tp]
    sq_counts.append(len(tmp))

data_dict = {
    "sq_types": squirrel_types,
    "counts": sq_counts
}

count_data=pandas.DataFrame(data_dict)
count_data.to_csv("Squirrel_counts.csv")



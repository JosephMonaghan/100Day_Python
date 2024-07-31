import requests
import os
import datetime as dt
import pandas

PIXELA_ENDPOINT="https://pixe.la/v1/users"
username = "joseph01234"
token = os.environ.get("pixela_token")
#token = "adsfadsfjkine"

user_params = {
    "username": username,
    "newToken": "adsfadsfjkine"
}



graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"

graph_params = {
    "id": "cycling",
    "name": "cycling",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

headers_pixela = {
    "X-USER-TOKEN": token
}

# response = requests.put(url=PIXELA_ENDPOINT,json=user_params,headers=headers_pixela)
# print(response.text)

# # output = requests.post(url=graph_endpoint,json=graph_params,headers=headers_pixela)
# # print(output.text)


data = pandas.read_csv("Joseph01234_workouts.csv")


pixel_endpoint=f"{graph_endpoint}/{graph_params['id']}"
for row, vals in data.iterrows():
    if vals["Fitness Discipline"] == "Cycling":
        #print(vals["Distance (km)"])
        year = vals["Workout Timestamp"].split("-")[0]
        month = vals["Workout Timestamp"].split("-")[1]
        day = vals["Workout Timestamp"].split("-")[2]
        day =day.split(" ")[0]

        pixel_params = {
            "date": f"{year}{month}{day}",
            "quantity": str(vals["Distance (km)"]),
        }

        output = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers_pixela)
        print(output.text)
        output.raise_for_status()

        

# today = dt.datetime.now()
# pixel_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "70",
# }



# output = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers_pixela)
# print(output.text)



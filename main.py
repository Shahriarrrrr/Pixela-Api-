import requests
import datetime

USERNAME = "" #Give your own username
TOKEN = "" #Make you own token
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": "ha1231231231@",
    "username": "shahriar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS) #Create user
# print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_PARAMS = {
    "id": "running1",
    "name": "Running graph",
    "unit": "kmt",
    "type": "float",
    "color": "momiji"
}

HEADERS = {
    "X-USER-TOKEN":TOKEN
}


# graph_response = requests.post(url=GRAPH_ENDPOINT,json=GRAPH_PARAMS,headers=HEADERS) #Create the graph
# print(graph_response.text)

today_date = datetime.date.today()
# # formated_date = today_date.replace("-","")
# formated_date = "20240912"


PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/running1"
PIXEL_PARAMS = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many Kilometers did you cycle today?\n"),
}

pixel_response = requests.post(url=PIXEL_ENDPOINT,json=PIXEL_PARAMS,headers=HEADERS) #Update the Pixel
print(pixel_response.text)

# DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/running1/20240913"
# delete_response = requests.delete(url=DELETE_ENDPOINT,headers=HEADERS)
# print(delete_response)
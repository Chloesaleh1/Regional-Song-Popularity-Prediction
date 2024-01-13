import requests
import json
import csv
import pandas as pd
import time

CLIENT_ID = '798448aecc324976bf1bc428fc5d269a'
CLIENT_SECRET = '4897cc068f474fa5a41aedd097a0c6ed'

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

track_id = ""
track_ids = []
with open('audio_ids.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    fifty_count = 0
    track_count = 0
    for row in csv_reader:
        if(track_count == 0 and fifty_count == 0):
            print(row)
        if(track_count == 49):
            fifty_count += 1
            track_id += row[1]
            track_ids.append(track_id)
            track_id = ""
            track_count = 0
        else:
            track_id += row[1] + ","
            track_count += 1

csv_file = 'output.csv'
data = list()
X = 4000
Y = 4000
for i in range(X, len(track_ids)):
    r = requests.get(BASE_URL + 'tracks?ids=' + track_ids[i], headers=headers)
    #time.sleep(0.5)
    print(i)
    if(i % 100 == 0):
        print("Running...", r)
    # if(r.json() == None):
    #     continue
    print(r)
    if(r.json() != None and "tracks" in r.json()):
        tracks = r.json()["tracks"]
        for track in tracks:
            if(track["available_markets"] != None and len(track["available_markets"]) != 0):
                data.append((track["id"],track["available_markets"],track["popularity"]))
            else:
                track["available_markets"] = []
                data.append((track["id"],track["available_markets"],track["popularity"]))
        

with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    row = ["track_id","available_markets","popularity"]
    if file.tell() == 0:
        writer.writerow(row)
    writer.writerows(data)



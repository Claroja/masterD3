import json
dic = [{"x1":i,"y1":0.01*i*i,"x2":i+1,"y2":0.01*(i+1)*(i+1)} for i in range(-150,151,1)]
json.dump(dic,open("./test.json","w"))


import pandas as pd
df = pd.read_json("./temp/world_map.json")
for i in range(len(df['features'])):
    if df['features'][i]['geometry'] == None:
        df.drop(i, axis=0, inplace=True)
df=df.reset_index(drop=True)
df.to_json("./temp/world_map2.json")

df2 = pd.read_json("./temp/china.geojson")

import json
a=json.load(open("./temp/world_map.json","r"))
a['features']

li=[]
for i in range(len(a['features'])):
    if a['features'][i]['geometry']:
        li.append(a['features'][i])

b={'features':li,'type':a['type']}
json.dump(b,open("./temp/world_map2.json","w"))
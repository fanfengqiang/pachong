import json

lifile=[]

with open('./ip.txt','r') as f:
    for line in f.readlines():
        rs = line.rstrip('\n')
        lifile.append({"proxy":'http://'+rs,"proxy_scheme":"http"})
    pass
jsfile=json.dumps(lifile)

with open('./proxy_list.json', "w") as f:
    f.write(jsfile)
    f.close()
import requests

url = "https://raw.githubusercontent.com/kalyaniuniversity/mgx-datasets/master/DLBCL/datasets/dlbcl-fl.csv"

res = requests.get(url, allow_redirects=True)

with open('dlbcl-fl.csv', 'wb') as f_obj:
    f_obj.write(res.content)

print("Done")
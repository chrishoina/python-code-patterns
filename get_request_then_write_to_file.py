# make sure you "pip or pip3 install" the requests library. The Json library should come pre-packaged with python.
import requests 
import json 

#use your "target (aka web site of interes) URL in this field"
# you don't need the [] for this, just the URL.
url = "https://www.[target url].html"

response = requests.get(url)

# this is a cut/paste from the requests documentation. You can modify chunk size, but it doesn't seem necessary to do. Like the url above, you don't need the [], just chose a file name in between the quotes. 'wb' stands for "write in binary".

# Once this is written, it should be located in the same folder where your python file lives. 

with open('[chosen file name]', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=128):
        fd.write(chunk)

# This isn't necessary, but it will show you in termimal if the request status code was successful (a 200 is good, versus a 404 which is bad)
print(response.status_code)
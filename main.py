import requests
import json

if __name__ == '__main__':
    url= 'https://httpbin.org/post'
    payload = {'nombre':'Roberto','curso':'python', 'nivel':'intermedio'}

    response = requests.post(url, data= json.dumps(payload) )
    #print(response.url)
    #print(response)
    if response.status_code == 200:
        #print(response.content)
        #content = response.content
        #response_json = response.json() #dict
        #origin = response_json['origin']
        #print(origin)
        #print(content)
        #file = open('google.html', 'wb')
        #file.write(content)
        #file.close()
        #response_json = json.loads(response.text)
        #origin = response_json['origin']
        #print(origin)
        print(response.content)

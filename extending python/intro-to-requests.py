#https://pypi.org/project/requests/



import requests 

#curl -I http://httpbin.org/get
x = requests.get('http://httpbin.org/get')

print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code == 200:
    print("success!")
elif x.status_code == 404:
    print("not found")

print(x.elapsed)
print(x.cookies)



'''

x = requests.get('http://httpbin.org/get', params={'id':'1'})
print(x.url)

x = requests.get('http://httpbin.org/get?id=2')
print(x.url)


x = requests.get('http://httpbin.org/get', params={'id':'3'}, headers={'Accept':'application/json', 'test_header':'test'})
print(x.text)

x = requests.delete('http://httpbin.org/delete')
print(x.text)


x = requests.post('http://httpbin.org/post', data={'a':'b','c':'b','e':'f'})
print(x.text)




#wget https://images.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png
files = {'filr': open('googlelogo_light_color_272x92dp.png','rb')}
x = requests.post('http://httpbin.org/post',files=files)
print(x.text)

# to run this function below put this in terminal :(echo -ne dXNlcm5hbWU6cGFzc3dvcmQ= | base64 -d )
x = requests.get('http://httpbin.org/get', auth=('username','password'))
print(x.text)

x = requests.get( 'http://expeired.badssl.com',verify=False)

'''


#curl -I https://github.com
x = requests.get('http://github.com',allow_redirects=False)
print(x.content)

x = requests.get('http://httpbin.org/get', timeout= 1)
print(x.content)

x = requests.get('http://httpbin.org/cookies' , cookies= {'a':'b'})
print(x.content)

x = requests.Session()
x.cookies.update({'a':'b'})
print(x.get('http://httpbin.org/cookies').text)
print(x.get('http://httpbin.org/cookies').text)




x = requests.get('http://api.github.com/events')
print(x.json())


x = requests.get('https://images.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png')
with open('google2.png','wb') as f:
    f.write(x.content)





'''
also study 

Automatic Content Decompression and Decoding
SOCKS Proxy Support
Streaming Downloads
Chunked HTTP Requests


from   https://pypi.org/project/requests/
'''
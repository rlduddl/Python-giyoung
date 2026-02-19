from urllib import request

target = request.urlopen("https://www.google.com")
output = target.read()
print(output)
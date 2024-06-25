import urllib.request as ur
import webbrowser


url = 'http://www.example.com'
conn = ur.urlopen(url)
conn.status

data = conn.read()
print(data[:50])
str_data = data.decode('utf-8')
print(str_data[:50])

for key, value in conn.getheaders():
    print(key, value)
    


url = 'http://www.python.org/'
webbrowser.open_new(url)
webbrowser.open(url)
webbrowser.open_new_tab(url)



import socket


socket.gethostbyname('www.crappytaxidermy.com')
socket.gethostbyname_ex('www.crappytaxidermy.com')
socket.getaddrinfo('www.crappytaxidermy.com', 80)
socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET, socket.SOCK_STREAM)
socket.getservbyname('http')
socket.getservbyport(80)
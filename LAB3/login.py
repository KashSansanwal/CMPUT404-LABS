'''
Name: Kashish Sansanwal
Date: 27/1/2023
Lab: 3
'''

import cgi
import cgitb 
cgitb.enable() 
from templates import login_page, secret_page, after_login_incorrect
import secret
import os
import http.cookies as SimpleCookie

s = cgi.FieldStorage() 

username,password = s.getfirst("username"), s.getfirst("password")
form_ok = username == secret.username and password == secret.password 

cookie = SimpleCookie.SimpleCookie(os.environ.get("HTTP_COOKIE")) 
cookie_username, cookie_password = None, None

if cookie.get("username"):
    cookie_username = cookie.get("username").value 
if cookie.get("password"): 
    cookie_password = cookie.get("password").value 

cookie_ok = cookie_username == secret.username and cookie_password == secret.password 

if cookie_ok: 
    username = cookie_username
    password = cookie_password  

print("Content-Type: text/html")

if form_ok: 
    print(f"Set-Cookie: username={username}") 
    print(f"Set-Cookie: password={password}") 
print()

if not username and not password: 
    print(login_page()) 

elif username == secret.username and password == secret.password: 
    print(secret_page(username, password))

else:
    print(login_page())
    print(f"username: {username}, password: {password}")
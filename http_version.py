import sys
import requests
from bs4 import BeautifulSoup
name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

page_load = requests.get("http://demo-rails-app-testing.ipm-corporation.com/signup")
cookies = dict(page_load.cookies)
soup = BeautifulSoup(page_load.text, 'html.parser')
auth_token = soup.findAll(attrs={"name" : "authenticity_token"})[0]['value']

data = {
  'utf8': '\u2713',
  'authenticity_token': auth_token,
  'user[name]': name,
  'user[email]': email,
  'user[password]': password,
  'user[password_confirmation]': password,
  'commit': 'Create my account'
}

response = requests.post(
    'http://demo-rails-app-testing.ipm-corporation.com/users',
    cookies=cookies,
    data=data,
    verify=False
)







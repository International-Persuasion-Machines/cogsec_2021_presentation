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

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
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
    'http://demo-rails-app-testing.ipm-corporation.com/users?block_bot_useragents=true',
    cookies=cookies,
    data=data,
    headers=headers,
    verify=False
)
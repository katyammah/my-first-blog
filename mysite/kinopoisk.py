import requests
user_id = 51389537
url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)
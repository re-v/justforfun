# https://api.github.com/search/repositories?q=topic:crawler+language:python+created:2018-07-15
# https://api.pushover.net/1/message.json?token=xx&message=xx

#get_info_list -- push it

from datetime import datetime
import requests

def get_info_list():
    api = 'https://api.github.com/search/repositories?q='
    query = 'topic:crawler+language:python+'
    when = 'created:' + '2018-02-08'
    # when  = 'create:' + str(datetime.now()).split()[0]
    full_url = api + query + when
    r = requests.get(full_url)
    return r.json()['items']

def make_message(repo_info):
    title = repo_info['name']
    url = repo_info['html_url']
    message = repo_info['description']
    token = 'a9s5y8vk4phsa7sejx3j4m2a9jsek4'
    user = 'udijy4h3x9xeddqx7m3ee3rzn6uvbp'
    api = 'https://api.pushover.net/1/message.json?'
    template = 'token={token}&user={user}&title={title}&url={url}&message={message}'
    query = template.format(
        token=token,
        user=user,
        title=title,
        url=url,
        message=message,
    )
    full_url = api + query
    return full_url

def push_it(message):
    requests.post(message)
    print('ok!')

info_list = get_info_list()
for info in info_list:
    message = make_message(info)
    push_it(message)

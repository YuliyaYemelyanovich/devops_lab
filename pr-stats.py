import requests
import getpass
import argparse

#def parse_args







#getpass.getpass()
uname = 'yuliyayemelyanovich'
pwd = getpass.getpass()
url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?page=1&per_page=100'
all_pr = requests.get(url, auth=(uname, pwd), params={'state': 'all'}).json()
closed_pr = requests.get(url, auth=(uname, pwd), params={'state': 'closed'}).json()
open_pr = requests.get(url, auth=(uname, pwd), params={'state': 'open'}).json()

print('All requests: %d \nOpened requests: %d \nClosed requests: %d' % (len(all_pr), len(closed_pr), len(open_pr)))


for i in all_pr:
	if i['user']['login'] == 'YuliyaYemelyanovich':
		print(i['title'])


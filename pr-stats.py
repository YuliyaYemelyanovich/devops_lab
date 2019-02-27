import requests
import getpass
import argparse
import time


class PR_stats:

    def __init__(self):
        args = PR_stats.parse_args()
        self.username = args.username
        self.repo = args.repo
        self.login = args.login
        self.title = args.title
        self.before = args.before
        self.after = args.after
        self.pr_info = self.get_pr_info()

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(prog='Pull Requests statistics')
        parser.add_argument('username', help='Username to login on github')
        parser.add_argument('repo', help='Repo information in format username/repo')
        helptext = 'Output pull requests opened by user with given login'
        parser.add_argument('--login', '-l', help=helptext)
        parser.add_argument('--title', '-t', help='Output pull requests with given title')
        helptext = 'Output pull requests opened before given in format yyyy-mm-dd h:m:s'
        parser.add_argument('--before', '-b', help=helptext)
        helptext = 'Output pull requests opened after given date in format yyyy-mm-dd h:m:s'
        parser.add_argument('--after', '-a', help=helptext)
        parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
        return parser.parse_args()

    def run(self):
        self.print_stats()
        if(self.login is not None):
            self.search_by_login()
        if(self.title is not None):
            self.search_by_title()
        if(self.before is not None):
            self.search_before()
        if(self.after is not None):
            self.search_after()
        self.print_pr_info()

    def get_pr_info(self):
        url = 'https://api.github.com/repos/{}/pulls?page=1&per_page=100'
        url = url.format(self.repo)
        pwd = getpass.getpass()
        return requests.get(url, auth=(self.username, pwd), params={'state': 'all'}).json()

    def print_stats(self):
        closed = 0
        opened = 0
        all_pr = 0
        for i in self.pr_info:
            if(i['state'] == 'open'):
                opened += 1
            else:
                closed += 1
            all_pr += 1
        print('     =====STATISTICS=====     ')
        print('Pull requests in repo %s' % self.repo)
        print('Total: {} '.format(all_pr))
        print('Opened: {} ({}%)'.format(opened, round(opened / all_pr * 100, 1)))
        print('Closed: {} ({}%)'.format(closed, round(closed / all_pr * 100, 1)))
        print('     ====================     ')

    def search_by_login(self):
        result = []
        for pr in self.pr_info:
            if pr['user']['login'] == self.login:
                result.append(pr)
        self.pr_info = result

    def search_by_title(self):
        result = []
        for pr in self.pr_info:
            if self.title in pr['title']:
                result.append(pr)
        self.pr_info = result

    def search_before(self):
        result = []
        try:
            before = time.strptime(self.before, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print('Invalid data format!')
            exit()
        for pr in self.pr_info:
            created_at = time.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            if created_at <= before:
                result.append(pr)
        self.pr_info = result

    def search_after(self):
        result = []
        try:
            after = time.strptime(self.after, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print('Invalid data format!')
            exit()
        for pr in self.pr_info:
            created_at = time.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            if created_at >= after:
                result.append(pr)
        self.pr_info = result

    def print_pr_info(self):
        length = len(self.pr_info)
        if length == 0:
            print('Nothing found!')
        else:
            print('Pull requests found: {}'.format(length))
            print('---------------')
            for pr in self.pr_info:
                print('Title: {}'.format(pr['title']))
                print('State: {}'.format(pr['state']))
                print('Opened by: {}'.format(pr['user']['login']))
                print('Created at: {}'.format(pr['created_at']))
                print('---------------')


if __name__ == '__main__':
    pr = PR_stats()
    pr.run()

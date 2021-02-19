'''
here we used threading module and instead of calling visit_website function we creates separate
threads for each website and start the threads. So instead of waiting for the response of first
function in for loop call sequence websites triggering separately without any dependency.

'''

import time
import threading
import requests

websites = ['https://www.linkedin.com/',
            'https://www.oreilly.com/',
            'https://www.indeed.com/',
            'https://www.glassdoor.com/',
            'https://www.cv-library.ie/search-jobs',
            'https://leetcode.com/',
            'https://docs.python.org/3/library/',
            'https://www.tutorialspoint.com/',
            'https://interviewgenie.com/resources',
            'https://wiki.python.org/moin/TimeComplexity',
            'https://github.com/ARBaynes/python-anagrams',
            'https://pypi.org/project/filelock/',
            'https://www.pramp.com/']


def visit_websites(url):
    """
        Makes a GET request to a website URL and prints response information
    """
    r = requests.get(url)

    print(f'{url} returned {r.status_code} after {r.elapsed} seconds')
    print(time.time() - start)

start=time.time()
if __name__ == '__main__':
    for website in websites:
        thread_object = threading.Thread(target=visit_websites, args=[website])
        thread_object.start()

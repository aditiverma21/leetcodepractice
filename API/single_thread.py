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


if __name__ == '__main__':

    print("Start of main thread")
    for website in websites:
        visit_websites(website)
    print("End of main thread")

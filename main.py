import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'W3'
HOMEPAGE = 'https://www.w3schools.com/sql/func_mysql_ucase.asp'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME , HOMEPAGE , DOMAIN_NAME)



#each queued links is a new job
def create_jobs():
    for link in file_to_sets(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# check if there are items in the queue , if so crawl them
def crawl():
    queue_links = file_to_sets(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) +  'links in the queue')
        create_jobs()








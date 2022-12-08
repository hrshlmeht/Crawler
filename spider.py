from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:

    # class variables (shared amongst all the instances)

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self , project_name , base_url , domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + './queue.txt'
        Spider.crawled_file = Spider.project_name + './crawled.txt'
        self.boot()
        self.crawl_page('First Spider' , Spider.base_url)

    @staticmethod
    def boot():
        create_project_directory(Spider.project_name)
        create_data(Spider.project_name , Spider.base_url)
        Spider.queue = file_to_sets(Spider.queue_file)
        Spider.crawled = file_to_sets(Spider.crawled_file)












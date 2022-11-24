import os

# path = r"my/path/to/file.txt"
# assert os.path.isfile(path)
# with open(path, "r") as f:
#     pass
#

# each website is crawled will be having a separate folder
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)


def create_data(project_name , base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    f =open(path,'wb')
    f.write(data)
    f.close()

write_file('Directory1' , 'https://www.linkedin.com/in/harshalmehtaprofile/' )


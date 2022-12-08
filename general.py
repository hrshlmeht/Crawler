import os
#each website you crawl is a different folder
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)
#aking the data
def create_data(prj_name , base_url):
    queue =   prj_name + '/queue.txt'
    crawled = prj_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue, base_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

#create a new file
def write_file(path , data):
    f= open(path , 'w')
    f.write(data)
    f.close()

#adding to the current existing file
def append_to_file(path, data):
    with open(path , 'a') as file:
        file.write(data + '\n')


#delete the contents of the text
def delete_file_content(path):
    with open(path , 'w'):
        pass


#read a file and convert each item into set items
def file_to_sets(filename):
    results = set()
    with open(filename , 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))  #nothing just replacing the \n with nothing

    return results


#iterate through a set , as each item will be there in the new file
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
            append_to_file(file , link)




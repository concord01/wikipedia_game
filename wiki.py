import wikipediaapi
from queue import Queue
import time

user_agent = "p3_wiki (ho7652jo0401@pusd.us)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")


# function to return list of links
def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)
    return links_list


def wikipedia_game_solver(start_page, target_page):
    print("working on it...")
    start_time=time.time()

    queue = Queue() #queue for which items to check
    visited = set() #keeps track of visited links
    parent = {} #dictionary to keep track of parent

    # start off by adding start page to queue and visited pages
    queue.put(start_page.title)
    visited.add(start_page.title)

    #keep looping as long as queue is not empty
    while not queue.empty():
        #get next item in queue
        current_page_title = queue.get()
        #break out of loop if we find page we're looking for
        if current_page_title == target_page.title:
            break
        
        #fetch all the links at the current page
        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        #go through each of the links and add them to queue
        for link in links:
            #if page hasn't already been visited
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title
    #reconstruct path from target page to start page
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_titile = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("this algorithm took", end_time - start_time, "seconds")
    return path




        
#setting pages for wiki game
start_page = wiki.page("Queen (band)")
target_page = wiki.page("Joe Biden")

path = wikipedia_game_solver(start_page, target_page)
print(path)
import wikipediaapi
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
    links = fetch_links(start_page)

    # make a loop that checks every item in links and prints a message if target_page.title is in that list
    for link in links():
        if link == target_page.title:
            print("link found")
            
    
        
#setting pages for wiki game
start_page = wiki.page("Queen (band)")
target_page = wiki.page("Joe Biden")

wikipedia_game_solver(start_page, target_page)
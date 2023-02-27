import requests
from bs4 import BeautifulSoup
import time

def makeChooser(number):
    def result(list: list):
        if(len(list) >= number):
            return list[number - 1]
        else: 
            return ""
    return result


def scrapeYield(chooser,wikiLink, bannedLinks, bannedPrefixes):
    nextLink = wikiLink
    chosenLinks = [wikiLink]
    running = True
    comment = ""

    while running:
        links = getLinksFromPage(nextLink, bannedLinks, bannedPrefixes)
        nextLink = chooser(links)

        if nextLink == "":
            running = False
            comment = "Found an end."
        elif nextLink in chosenLinks:
            running = False
            comment = "Hit a loop."
        else:
            yield nextLink + "\n"
            chosenLinks.append(nextLink)
            
        time.sleep(1)

    yield "Stopped: " + comment
    yield " Found " + str(len(chosenLinks) - 1) + " links."


def checkLink(link,bannedLinks, bannedPrefixes):
    for s in bannedPrefixes:
        if (link.startswith(s)):
            return False
    return link not in bannedLinks

def getLinksFromPage(link, bannedLinks, bannedPrefixes):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    if r.ok:
        links = []
        ps = soup.find_all('p')
        for p in ps:
            foundLinks = p.find_all('a')
            for link in foundLinks:
                if link.has_attr('href'):
                    href = link['href']
                    if href[0] == '/' and checkLink(href, bannedLinks, bannedPrefixes):
                        links.append('https://en.wikipedia.org' + href)
        return links
    else:
        print(link)
        return []


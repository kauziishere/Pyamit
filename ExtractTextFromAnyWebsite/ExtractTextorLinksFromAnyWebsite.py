from bs4 import BeautifulSoup
import urllib
class extractData:
	def __init__(self, url):
		self.url = url
		self.header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
		self.soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=self.header)),'html.parser')

	def extract_text(self):
		return self.soup.get_text()

	def extract_links(self):
		links = [link.get('href') for link in self.soup.find_all('a')]
		return links

	def extract_title(self):
		return self.soup.title.string

"""
	Demo example
"""	
if __name__ == "__main__":
	obj = extractData("https://www.cs.cmu.edu/~./10701/description.html")
	print(obj.extract_title())
	print(obj.extract_links())
	print(obj.extract_text())

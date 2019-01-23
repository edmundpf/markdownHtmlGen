#:::gitScrape:::

import os
import requests
from utils import printerLib
from bs4 import BeautifulSoup

#:::SCRAPER CLASS:::

class Scraper:

	#: Init

	def __init__(self, url, filename=None):
		self.url = url
		self.printer = printerLib.Printer()
		self.color = self.printer.color
		self.filename = filename

	#: Get Page

	def getPage(self):

		return BeautifulSoup(requests.get(self.url).text, features='html.parser').find('div', {'class': 'Box-body p-6'})

	#: Get HTML/CSS from File

	def get_code(self, file):

		_str = ''

		with open(os.path.dirname(__file__) + '/' + file, 'r') as f:
			for line in f:
				if '\n' in line and line != '\n':
					_str += line[:(len(line) - 1)]
				elif '\n' not in line and len(line) >= 1:
					_str += line
		f.close()

		return _str

	#: Style Wrapping

	def styleWrap(self):

		markdown_css = self.get_code('../data/github-markdown.min.css') + self.get_code('../data/github-custom.min.css')
		self.printer.printLog('Retrieved Github markdown CSS files...')

		html_wrap = '<html><head><style>{0}</style></head><body>{1}</body></html>'
		github_html = self.getPage()
		self.printer.printLog('Scraped Github markdown HTML from public repository...')

		return BeautifulSoup(html_wrap.format(markdown_css, github_html), features='html.parser').prettify()

	#: Save Markdown HTML

	def saveMarkdown(self):

		if self.filename == None:
			file = os.path.abspath(os.path.dirname(__file__) + '/../files/' + self.url[(self.url.rfind('/') + 1):] + '.html')
		else:
			file = os.path.abspath(os.path.dirname(__file__) + '/../files/' + self.filename + '.html')

		f = open(file, 'w')
		f.write(self.styleWrap())
		self.printer.printLog('Wrapped Github HTML for proper styling...')
		f.close()

		self.printer.printSuccess('Saved markdown HTML to file: ' + self.color.bold_orange(file))

		return file

#:::END PROGRAM:::
#:::gitHtmlMaster:::

import sys
from utils import printerLib
from utils.gitScrape import Scraper

class Worker:

	#: Init

	def __init__(self, args=sys.argv, style='monokai'):

		self.printer = printerLib.Printer()
		self.color = self.printer.color
		self.printer.printLog(self.color.bold_purple('Markdown HTML Generator Launched...'))
		self.getArguments(args)

	#: Get Arguments

	def getArguments(self, init_args):

		try:

			args = {'file': ['-f', '--file'],
					'url': ['-u', '--url']}

			print_args = []

			for i in range(1, len(init_args)):
				for key in args:
					if init_args[i] in args[key]:
						if (i + 1) < len(init_args):
								setattr(self, key, init_args[i + 1])
								print_args.append(str(self.color.bold_orange(key.capitalize())) + ': ' + init_args[i + 1])
								break

			req_exit = False

			if 'url' not in self.__dict__:
				req_exit = printError('Missing URL argument.')

			if req_exit == True:
				self.printer.printExit('Invalid arguments.')
			else:
				self.printer.printLog(self.color.bold_seaGreen('ARGUMENTS: ') + ', '.join(print_args))

		except Exception as e:
			if str(e)[-1] != '.':
				e_str = str(e) + '.'
			else:
				e_str = str(e)
			self.printer.printExit('Invalid arguments: ' + e_str)

	#: Generate File

	def fileGen(self):

		if 'file' in self.__dict__:
			scraper = Scraper(url=self.url, filename=self.file)
		elif 'file' not in self.__dict__:
			scraper = Scraper(url=self.url)

		scraper.saveMarkdown()

#:::DRIVER:::

main = Worker()
main.fileGen()

#:::END PROGRAM:::
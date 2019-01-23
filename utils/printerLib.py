#:::printerLib:::

import sys
import datetime
import colorful

#:::PRINTER CLASS:::

class Printer:

	#: Init

	def __init__(self, style='monokai'):
		self.color = colorful
		self.color.use_style(style)

	#: Print Log w/ timestamp

	def printLog(self, text):

		print(self.color.bold(datetime.datetime.now().strftime("%m/%d/%Y-%H:%M:%S")) + ' ' + text)

	#: Print error message

	def printError(self, text):

		self.printLog(self.color.bold_magenta('ERROR: ') + text)
		return True

	#: Print success message

	def printSuccess(self, text):

		self.printLog(self.color.bold_seaGreen('SUCCESS: ') + text)
		return True

	#: Print exit message and exit

	def printExit(self, text):

		self.printLog(self.color.bold_magenta('ERROR: ') + text + ' Will exit...')
		sys.exit()
import time
from Helpers import HSL

class LED (object):
	def __init__ (self):
		self.fromColor = HSL([0, 0, 1])
		self.currentColor = HSL([0, 0, 1])
		self.toColor = HSL([0, 0, 1])
		self.interpolateTime = 5
		self.imterpolateStartTime = 0

	def update (self):
		if self.fromColor != self.toColor:
			# TODO: interpolation magic goes here
			percentDone = (time.time() - self.imterpolateStartTime) / self.interpolateTime
			if percentDone >= 1:
				self.fromColor = self.toColor
			self.currentColor = HSL([self.fromColor.h + (self.fromColor.h - self.toColor.h) / percentDone, self.fromColor.s + (self.fromColor.s - self.toColor.s) / percentDone, self.fromColor.l + (self.fromColor.l - self.toColor.l) / percentDone])
		self.setColor(self.currentColor, False)

	def setColor (self, color, flashFade):
		# TODO: interface w/ uPayMeiFixIt's LED hardware interface
		# if flashFade:
			print color
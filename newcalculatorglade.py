#!/usr/bin/env python

import sys
import math
try:
	#import pygtk
	import gi
	#pygtk.require('3.0')
	gi.require_version('Gtk', '3.0')
except:
	pass
try:
	#import gi
	#import gtk3.glade
	from gi.repository import Gtk
	#import Gtk.glade

except:
	print('GTK not available')
	sys.exit(1)

class Calculator:
	def __init__(self):
		self.eval_string=""
		self.gladefile = "calculator.glade"
		self.wTree = Gtk.Builder()
		self.wTree.add_from_file(self.gladefile)
		dic = {
			"on_window_calculator_destroy" :self.quit_cancel,
			"on_Apply_clicked" : self.quit_apply,
			"on_Cancel_clicked" : self.quit_cancel,
			"on_CLR_clicked" : self.displayClr,
			"on_Pi_clicked" : self.displayPi,
			"on_Left_bracket_clicked" : self.displayLeftBracket,
			"on_Right_bracket_clicked" : self.displayRightBracket,
			"on_Seven_clicked" : self.displaySeven,
			"on_Eight_clicked" : self.displayEight,
			"on_Nine_clicked"  : self.displayNine,
			"on_Divide_clicked" : self.displayDiv,
			"on_Four_clicked" : self.displayFour,
			"on_Five_clicked" : self.displayFive,
			"on_Six_clicked" : self.displaySix,
			"on_Multiply_clicked" : self.displayMultiply,
			"on_One_clicked" : self.displayOne,
			"on_Two_clicked" : self.displayTwo,
			"on_Three_clicked" : self.displayThree,
			"on_Minus_clicked" : self.displayMinus,
			"on_Zero_clicked" : self.displayZero,
			"on_Dot_clicked" : self.displayDot,
			"on_Equal_clicked" : self.displayEqual,
			"on_Add_clicked" : self.displayAdd,
			"on_visibility_notify" : self.visibility_notify,
			"on_toggle_clicked" : self.show_visibility,
			}
			
		self.wTree.connect_signals( dic )
		
		# ### window.connect("notify::title", callback)
		#self.CalcKbd = self.wTree.get_object("CalcKbd")
		
		self.window = self.wTree.get_object("window_calculator")
		self.window.show()

	def compute(self):
		print"string:",self.eval_string
		try   :
			b=str(eval(self.eval_string))
		except:
			b= "error"
			print"error string:",self.eval_string,sys.exc_info()[0]
			self.eval_string=''
		else  : self.eval_string=b
		self.wTree.get_object("displayText").set_text(b)

	def delete(self):
		self.eval_string=''
		self.wTree.get_object("displayText").set_text("")

	def displayOperand(self,i):
		self.eval_string=self.eval_string+i
		self.wTree.get_object("displayText").set_text(str(self.eval_string))
	
	def displayClr(self,widget):
		self.delete()

	def displayLeftBracket(self,widget):
		self.displayOperand("(")

	def displayRightBracket(self,widget):
		self.displayOperand(")")

	def displaySeven(self,widget):
		self.displayOperand("7")

	def displayEight(self,widget):
		self.displayOperand("8")

	def displayNine(self,widget):
		self.displayOperand("9")
	
	def displayFour(self,widget):
		self.displayOperand("4")

	def displayFive(self,widget):
		self.displayOperand("5")

	def displaySix(self,widget):
		self.displayOperand("6")

	def displayOne(self,widget):
		self.displayOperand("1")

	def displayTwo(self,widget):
		self.displayOperand("2")

	def displayThree(self,widget):
		self.displayOperand("3")

	def displayZero(self,widget):
		self.displayOperand("0")

	def displayDot(self,widget):
		self.displayOperand(".")	

	def displayPi(self,widget):
		self.displayOperand("math.pi")	
	
	def displayDiv(self,widget):
		self.displayOperand("/")	

	def displayMultiply(self,widget):
		self.displayOperand("*")
	
	def displayMinus(self,widget):
		self.displayOperand("-")
	
	def displayEqual(self,widget):
		self.compute()

	def displayAdd(self,widget):
		self.displayOperand("+")

	def quit_apply(self,widget):
		self.compute()
		print "last evaluation",self.wTree.get_object("displayText").get_text()
		Gtk.main_quit()

	def quit_cancel(self,widget):
		print "quit with cancel"
		Gtk.main_quit()
		
	def show_visibility(self, widget):
		v = widget.get_property("visible")
		print "Visibility: %s" % (widget.get_property("visible"))
		if (v):
			widget.set_property("visible", False)
			#self.delete()
			#self.displayOperand("Visibility: %s" % ("OFF"))
		else:
			widget.set_property("visible", True)
			#self.delete()
			#self.displayOperand("Visibility: %s" % ("ON"))
			
	def visibility_notify(self, widget, event):
		#print "visibility_notify: %s" % (event)
		obj = self.wTree.get_object("CalcKbd")
		v = obj.get_property("visible")
		if (v):
			self.delete()
			self.displayOperand("Visibility: %s" % ("ON"))
		else:
			self.delete()
			self.displayOperand("Visibility: %s" % ("OFF"))
		print "Visibility Notification: %s" % (obj.get_property("visible"))

if __name__ == "__main__":	
	cal = Calculator()
	Gtk.main()
	
	

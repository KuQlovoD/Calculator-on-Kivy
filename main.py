from kivy.app import App

from kivy.uix.button import Button			#import buttton from kivy
from kivy.uix.boxlayout import BoxLayout	#import BL for vertical division
from kivy.uix.gridlayout import GridLayout	#import GL for positioning buttons
from kivy.uix.label import Label 			#import Label for input, result and calc
from functions import *						#import functions 

from kivy.config import Config				#import Config for design
Config.set('graphics', 'resizable', 0)		#don't changes size
Config.set('graphics', 'width', 400)		#set width for window
Config.set('graphics', 'height', 500)		#set height for window




class CalculatorApp(App):


	#add in label number that pressed
	def add_number(self, instance):
		add_number_func(self, instance)
	

	#clear label from numbers
	def clear_label(self, instance):
		clear_label_func(self)


	#setting basic operation
	def add_operation(self, instance):
		add_operation_func(self, instance)


	#one division on number that input
	def get_result_div_one(self, instance):
		get_result_div_one_func(self)


	#square of number that input
	def get_result_sqr(self, instance):
		get_result_sqr(self)


	#radical of number that input
	def get_result_sqrt(self, instance):
		get_result_sqrt(self)


	#inversion of number that input
	def get_result_inversion(self, inversion):
		get_result_inversion(self)


	#getting result from expression
	def get_result(self, instance):
		get_result_func(self)



	#build basic app
	def build(self):

		self.formula = "0"					#
		self.valide_second_number = False	#validation on input second number
		self.is_sub_operation = False		#validation on pressing additional operation

		bl = BoxLayout(orientation = "vertical", padding=2)		#create BL
		gl = GridLayout(cols=4, size_hint=(1, .8), spacing=1)	#create GL


		#create label for  result and calc
		self.lbl_calc = Label(text="", size_hint=(1, .05), font_size=16, text_size=(400 - 4, 500 * .05 - 4), halign='right', valign='center')
		self.lbl_result = Label(text="0", size_hint=(1, .15), font_size=40, text_size=(400 - 4, 500 * .15 - 4), halign='right', valign='center')
		bl.add_widget( self.lbl_calc )		#add calc label
		bl.add_widget( self.lbl_result )	#add result label


		bc1 = [.19, .19, .19, .8]			#color #303030 for button
		bc2 = [.7, .7, .7, .8]				#color #121212 for button

		#add buttons on GL
		gl.add_widget( 
			Button( text="%", 				#create button and "text" is value that display in button
			background_color = bc2, 		#set button's background color
			on_press = self.add_operation ) #set function that run when button pressed
			)
		gl.add_widget( Button(text="CE",	background_color = bc2, on_press = self.clear_label) )
		gl.add_widget( Button(text="C", 	background_color = bc2, on_press = self.clear_label) )
		gl.add_widget( Button(text="Clear", background_color = bc2, on_press = self.clear_label) )

		gl.add_widget( Button(text="1/x", 	background_color = bc2, on_press = self.get_result_div_one) )
		gl.add_widget( Button(text="x*x", 	background_color = bc2, on_press = self.get_result_sqr) )
		gl.add_widget( Button(text="?", 	background_color = bc2, on_press = self.get_result_sqrt) )
		gl.add_widget( Button(text="/", 	background_color = bc2, on_press = self.add_operation) )

		gl.add_widget( Button(text="7", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="8", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="9", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="x", 	background_color = bc2, on_press = self.add_operation) )

		gl.add_widget( Button(text="4", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="5", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="6", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="-", 	background_color = bc2, on_press = self.add_operation) )

		gl.add_widget( Button(text="1", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="2", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="3", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="+", 	background_color = bc2, on_press = self.add_operation) )

		gl.add_widget( Button(text="+/-", 	background_color = bc1, on_press = self.get_result_inversion))
		gl.add_widget( Button(text="0", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text=".", 	background_color = bc1, on_press = self.add_number) )
		gl.add_widget( Button(text="=", 	background_color = bc2, on_press = self.get_result) )

		bl.add_widget( gl )	#add GL on BL

		return bl 			#return BL

		
		
#running app
if __name__=="__main__":
	CalculatorApp().run()

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)




class CalculatorApp(App):
	#change label value
	def update_label_result(self):
		self.lbl_result.text = self.formula

	def update_label_calc(self):
		self.lbl_calc.text += self.formula

	#add in label number that pressed
	def add_number(self, instance):
		if self.formula == "0":
			self.formula = ""
		self.formula += str(instance.text)
		self.update_label_result()
	

	#clear label from numbers
	def clear_label(self, instance):
		self.formula = "0"
		self.update_label_result()
		self.lbl_calc.text = ""


	#setting basic operation
	def add_operation(self, instance):

		if self.lbl_calc.text != "":
			self.get_result(self)
			self.lbl_calc.text = ""
		if str(instance.text) == "x":
			self.formula += "*"
		else:
			self.formula += str(instance.text)
		self.update_label_calc()
		self.formula = "0"


	def get_result_div_one(self, instance):
		pass

	def get_result_sqr(self, instance):
		pass

	def get_result_sqrt(self, instance):
		pass

	def get_result_inversion(self):
		pass

	def get_result(self, instance):
		self.update_label_calc()
		self.lbl_result.text = str(eval(self.lbl_calc.text))
		self.formula = "="
		self.update_label_calc()
		self.formula = self.lbl_result.text
		


	def build(self):
		self.formula = "0"
		bl = BoxLayout(orientation = "vertical", padding=2)
		gl = GridLayout(cols=4, size_hint=(1, .8), spacing=1)

		self.lbl_calc = Label(text="", size_hint=(1, .05), font_size=16, text_size=(400 - 4, 500 * .05 - 4), halign='right', valign='center')
		self.lbl_result = Label(text="0", size_hint=(1, .15), font_size=50, text_size=(400 - 4, 500 * .15 - 4), halign='right', valign='center')
		bl.add_widget( self.lbl_calc )
		bl.add_widget( self.lbl_result )


		bc1 = [.19, .19, .19, .8]
		bc2 = [.7, .7, .7, .8]

		gl.add_widget( Button(text="%", 	background_color = bc2, on_press = self.add_operation) )
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

		bl.add_widget( gl )

		return bl

		
		

if __name__=="__main__":
	CalculatorApp().run()

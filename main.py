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
	
	def build(self):

		bl = BoxLayout(orientation = "vertical", padding=2)
		gl = GridLayout(cols=4, size_hint=(1, .8), spacing=1)

		self.lbl = Label(text="0", size_hint=(1, .2), font_size=40, text_size=(400 - 4, 500 * 0.2 - 4), halign='right', valign='center')
		bl.add_widget( self.lbl )

		bc1 = [.19, .19, .19, 1]
		bc2 = [.7, .7, .7, 1]

		gl.add_widget( Button(text="%", 	background_color=bc1),  )
		gl.add_widget( Button(text="CE",	background_color=bc1) )
		gl.add_widget( Button(text="C", 	background_color=bc1) )
		gl.add_widget( Button(text="Clear", background_color=bc1) )

		gl.add_widget( Button(text="1/x", 	background_color=bc1) )
		gl.add_widget( Button(text="x*x", 	background_color=bc1) )
		gl.add_widget( Button(text="?", 	background_color=bc1) )
		gl.add_widget( Button(text="/", 	background_color=bc1) )

		gl.add_widget( Button(text="7", 	background_color=bc2) )
		gl.add_widget( Button(text="8", 	background_color=bc2) )
		gl.add_widget( Button(text="9", 	background_color=bc2) )
		gl.add_widget( Button(text="X", 	background_color=bc1) )

		gl.add_widget( Button(text="4", 	background_color=bc2) )
		gl.add_widget( Button(text="5", 	background_color=bc2) )
		gl.add_widget( Button(text="6", 	background_color=bc2) )
		gl.add_widget( Button(text="-", 	background_color=bc1) )

		gl.add_widget( Button(text="1", 	background_color=bc2) )
		gl.add_widget( Button(text="2", 	background_color=bc2) )
		gl.add_widget( Button(text="3", 	background_color=bc2) )
		gl.add_widget( Button(text="+", 	background_color=bc1) )

		gl.add_widget( Button(text="+/-", 	background_color=bc2) )
		gl.add_widget( Button(text="0", 	background_color=bc2) )
		gl.add_widget( Button(text=".", 	background_color=bc2) )
		gl.add_widget( Button(text="=", 	background_color=bc1) )

		bl.add_widget( gl )

		return bl

		
		

if __name__=="__main__":
	CalculatorApp().run()

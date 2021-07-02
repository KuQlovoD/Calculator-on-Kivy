from math import *	#import math module's methods


#updating result's label
def update_label_result(self):
	self.lbl_result.text = self.formula


#updating expession label
def update_label_calc(self):
	self.lbl_calc.text += self.formula


#add number on expession
def add_number_func(self, instance):
	length = len(self.lbl_calc.text)

	if valide_end_expression(self):
		clear_label_func(self)

	if (self.formula == "0" and str(instance.text) != ".") or (self.lbl_calc.text != "" and not self.valide_second_number):
		self.formula = ""
		if self.lbl_calc.text != "" :
			self.valide_second_number = True

	self.formula += str(instance.text)
	update_label_result(self)


#clearing labels
def clear_label_func(self):
	self.formula = "0"
	update_label_result(self)
	self.lbl_calc.text = ""
	self.valide_second_number = False


#add operation on expession
def add_operation_func(self, instance):
	
	length = len(self.lbl_calc.text)		#get expression length for to find operation

	
	if self.lbl_calc.text != "":

		if self.lbl_calc.text[length-1] == "=":			#happening when previous expession calculated
			self.lbl_calc.text = self.lbl_result.text 	#save result previous expession
			self.formula = ""							#release inputing number
		else: 
			get_result_func(self)						#getting result
			self.lbl_calc.text = self.lbl_result.text 	#save result previous expession
			self.valide_second_number = False			#validation on input second number


	else:									#happening when expession don't input
		update_label_calc(self)				#updating expession
	
	
	if str(instance.text) == "x":					#happening when pressing "x"
		self.lbl_calc.text += "*"					#change "x" in "*" and add it expession 
	else:
		self.lbl_calc.text += str(instance.text)	#add operation in expession (happening when pressong not "x")



def get_result_func(self):

	label_text = self.lbl_calc.text #save expression data
	length = len(label_text)		#get expression length for to find operation

	#multiply press on "="
	if valide_end_expression(self) :

		self.lbl_calc.text = self.lbl_result.text 	#change expression on result
		index = 0  									#operation's index
		valide_abs_one = False						#less than one per module

		#find operation's index
		for i in range(length):
			try:
				#condition for numbers that less then one
				if label_text[i] != "." and label_text[i] != "e" and ( label_text[i] != "-" or not valide_abs_one ) :
					number = int(label_text[i])
				else:
					valide_abs_one = True
			except:
				index = i
				break

		self.lbl_calc.text += label_text[index:length-1]	#repeat operation and initial value

	elif not self.is_sub_operation:
		update_label_calc(self)	#first pressing on "="
	else:
		self.is_sub_operation = False

	if self.lbl_calc.text == "sqrt(" + self.lbl_result.text + ")":
		self.lbl_result.text = str(sqrt(float(self.lbl_result.text)))
	else:
		self.lbl_result.text = str(eval(self.lbl_calc.text))

	self.lbl_calc.text += "="




def valide_end_expression(self):
	label_text = self.lbl_calc.text #save expression data
	length = len(label_text)		#get expression length for to find operation

	#multiply press on "="
	if label_text != "" and label_text[length-1] == "=":
		return True



def get_result_div_one_func(self):
	length = len(self.lbl_calc.text)

	if self.lbl_calc.text != "":

		if self.lbl_calc.text[length-1] == "=":
			self.lbl_calc.text = "1/("
			self.lbl_calc.text += self.lbl_result.text
			self.lbl_calc.text += ")"
			self.formula = ""
		else: 
			get_result_func(self)
			self.lbl_calc.text = "1/("
			self.lbl_calc.text += self.lbl_result.text
			self.lbl_calc.text += ")"
			self.valide_second_number = False

	else:
		self.lbl_calc.text = "1/(" + self.formula + ")"



	self.is_sub_operation = True
	get_result_func(self)


def get_result_sqr(self):
	length = len(self.lbl_calc.text)

	if self.lbl_calc.text != "":

		if self.lbl_calc.text[length-1] == "=":
			self.lbl_calc.text = self.lbl_result.text
			self.lbl_calc.text += "*"
			self.lbl_calc.text += self.lbl_result.text
			self.formula = ""
		else: 
			get_result_func(self)
			self.lbl_calc.text = self.lbl_result.text
			self.lbl_calc.text += "*"
			self.lbl_calc.text += self.lbl_result.text
			self.valide_second_number = False

	else:
		self.lbl_calc.text = self.formula + "*" + self.formula

	self.is_sub_operation = True
	get_result_func(self)



def get_result_sqrt(self):
	length = len(self.lbl_calc.text)

	if self.lbl_calc.text != "":

		if self.lbl_calc.text[length-1] == "=":
			self.lbl_calc.text = "sqrt("
			self.lbl_calc.text += self.lbl_result.text
			self.lbl_calc.text += ")"
			self.formula = ""
		else: 
			get_result_func(self)
			self.lbl_calc.text = "sqrt("
			self.lbl_calc.text += self.lbl_result.text
			self.lbl_calc.text += ")"
			self.valide_second_number = False

	else:
		self.lbl_calc.text = "sqrt(" + self.formula + ")"

	self.is_sub_operation = True
	get_result_func(self)



def get_result_inversion(self):
	self.formula = self.lbl_result.text
	self.formula = str(-int(self.formula))
	update_label_result(self)

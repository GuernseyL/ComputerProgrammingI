﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Tomato
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(87, 25)
		self._label1.TabIndex = 0
		self._label1.Text = "Factorial:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Tomato
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(13, 47)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(87, 25)
		self._label2.TabIndex = 1
		self._label2.Text = "Product:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Tomato
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label3.Location = System.Drawing.Point(106, 47)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(216, 25)
		self._label3.TabIndex = 2
		self._label3.Click += self.Label3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCoral
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(106, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(216, 29)
		self._textBox1.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RosyBrown
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(12, 76)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 46)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.RosyBrown
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(118, 76)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 46)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RosyBrown
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(223, 76)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 46)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.IndianRed
		self.ClientSize = System.Drawing.Size(335, 136)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Factorial"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Factorial = int(self._textBox1.Text)
		Product = 1
		for i in range(1, Factorial+1):
			Product = Product * i
			self._label3.Text = str(Product)

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._label3.Text = " "
		
	def Button3Click(self, sender, e):
		Application.Exit()
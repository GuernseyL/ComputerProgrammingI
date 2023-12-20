﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(225, 230)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 94)
		self._button3.TabIndex = 19
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gold
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(119, 230)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 94)
		self._button2.TabIndex = 18
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Goldenrod
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label4.Location = System.Drawing.Point(13, 186)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(312, 41)
		self._label4.TabIndex = 17
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Goldenrod
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox3.Location = System.Drawing.Point(169, 126)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(150, 29)
		self._textBox3.TabIndex = 16
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Goldenrod
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox2.Location = System.Drawing.Point(169, 76)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(150, 29)
		self._textBox2.TabIndex = 15
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Goldenrod
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(169, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(150, 29)
		self._textBox1.TabIndex = 14
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gold
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(13, 230)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 94)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Goldenrod
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label3.Location = System.Drawing.Point(13, 126)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 40)
		self._label3.TabIndex = 12
		self._label3.Text = "Pence"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Goldenrod
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(13, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(150, 41)
		self._label2.TabIndex = 11
		self._label2.Text = "Shillings"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Goldenrod
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(13, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(150, 44)
		self._label1.TabIndex = 10
		self._label1.Text = "Pounds"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(336, 341)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog65h.2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pounds = float(self._textBox1.Text)
		shillings = float(self._textBox2.Text)
		pence = float(self._textBox3.Text)
		mpound = shillings/20.0 + pence/240.0 + pounds/1.0
		self._label4.Text = str(mpound)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Gold
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._textBox1.Location = System.Drawing.Point(175, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(150, 26)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Gold
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._textBox2.Location = System.Drawing.Point(175, 44)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(150, 26)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Gold
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._textBox3.Location = System.Drawing.Point(175, 76)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(150, 26)
		self._textBox3.TabIndex = 2
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label1.Location = System.Drawing.Point(12, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(149, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Pounds"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label2.Location = System.Drawing.Point(13, 44)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(149, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Shillings"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label3.Location = System.Drawing.Point(12, 76)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(149, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Pence"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label4.Location = System.Drawing.Point(13, 105)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(312, 26)
		self._label4.TabIndex = 6
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gold
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._button1.Location = System.Drawing.Point(12, 136)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 67)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gold
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._button2.Location = System.Drawing.Point(120, 134)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 68)
		self._button2.TabIndex = 8
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._button3.Location = System.Drawing.Point(227, 135)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 68)
		self._button3.TabIndex = 9
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Goldenrod
		self.ClientSize = System.Drawing.Size(337, 214)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pounds = int(self._textBox1.Text)
		shillings = int(self._textBox2.Text)
		pence = int(self._textBox3.Text)
		spound = shillings/20.0
		ppound = pence/12.0)
		mpound = spound + ppound + pounds
		self._label4.Text = str(mpound)
		
	def MainFormLoad(self, sender, e):
		pass

	def TextBox3TextChanged(self, sender, e):
		pass
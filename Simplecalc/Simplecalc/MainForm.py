import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(13, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(205, 29)
		self._textBox1.TabIndex = 0
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.ForestGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(12, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(205, 38)
		self._label1.TabIndex = 1
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.ForestGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(12, 138)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(205, 46)
		self._label2.TabIndex = 2
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._label2.Click += self.Label2Click
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkOliveGreen
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox2.Location = System.Drawing.Point(12, 94)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(205, 29)
		self._textBox2.TabIndex = 3
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(236, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(66, 63)
		self._button1.TabIndex = 4
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(308, 13)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(66, 63)
		self._button2.TabIndex = 5
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(380, 13)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(66, 63)
		self._button3.TabIndex = 6
		self._button3.Text = "*"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.SeaGreen
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(236, 82)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(66, 63)
		self._button4.TabIndex = 7
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.SeaGreen
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(308, 82)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(66, 63)
		self._button5.TabIndex = 8
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.SeaGreen
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(380, 82)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(66, 63)
		self._button6.TabIndex = 9
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.SeaGreen
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(236, 151)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(66, 63)
		self._button7.TabIndex = 10
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.SeaGreen
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(308, 151)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(66, 63)
		self._button8.TabIndex = 11
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.SeaGreen
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(380, 151)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(66, 63)
		self._button9.TabIndex = 12
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(463, 231)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Simplecalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		self._label1.Text = "+"
		self._label2.Text = str(Sum)

	def Label2Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sub = num1 - num2
		self._label1.Text = "-"
		self._label2.Text = str(Sub)

	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Product = num1 * num2
		self._label1.Text = "*"
		self._label2.Text = str(Product)

	def Button4Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Power = num1 ** num2
		self._label1.Text = "^"
		self._label2.Text = str(Power)

	def Button5Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		Quotient = num1 / num2
		self._label1.Text = "/"
		self._label2.Text = str(round(Quotient, 2))

	def Button6Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		QuotientNoR = num1 // num2
		self._label1.Text = "//"
		self._label2.Text = str(round(QuotientNoR, 2))

	def Button7Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		Remainder = num1 % num2
		self._label1.Text = "MOD"
		self._label2.Text = str(round(Remainder, 2))

	def Button8Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label1.Text = " "
		self._label2.Text = " "

	def Button9Click(self, sender, e):
		Application.Exit()
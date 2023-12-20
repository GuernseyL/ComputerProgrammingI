import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Location = System.Drawing.Point(441, 337)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(238, 23)
		self._label6.TabIndex = 53
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label7.Location = System.Drawing.Point(441, 291)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(238, 22)
		self._label7.TabIndex = 52
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label8.Location = System.Drawing.Point(441, 246)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(238, 23)
		self._label8.TabIndex = 51
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label12.Location = System.Drawing.Point(441, 204)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(238, 23)
		self._label12.TabIndex = 50
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label11.Location = System.Drawing.Point(441, 164)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(238, 23)
		self._label11.TabIndex = 49
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label10.Location = System.Drawing.Point(441, 117)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(238, 23)
		self._label10.TabIndex = 48
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label9.Location = System.Drawing.Point(441, 73)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(238, 23)
		self._label9.TabIndex = 47
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(184, 73)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(238, 23)
		self._label13.TabIndex = 46
		self._label13.Text = "Sum:"
		self._label13.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(184, 117)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(238, 23)
		self._label14.TabIndex = 45
		self._label14.Text = "Differance:"
		self._label14.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(184, 164)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(238, 23)
		self._label15.TabIndex = 44
		self._label15.Text = "Product:"
		self._label15.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(184, 204)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(238, 23)
		self._label16.TabIndex = 43
		self._label16.Text = "Average:"
		self._label16.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(184, 246)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(238, 23)
		self._label4.TabIndex = 42
		self._label4.Text = "Abs. Difference:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(184, 290)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(238, 23)
		self._label3.TabIndex = 41
		self._label3.Text = "Max:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(184, 337)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(238, 23)
		self._label1.TabIndex = 40
		self._label1.Text = "Min:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(441, 37)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(238, 20)
		self._textBox2.TabIndex = 39
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(184, 37)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(238, 20)
		self._textBox1.TabIndex = 38
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(518, 375)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(161, 23)
		self._button3.TabIndex = 37
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(351, 375)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(161, 23)
		self._button2.TabIndex = 36
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(184, 375)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(161, 23)
		self._button1.TabIndex = 35
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.AppWorkspace
		self.ClientSize = System.Drawing.Size(863, 435)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Calculator 2.0"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		Product = num1 * num2
		Average = (num1 + num2)/2.0
		AbsDiff = abs(Diff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		
		if Max == num1:
			Min = num2
		else:
			Min = num1
				
		self._label9.Text = str(Sum)
		self._label10.Text = str(Diff)
		self._label11.Text = str(Product)
		self._label12.Text = str(Average)
		self._label8.Text = str(AbsDiff)
		self._label7.Text = str(Max)
		self._label6.Text = str(Min)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
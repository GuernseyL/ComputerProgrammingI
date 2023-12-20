import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gold
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Yellow
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(149, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(132, 29)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Yellow
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox2.Location = System.Drawing.Point(174, 45)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(132, 29)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Gold
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(13, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(155, 32)
		self._label2.TabIndex = 2
		self._label2.Text = "# of Pay Periods"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gold
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label3.Location = System.Drawing.Point(13, 87)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(216, 32)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary per Pay Periods"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cornsilk
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(13, 123)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 52)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cornsilk
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(119, 123)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 52)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cornsilk
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(225, 122)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 52)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Goldenrod
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label4.Location = System.Drawing.Point(235, 87)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(181, 32)
		self._label4.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Khaki
		self.ClientSize = System.Drawing.Size(428, 190)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Salary"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		AnnualPay = float(self._textBox1.Text)
		PayPeriods = float(self._textBox2.Text)
		SalaryPeriod = AnnualPay / PayPeriods
		self._label4.Text = str(round(SalaryPeriod, 2))

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label4.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()
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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Khaki
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(12, 21)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Class A Sold:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(156, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(180, 29)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox2.Location = System.Drawing.Point(156, 53)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(180, 29)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Khaki
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Class B Sold:"
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkGoldenrod
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox3.Location = System.Drawing.Point(156, 88)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(180, 29)
		self._textBox3.TabIndex = 5
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Khaki
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label3.Location = System.Drawing.Point(12, 94)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Class C Sold:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Khaki
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label4.Location = System.Drawing.Point(344, 21)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(121, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Class A Cost:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Khaki
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label5.Location = System.Drawing.Point(344, 56)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(121, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Class B Cost:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Khaki
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label6.Location = System.Drawing.Point(344, 94)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(121, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Class C Cost:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Goldenrod
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label7.Location = System.Drawing.Point(471, 94)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(184, 23)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Goldenrod
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label8.Location = System.Drawing.Point(471, 56)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(184, 23)
		self._label8.TabIndex = 10
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Goldenrod
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label9.Location = System.Drawing.Point(471, 21)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(184, 23)
		self._label9.TabIndex = 9
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Goldenrod
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label10.Location = System.Drawing.Point(471, 130)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(184, 23)
		self._label10.TabIndex = 12
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Khaki
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label11.Location = System.Drawing.Point(344, 130)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(121, 23)
		self._label11.TabIndex = 13
		self._label11.Text = "Total Cost:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGoldenrodYellow
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(12, 130)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 34)
		self._button1.TabIndex = 14
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGoldenrodYellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(122, 130)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 34)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGoldenrodYellow
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(232, 130)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 34)
		self._button3.TabIndex = 16
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGoldenrod
		self.ClientSize = System.Drawing.Size(674, 175)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Stadium"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		SoldA = float(self._textBox1.Text)
		SoldB = float(self._textBox2.Text)
		SoldC = float(self._textBox3.Text)
		CostA = SoldA*15.0
		CostB = SoldB*12.0
		CostC = SoldC*9.0
		CostTotal = CostA + CostB + CostC
		self._label9.Text = "$" + str(round(CostA, 2))
		self._label8.Text = "$" + str(round(CostB, 2))
		self._label7.Text = "$" + str(round(CostC, 2))
		self._label10.Text = "$" + str(round(CostTotal, 2))
		

	def Button2Click(self, sender, e):
		self._textBox1.Text =  " "
		self._textBox2.Text =  " "
		self._textBox3.Text =  " "
		self._label7.Text =  " "
		self._label8.Text =  " "
		self._label9.Text =  " "
		self._label10.Text =  " "

	def Button3Click(self, sender, e):
		Application.Exit()
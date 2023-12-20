import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RoyalBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(12, 161)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(124, 48)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DodgerBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(155, 29)
		self._label1.TabIndex = 2
		self._label1.Text = "Sales this month:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DodgerBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.Location = System.Drawing.Point(12, 100)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(124, 29)
		self._label2.TabIndex = 3
		self._label2.Text = "Commission:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DodgerBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label3.Location = System.Drawing.Point(12, 42)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(234, 29)
		self._label3.TabIndex = 4
		self._label3.Text = "Advanced Pay Rewarded:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DodgerBlue
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label4.Location = System.Drawing.Point(12, 71)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(167, 29)
		self._label4.TabIndex = 5
		self._label4.Text = "Commission Rate:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DodgerBlue
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label5.Location = System.Drawing.Point(12, 129)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(83, 29)
		self._label5.TabIndex = 6
		self._label5.Text = "Net Pay:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.RoyalBlue
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label6.Location = System.Drawing.Point(101, 129)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(155, 29)
		self._label6.TabIndex = 8
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.RoyalBlue
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label7.Location = System.Drawing.Point(142, 100)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(155, 29)
		self._label7.TabIndex = 7
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.RoyalBlue
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label8.Location = System.Drawing.Point(185, 71)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(155, 29)
		self._label8.TabIndex = 9
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.RoyalBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(173, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(155, 29)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.RoyalBlue
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox2.Location = System.Drawing.Point(252, 42)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(155, 29)
		self._textBox2.TabIndex = 11
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.RoyalBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(142, 161)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(124, 48)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RoyalBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(272, 161)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(124, 48)
		self._button3.TabIndex = 13
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(421, 415)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "CompSal"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		sales = int(self._textBox1.Text)
		Advanced = int(self._textBox2.Text)
		if sales > 0 and sales < 10000:
			Rate = "5%"
		elif sales >= 10000 and sales < 15000:
			Rate = "10%"
		elif sales >= 15000 and sales < 18000:
			Rate = "12%"
		elif sales >= 18000 and sales < 22000:
			Rate = "14%"
		elif sales > 22000:
			Rate = "16%"
			self._label6.Text = "Invalid Sales"
		self._label6.Text = Rate
import System.Drawing
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.IndianRed
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 76)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(124, 30)
		self._label1.TabIndex = 0
		self._label1.Text = "Runner #1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.IndianRed
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 111)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(124, 30)
		self._label2.TabIndex = 1
		self._label2.Text = "Runner #2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.IndianRed
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 147)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(124, 30)
		self._label3.TabIndex = 2
		self._label3.Text = "Runner #3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Orange
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(177, 36)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(124, 30)
		self._label4.TabIndex = 3
		self._label4.Text = "Names"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(361, 36)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(124, 30)
		self._label5.TabIndex = 4
		self._label5.Text = "Time"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Peru
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(132, 311)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(140, 30)
		self._label6.TabIndex = 7
		self._label6.Text = "Third Place"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Silver
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(132, 270)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(140, 30)
		self._label7.TabIndex = 6
		self._label7.Text = "Second Place"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Goldenrod
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(132, 228)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(140, 30)
		self._label8.TabIndex = 5
		self._label8.Text = "First Place"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Peru
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(291, 311)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(124, 30)
		self._label9.TabIndex = 10
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Silver
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(291, 270)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(124, 30)
		self._label10.TabIndex = 9
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Goldenrod
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(291, 228)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(124, 30)
		self._label11.TabIndex = 8
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SpringGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(81, 372)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(126, 56)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SpringGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(213, 372)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(126, 56)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SpringGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(345, 372)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(126, 56)
		self._button3.TabIndex = 14
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.OrangeRed
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(142, 73)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(159, 29)
		self._textBox1.TabIndex = 15
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.OrangeRed
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(142, 112)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(159, 29)
		self._textBox2.TabIndex = 16
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.OrangeRed
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(142, 148)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(159, 29)
		self._textBox3.TabIndex = 17
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.PaleTurquoise
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(345, 148)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(159, 29)
		self._textBox4.TabIndex = 20
		# 
		# textBox5
		# 
		self._textBox5.BackColor = System.Drawing.Color.PaleTurquoise
		self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(345, 112)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(159, 29)
		self._textBox5.TabIndex = 19
		# 
		# textBox6
		# 
		self._textBox6.BackColor = System.Drawing.Color.PaleTurquoise
		self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(345, 73)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(159, 29)
		self._textBox6.TabIndex = 18
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(566, 454)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Race"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		ROne = str(self._textBox1.Text)
		RTwo = str(self._textBox2.Text)
		RThree = str(self._textBox3.Text)
		TOne = float(self._textBox6.Text)
		TTwo = float(self._textBox5.Text)
		TThree = float(self._textBox4.Text)
		if TOne <= TTwo and TTwo <= TThree:
			self._label11.Text = ROne
			self._label10.Text = RTwo
			self._label9.Text = RThree
		elif TOne <= TTwo and TThree < TTwo and TOne < TThree:
			self._label11.Text = ROne
			self._label10.Text = RThree
			self._label9.Text = RTwo
		elif TTwo < TOne and TOne <= TThree:
			self._label11.Text = RTwo
			self._label10.Text = ROne
			self._label9.Text = RThree
		elif TTwo < TOne and TThree < TOne and TTwo < TThree:
			self._label11.Text = RTwo
			self._label10.Text = RThree
			self._label9.Text = ROne
		elif TThree < TTwo and TTwo <= TOne:
			self._label11.Text = RThree
			self._label10.Text = RTwo
			self._label9.Text = ROne
		elif TThree < TTwo and TOne < TWo and TOne < Three:
			self._label11.Text = RThree
			self._label10.Text = ROne
			self._label9.Text = RTwo

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._textBox3.Text = " "
		self._textBox4.Text = " "
		self._textBox5.Text = " "
		self._textBox6.Text = " "
		self._label11.Text = " "
		self._label10.Text = " "
		self._label9.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()
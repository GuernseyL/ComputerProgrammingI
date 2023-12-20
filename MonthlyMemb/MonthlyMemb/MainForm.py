import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._chkYoga = System.Windows.Forms.CheckBox()
		self._chkKarate = System.Windows.Forms.CheckBox()
		self._chkPT = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.LightSalmon
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(27, 66)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(212, 33)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Child (12 and Under)"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.LightSalmon
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(26, 96)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(187, 33)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Student"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.LightSalmon
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(26, 126)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(187, 33)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Standard Adult"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.Color.LightSalmon
		self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.Location = System.Drawing.Point(27, 156)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(187, 33)
		self._radioButton4.TabIndex = 2
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senoir Citizen"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Goldenrod
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(26, 303)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(183, 29)
		self._textBox1.TabIndex = 4
		# 
		# chkYoga
		# 
		self._chkYoga.BackColor = System.Drawing.Color.Coral
		self._chkYoga.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkYoga.Location = System.Drawing.Point(296, 96)
		self._chkYoga.Name = "chkYoga"
		self._chkYoga.Size = System.Drawing.Size(187, 33)
		self._chkYoga.TabIndex = 5
		self._chkYoga.Text = "Yoga"
		self._chkYoga.UseVisualStyleBackColor = False
		# 
		# chkKarate
		# 
		self._chkKarate.BackColor = System.Drawing.Color.Coral
		self._chkKarate.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkKarate.Location = System.Drawing.Point(296, 126)
		self._chkKarate.Name = "chkKarate"
		self._chkKarate.Size = System.Drawing.Size(187, 33)
		self._chkKarate.TabIndex = 6
		self._chkKarate.Text = "Karate"
		self._chkKarate.UseVisualStyleBackColor = False
		# 
		# chkPT
		# 
		self._chkPT.BackColor = System.Drawing.Color.Coral
		self._chkPT.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkPT.Location = System.Drawing.Point(296, 157)
		self._chkPT.Name = "chkPT"
		self._chkPT.Size = System.Drawing.Size(187, 33)
		self._chkPT.TabIndex = 7
		self._chkPT.Text = "Personal Trainer"
		self._chkPT.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOrange
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(396, 256)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 32)
		self._label1.TabIndex = 8
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkOrange
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(396, 300)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 32)
		self._label2.TabIndex = 9
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Orange
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(267, 303)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(123, 32)
		self._label3.TabIndex = 11
		self._label3.Text = "Total Cost:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Orange
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(267, 256)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(123, 32)
		self._label4.TabIndex = 10
		self._label4.Text = "Monthly Fee:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Goldenrod
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(26, 268)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(183, 32)
		self._label5.TabIndex = 12
		self._label5.Text = "Number of Months:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Tomato
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(26, 31)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(188, 32)
		self._label6.TabIndex = 13
		self._label6.Text = "Type of Membership"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Tomato
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(287, 32)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(81, 32)
		self._label7.TabIndex = 14
		self._label7.Text = "Options"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(26, 339)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(152, 50)
		self._button1.TabIndex = 15
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(184, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(163, 50)
		self._button2.TabIndex = 16
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleGoldenrod
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(353, 339)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(152, 50)
		self._button3.TabIndex = 17
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(517, 403)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._chkPT)
		self.Controls.Add(self._chkKarate)
		self.Controls.Add(self._chkYoga)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "MonthlyMemb"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		if self._radioButton3.Checked == True:
			BF = 40
		elif self._radioButton1.Checked == True:
			BF = 20
		elif self._radioButton2.Checked == True:
			BF = 25
		elif self._radioButton4.Checked == True:
			BF = 30
		
		if self._chkYoga.Checked == True:
			BF += 10
		
		if self._chkKarate.Checked == True:
			BF += 30
		
		if self._chkPT.Checked == True:
			BF += 50
		
		if int(self._textBox1.Text) < 1:
			MessageBox.Show("You must enter atleast 1 month")
		elif int(self._textBox1.Text) >= 1 and int(self._textBox1.Text) <= 3:
			DC = 1.0
		elif int(self._textBox1.Text) >= 4 and int(self._textBox1.Text) <= 6:
			DC = 0.95
		elif int(self._textBox1.Text) >= 7 and int(self._textBox1.Text) <= 9:
			DC = 0.92
		elif int(self._textBox1.Text) >= 10 and int(self._textBox1.Text) <= 24:
			DC = 0.9
		elif int(self._textBox1.Text) > 24:
			MessageBox.Show("Your subscription must be less than 2 years")
		
		MF = BF * DC
		YF = MF * int(self._textBox1.Text)
		
		self._label1.Text = str(MF)
		self._label2.Text = str(YF)
		
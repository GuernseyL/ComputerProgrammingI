import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.SandyBrown
		self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._checkBox1.Location = System.Drawing.Point(135, 13)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Radio 1"
		self._checkBox1.UseVisualStyleBackColor = False
		self._checkBox1.CheckedChanged += self.CheckBox1CheckedChanged
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Peru
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._radioButton1.Location = System.Drawing.Point(13, 12)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(116, 24)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Channel 1"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Peru
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._radioButton2.Location = System.Drawing.Point(12, 42)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(116, 24)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Channel 2"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.SandyBrown
		self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._checkBox2.Location = System.Drawing.Point(134, 43)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 2
		self._checkBox2.Text = "Radio 2"
		self._checkBox2.UseVisualStyleBackColor = False
		self._checkBox2.CheckedChanged += self.CheckBox2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Peru
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._radioButton3.Location = System.Drawing.Point(12, 72)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(116, 24)
		self._radioButton3.TabIndex = 5
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Channel 3"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.SandyBrown
		self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._checkBox3.Location = System.Drawing.Point(134, 72)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 4
		self._checkBox3.Text = "Radio 3"
		self._checkBox3.UseVisualStyleBackColor = False
		self._checkBox3.CheckedChanged += self.CheckBox3CheckedChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Sienna
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(13, 103)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 149)
		self._label1.TabIndex = 6
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Chocolate
		self.ClientSize = System.Drawing.Size(250, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._checkBox1)
		self.Name = "MainForm"
		self.Text = "Radio"
		self.ResumeLayout(False)


	def RadioButton1CheckedChanged(self, sender, e):
		Channel = "Channel 1"
		self._label1.Text = "You have selected " + str(Channel)

	def RadioButton2CheckedChanged(self, sender, e):
		Channel = "Channel 2"
		self._label1.Text = "You have selected " + str(Channel)

	def RadioButton3CheckedChanged(self, sender, e):
		Channel = "Channel 3"
		self._label1.Text = "You have selected " + str(Channel)

	def CheckBox1CheckedChanged(self, sender, e):
		if self._checkBox1.Checked == True:
			self._label1.Text += " and Radio 1"
		else:
			self._label1.Text = " "

	def Label1Click(self, sender, e):
		pass

	def CheckBox2CheckedChanged(self, sender, e):
		if self._checkBox2.Checked == True:
			self._label1.Text += " and Radio 2"
		else:
			self._label1.Text = " "

	def CheckBox3CheckedChanged(self, sender, e):
		if self._checkBox3.Checked == True:
			self._label1.Text += " and Radio 3"
		else:
			self._label1.Text = " "
import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._button1.Location = System.Drawing.Point(13, 348)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(218, 96)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._button2.Location = System.Drawing.Point(336, 348)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(187, 95)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._button3.Location = System.Drawing.Point(606, 348)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(223, 95)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ScrollBar
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(816, 323)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.AppWorkspace
		self.ClientSize = System.Drawing.Size(842, 456)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122a.2"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number\t\tSquare\t\tSquare Root"
		self._listBox1.Items.Add(header)
		for num in range(1, 50+1):
			numnsqrd = num**2
			numnsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(numnsqrd) + "\t\t" + str(round(numnsqrt, 4))
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass
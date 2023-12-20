import System.Drawing
import System.Windows.Forms

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
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(8, 349)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(98, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkCyan
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(108, 348)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(98, 91)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkCyan
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(211, 348)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(98, 91)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.PaleTurquoise
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(296, 316)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSlateGray
		self.ClientSize = System.Drawing.Size(322, 451)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "X\t\tY"
		self._listBox1.Items.Add(heading)
		for X in range(-12, 17):
			Line = str(X) + "\t\t" + str(float(X**6 - 3*X**5 - 93*X**4 + 87*X**3 + 1596*X**2 - 1380*X - 2800))
			self._listBox1.Items.Add(Line)

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self.ListBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Coral
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(13, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(929, 292)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(13, 321)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(308, 88)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(327, 321)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(306, 88)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(636, 321)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(306, 88)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkSalmon
		self.ClientSize = System.Drawing.Size(954, 421)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122h"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Base\t\tSquare\t\tSquare Root\tCube\t\t4th Root"
		self._listBox1.Items.Add(heading)
		for base in range(1, 21):
			basesr = base**0.5
			basefr = base**0.25
			line = str(base) + "\t\t" + str(int(base**2)) + "\t\t" + str(round(basesr, 4)) + "\t\t" + str(int(base**3)) + "\t\t" + str(round(basefr, 4))
			self._listBox1.Items.Add(line)

	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
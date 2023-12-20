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
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ButtonFace
		self._listBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(13, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(848, 352)
		self._listBox1.TabIndex = 0
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(422, 374)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(8, 8)
		self._button1.TabIndex = 2
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(13, 374)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(154, 44)
		self._button2.TabIndex = 3
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(708, 370)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(152, 48)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(342, 370)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(142, 48)
		self._button4.TabIndex = 5
		self._button4.Text = "Clear"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlDark
		self.ClientSize = System.Drawing.Size(872, 430)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self.Name = "MainForm"
		self.Text = "Prog1221"
		self.ResumeLayout(False)


	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def CheckBox2CheckedChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		heading = "Number\t\tSquare\t\tSquare Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 50+1):
			nsqrd = num**2
			nsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(nsqrd) + "\t\t" + str(round(nsqrt, 4))
			self.ListBox1.Items.Add(msg)

	def Button4Click(self, sender, e):
		self.listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		application.exit()
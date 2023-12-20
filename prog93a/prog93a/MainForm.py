import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(143, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "Kilowatts Used:"
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(13, 43)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(353, 196)
		self._listBox1.TabIndex = 1
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Cornsilk
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._textBox1.Location = System.Drawing.Point(162, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(204, 29)
		self._textBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Goldenrod
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button1.Location = System.Drawing.Point(12, 245)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 79)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button2.Location = System.Drawing.Point(132, 245)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 79)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Goldenrod
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._button3.Location = System.Drawing.Point(252, 245)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(114, 79)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gold
		self.ClientSize = System.Drawing.Size(381, 340)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Kilowatts = float(self._textBox1.Text)
		Base = Kilowatts*0.0475
		Surcharge = Base*0.10
		Citytax = Base*0.03
		Due = Base + Citytax + Surcharge
		Late = Due*1.04
		ListK = "Kilowatts Used\t\t" + str(Kilowatts)
		Divider = "---------------------------------------------------"
		ListB = "Base\t\t\t" +  str(round(Base, 2))
		ListS = "Surcharge\t\t" + str(round(Surcharge, 2))
		ListC = "Citytax\t\t\t" + str(round(Citytax, 2))
		Dividerbeta = "\t\t\t_____"
		ListP = "Amount due\t\t" + str(round(Due, 2))
		ListL = "Amount after May 20th\t" + str(round(Late, 2))
		self._listBox1.Items.Add(ListK)
		self._listBox1.Items.Add(Divider)
		self._listBox1.Items.Add(ListB)
		self._listBox1.Items.Add(ListS)
		self._listBox1.Items.Add(ListC)
		self._listBox1.Items.Add(Dividerbeta)
		self._listBox1.Items.Add(ListP)
		self._listBox1.Items.Add(ListL)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()
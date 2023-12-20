import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(27, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(114, 21)
		self._label1.TabIndex = 0
		self._label1.Text = "Pick a car:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(24, 253)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 60)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(147, 253)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 60)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(270, 253)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 60)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label2.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(30, 190)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(114, 33)
		self._label2.TabIndex = 4
		self._label2.Text = "MPG:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label3.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(27, 129)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(114, 33)
		self._label3.TabIndex = 5
		self._label3.Text = "Gallons:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label4.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(27, 69)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(114, 33)
		self._label4.TabIndex = 6
		self._label4.Text = "Miles:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label5.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(150, 69)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(114, 33)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label6.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(150, 129)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(114, 33)
		self._label6.TabIndex = 8
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._label7.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(153, 190)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(114, 33)
		self._label7.TabIndex = 7
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(153, 25)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(177, 21)
		self._comboBox1.TabIndex = 10
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(832, 337)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
		if car == "1979 Firebird":
			miles = 412
			gallons = 40
		if car == "1980 Subaru":
			miles = 361
			gallons = 18
		if car == "1975 Cutlass":
			miles = 161
			gallons = 11
			
		mpg = miles / float(gallons)
		mpg = round(mpg, 10)
		
		
		self._label7.Text = str(mpg)
		self._label6.Text = str(gallons)
		self._label5.Text = str(miles)

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label6.Text = ""
		self._label5.Text = ""
		
	
	def Button3Click(self, sender, e):
		Application.Exit()
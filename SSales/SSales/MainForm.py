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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(341, 172)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Green
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(21, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(244, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Amount sold of package A"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.YellowGreen
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(278, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(129, 29)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Green
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(21, 67)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(244, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Amount sold of package B"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Green
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(21, 114)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(244, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Amount sold of package C"
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.YellowGreen
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(278, 67)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(129, 29)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.YellowGreen
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(278, 114)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(129, 29)
		self._textBox3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LimeGreen
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(21, 214)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(314, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Cost of packages A:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LimeGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(21, 246)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(314, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Cost of packages B:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LimeGreen
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(21, 279)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(314, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Cost of packages C:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LimeGreen
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(21, 315)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(314, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "Total cost:"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(341, 234)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 56)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(341, 296)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(122, 56)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGreen
		self.ClientSize = System.Drawing.Size(477, 374)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "SSales"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		SOne = int(self._textBox1.Text)
		STwo = int(self._textBox2.Text)
		SThree = int(self._textBox3.Text)
		if SOne >= 10 and SOne <= 19:
			DOne = .80
		elif SOne >= 20 and SOne <= 49:
			DOne = .70
		elif SOne >= 50 and SOne <= 99:
			DOne = .60
		elif SOne >= 100:
			DOne = .50
			
		if STwo >= 10 and STwo <= 19:
			DTwo = .80
		elif STwo >= 20 and STwo <= 49:
			DTwo = .70
		elif STwo >= 50 and STwo <= 99:
			DTwo = .60
		elif STwo >= 100:
			DTwo = .50
		
		if SThree >= 10 and SThree <= 19:
			DThree = .80
		elif SThree >= 20 and SThree <= 49:
			DThree = .70
		elif SThree >= 50 and SThree <= 99:
			DThree = .60
		elif SThree >= 100:
			DThree = .50
			
		POne = 99 * SOne
		PTwo = 199 * STwo
		PThree = 299 * SThree
		TOne = float(POne) * DOne
		TTwo = float(PTwo) * DTwo
		TThree = float(PThree) * DThree
		TAll = TOne + TTwo + TThree
		self._label4.Text += str(round(TOne, 2))
		self._label5.Text += str(round(TTwo, 2))
		self._label6.Text += str(round(TThree, 2))
		self._label7.Text += str(round(TAll, 2))
			
		
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.num1 = 0
		self.num2 = 0
		self.num3 = 0
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("SlotMachine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._pictureBox10 = System.Windows.Forms.PictureBox()
		self._pictureBox11 = System.Windows.Forms.PictureBox()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label4 = System.Windows.Forms.Label()
		self._pictureBox12 = System.Windows.Forms.PictureBox()
		self._pictureBox13 = System.Windows.Forms.PictureBox()
		self._pictureBox14 = System.Windows.Forms.PictureBox()
		self._pictureBox15 = System.Windows.Forms.PictureBox()
		self._pictureBox16 = System.Windows.Forms.PictureBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._pictureBox10.BeginInit()
		self._pictureBox11.BeginInit()
		self._pictureBox1.BeginInit()
		self._pictureBox12.BeginInit()
		self._pictureBox13.BeginInit()
		self._pictureBox14.BeginInit()
		self._pictureBox15.BeginInit()
		self._pictureBox16.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.Color.White
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(175, 13)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(156, 226)
		self._pictureBox2.TabIndex = 1
		self._pictureBox2.TabStop = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.Color.White
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(337, 12)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(156, 226)
		self._pictureBox3.TabIndex = 2
		self._pictureBox3.TabStop = False
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button1.Location = System.Drawing.Point(499, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(249, 342)
		self._button1.TabIndex = 3
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._button2.Location = System.Drawing.Point(499, 361)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(249, 52)
		self._button2.TabIndex = 4
		self._button2.Text = "Pickpocket"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(499, 420)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(65, 39)
		self._label1.TabIndex = 5
		self._label1.Text = "Bet:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Goldenrod
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(606, 459)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(142, 41)
		self._label2.TabIndex = 6
		self._label2.Text = "100"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._textBox1.Location = System.Drawing.Point(606, 420)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(142, 38)
		self._textBox1.TabIndex = 7
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Transparent
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(499, 457)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(101, 43)
		self._label3.TabIndex = 8
		self._label3.Text = "Cash:"
		# 
		# progressBar1
		# 
		self._progressBar1.Location = System.Drawing.Point(499, 517)
		self._progressBar1.Maximum = 15000
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(249, 34)
		self._progressBar1.TabIndex = 9
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.Color.White
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._pictureBox4.Location = System.Drawing.Point(13, 246)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(480, 305)
		self._pictureBox4.TabIndex = 10
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackColor = System.Drawing.Color.White
		self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(47, 258)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(76, 71)
		self._pictureBox5.TabIndex = 11
		self._pictureBox5.TabStop = False
		self._pictureBox5.Visible = False
		self._pictureBox5.Click += self.PictureBox5Click
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackColor = System.Drawing.Color.White
		self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
		self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox6.Location = System.Drawing.Point(129, 258)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(76, 71)
		self._pictureBox6.TabIndex = 12
		self._pictureBox6.TabStop = False
		self._pictureBox6.Visible = False
		self._pictureBox6.Click += self.PictureBox6Click
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackColor = System.Drawing.Color.White
		self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
		self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox7.Location = System.Drawing.Point(211, 258)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(76, 71)
		self._pictureBox7.TabIndex = 13
		self._pictureBox7.TabStop = False
		self._pictureBox7.Visible = False
		self._pictureBox7.Click += self.PictureBox7Click
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackColor = System.Drawing.Color.White
		self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
		self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox8.Location = System.Drawing.Point(293, 258)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(76, 71)
		self._pictureBox8.TabIndex = 14
		self._pictureBox8.TabStop = False
		self._pictureBox8.Visible = False
		self._pictureBox8.Click += self.PictureBox8Click
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackColor = System.Drawing.Color.White
		self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
		self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox9.Location = System.Drawing.Point(375, 258)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(76, 71)
		self._pictureBox9.TabIndex = 15
		self._pictureBox9.TabStop = False
		self._pictureBox9.Visible = False
		self._pictureBox9.Click += self.PictureBox9Click
		# 
		# pictureBox10
		# 
		self._pictureBox10.BackColor = System.Drawing.Color.White
		self._pictureBox10.BackgroundImage = resources.GetObject("pictureBox10.BackgroundImage")
		self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox10.Location = System.Drawing.Point(47, 459)
		self._pictureBox10.Name = "pictureBox10"
		self._pictureBox10.Size = System.Drawing.Size(76, 71)
		self._pictureBox10.TabIndex = 16
		self._pictureBox10.TabStop = False
		self._pictureBox10.Visible = False
		# 
		# pictureBox11
		# 
		self._pictureBox11.BackColor = System.Drawing.Color.White
		self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
		self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox11.Location = System.Drawing.Point(129, 459)
		self._pictureBox11.Name = "pictureBox11"
		self._pictureBox11.Size = System.Drawing.Size(76, 71)
		self._pictureBox11.TabIndex = 17
		self._pictureBox11.TabStop = False
		self._pictureBox11.Visible = False
		# 
		# timer1
		# 
		self._timer1.Tick += self.Timer1Tick
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.White
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Location = System.Drawing.Point(13, 13)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(156, 226)
		self._pictureBox1.TabIndex = 18
		self._pictureBox1.TabStop = False
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(843, 38)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(112, 41)
		self._label4.TabIndex = 19
		self._label4.Text = "= 2x"
		# 
		# pictureBox12
		# 
		self._pictureBox12.BackColor = System.Drawing.Color.White
		self._pictureBox12.BackgroundImage = resources.GetObject("pictureBox12.BackgroundImage")
		self._pictureBox12.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox12.Location = System.Drawing.Point(761, 22)
		self._pictureBox12.Name = "pictureBox12"
		self._pictureBox12.Size = System.Drawing.Size(76, 71)
		self._pictureBox12.TabIndex = 20
		self._pictureBox12.TabStop = False
		# 
		# pictureBox13
		# 
		self._pictureBox13.BackColor = System.Drawing.Color.White
		self._pictureBox13.BackgroundImage = resources.GetObject("pictureBox13.BackgroundImage")
		self._pictureBox13.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox13.Location = System.Drawing.Point(761, 99)
		self._pictureBox13.Name = "pictureBox13"
		self._pictureBox13.Size = System.Drawing.Size(76, 71)
		self._pictureBox13.TabIndex = 21
		self._pictureBox13.TabStop = False
		# 
		# pictureBox14
		# 
		self._pictureBox14.BackColor = System.Drawing.Color.White
		self._pictureBox14.BackgroundImage = resources.GetObject("pictureBox14.BackgroundImage")
		self._pictureBox14.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox14.Location = System.Drawing.Point(761, 176)
		self._pictureBox14.Name = "pictureBox14"
		self._pictureBox14.Size = System.Drawing.Size(76, 71)
		self._pictureBox14.TabIndex = 22
		self._pictureBox14.TabStop = False
		# 
		# pictureBox15
		# 
		self._pictureBox15.BackColor = System.Drawing.Color.White
		self._pictureBox15.BackgroundImage = resources.GetObject("pictureBox15.BackgroundImage")
		self._pictureBox15.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox15.Location = System.Drawing.Point(761, 253)
		self._pictureBox15.Name = "pictureBox15"
		self._pictureBox15.Size = System.Drawing.Size(76, 71)
		self._pictureBox15.TabIndex = 23
		self._pictureBox15.TabStop = False
		# 
		# pictureBox16
		# 
		self._pictureBox16.BackColor = System.Drawing.Color.White
		self._pictureBox16.BackgroundImage = resources.GetObject("pictureBox16.BackgroundImage")
		self._pictureBox16.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox16.Location = System.Drawing.Point(761, 330)
		self._pictureBox16.Name = "pictureBox16"
		self._pictureBox16.Size = System.Drawing.Size(76, 71)
		self._pictureBox16.TabIndex = 24
		self._pictureBox16.TabStop = False
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(843, 116)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(112, 41)
		self._label5.TabIndex = 25
		self._label5.Text = "= 5x"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(843, 197)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(112, 41)
		self._label6.TabIndex = 26
		self._label6.Text = "= 15x"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(843, 271)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(112, 41)
		self._label7.TabIndex = 27
		self._label7.Text = "= 35x"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(843, 348)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(112, 41)
		self._label8.TabIndex = 28
		self._label8.Text = "= 100x"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(967, 563)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._pictureBox16)
		self.Controls.Add(self._pictureBox15)
		self.Controls.Add(self._pictureBox14)
		self.Controls.Add(self._pictureBox13)
		self.Controls.Add(self._pictureBox12)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._pictureBox11)
		self.Controls.Add(self._pictureBox10)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Name = "MainForm"
		self.Text = "SlotMachine"
		self.Load += self.MainFormLoad
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._pictureBox10.EndInit()
		self._pictureBox11.EndInit()
		self._pictureBox1.EndInit()
		self._pictureBox12.EndInit()
		self._pictureBox13.EndInit()
		self._pictureBox14.EndInit()
		self._pictureBox15.EndInit()
		self._pictureBox16.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd.Next(1, 51)
		if money > 30:
			MessageBox.Show("You failed to steal money!")
		else:
			cmoney = float(self._label2.Text)
			self._label2.Text = str(round(cmoney + money, 2))
		pass

	def Button1Click(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._pictureBox10.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		# Copy these (above) into timerTick
		
		if self._textBox1.Text == "":
			MessageBox.Show("You must enter an amount to bet first!")
			return
		
		money = float(self._label2.Text)
		bet = float(self._textBox1.Text)
		money2 = money - bet
		
		if money == 0:
			MessageBox.Show("You have no money!")
		elif bet < 1:
			MessageBox.Show("You must bet at least 1 dollar!")
		elif bet > money and bet > money2:
			MessageBox.Show("You don't have enough money!")
		else:
			self._button1.BackgroundImage = levOn
			self._pictureBox4.Visible = True
			self._timer1.Enabled = True
			self._label2.Text = str(round(money2, 2))
			self._progressBar1.Value = 0
			
			num1 = self.num1
			num2 = self.num2
			num3 = self.num3
			
			if num1 == 1 and num2 == 1 and num3 == 1:
				money2 += bet * 2
				
			if num1 == 2 and num2 == 2 and num3 == 2:
				money2 += bet * 5
			
			if num1 == 3 and num2 == 3 and num3 == 3:
				money2 += bet * 15
				
			if num1 == 4 and num2 == 4 and num3 == 4:
				money2 += bet * 35
			
			if num1 == 5 and num2 == 5 and num3 == 5:
				money2 += bet * 100
			
			self.num1 = 0
			self.num2 = 0
			self.num3 = 0
			self._label2.Text = str(round(money2, 2))
			
			if money2 == 0:
				MessageBox.Show("You ran out of cash!")
		pass
	
	

	def Timer1Tick(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._pictureBox10.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		# Copied from Button1Click
		
		pb1 = self._pictureBox1
		pb2 = self._pictureBox2
		pb3 = self._pictureBox3
		
		for lcv in range(0, 1000):
			num1 = rnd.Next(1, 6)  # Generate a number between 1 & 5
			num2 = rnd.Next(1, 6)
			num3 = rnd.Next(1, 6)
			
			self.num1 = num1
			self.num2 = num2
			self.num3 = num3
			
			# Copy/paste this for num2/pb2 and num3/pb3
			if num1 == 1:
				pb1.BackgroundImage = im1
			elif num1 == 2:
				pb1.BackgroundImage = im2
			elif num1 == 3:
				pb1.BackgroundImage = im3
			elif num1 == 4:
				pb1.BackgroundImage = im4
			elif num1 == 5:
				pb1.BackgroundImage = im5
			
			if num2 == 1:
				pb2.BackgroundImage = im1
			elif num2 == 2:
				pb2.BackgroundImage = im2
			elif num2 == 3:
				pb2.BackgroundImage = im3
			elif num2 == 4:
				pb2.BackgroundImage = im4
			elif num2 == 5:
				pb2.BackgroundImage = im5
				
			if num3 == 1:
				pb3.BackgroundImage = im1
			elif num3 == 2:
				pb3.BackgroundImage = im2
			elif num3 == 3:
				pb3.BackgroundImage = im3
			elif num3 == 4:
				pb3.BackgroundImage = im4
			elif num3 == 5:
				pb3.BackgroundImage = im5
			
			self._progressBar1.Increment(1)
			if self._progressBar1.Value == self._progressBar1.Maximum:
				self._timer1.Enabled = False
				self._pictureBox4.Visible = False
				self._button1.BackgroundImage = levOff
				
		pass

	def PictureBox5Click(self, sender, e):
		pass

	def PictureBox6Click(self, sender, e):
		pass

	def PictureBox7Click(self, sender, e):
		pass

	def PictureBox8Click(self, sender, e):
		pass

	def PictureBox9Click(self, sender, e):
		pass
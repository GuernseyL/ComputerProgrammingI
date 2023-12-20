require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(285, 361)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(382, 361)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(483, 361)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 23)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.Location = System::Drawing::Point.new(285, 196)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 3
		@label1.Text = "Radius"
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label2.Location = System::Drawing::Point.new(285, 257)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(273, 23)
		@label2.TabIndex = 4
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ActiveCaption
		@label3.Location = System::Drawing::Point.new(285, 317)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(273, 23)
		@label3.TabIndex = 5
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(391, 193)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(166, 20)
		@textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.AppWorkspace
		self.ClientSize = System::Drawing::Size.new(856, 447)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end


	def Button1Click(sender, e)
		radius = float(@textBox1.Text)
		area = (radius * radius) * 3.14159
		circum = radius * 2 * 3.14159
		@label2.Text = "Area: " + str(area)
		@label3.Text = "Circum: " + str(circum)
	end

end


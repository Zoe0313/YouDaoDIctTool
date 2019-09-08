# 有道翻译小工具

### **PyQt概要**

	PyQt是Python语言的GUI编程解决方案之一。可以用来代替Python内置的Tkinter。其它替代者还有PyGTK、wxPython等。与Qt一样，PyQt是一个自由软件。


### **安装与配置**

	1、安装pyqt5
		sudo apt-get install pyqt5*
	2、安装qt designer
		sudo apt-get install qttools5-dev-tools
	3、确认是否安装成功
		/usr/lib/x86_64-linux-gnu/qt5/bin/designer
	4、设置pycharm
		File->setting->Tools->External Tools
		单击+号新建：
			Name：QtDesigner
			Group：Qt5
			Program：/usr/lib/x86_64-linux-gnu/qt5/bin/designer
			Parameters：$FileName$
			Working directory：$ProjectFileDir$
		再次单击+号新建：
			Name：PyUIC
			Group：Qt5
			Program：/usr/bin/python3
			Parameters：-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
			Working directory：$FileDir$
		保存以后，在主菜单的Tools中看到Qt这个工具包
	5、点击QtDesigner开始编辑ui界面，保存成test.ui
	6、在pycharm中右键点击test.ui文件，选择Qt5->PyUIC，自动生成test.py文件
	7、新建QtTool.py继承test.py中的界面类，撰写界面逻辑。

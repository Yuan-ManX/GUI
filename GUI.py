import sys
from PyQt5 import QtWidgets,QtGui,QtCore,Qt

# 加载
app = QtWidgets.QApplication(sys.argv)

# 设置win窗口
windows = QtWidgets.QWidget()
windows.resize(800,500)
windows.move(400,100)

'''
pr = windows.frameGeometry()
cp = QtWidgets.QDesktopWidget().
'''

# 添加标题和图标
windows.setWindowTitle("音频工具")
# windows.setWindowIcon('图标')

# 设置字体
QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

# 提示语
windows.setToolTip('Runnnnnn!!!')

# 设置按钮并设置颜色
button = QtWidgets.QPushButton(windows)
button.setGeometry(350,200,100,50)
button.setToolTip('Lookkkkkk!!!')
button.setStyleSheet("background-color: rgb(255,0,0;"
                    "border-color: rgb(0,0,255);"
                    "font: 75 12pt \"Arial Narrow\";"
                    "color: rgb(0,255,0);")
button.clicked.connect(QtCore.QCoreApplication.instance().quit)

# 设置标签信息
label = QtWidgets.QLabel(windows)
label.setGeometry(QtCore.QRect(200,150,200,150))
label.setText("你猜猜这是什么？")
label.setObjectName('label')

# show显示和退出
windows.show()
sys.exit(app.exec_())
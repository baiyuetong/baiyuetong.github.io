import wx

class MyFrame(wx.Frame):
    """ 创建一个类继承自 Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,300))

        # 通常 Frame里面不直接放控件，
        # 定义一个 面板 Panel，里面放其它控件
        self.panel = wx.Panel(self, wx.ID_ANY)


        # 定义按钮， pos参数指定按钮在panel里面的坐标
        # size参数指定按钮控件的宽度和高度，单位为像素
        self.button = wx.Button(
            self.panel, wx.ID_ANY, "点击试试",
            pos=(30, 30), size=(100,40))

        # 指定该按钮的点击事件的处理方法是 clickButton      
        self.button.Bind( wx.EVT_BUTTON, self.clickButton)
 
        self.clickNum = 0 # 点击按钮次数
        self.Show(True)
    
    def clickButton(self,event):
        self.clickNum += 1
        # 输出信息到标准输出上
        print(f"点击{self.clickNum}次")

app = wx.App(False)
frame = MyFrame(None, '图形界面测试应用')
app.MainLoop()


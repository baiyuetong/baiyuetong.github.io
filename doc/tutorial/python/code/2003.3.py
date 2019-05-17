import wx

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,300))
        self.panel = wx.Panel(self, wx.ID_ANY)


        self.button1 = wx.Button(
            self.panel, wx.ID_ANY, "点击1",
            pos=(30, 30), size=(50,40))

        self.textCtrl1 = wx.TextCtrl( 
            self.panel, wx.ID_ANY, 
            pos=(30, 80), size=(280,130) )
 

        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, '图形界面测试应用')
app.MainLoop()


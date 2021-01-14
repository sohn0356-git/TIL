import wx
import app1
from userdb import *
from itemdb import *

# 1. 화면에서 데이터를 입력하면 DB에 INSERT되고 List화면에 출력된다.
# 2. List 화면에는 ID와 NAME만 출력되고 항목을 클릭했을 때 ID, PWD, NAME, AGE 모두 출력되게한다.


data = []
users = app1.init()
print('-----------------')
for user in users:
    data.append("%s %s %d" % (user.id, user.name, user.age))

app = wx.App()
frame = wx.Frame(None, title='Shop Management')
panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)
textId = wx.TextCtrl(panel1)
textId.SetHint('id : ?')
textPwd = wx.TextCtrl(panel1)
textPwd.SetHint('Pwd : ?')
textName = wx.TextCtrl(panel1)
textName.SetHint('Name : ?')
textAge = wx.TextCtrl(panel1)
textAge.SetHint('Age : ?')
bt = wx.Button(panel1, label='ADD')

userList = wx.ListBox(panel2,choices=data)
userList.SetBackgroundColour(colour='green')
userList.SetSize(wx.EXPAND,wx.EXPAND)

# List Event ............................
def itemSelect(event):
    global  userList
    global data
    userIdx = userList.GetSelection()
    wx.MessageBox(data[userIdx],'User Information',wx.OK)

userList.Bind(wx.EVT_LISTBOX,itemSelect)
# Button Event ..........................
def onClick(event):
    global textId
    global textPwd
    global textName
    global textAge
    global userList
    global data
    id = textId.GetValue()
    pwd = textPwd.GetValue()
    name = textName.GetValue()
    age = textAge.GetValue()
    wx.MessageBox(id+"생성 완료", ' Alert', wx.OK)

    userList.Append(id+' '+name + ' ' + age)
    print('Inserted')
    app1.userInsert(User(id=id,pwd=pwd,name=name,age=int(age)))
    data = app1.init()
    textId.SetValue('')
    textPwd.SetValue('')
    textName.SetValue('')

bt.Bind(wx.EVT_BUTTON,onClick)
box1 = wx.BoxSizer(wx.VERTICAL)
box1.Add(textId)
box1.Add(textPwd)
box1.Add(textName)
box1.Add(textAge)
box1.Add(bt)
panel1.SetSizer(box1)


panel1.SetBackgroundColour('blue')
panel2.SetBackgroundColour('green')
grid = wx.GridSizer(1,2,10,50)
grid.Add(panel1, 0, wx.EXPAND)
grid.Add(panel2, 0, wx.EXPAND)
frame.SetSizer(grid)
frame.Show(True)
app.MainLoop()
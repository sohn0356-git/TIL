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
btAdd = wx.Button(panel1, label='ADD')
btDelete = wx.Button(panel1, label="DELETE")

userList = wx.ListBox(panel2,choices=data)
userList.SetBackgroundColour(colour='green')
userList.SetSize(wx.EXPAND,wx.EXPAND)

# List Event ............................
def itemSelect(event):
    global  userList
    userIdx = userList.GetSelection()
    wx.MessageBox(userList.GetString(userIdx),'User Information',wx.OK)

userList.Bind(wx.EVT_LISTBOX,itemSelect)
# Button Event ..........................
def onClick(event):
    global textId
    global textPwd
    global textName
    global textAge
    global userList
    global data
    global panel2

    id = textId.GetValue()
    pwd = textPwd.GetValue()
    name = textName.GetValue()
    age = textAge.GetValue()
    wx.MessageBox(id+"생성 완료", ' Alert', wx.OK)

    print('Inserted')
    app1.userInsert(User(id=id,pwd=pwd,name=name,age=int(age)))

    userList.Clear()
    users = app1.init()
    for user in users:
        userList.Append("%s %s %d" % (user.id, user.name, user.age))


    textId.SetValue('')
    textPwd.SetValue('')
    textName.SetValue('')
    textAge.SetValue('')

def onClickDelete(event):
    global textId
    global userList

    id = textId.GetValue()
    wx.MessageBox(id + "제거 완료", ' Alert', wx.OK)

    print('Deleted')
    app1.userDelete(id)

    userList.Clear()
    users = app1.init()
    for user in users:
        userList.Append("%s %s %d" % (user.id, user.name, user.age))


    textId.SetValue('')

btAdd.Bind(wx.EVT_BUTTON, onClick)
btDelete.Bind(wx.EVT_BUTTON, onClickDelete)
box1 = wx.BoxSizer(wx.VERTICAL)
box1.Add(textId)
box1.Add(textPwd)
box1.Add(textName)
box1.Add(textAge)
box1.Add(btAdd)
box1.Add(btDelete)
panel1.SetSizer(box1)


panel1.SetBackgroundColour('blue')
panel2.SetBackgroundColour('green')
grid = wx.GridSizer(1,2,10,50)
grid.Add(panel1, 0, wx.EXPAND)
grid.Add(panel2, 0, wx.EXPAND)
frame.SetSizer(grid)
frame.Show(True)
app.MainLoop()
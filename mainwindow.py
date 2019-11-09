#coding=utf-8
import Tkinter as tk
from phoneinfo import PhoneInfo

class phonePanel(object):

    def __init__(self, master):
        self.master = master
        self.setupWindow(master)
        pass

    def setupWindow(self, windowPanel):
        windowPanel.title('Android EasyUI Desktop Tool')
        width = 480
        height = 640
        screenwidth = windowPanel.winfo_screenwidth()  
        screenheight = windowPanel.winfo_screenheight() 
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)   
        windowPanel.geometry(alignstr)
        self.fillPhoneInfo(windowPanel)
        self.fillBt(windowPanel)
    def clickme(self):
        pass

    def fillBt(self, windowPanel):
        tk.Button(windowPanel, text ="点我", command = self.clickme).pack()

    def fillPhoneInfo(self, windowPanel):
        infoPanel = tk.LabelFrame(windowPanel, text="Phone Info", padx=10, pady=10)
        infoPanel.pack(padx=10, pady=10)
        info = PhoneInfo()
        tk.Label(infoPanel, text="Serial Num        ").grid(row=0,column=1)
        tk.Label(infoPanel, text=info.serialNum).grid(row=0,column=2)
        tk.Label(infoPanel, text="Product Name      ").grid(row=1,column=1)
        tk.Label(infoPanel, text=info.productModel).grid(row=1,column=2)
        tk.Label(infoPanel, text="Android version       ").grid(row=2,column=1)
        tk.Label(infoPanel, text=info.androidVersion).grid(row=2,column=2)
        tk.Label(infoPanel, text="Install mode      ").grid(row=3,column=1)
        tk.Label(infoPanel, text=info.installMode).grid(row=3,column=2)
        pass

    def show(self):
        # myWindow.resizable(width=False, height=True)

        # group = tk.LabelFrame(self.master, text="Phone Info", padx=5, pady=5)
        # group.pack(padx=10, pady=10)
        
        # # v = tk.IntVar()

        # abc = PhoneInfo()
        # r1 = tk.Label(group, text="Serial No.       ").grid(row=0,column=1)
        # r2 = tk.Label(group, text=abc.serialNum).grid(row=0,column=2)
        self.master.mainloop()
        # r3 = tk.Label(group, text=r"老师/学长介绍").pack(anchor="w")
        # myWindow = tk.Tk()




def main():
    myWindow = tk.Tk()
    phonePanel(myWindow).show()
    # myWindow.mainloop()
    pass

if __name__ == "__main__":
    main()
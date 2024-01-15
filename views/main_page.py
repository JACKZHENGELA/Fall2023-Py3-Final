import ttkbootstrap as tb
from K import *
from views.helper import View

class MainPage(View):
    def __init__(self, app):
        super().__init__(app)

        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame)
        self.top1.pack(expand=True, fill=BOTH)

        self.bottom1 = tb.Frame(self.frame)
        self.bottom1.pack(expand=True, fill=BOTH)

        self.top2 = tb.Frame(self.top1)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)

        self.bottom2 = tb.Frame(self.bottom1)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)

        self.top3 = tb.Frame(self.top2)
        self.top3.pack(side=BOTTOM, ipadx=37, ipady=25)

        self.bottom3 = tb.Frame(self.bottom2)
        self.bottom3.pack(side=TOP, ipadx=131, ipady=15)

        tb.Label(self.top3, text="Farmer's Life", bootstyle=PRIMARY, font=('Comic Sans', 30)).pack(side=TOP, pady=60)
        tb.Label(self.top3, text="Create tasks and purchase fruits as a farmer!", bootstyle=PRIMARY, font=('Helvetica', 15)).pack(side=TOP)
        tb.Button(self.bottom2, text="Register", command=self.app.register_page, bootstyle=SECONDARY).pack(side=BOTTOM, ipadx=30, ipady=5, pady=40)
        tb.Button(self.bottom2, text="Login", command=self.app.login_page, bootstyle=SECONDARY).pack(side=BOTTOM, ipadx=39,ipady=5)

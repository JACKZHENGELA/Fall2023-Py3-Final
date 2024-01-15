import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

class OrdersPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.orders = []
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=PRIMARY)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=PRIMARY)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=PRIMARY)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=10, pady=50)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=PRIMARY)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=10, pady=50)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(expand=True, ipadx=116)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(expand=True, ipadx=11, ipady=15)
        tb.Label(self.top3, text=f"", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=TOP, pady=1)
        self.color = tb.Label(self.top3, text=f"None: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.color.pack(side=TOP, pady=10)
        self.fruit_type = tb.Label(self.top3, text=f"None: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.fruit_type.pack(side=TOP, pady=10)
        self.grown = tb.Label(self.top3, text=f"None: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.grown.pack(side=TOP, pady=10)
        self.planter = tb.Label(self.top3, text=f"None: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.planter.pack(side=TOP, pady=10)
        self.size = tb.Label(self.top3, text=f"None: ", bootstyle="inverse-primary", font=('Helvetica', 15))
        self.size.pack(side=TOP, pady=10)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(fill=X, ipady=0)

        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)
        tb.Button(self.bottom4, text="Back",command=self.app.user_page, bootstyle=DANGER).pack(expand=True, side=LEFT,ipady=3, pady=10, ipadx=17)

        tb.Button(self.bottom4, text="Get the Task You wanna get", command=self.app.get_fruits_view,
                  bootstyle=SUCCESS).pack(expand=True, side=LEFT,ipady=3, pady=10, ipadx=17)

import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

class LoginPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame)
        self.top1.pack(padx=320, expand=TRUE, fill=X)

        tb.Label(self.top1, text="Login", font=H3).pack(pady=PM, fill=X)
        tb.Label(self.top1, text="Email:").pack(pady=PXS, expand=TRUE, fill=BOTH)
        self.search_bar = tb.Entry(self.top1, textvariable=self.email_var).pack(pady=PXS, fill=X)

        tb.Label(self.top1, text="Password:").pack(pady=PXS, expand=TRUE, fill=BOTH)
        self.search_bar = tb.Entry(self.top1, textvariable=self.password_var, show="*").pack(pady=PXS, fill=X)

        tb.Button(self.top1, text="Sign Up",command=self.app.register_page, bootstyle=DANGER).pack(side=LEFT, ipadx=20, ipady=3, pady=10)
        tb.Button(self.top1, text="Submit", bootstyle=SUCCESS, command=self.login).pack(side=RIGHT, ipadx=12, ipady=3, pady=30)


    def login(self):
        # self.app.authenticated = True
        # self.app.user_page()
        email = self.email_var.get()
        password = self.password_var.get()
        auth = req.post(f"{self.app.url}token", data={"username": email,
                                                                  "password": password}).json()

        try:
            self.app.token = {"access_token": auth["access_token"], "token_type": "string"}
            self.app.authenticated = TRUE
            self.app.email = email
            self.password_var.set("")
            self.app.user_page()
        except:
            self.create_toast("401 Error", "Bad Credentials")

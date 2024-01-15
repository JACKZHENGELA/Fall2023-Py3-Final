import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req

from requests.auth import HTTPBasicAuth

class UserPage(View):
    def __init__(self, app):
        super().__init__(app)
        self.email_var = tb.StringVar()
        self.password_var = tb.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.nav_frame = tb.Frame(self.frame, bootstyle=PRIMARY)
        self.nav_frame.pack(fill=X, ipadx=PXS, ipady=PXS)

        self.container = tb.Frame(self.frame)
        self.container.pack(fill=BOTH, expand=True)


        self.logout_button = tb.Button(self.nav_frame,
                                      text="Logout Account",
                                      bootstyle=DANGER,
                                      command=self.app.logout).pack(side=RIGHT, padx=PXS)
        self.ViewYourProfile = tb.Button(self.nav_frame,
                                         text="View Your Profile",
                                         bootstyle=SECONDARY,
                                         command=self.app.profile_page).pack(side=RIGHT, padx=PXS)
        self.mydata_button = tb.Button(self.nav_frame,
                                        text="My Data",
                                        bootstyle=SECONDARY,
                                        command=self.app.get_fruits_view).pack(side=RIGHT, padx=PXS)
        self.Update_Tasks = tb.Button(self.nav_frame,
                                       text="Updater",
                                       bootstyle=SECONDARY,
                                       command=self.app.update_task_view).pack(side=RIGHT, padx=PXS)

        self.Delete = tb.Button(self.nav_frame,
                                text="Delete",
                                bootstyle=SECONDARY,
                                command=self.app.show_delete_page).pack(side=RIGHT, padx=PXS)
        self.Create_Fruits_Order = tb.Button(self.nav_frame,
                                             text="Order Fruits",
                                             bootstyle=SECONDARY,
                                             command=self.app.delivery_page).pack(side=RIGHT, padx=PXS)
        self.MakeProjects = tb.Button(self.nav_frame,
                                      text="Make Plans",
                                      command=self.app.show_task_creater,
                                      bootstyle=SECONDARY).pack(side=RIGHT, padx=PXS)
        self.AccessPersonalInfo = tb.Button(self.nav_frame,
                                            text="Create A Farmer", command=self.app.show_information, bootstyle=SECONDARY).pack(side=RIGHT, padx=PXS)

        self.title_label = tb.Label(self.container, bootstyle=PRIMARY, text="Farmer's Life", font=H1)
        self.subtitle_label = tb.Label(self.container, text="Thank you for using Farmer's Life! \nIn this app you can create your own farmer profile, buy fruits as a farmer, \nand create your tasks as a farmer!\nEnjoy!", font=LEAD)

        self.title_label.pack(anchor=NW, padx=PL, pady=(15, 0))
        self.subtitle_label.pack(anchor=NW, padx=PL)










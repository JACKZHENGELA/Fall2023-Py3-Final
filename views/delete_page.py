import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req


class DeletePage(View):
    def __init__(self, app):
        super().__init__(app)
        self.id = tb.IntVar()
        self.growth = tb.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        self.top1 = tb.Frame(self.frame, bootstyle=PRIMARY)
        self.top1.pack(expand=True, fill=BOTH)
        self.bottom1 = tb.Frame(self.frame, bootstyle=PRIMARY)
        self.bottom1.pack(expand=True, fill=BOTH)
        self.top2 = tb.Frame(self.top1, bootstyle=PRIMARY)
        self.top2.pack(side=BOTTOM, ipadx=10, ipady=5)
        self.bottom2 = tb.Frame(self.bottom1, bootstyle=PRIMARY)
        self.bottom2.pack(side=TOP, ipadx=10, ipady=5)
        self.top3 = tb.Frame(self.top2, bootstyle=PRIMARY)
        self.top3.pack(side=BOTTOM, ipadx=37, ipady=25)
        self.bottom3 = tb.Frame(self.bottom2, bootstyle=PRIMARY)
        self.bottom3.pack(side=TOP, ipadx=70, ipady=15)
        tb.Label(self.top3, text="", bootstyle="inverse-primary").pack(side=TOP, ipadx=1, ipady=1, padx=10, pady=2)
        tb.Label(self.top3, text="Deleter", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=10)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(side=TOP, pady=10)
        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)

        tb.Button(self.bottom4, text="Back", command=self.app.user_page, bootstyle=DANGER).pack(expand=True, ipady=6,
                                                                                                ipadx=80, pady=10)

        tb.Button(self.top4, text="Delete Fruits Data", command=self.profile, bootstyle=INFO).pack(side=LEFT,
                                                                                                         ipady=6,
                                                                                                         ipadx=20,
                                                                                                         padx=29,
                                                                                                         pady=10)
        tb.Button(self.top4, text="Delete Tasks Data", command=self.balls, bootstyle=INFO).pack(side=RIGHT,
                                                                                                        ipady=6,
                                                                                                        ipadx=20,
                                                                                                        padx=29,
                                                                                                        pady=10)

        tb.Button(self.top4, text="Delete Information", command=self.balls, bootstyle=INFO).pack(side=RIGHT,
                                                                                                ipady=6,
                                                                                                ipadx=20,
                                                                                                padx=29,
                                                                                                pady=10)

        self.bottom5 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom5.pack(expand=True, ipadx=5, ipady=0)
        tb.Label(self.bottom5, text="put in your id:", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT,
                                                                                                          pady=10)

        tb.Entry(self.bottom5, bootstyle=INFO, textvariable=self.id).pack(side=RIGHT, pady=10, expand=True)

    def profile(self):
        task_id = str(self.id.get())
        profile = req.delete(f'{self.app.url}fruits/{task_id}?auth={self.app.token["access_token"]}',
                             headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                      'Content-Type': 'application/json'}).json()
        self.app.views.get('user_orders').color.configure(text=f'Fruit Color: {profile["color"]}')
        self.app.views.get('user_orders').fruit_type.configure(text=f'Fruit Type: {profile["fruit_type"]}')
        self.app.views.get('user_orders').grown.configure(text=f'Grown: {profile["grown"]}')
        self.app.views.get('user_orders').planter.configure(text=f'Planter: {profile["planter"]}')
        self.app.views.get('user_orders').size.configure(text=f'Size: {profile["size"]}')

    def balls(self):
        task_id = str(self.id.get())
        profile = req.delete(f'{self.app.url}tasks/{task_id}?auth={self.app.token["access_token"]}',
                             headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                      'Content-Type': 'application/json'}).json()
        self.app.views.get('user_orders').color.configure(text=f'Title: {profile["title"]}')
        self.app.views.get('user_orders').fruit_type.configure(text=f'Description: {profile["description"]}')
        self.app.views.get('user_orders').grown.configure(text=f'Priority: {profile["priority"]}')
        self.app.views.get('user_orders').planter.configure(text=f'Completion: {profile["complete"]}')
        self.app.views.get('user_orders').size.configure(text="")

    def funny(self):
        task_id = str(self.id.get())
        profile = req.delete(f'{self.app.url}profiles/{task_id}?auth={self.app.token["access_token"]}',
                          headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                   'Content-Type': 'application/json'}).json()
        self.app.views.get('user_orders').color.configure(text=f'gpa: {profile["gpa"]}')
        self.app.views.get('user_orders').fruit_type.configure(text=f'School: {profile["school"]}')
        self.app.views.get('user_orders').grown.configure(text=f'Gender: {profile["gender"]}')
        self.app.views.get('user_orders').planter.configure(text=f'Have Pets?: {profile["have_pet"]}')
        self.app.views.get('user_orders').size.configure(text="")

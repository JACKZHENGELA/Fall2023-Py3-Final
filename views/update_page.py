import ttkbootstrap as tb
from K import *
from views.helper import View
import requests as req
from json import dumps


class UpdatePage(View):
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
        self.bottom4 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom4.pack(expand=True, ipadx=56, ipady=0)
        tb.Label(self.top3, text="", bootstyle="inverse-primary").pack(side=TOP, ipadx=1, ipady=1, padx=10, pady=2)
        tb.Label(self.top3, text="Updater", bootstyle="inverse-primary", font=('Helvetica', 30)).pack(side=TOP, pady=10)
        self.top4 = tb.Frame(self.top3, bootstyle=PRIMARY)
        self.top4.pack(side=TOP, pady=10)

        tb.Button(self.bottom4, text="Back", command=self.app.user_page, bootstyle=DANGER).pack(expand=True, ipady=6,
                                                                                                ipadx=80, pady=10)

        tb.Button(self.top4, text="Nolan Wang Fruit", command=self.ball_cancer, bootstyle=INFO).pack(
                                                                                                         ipady=6,
                                                                                                         ipadx=20,
                                                                                                         padx=29,
                                                                                                         pady=10)
        tb.Button(self.top4, text="Jack Wang Fruit", command=self.touch_grass, bootstyle=INFO).pack(
                                                                                                        ipady=6,
                                                                                                        ipadx=20,
                                                                                                        padx=29,
                                                                                                        pady=10)
        tb.Button(self.top4, text="Update Gender Male", command=self.good_code, bootstyle=INFO).pack(

            ipady=6,
            ipadx=20,
            padx=29,
            pady=10)

        tb.Button(self.top4, text="Update Gender Female", command=self.also_good_code, bootstyle=INFO).pack(

            ipady=6,
            ipadx=20,
            padx=29,
            pady=10)

        tb.Button(self.top4, text="Update Plant Status", command=self.the_voices_are_getting_louder, bootstyle=INFO).pack(

            ipady=6,
            ipadx=20,
            padx=29,
            pady=10)

        tb.Button(self.top4, text="Update Animal Feeding", command=self.i_hate_music_appreciation, bootstyle=INFO).pack(

            ipady=6,
            ipadx=20,
            padx=29,
            pady=10)

        self.bottom5 = tb.Frame(self.bottom3, bootstyle=PRIMARY)
        self.bottom5.pack(expand=True, ipadx=5, ipady=0)
        tb.Label(self.bottom5, text="put in your id:", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(side=LEFT,
                                                                                                          pady=10)

        tb.Entry(self.bottom5, bootstyle=INFO, textvariable=self.id).pack(side=RIGHT, pady=10, expand=True)

        tb.Label(self.bottom4, text="put in growth/completion/Have Pets:", bootstyle="inverse-primary", font=('Helvetica', 15)).pack(
            side=LEFT,
            pady=10)

        tb.Entry(self.bottom4, bootstyle=INFO, textvariable=self.growth).pack(side=RIGHT, pady=10, expand=True)




    def ball_cancer(self):
        task_id = str(self.id.get())
        data = {"color": "red", "fruit_type": "nolan wang fruit", "grown": self.growth.get(), "size": 1}
        req.put(f'{self.app.url}fruits/{task_id}', headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                    'Content-Type': 'application/json'}, json=data)
        self.create_toast("201", "NICE!")
        self.app.user_page()


    def touch_grass(self):
        task_id = str(self.id.get())
        data = {"color": "red", "fruit_type": "jack wang fruit", "grown":self.growth.get(), "size": 1}
        req.put(f'{self.app.url}fruits/{task_id}',
                headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                 'Content-Type': 'application/json'}, json=data).json()
        self.create_toast("201", "NICE!")
        self.app.user_page()

    def good_code(self):
        task_id = str(self.id.get())
        data = {"gender": "Male", "gpa": "4.0", "have_pet": self.growth.get(), "school": "SMIC"}
        req.put(f'{self.app.url}profiles/{task_id}',
                 headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                          'Content-Type': 'application/json'}, json=data).json()
        self.create_toast("201", "NICE!")
        self.app.user_page()

    def also_good_code(self):
        task_id = str(self.id.get())

        data = {"gender": "Female", "gpa": "4.0", "have_pet": self.growth.get(), "school": "SMIC"}
        req.put(f'{self.app.url}profiles/{task_id}?auth={self.app.token["access_token"]}',
                 headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                          'Content-Type': 'application/json'}, json=data)
        self.create_toast("201", "NICE!")
        self.app.user_page()

    def the_voices_are_getting_louder(self):
        task_id = str(self.id.get())
        data = {"completion": self.growth.get(), "description": "Plants plants", "priority": 5,"title": "Plants"}
        req.put(f'{self.app.url}tasks/{task_id}?auth={self.app.token["access_token"]}',
                headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                         'Content-Type': 'application/json'}, json=data)
        self.create_toast("201", "NICE!")
        self.app.user_page()

    def i_hate_music_appreciation(self):
        task_id = str(self.id.get())
        response = req.get(f'{self.app.url}tasks/{task_id}?auth={self.app.token["access_token"]}',
                           headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                                    'Content-Type': 'application/json'})

        json_data = response.json()
        fruit_id = json_data["id"]
        data = {"completion": self.growth.get(), "description": "Feed Animals", "priority": 5,"title": "Animal"}
        req.put(f'{self.app.url}tasks/{fruit_id}?auth={self.app.token["access_token"]}',
                headers={'Authorization': f'Bearer {self.app.token["access_token"]}',
                         'Content-Type': 'application/json'}, json=data)
        self.create_toast("201", "NICE!")
        self.app.user_page()




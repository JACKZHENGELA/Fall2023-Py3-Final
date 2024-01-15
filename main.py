import ttkbootstrap as tb
from K import *
from views import main_page, tasks, login_page, register_page, user_page, profile_page,fruits_page, user_tasks, update_page, get_fruits, delete_page, tasks_creater, personal_information


class TaskApp(tb.Window):
    def __init__(self):
        super().__init__(themename="minty")
        self.title("Task Manager")
        self.geometry("1280x720")

        # User variables
        self.authenticated = False
        self.email = tb.StringVar()
        self.nick = tb.StringVar()
        self.name = tb.StringVar()
        self.token: dict = {}
        self.url = 'http://0.0.0.0:8000/'

        # Views variables
        self.current_view = None

        self.views = {
            "main_page": main_page.MainPage(self),
            "login_page": login_page.LoginPage(self),
            "register_page": register_page.RegisterPage(self),
            "user_page": user_page.UserPage(self),
            "profile_page": profile_page.ProfilePage(self),
            "delivery_page": fruits_page.OrderPage(self),
            "user_orders": user_tasks.OrdersPage(self),
            "update_page": update_page.UpdatePage(self),
            "view_tasks": tasks.TasksView(self),
            "view_task": tasks.TaskView(self),
            "create_task": tasks.CreateTaskView(self),
            "get_fruits": get_fruits.GetPage(self),
            "Delete_tasks": delete_page.DeletePage(self),
            "project_creator": tasks_creater.CreatePage(self),
            "personal": personal_information.CPage(self)
        }

        # Init Welcome Screen
        self.login_page()




    def logout(self):
        self.authenticated = False
        self.main_page()

    def main_page(self):
        self.set_current_view("main_page")

    def login_page(self):
        self.set_current_view("login_page")

    def register_page(self):
        self.set_current_view("register_page")

    def user_page(self):
        self.set_current_view("user_page")

    def profile_page(self):
        self.set_current_view("profile_page")

    def delivery_page(self):
        self.set_current_view("delivery_page")

    def show_information(self):
        self.set_current_view("personal")

    def user_orders(self):
        self.set_current_view("user_orders")

    def show_task_view(self):
        self.set_current_view("view_task")

    def show_tasks_view(self):
        self.set_current_view("view_tasks")

    def show_create_task_view(self):
        self.set_current_view("create_task")

    def update_task_view(self):
        self.set_current_view("update_page")

    def get_fruits_view(self):
        self.set_current_view("get_fruits")

    def show_delete_page(self):
        self.set_current_view("Delete_tasks")

    def show_task_creater(self):
        self.set_current_view("project_creator")

    def set_current_view(self, key):
        self.destroy_current_view()
        self.current_view = key
        self.views.get(key).pack_view()

    def destroy_current_view(self):
        if self.current_view:
            self.views.get(self.current_view).unpack_view()


if __name__ == "__main__":
    app = TaskApp()
    app.place_window_center()
    app.mainloop()

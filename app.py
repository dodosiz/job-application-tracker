import tkinter as tk
import ast


class App:
    font_normal = "Helvetica 9"
    font_bold = "Helvetica 12 bold"

    def __init__(self, master):
        self.data = self.read_data()
        self.main_frame = self.create_main_frame(master)
        self.top_menu = self.create_top_menu()
        self.location, self.office = self.create_form(self.add_new, "Add", "green", "Location", "Office")
        self.location_for_office_to_delete, self.office_to_delete = self.create_form(
            self.delete_office, "Delete", "red", "Location", "Office")
        self.location_to_delete = self.create_form(self.delete_location, "Delete", "red", "Location")
        self.create_save_button()
        self.entries_frame = self.render_entries()

    def create_top_menu(self):
        top_menu = tk.Frame(self.main_frame, highlightbackground="black", highlightthickness=1)
        top_menu.pack(fill=tk.X)
        return top_menu

    def create_save_button(self):
        save_button_frame = tk.Frame(self.main_frame)
        save_button_frame.pack(fill=tk.X, ipady=10)
        save_button = tk.Button(save_button_frame, text="Save List", background="green", command=self.save_list)
        save_button.pack(side=tk.LEFT)

    def save_list(self):
        f = open("data.txt", "w")
        f.write(str(self.data))
        f.close()

    def create_form(self, action, button_text, button_color, label_text_1, label_text_2 = False):
        form = tk.Frame(self.top_menu)
        form.pack(side=tk.LEFT, ipadx=20)
        entry_label_1 = self.create_entry_label(label_text_1, form)
        entry_label_2 = False
        if label_text_2:
            entry_label_2 = self.create_entry_label(label_text_2, form)
        self.create_button(button_text, button_color, action, form)
        if entry_label_2:
            return entry_label_1, entry_label_2
        else:
            return entry_label_1

    @staticmethod
    def create_entry_label(text, form):
        label = tk.Label(form, text=text)
        label.pack()
        value = tk.StringVar()
        entry = tk.Entry(form, textvariable=value)
        entry.pack()
        return value

    @staticmethod
    def create_button(text, color, command, form):
        add_new_button = tk.Button(form, text=text, padx=10, command=command, background=color)
        add_new_button.pack()

    @staticmethod
    def create_main_frame(master):
        main_frame = tk.Frame(master, width=500, height=400)
        main_frame.pack_propagate(0)
        main_frame.pack(fill=tk.BOTH)
        return main_frame

    @staticmethod
    def read_data():
        f = open('data.txt', 'r')
        raw_data = f.read()
        data = ast.literal_eval(raw_data)
        f.close()
        return data

    def add_new(self):
        location = self.location.get()
        office = self.office.get()
        if location in self.data:
            self.data[location].append(office)
        else:
            self.data[location] = [office]
        self.location.set("")
        self.office.set("")
        self.entries_frame.destroy()
        self.entries_frame = self.render_entries()

    def delete_office(self):
        location = self.location_for_office_to_delete.get()
        office = self.office_to_delete.get()
        if location in self.data:
            if office in self.data[location]:
                self.data[location].remove(office)
                self.location_for_office_to_delete.set("")
                self.office_to_delete.set("")
                self.entries_frame.destroy()
                self.entries_frame = self.render_entries()

    def delete_location(self):
        location = self.location_to_delete.get()
        if location in self.data:
            del self.data[location]
            self.location_to_delete.set("")
            self.entries_frame.destroy()
            self.entries_frame = self.render_entries()

    def render_entries(self):
        entries_frame = tk.Frame(self.main_frame, borderwidth=1)
        entries_frame.pack(fill=tk.X)
        for key in self.data:
            location_frame = tk.Frame(entries_frame)
            location_frame.pack(fill=tk.X)
            location_label = tk.Label(location_frame, text=key, font=self.font_bold)
            location_label.pack(side=tk.LEFT)
            for office in self.data[key]:
                office_frame = tk.Frame(entries_frame)
                office_frame.pack(fill=tk.X)
                office_label = tk.Label(office_frame, text=office, font=self.font_normal)
                office_label.pack(side=tk.LEFT)
        return entries_frame




root = tk.Tk()
App(root)
root.mainloop()
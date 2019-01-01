from tkinter import *
from devices import bluray, avr, projector, screen
import os
import json
import time


class HomeScreen(object):
    def __init__(self, master):
        try:
            with open(os.path.join('devices', 'rc_model_map.json')) as f:
                self.rc_dict = json.load(f)
        except Exception as e:
            print('Exception thrown {}'.format(e))

        self.rc_bluray = bluray.Bluray(self.rc_dict['bluray'])
        self.rc_avr = avr.Avr(self.rc_dict['avr'])
        self.rc_projector = projector.Projector(self.rc_dict['projector'])
        self.rc_screen = screen.Screen(self.rc_dict['screen'])

        self.master = master
        self.master.title('RaspPi Remote')

        self.topframe = Frame(master, height=35, width=400)
        self.topframe.grid_propagate(0)
        self.topframe.grid(row=0, column=0)
        self.centerframe = Frame(master)
        self.centerframe.grid(row=2, column=0)

        self.label = Label(self.topframe, text='Select device: ')

        self.label.grid(row=0, column=3)

        self.device_list = ['All', 'Bluray', 'AVR', 'Projector', 'Screen']
        self.devices = StringVar(master)
        self.devices.set(self.device_list[0])
        self.device_menu = OptionMenu(self.topframe, self.devices, *self.device_list, command=self.home_buttons)
        self.device_menu.config(font=('calibri', (10)), fg='white', bg='#FFBF00')
        self.device_menu['menu'].config(font=('calibri', (10)), fg='white', bg='#FFBF00')
        self.device_menu.grid(row=0, column=5)

        self.home_buttons(self.devices.get())

    def home_buttons(self, dev_name):
        if dev_name == 'All':
            self.clearcenter()
            self.on_button = Button(self.centerframe, text='ON', command=self.pwr_on_all, fg="green",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=5, column=3, rowspan=2)
            self.off_button = Button(self.centerframe, text='OFF', command=self.pwr_off_all, fg="red",
                                     activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.off_button.grid(row=5, column=10, rowspan=2)

        elif dev_name == 'Bluray':
            self.clearcenter()
            self.on_button = Button(self.centerframe, text='ON', command=self.rc_bluray.pwr_on, fg="green",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=2, column=1, rowspan=2)
            self.off_button = Button(self.centerframe, text='OFF', command=self.rc_bluray.pwr_off, fg="red",
                                     activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.off_button.grid(row=2, column=2, rowspan=2)
            self.on_button = Button(self.centerframe, text='Play', command=self.rc_bluray.pwr_on, fg="blue",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=8, column=1, rowspan=1)
            self.on_button = Button(self.centerframe, text='Stop', command=self.rc_bluray.pwr_on, fg="red",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=8, column=2, rowspan=1)
            self.on_button = Button(self.centerframe, text='Pause', command=self.rc_bluray.pwr_on, fg="red",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=8, column=3, rowspan=1)
            self.on_button = Button(self.centerframe, text='Eject', command=self.rc_bluray.pwr_on, fg="red",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=10, column=2, rowspan=1)

        elif dev_name == 'AVR':
            self.clearcenter()
            self.on_button = Button(self.centerframe, text='ON', command=self.rc_avr.pwr_on, fg="green",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=5, column=3, rowspan=2)
            self.off_button = Button(self.centerframe, text='OFF', command=self.rc_avr.pwr_off, fg="red",
                                     activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.off_button.grid(row=5, column=10, rowspan=2)

        elif dev_name == 'Projector':
            self.clearcenter()
            self.on_button = Button(self.centerframe, text='ON', command=self.rc_projector.pwr_on, fg="green",
                                    activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.on_button.grid(row=5, column=3, rowspan=2)
            self.off_button = Button(self.centerframe, text='OFF', command=self.rc_projector.pwr_off, fg="red",
                                     activebackground='#58ACFA', height=2, width=10, bg='#81BEF7')
            self.off_button.grid(row=5, column=10, rowspan=2)

        elif dev_name == 'Screen':
            self.clearcenter()

    def test(self):
        print("Hello")

    def clearcenter(self):
        self.centerframe.destroy()
        self.centerframe = Frame(self.master)
        self.centerframe.grid(row=2, column=0)

    def pwr_on_all(self):
        self.rc_projector.pwr_on()
        time.sleep(2)
        self.rc_bluray.pwr_on()
        time.sleep(2)
        self.rc_avr.pwr_on()
        time.sleep(2)
        self.rc_screen.down()

    def pwr_off_all(self):
        self.rc_projector.pwr_off()
        time.sleep(2)
        self.rc_bluray.pwr_off()
        time.sleep(2)
        self.rc_avr.pwr_off()
        time.sleep(2)
        self.rc_screen.up()


def start():
    root = Tk()
    root.geometry("400x310")
    my_home = HomeScreen(root)
    root.mainloop()


if __name__ == '__main__':
    start()

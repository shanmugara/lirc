from tkinter import *
from devices import bluray, avr, projector, screen
from PIL import ImageTk, Image
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

        self.image_on = ImageTk.PhotoImage(Image.open('images/power_on.png'))
        self.image_off = ImageTk.PhotoImage(Image.open('images/power_off.png'))
        self.image_play = ImageTk.PhotoImage(Image.open('images/play.png'))
        self.image_stop = ImageTk.PhotoImage(Image.open('images/stop.png'))
        self.image_pause = ImageTk.PhotoImage(Image.open('images/pause.png'))
        self.image_rewind = ImageTk.PhotoImage(Image.open('images/rewind.png'))
        self.image_ff = ImageTk.PhotoImage(Image.open('images/fast-forward.png'))
        self.image_enter = ImageTk.PhotoImage(Image.open('images/enter-key.png'))
        self.image_left = ImageTk.PhotoImage(Image.open('images/left.png'))
        self.image_right = ImageTk.PhotoImage(Image.open('images/right.png'))
        self.image_eject = ImageTk.PhotoImage(Image.open('images/eject.png'))

        self.master = master
        self.master.title('RaspPi Remote')

        self.topframe = Frame(master, height=35, width=400)
        self.topframe.grid_propagate(0)
        self.topframe.grid(row=0, column=0)
        self.centerframe = Frame(master)
        self.centerframe.grid(row=2, column=0)

        self.label_top = Label(self.topframe, text='Select device: ')
        self.label_top.grid(row=0, column=3)

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
                                    activebackground='#58ACFA', height=40, width=40, bg='#81BEF7', image=self.image_on)
            self.on_button.grid(row=1, column=1, rowspan=2, padx=(20, 20), pady=(20, 10))
            self.off_button = Button(self.centerframe, text='OFF', command=self.pwr_off_all, fg="red",
                                     activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                     image=self.image_off)
            self.off_button.grid(row=1, column=30, rowspan=2, padx=(20, 20), pady=(20, 10))
            self.label_on_all = Label(self.centerframe, text='ON ALL', fg="green")
            self.label_on_all.grid(row=5, column=1)

            self.label_off_all = Label(self.centerframe, text='OFF ALL', fg="red")
            self.label_off_all.grid(row=5, column=30)

        elif dev_name == 'Bluray':
            self.clearcenter()
            self.on_button = Button(self.centerframe, text='ON', command=self.rc_bluray.pwr_on, fg="green",
                                    activebackground='#58ACFA', height=40, width=40, bg='#81BEF7', image=self.image_on)
            self.on_button.grid(row=2, column=1, rowspan=2)
            # self.off_button = Button(self.centerframe, text='OFF', command=self.rc_bluray.pwr_off, fg="red",
            #                          activebackground='#58ACFA', height=40, width=40, bg='#81BEF7', image=self.image_off)
            # self.off_button.grid(row=2, column=2, rowspan=2)
            self.play_button = Button(self.centerframe, text='Play', command=self.rc_bluray.pwr_on, fg="blue",
                                      activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                      image=self.image_play)
            self.play_button.grid(row=8, column=1, rowspan=1)
            self.stop_button = Button(self.centerframe, text='Stop', command=self.rc_bluray.pwr_on, fg="red",
                                      activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                      image=self.image_stop)
            self.stop_button.grid(row=8, column=2, rowspan=1)
            self.pause_button = Button(self.centerframe, text='Pause', command=self.rc_bluray.pwr_on, fg="red",
                                       activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                       image=self.image_pause)
            self.pause_button.grid(row=8, column=3, rowspan=1)
            self.eject_button = Button(self.centerframe, text='Eject', command=self.rc_bluray.pwr_on, fg="red",
                                       activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                       image=self.image_eject)
            self.eject_button.grid(row=8, column=4,  rowspan=1)
            self.rewind_button = Button(self.centerframe, text='Rewind', command=self.rc_bluray.rewind, fg="red",
                                       activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                       image=self.image_rewind)
            self.rewind_button.grid(row=10, column=1, rowspan=1)
            self.ff_button = Button(self.centerframe, text='FF', command=self.rc_bluray.ff, fg="red",
                                        activebackground='#58ACFA', height=40, width=40, bg='#81BEF7',
                                        image=self.image_ff)
            self.ff_button.grid(row=10, column=2, rowspan=1)

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

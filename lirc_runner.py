from guizero import App, Combo, CheckBox, Text, TextBox, ButtonGroup, PushButton
from devices import bluray, avr, projector, screen


class Homescreen(object):
    comps_list = ['all', 'bluray', 'avr', 'projector', 'screen']

    def __init__(self):
        self.rc_bluray = bluray.Bluray('123')
        self.rc_avr = avr.Avr('123')
        self.rc_projector = projector.Projector('123')
        self.rc_screen = screen.Screen('123')

        self.app = App(title="LIRC RasPi Remote", layout="grid", width=600, height=500)
        self.blank_line = Text(self.app, text="Device", grid=[0, 0], align="bottom")

        self.device_list = Combo(self.app, options=self.comps_list, grid=[200, 0],
                                 align="left", command=self.exec_rc)

        self.disp_text = TextBox(self.app, grid=[0, 1])
        self.exec_rc(self.device_list.value)
        self.app.display()

    def exec_rc(self, device):
        self.disp_text.value = device
        if device.lower() == 'bluray':
            pass
        elif device.lower() == 'avr':
            pass
        elif device.lower() == 'projector':
            pass
        elif device.lower() == 'screen':
            pass
        elif device.lower() == 'all':
            self.pwr_all_button = PushButton(self.app, grid=[300, 6], command=self.pwr('all'))
            self.pwr_all_button.text = 'ON/OFF'
            self.app.display()

    def pwr(self, device):
        if device == 'all':
            for d in self.comps_list:
                pass
        else:
            pass

    def send_pwr(self):
        pass





def start_rc():


    homescreen = Homescreen()


def main():
    start_rc()

    # home_screen()


if __name__ == "__main__":
    main()

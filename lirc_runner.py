from guizero import App, Combo, CheckBox, Text, TextBox, ButtonGroup, PushButton
from devices import bluray, avr, projector, screen
import os
import json


class Homescreen(object):
    comps_list = ['all', 'bluray', 'avr', 'projector', 'screen']

    def __init__(self):
        try:
            with open(os.path.join('devices', 'rc_model_map.json')) as f:
                self.rc_dict = json.load(f)
        except Exception as e:
            print('Exception thrown {}'.format(e))

        self.rc_bluray = bluray.Bluray(self.rc_dict['bluray'])
        self.rc_avr = avr.Avr(self.rc_dict['avr'])
        self.rc_projector = projector.Projector(self.rc_dict['projector'])
        self.rc_screen = screen.Screen(self.rc_dict['screen'])

        self.app = App(title="LIRC RasPi Remote", layout="grid", width=600, height=500)
        self.blank_line = Text(self.app, text="Device", grid=[0, 0], align="bottom")

        self.device_list = Combo(self.app, options=self.comps_list, grid=[200, 0],
                                 align="left", command=self.home_buttons)

        self.disp_text = TextBox(self.app, grid=[0, 1])
        self.home_buttons(self.device_list.value)
        self.app.display()

    def home_buttons(self, device):
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
            self.pwr_on_all_button = PushButton(self.app, grid=[300, 6], command=self.pwr_on_all)
            self.pwr_on_all_button.text = 'ON'
            self.pwr_off_all_button = PushButton(self.app, grid=[400, 6], command=self.pwr_off_all)
            self.pwr_off_all_button.text = 'OFF'
            self.app.display()

    def pwr_on_all(self):
        self.projector_pwr_on()
        self.avr_pwr_on()
        self.bluray_pwr_on()
        self.rc_screen.down()

    def bluray_pwr_on(self):
        self.rc_bluray.pwr_on()

    def avr_pwr_on(self):
        self.rc_avr.pwr_on()

    def projector_pwr_on(self):
        self.rc_projector.pwr_on()

    def screen_pwr(self):
        pass

    def pwr_off_all(self):
        self.projector_pwr_off()
        self.avr_pwr_off()
        self.bluray_pwr_off()
        self.rc_screen.up()

    def bluray_pwr_off(self):
        self.rc_bluray.pwr_off()

    def avr_pwr_off(self):
        self.rc_avr.pwr_off()

    def projector_pwr_off(self):
        self.rc_projector.pwr_off()


def start_rc():
    homescreen = Homescreen()


def main():
    start_rc()

    # home_screen()


if __name__ == "__main__":
    main()

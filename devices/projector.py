from subprocess import check_output, DEVNULL

class Projector(object):
    def __init__(self, remotecode):
        self.remote_model = remotecode

    def pwr_on(self):
        pwr_out = check_output(['irsend', 'SEND_ONCE', self.remote_model, 'KEY_POWER'])

    def pwr_off(self):
        pwr_out = check_output(['irsend', 'SEND_ONCE', self.remote_model, 'POWER_OFF'])
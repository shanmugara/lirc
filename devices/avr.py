from subprocess import check_output, DEVNULL


class Avr(object):
    def __init__(self, remotecode):
        self.remote_model = remotecode

    def pwr(self):
        pwr_out = check_output(['lirsend', 'SEND_ONCE', self.remote_model, 'BTN_PWR'])

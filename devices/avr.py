from subprocess import check_output, DEVNULL


class Avr(object):
    def __init__(self, remotecode):
        self.remote_model = remotecode

    def pwr(self):
        pass

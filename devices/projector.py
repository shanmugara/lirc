from subprocess import check_output, DEVNULL

class Projector(object):
    def __init__(self, remotecode):
        self.remote_model = remotecode

    def pwr(self):
        pass
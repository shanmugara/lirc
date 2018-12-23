from subprocess import check_output, DEVNULL

class Screen(object):
    def __init__(self, remotecode):
        self.remote_model = remotecode

    def up(self):
        pass

    def down(self):
        pass
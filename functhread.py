import threading

# http://softwareramblings.com/2008/06/running-functions-as-threads-in-python.html
class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
        
    def run(self):
        self._target(*self._args)

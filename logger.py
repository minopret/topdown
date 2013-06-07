class Logger(object):
    EMERG = 0
    ALERT = 1
    CRIT = 2
    ERR = 3
    WARNING = 4
    NOTICE = 5
    INFO = 6
    DEBUG = 7

    def log(self, s, priority=DEBUG):
        _ = priority
        print s

    def debug(self, s):
        self.log(s, priority=Logger.DEBUG)

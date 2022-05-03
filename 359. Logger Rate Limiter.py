class Logger(object):

    def __init__(self):
        # use a dict to record
        self.last_printed_time = {
        }

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.last_printed_time or self.last_printed_time[message] + 10 <= timestamp:
            self.last_printed_time[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
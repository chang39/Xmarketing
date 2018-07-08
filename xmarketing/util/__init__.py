class Result:

  def __init__(self):
    self.code = '1'

  def fail(self):
    self.code = '1'
    return self

  def success(self):
    self.code = '0'
    return self

  def set_message(self, message):
    self.message = message
    return self

  def set_data(self, data):
    self.data = data
    return self

  def to_dict(self):
    return self.__dict__

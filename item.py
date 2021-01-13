"""
class Car:
  category = 'tesla'
  number = 3

  def update(self):
    self.number += 1


class Academy:
  category = ['Math', 'English', 'history']
  teacher = 3
  students = 30

def update(study) :
    study.students -= 10


class Room():
    status = 'clean'

    def __init__(self):
        print('new room')

    def clean(self):
        self.status = 'clean'

    def openPartry(self):
        self.status = 'not clean'

"""

class Academy() :
  category = [['math', 100], ['music', 100], ['art', 100]] 
  # category[0][1] # math class count
  teacher = 10
  students = 100

  def end_class(self, category="math", go_home=10):

    if category == "math":
      self.category[0][1] -= go_home


    elif category == "music":
      self.category[1][1] -= go_home
      
    else :
      self.category[2][1] -= go_home
    print("math", self.category)
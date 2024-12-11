class A:
  def __init__(self):
   self.x = 1

class B(A):
  def __init__(self):
    super().__init__()
    self.y = 2

  def main():
        obj_b = B()
        print(ob_b.x + obj_b.y)

  main()
            

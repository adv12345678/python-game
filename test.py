
class A(object):
    def __init__(self):
        self.num = 23


class B(A):
    def __init__(self):
        super(B,self).__init__()
        print self.num


n = B()

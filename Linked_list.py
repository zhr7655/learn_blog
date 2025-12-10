#链表的基础实现
class Link:
    def __init__(self,first,rest=None):
        if rest:
            assert isinstance(rest,Link)
        self.first = first
        self.rest = rest
        
    def __repr__(self):
        if self.rest:
            return 'Link(' + str(self.first) + ',' + self.rest.__repr__() +')'
        else:
            return 'Link(' + str(self.first) + ')'

a = Link(1,Link(2,Link(3)))


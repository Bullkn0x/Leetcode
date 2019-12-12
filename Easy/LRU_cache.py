from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.dic=OrderedDict()
        self.capacity=capacity
        """
        :type capacity: int
        """
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            v=self.dic.pop(key)
            self.dic[key] = v
            print(v)
            return v
        print('-1')
        return -1
        
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic.pop(key)
        if len(self.dic) == self.capacity:
            self.dic.popitem(last=False)
            
        self.dic[key] = value
        
        

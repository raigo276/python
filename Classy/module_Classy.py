class Classy(object):
    def __init__(self):
        self.items = []
        self.dict_classiness = {"tophat":2, "bowtie":4, "monocle":5}

    def addItem(self, fancy_item):       
        self.items.append(fancy_item)        
        
    def getClassiness(self):        
        sum = 0
        if len(self.items) == 0:
            return 0
        for i in range(0, len(self.items)):
            if self.items[i] in self.dict_classiness.keys():
                sum = sum + self.dict_classiness[self.items[i]]        
        return sum

    def show_excitement(self):
        sentence = "I am super excited for this course!"
        return ('{0} {0} {0} {0} {0}'.format(sentence))

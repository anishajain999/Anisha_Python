from collections import Counter

class Search:
    def __init__(self, para, search):
        self.para = para
        self.search = search
    def SearchString(self):
        p = self.para.split(" ")
        l = []
        print(self.para, self.search)
        for i in p:
            # print(i)
            if i.startswith(self.search):
            # print(i)
                l.append(i)
        # print(l)
        duplicate_list = Counter(l)
        # print(duplicate_list.most_common())
        lst = duplicate_list.most_common()
        # print((lst))
        for l in range(3):
            print(lst[l])
        # return lst
        
para = input("Enter Paragraph: ").lower()
search = input("Enter Search string: ").lower()

s = Search(para,search)
print(s.SearchString())
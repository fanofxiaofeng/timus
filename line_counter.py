import os

class uti:
    def __init__(self):
        pass

    def line_counter(self, name):        
        f = open(name, 'r')
        cnt = 0
        blank = 0
        comment = 0
        while True:
            line = f.readline()
            if not line:
                break
            cnt += 1
            if len(line.split()) == 0:
                blank += 1
            elif line.split()[0][0] == '#':
                comment += 1            
                
        # print "There are %d line(s) in %s" % (cnt, name)
        # print "There are %d blank line(s) in %s" % (blank, name)
        # print "There are %d comment line(s) in %s" % (comment, name)
        # print "-" * 60
        # print "There are %d ordinary line(s) in %s" % (cnt - blank - comment, name)
        return (cnt, blank, comment)
        f.close()

    def getInfo(self, folder, extension):   

        temp = os.walk(folder)
        cnt = 0
        blank = 0
        comment = 0
        for item in temp:
            for f in item[-1]:
                if os.path.splitext(f)[-1] == extension:
                    record = os.path.abspath(os.path.join(item[0], f))
                    print record
                    (temp_cnt, temp_blank, temp_comment) = self.line_counter(record)
                    print "cnt: %d, blank: %d, comment: %d" % (temp_cnt, temp_blank, temp_comment)
                    cnt += temp_cnt
                    blank += temp_blank
                    comment += temp_comment
        return (cnt, blank, comment)
                    

u = uti()
(cnt, blank, comment) = u.getInfo('.', '.py')
print "cnt: %d, blank: %d, comment: %d" % (cnt, blank, comment)

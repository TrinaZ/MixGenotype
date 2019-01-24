# _*_ coding = utf-8_*_
import re
import sys

for q in range(0,10):
    dict = {}
    read1left = []
    read1right = []
    read2left = []
    read2right = []
    dire1 = []
    dire2 = []
    start = []
    end = []
    flag = []
    mq = []
    cigar = []
    # direction = []
    i = 0


    # read the sam files
    class Variation:
        def __init__(self):
            self.AbnoramlRead = 0
            self.NormalRead = 0
            self.IncompleteRead = 0
            self.FullyRead = 0
            self.SingleRead = 0
            self.SplitRead = 0
            self.FsamRead = 0
            self.Sum4MQ = 0
            self.ReadDepth = 0.0
            self.WeightedRD = 0.0
            self.Fwrd = 0.0
            self.Vlength = 0
            self.Direction1 = 0
            self.Dir2 = 0
            self.AffectedRead = 0
            self.Result = 0

        def SetFeature(self, AbnormalRead, NormalRead, IncompleteRead, FullyRead, SingleRead, SplitRead, FsamRead,
                       Sum4MQ, ReadDepth, WeightedRD, Fwrd, Vlength, Direction1, Dir2, AffectedRead, Result):
            self.AbnormalRead = AbnormalRead
            self.NormalRead = NormalRead
            self.IncompleteRead = IncompleteRead
            self.FullyRead = FullyRead
            self.SingleRead = SingleRead
            self.SplitRead = SplitRead
            self.FsamRead = FsamRead
            self.Sum4MQ = Sum4MQ
            self.ReadDepth = ReadDepth
            self.WeightedRD = WeightedRD
            self.Fwrd = Fwrd
            self.Vlength = Vlength
            self.Direction1 = Direction1
            self.Dir2 = Dir2
            self.AffectedRead = AffectedRead
            self.Result = Result
    f = open('F:/importantfilecopy/tandomrepeat/2019.121test/3/sam10/10'+str(q)+'.sam', 'r')
    line = f.readline()
    line = f.readline()
    for line in f:
        line = line.strip().split("\t")
        flag.append(line[1])
        mq.append(line[4])
        cigar.append(line[5])
        if i % 2 != 0:
            read1left.append(line[3])
            # read1right.append(line[7])
            dire1.append(line[8])
        else:
            read2left.append(line[3])
            # read2right.append(line[7])
            dire2.append(line[8])
        i += 1

    x = 0
    VariationList = []
    type = []
    f2 = open('F:/importantfilecopy/tandomrepeat/2019.121test/3/v'+str(q)+'.txt', 'r')
    for line1 in f2:
        line1 = line1.strip().split("\t")
        start.append(line1[1])
        pos = line1[7]
        end.append(int(pos.split(";")[1].split("=")[1]))
        type.append(int(pos.split(";")[2].split("=")[1]))


    for (elem_start,elem_end) in zip(list(start),list(end)):
        fsam = 0
        spread1left = []
        spread2left = []
        f = open('F:/importantfilecopy/tandomrepeat/2019.121test/3/sam10/10'+str(q)+'.f.sam', 'r')
        line = f.readline()
        line = f.readline()
        # line = f.readline()
        for line in f:
            line = line.strip().split("\t")
            spread1left.append(line[3])
            spread2left.append(line[7])
        for (elem_spread1left, elem_spread2left) in zip(list(spread1left), list(spread2left)):
            if int(elem_start) < int(elem_end):
                if (int(elem_start) - 100) < int(elem_spread1left) < int(elem_end):
                    fsam += 1
                if (int(elem_start) - 100) < int(elem_spread2left) < int(elem_end):
                    fsam += 1
            else:
                if (int(elem_end) - 100) < int(elem_spread1left) < int(elem_start):
                    fsam += 1
                if (int(elem_end) - 100) < int(elem_spread2left) < int(elem_start):
                    fsam += 1
        # print fsam
        normal = 0
        count = 0
        for (elem_read1left,elem_read2left) in zip(list(read1left),list(read2left)):
            if(abs(int(elem_read2left)-int(elem_read1left))<455)or (abs(int(elem_read2left)-int(elem_read1left)>545)):
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100) < int(elem_read1left)<int(elem_end):
                        count += 1
                    if (int(elem_start)-100) < int(elem_read2left)<int(elem_end):
                        count += 1
                else:
                    if (int(elem_end) - 100) < int(elem_read1left) < int(elem_start):
                        count += 1
                    if (int(elem_end) - 100) < int(elem_read2left) < int(elem_start):
                        count += 1
            else:
                if (int(elem_start) < int(elem_end)):
                    if (int(elem_start)-100) < int(elem_read1left)<int(elem_end):
                        normal += 1
                    if (int(elem_start)-100) < int(elem_read2left)<int(elem_end):
                        normal += 1
                else:
                    if (int(elem_end) - 100) < int(elem_read1left) < int(elem_start):
                        normal += 1
                    if (int(elem_end) - 100) < int(elem_read2left) < int(elem_start):
                        normal += 1

        incom = 0
        incompletelymappedreads = 0
        fullymappedreads = 0
        for (elem_read1left,elem_read2left,elem_cigar) in zip(list(read1left),list(read2left),list(cigar)):
            if elem_cigar != '100M':
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100) < int(elem_read1left)<int(elem_end):
                        incompletelymappedreads += 1
                    if (int(elem_start)-100) < int(elem_read2left)<int(elem_end):
                        incompletelymappedreads += 1
                else:
                    if (int(elem_end) - 100) < int(elem_read1left) < int(elem_start):
                        incompletelymappedreads += 1
                    if (int(elem_end) - 100) < int(elem_read2left) < int(elem_start):
                        incompletelymappedreads += 1
            else:
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100) < int(elem_read1left)<int(elem_end):
                        fullymappedreads += 1
                    if (int(elem_start)-100) < int(elem_read2left)<int(elem_end):
                        fullymappedreads += 1
                else:
                    if (int(elem_end) - 100) < int(elem_read1left) < int(elem_start):
                        fullymappedreads += 1
                    if (int(elem_end) - 100) < int(elem_read2left) < int(elem_start):
                        fullymappedreads += 1
        singlemappedread = 0
        for (elem_read1left, elem_read2left) in zip(list(read1left), list(read2left)):
            if int(elem_start) < int(elem_end):
                if int(elem_start) < (int(elem_read1left) + 100) < int(elem_end) and int(elem_read2left) > int(elem_end):
                    singlemappedread += 1
                if (int(elem_read1left) + 100) < int(elem_start) and int(elem_start) < (int(elem_read2left) + 100) < int(elem_end):
                    singlemappedread += 1
            else:
                if int(elem_end) < (int(elem_read1left) + 100) < int(elem_start) and int(elem_read2left) > int(elem_start):
                    singlemappedread += 1
                if (int(elem_read2left) + 100) < int(elem_end) and int(elem_end) < (int(elem_read2left) + 100) < int(elem_start):
                    singlemappedread += 1
        splitmappedread = 0
        for (elem_read1left,elem_read2left) in zip(list(read1left),list(read2left)):
            if int(elem_start) >= int(elem_end):
                if int(elem_read1left)<int(elem_start) and (int(elem_read1left)+100)>int(elem_end):
                    splitmappedread += 1
                if int(elem_read2left)<int(elem_start) and (int(elem_read2left)+100)> int(elem_end):
                    splitmappedread += 1
        #count the map quality of the split map read
        mapq = 0
        for (elem_read1left, elem_read2left, elem_mq) in zip(list(read1left), list(read2left), list(mq)):
            if int(elem_start) < int(elem_end):
                if int(elem_start) < (int(elem_read1left) + 100) < int(elem_end) and int(elem_read2left) > int(elem_end):
                    mapq += int(elem_mq)
                if (int(elem_read1left) + 100) < int(elem_start) and int(elem_start) < (int(elem_read2left) + 100) < int(elem_end):
                    mapq += int(elem_mq)
            else:
                if int(elem_end) < (int(elem_read1left) + 100) < int(elem_start) and int(elem_read2left) > int(elem_start):
                    mapq += int(elem_mq)
                if (int(elem_read2left) + 100) < int(elem_end) and int(elem_end) < (int(elem_read2left) + 100) < int(elem_start):
                    mapq += int(elem_mq)
        #count the original readdepth
        readdepth = 0.00
        readdepth1 = 500
        dlength = abs(int(elem_end) - int(elem_start))+5
        for (elem_read1left,elem_read2left) in zip(list(read1left),list(read2left)):
            if int(elem_start) < int(elem_end):
                if (int(elem_start) - 100) < int(elem_read1left) < int(elem_end):
                    readdepth1 += 1
                if (int(elem_start) - 100) < int(elem_read2left) < int(elem_end):
                    readdepth1 += 1
            else:
                if (int(elem_end) - 100) < int(elem_read1left) < int(elem_start):
                    readdepth1 += 1
                if (int(elem_end) - 100) < int(elem_read2left) < int(elem_start):
                    readdepth1 += 1
            readdepth = float(readdepth1*200 / dlength)+5
        #count the weighted readdepth
        wrdepth = 0
        wrdepth = mapq*readdepth1/(100*dlength)
        # print wrdepth
        fwrdepth = 0
        readdepth2 = 0
        for (elem_read1left,elem_read2left,elem_mq) in zip(list(read1left),list(read2left),list(mq)):
            if int(elem_start) < int(elem_end):
                if (int(elem_start) - 200) < int(elem_read1left) < int(elem_end):
                    readdepth2 += 1
                    mapq += int(elem_mq)
                if (int(elem_start) - 200) < int(elem_read2left) < int(elem_end):
                    readdepth2 += 1
                    mapq += int(elem_mq)
            else:
                if (int(elem_end) - 200) < int(elem_read1left) < int(elem_start):
                    readdepth2 += 1
                    mapq += int(elem_mq)
                if (int(elem_end) - 200) < int(elem_read2left) < int(elem_start):
                    readdepth2 += 1
                    mapq += int(elem_mq)
            fwrdepth = float(readdepth2*mapq/(1000*dlength))
        affectedread = 0
        for (elem_read1left,elem_read2left) in zip(list(read1left),list(read2left)):
            if int(elem_start) - int(dlength/10) < int(elem_read1left) and int(elem_read2left) < (int(elem_end)+int(dlength/10)):
                affectedread += 1
        direction2 = 0
        direction1 = 0
        for (elem_read1left, elem_read2left,elem_flag) in zip(list(read1left), list(read2left),list(flag)):
            if int(elem_flag) == 83:
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100)<int(elem_read1left)< int(elem_end):
                        direction1 += 1
                    if int(elem_start) < int(elem_read2left) < (int(elem_end)+100):
                        direction1 += 1
                else:
                    if (int(elem_end)-100) < int(elem_read1left)  < int(elem_start):
                        direction1 += 1
                    if int(elem_end) < int(elem_read2left)< (int(elem_start)+100):
                        direction1 += 1
            if int(elem_flag) == 163:
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100) < int(elem_read1left) < int(elem_end):
                        direction1 += 1
                    if int(elem_start) < int(elem_read2left) < (int(elem_end)+ 100):
                        direction1 += 1
                else:
                    if (int(elem_end)-100) < int(elem_read1left)  < int(elem_start):
                        direction1 += 1
                    if int(elem_end) < int(elem_read2left)  < (int(elem_start)+ 100):
                        direction1 += 1
            else:
                if int(elem_start) < int(elem_end):
                    if (int(elem_start)-100) < int(elem_read1left) < int(elem_end):
                        direction2 += 1
                    if int(elem_start) < int(elem_read2left)  < (int(elem_end)+ 100):
                        direction2 += 1
                else:
                    if int(elem_end) < int(elem_read1left)  < int(elem_start):
                        direction2 += 1
                    if int(elem_end) < (int(elem_read2left) + 100) < int(elem_start):
                        direction2 += 1
        print direction1
        VariationList.append(Variation())
        VariationList[-1].SetFeature(count, normal, incompletelymappedreads, fullymappedreads, singlemappedread, splitmappedread, fsam, mapq, readdepth, wrdepth, fwrdepth, dlength, direction1, direction2, affectedread, type[x])
        # print VariationList[-1].Result
        x = x + 1

    fout = open("F:/importantfilecopy/tandomrepeat/2019.121test/thtenresults", "a")
    for variation in VariationList:
        fout.write(str(variation.AbnormalRead) + " " + str(variation.NormalRead) + " " + str(variation.IncompleteRead) + " " + str(variation.FullyRead)+ " " + str(variation.SingleRead) + " " + str(variation.SplitRead) + " " + str(variation.FsamRead) + " " + str(variation.Sum4MQ) + " " +str(variation.ReadDepth) + " " + str(variation.WeightedRD) +  " " +str(variation.Fwrd)+" "+ str(variation.Vlength) + " "  + str(variation.Direction1) + " " +str(variation.Dir2)+" "+ str(variation.AffectedRead) + "\t" + str(variation.Result) + "\n")
    q += 1


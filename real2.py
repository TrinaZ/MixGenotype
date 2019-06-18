# _*_ coding = utf-8_*_
import re
import sys

for q in range(0,1):
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
    chrom = []
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
    f1 = open('F:/realdatagene+/out/9/9.sam', 'r')
    for x in range(0, 99):
        line = f1.readline()
    for line in f1:
        line = line.strip().split("\t")
        chrom.append(line[2])
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
    ch = []
    ch2 = []
    f2 = open('F:/realdatagene+/out/9/91.txt', 'r')
    for line1 in f2:
        line1 = line1.strip().split("\t")
        ch.append(line1[0])
        start.append(line1[1])
        ch2.append(line1[2])
        end.append(line1[3])
        type.append(line1[4])

    for (elem_start,elem_end,elem_ch) in zip(list(start),list(end),list(ch)):
        fsam = 0
        incom = 0
        incompletelymappedreads = 0
        fullymappedreads = 0
        mapq = 0
        readdepth = 0.00
        readdepth1 = 500
        dlength = abs(float(elem_end) - float(elem_start)) + 5
        wrdepth = 0
        fwrdepth = 0
        readdepth2 = 0
        mapq2 = 0
        direction2 = 0
        direction1 = 0
        normal = 0
        count = 0
        for (elem_read1left, elem_read2left,elem_chrom,elem_cigar,elem_mq,elem_flag) in zip(list(read1left), list(read2left),list(chrom),list(cigar),list(mq),list(flag)):
            if str(elem_ch) == str(elem_chrom):
                if (int(elem_start) - 100) < int(elem_read1left) < int(elem_end) and (int(elem_start)-100)<int(elem_read2left)< int(elem_end):
                    readdepth1 += 1
                    mapq += int(elem_mq)
                    if str(elem_cigar) != '100M':
                        fsam += 1
                        incompletelymappedreads += 1
                    if str(elem_cigar) == '100M':
                        fullymappedreads += 1
                    if (abs(int(elem_read2left) - int(elem_read1left)) < 455) or (abs(int(elem_read2left) - int(elem_read1left) > 545)):
                        count += 1
                    if int(elem_flag) == 83:
                        direction1 += 1
                    if int(elem_flag) == 163:
                        direction1 += 1
                    else:
                        direction2 += 1
                readdepth = float(readdepth1 * 200 / dlength) + 5
                wrdepth = mapq * readdepth1 / (100 * dlength)
                if (int(elem_start) - 200) < int(elem_read1left) < int(elem_end):
                    readdepth2 += 1
                    mapq2 += int(elem_mq)
                if (int(elem_start) - 200) < int(elem_read2left) < int(elem_end):
                    readdepth2 += 1
                    mapq2 += int(elem_mq)
                fwrdepth = float(readdepth2 * mapq2 / (1000 * dlength))
                singlemappedread = 0
                splitmappedread = 0
                if int(elem_start) < (int(elem_read1left) + 100) < int(elem_end) and int(elem_read2left) > int(elem_end):
                    singlemappedread += 1
                if (int(elem_read1left) + 100) < int(elem_start) and int(elem_start) < (int(elem_read2left) + 100) < int(elem_end):
                    singlemappedread += 1
                if int(elem_read1left)<int(elem_start) and (int(elem_read1left)+100)>int(elem_end):
                    splitmappedread += 1
                if int(elem_read2left)<int(elem_start) and (int(elem_read2left)+100)> int(elem_end):
                    splitmappedread += 1
                affectedread = 0
                if int(elem_start) - int(dlength/10) < int(elem_read1left) and int(elem_read2left) < (int(elem_end)+int(dlength/10)):
                    affectedread += 1
        print direction1
        VariationList.append(Variation())
        VariationList[-1].SetFeature(count, normal, incompletelymappedreads, fullymappedreads, singlemappedread, splitmappedread, fsam, mapq, readdepth, wrdepth, fwrdepth, dlength, direction1, direction2, affectedread, type[x])
        # print VariationList[-1].Result
        x = x + 1

    fout = open("F:/realdatagene+/out/9/results", "a")
    for variation in VariationList:
        fout.write(str(variation.AbnormalRead) + " " + str(variation.NormalRead) + " " + str(variation.IncompleteRead) + " " + str(variation.FullyRead)+ " " + str(variation.SingleRead) + " " + str(variation.SplitRead) + " " + str(variation.FsamRead) + " " + str(variation.Sum4MQ) + " " +str(variation.ReadDepth) + " " + str(variation.WeightedRD) +  " " +str(variation.Fwrd)+" "+ str(variation.Vlength) + " "  + str(variation.Direction1) + " " +str(variation.Dir2)+" "+ str(variation.AffectedRead) + "\t" + str(variation.Result) + "\n")
    q += 1


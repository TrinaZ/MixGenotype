# _*_ coding = utf-8_*_
import re
import sys
for q in range(0,10):
    position = []
    length = []
    allletter = []
    num = []
    chr = []
    dict = {}
    y = 0
    class Variation:
        def __init__(self):
            self.Number = 0
            self.start = 0
            self.vdefine = 0
            self.hap = 0
            self.time = 0
            self.zero = 0
            self.letter = 0
        def SetFeature(self, Number, start, vdefine, hap, time, zero, letter):
            self.Number = Number
            self.start = start
            self.vdefine = vdefine
            self.hap = hap
            self.time = time
            self.zero = zero
            self.letter = letter
    VariationList = []
    x = 0
    f = open('F:/importantfilecopy/tandomrepeat/2019.121test/s'+str(q)+'.txt', 'r')
    for line in f:
        line = line.strip().split("\t")
        num.append(line[0])
        position.append(line[1])
        length.append(line[2])
        chr.append(line[6])
    allletter = []
    i = 0
    number = 100
    st = 0
    vd = 0
    ha = 0
    ti = 0
    ze = 0

    for (elem_num, elem_position,elem_length,elem_chr) in zip(list(num), list(position),list(length),list(chr)):
        if int(elem_num) < 40:
            number += 1
            st = int(elem_position)
            vd = int(elem_length)
            ha = 1
            ti = 5
            ze = 1
            le = elem_chr
            # a = int(elem_position) / 50
            # b = int(elem_length)/50 + int(elem_position) / 50
            # ref = open('F:/importantfilecopy/tandomrepeat/chr19_100w.fa', 'r')
            # line1 = ref.readline()
            # for line1 in ref:
            #     i += 1
            #     if (a-10) < i <a:
            #         le += line1.strip('\n')
            #         # print le
            #     if b < i < (b+10):
            #         le += line1.strip('\n')
            VariationList.append(Variation())
            VariationList[-1].SetFeature(number, st, vd, ha, ti, ze, le.strip('\n'))
            x = x + 1
        if int(elem_num) < 40:
            number += 1
            st = int(elem_position) - 500
            vd = abs(int(elem_length))+1000
            ha = 1
            ti = 5
            ze = 0
            ref = open('F:/importantfilecopy/tandomrepeat/chr19_100w.fa', 'r')
            line1 = ref.readline()
            i = 0
            le = ''
            a = int(elem_position) / 50
            for line1 in ref:
                i += 1
                if (a-10) < i < a:
                    le += line1.strip('\n')
                    print le
                if int(elem_position)/50 < i < ((int(elem_position) + abs(int(elem_length))) / 50 + 10):
                    le += line1.strip('\n')
                # print le
            VariationList.append(Variation())
            VariationList[-1].SetFeature(number, st, vd, ha, ti, ze, le.strip('\n'))
            x = x + 1
        elif int(elem_num) < 100:
            number += 1
            st = int(elem_position) - 490
            vd = abs(int(elem_length)) + 1000
            ha = 1
            ti = 5
            ze = 0
            ref = open('F:/importantfilecopy/tandomrepeat/chr19_100w.fa', 'r')
            line1 = ref.readline()
            i = 0
            le = ''
            a = int(elem_position) / 50
            for line1 in ref:
                i += 1
                if (a - 10) < i < a:
                    le += line1.strip('\n')
                if (int(elem_position) + abs(int(elem_length))) / 50 < i < ((int(elem_position) + abs(int(elem_length))) / 50 + 10):
                    le += line1.strip('\n')
                    # print le
            VariationList.append(Variation())
            VariationList[-1].SetFeature(number, st, vd, ha, ti, ze, le.strip('\n'))
            x = x + 1
    fout = open("F:/importantfilecopy/tandomrepeat/2019.121test/s"+str(q)+".txt", "a")
    for variation in VariationList:
        fout.write(str(variation.Number) + "\t" + str(variation.start) + "\t"+ str(variation.vdefine) + "\t" +str(variation.hap)+"\t"+str(variation.time) + "\t" + str(variation.zero) + "\t" + str(variation.letter) + "\n")
    q += 1

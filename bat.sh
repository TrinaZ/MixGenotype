#! /bin/bash
ref=chr19_100w.fa
table=s0.txt
./norsim  -r 0 -X 0 -D 0 -B 0  -I $table $ref n0.sim
./readgen -d 500 -s50 -c 5 -I n0.sim.idx $ref n0.sim l.fq r.fq
../bwa-0.7.5a/bwa index -a bwtsw $ref

../bwa-0.7.5a/bwa aln $ref l.fq>l.sai
../bwa-0.7.5a/bwa aln $ref r.fq>r.sai
../bwa-0.7.5a/bwa sampe -f 5.sam $ref l.sai r.sai l.fq r.fq


./samtools view -bS 5.sam > t3.bam
./samtools view -bf 4 t3.bam > t3.f.bam
./samtools view -h t3.f.bam > 5.f.sam



import os
import sys

gff_in = sys.argv[1]

gene_line_list = list()
gff_line_list = list()

with open(gff_in, 'r') as f:

    count = 0

    for line in f:
        line_list = line.split('\t')
        gff_line_list.append(line_list)
        count += 1

        if line_list[2] == 'gene':
            gene_line_list.append(count)

    count = 0

    for i in range(len(gene_line_list) - 1):

        tmp_gff = ''

        for cds in gff_line_list[int(gene_line_list[i]) + 1 : int(gene_line_list[i+1]) - 1]:
            tmp_gff += '\t'.join(cds)

        with open('tmp/busco_gene_' + str(count) + '.gff', 'w') as f:
            f.write(tmp_gff)

        count += 1
    
    tmp_gff = ''

    for cds in gff_line_list[int(gene_line_list[len(gene_line_list) - 1]) + 1 :]:
        tmp_gff += '\t'.join(cds)

    with open('tmp/busco_gene_' + str(len(gene_line_list) - 1) + '.gff', 'w') as f:
        f.write(tmp_gff)
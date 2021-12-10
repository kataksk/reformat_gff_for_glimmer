import os
import sys

gff_in = sys.argv[1]

gene_line_list = list()
gff_line_list = list()

with open(gff_in, 'r') as f:

    line_count = 0

    for line in f:
        line_list = line.split('\t')
        gff_line_list.append(line_list)
        line_count += 1

        if line_list[2] == 'gene':
            gene_line_list.append(line_count)

    # print(gene_line_list)
    # print(len(gene_line_list))
    # for i in range(len(gene_line_list) - 1):
    #     print(i)
    
    count = 0

    # print(gff_line_list[int(gene_line_list[0]) - 1 : int(gene_line_list[1]) - 1])
    # print(gff_line_list[int(gene_line_list[940]) - 1 : int(gene_line_list[941]) - 1])
    # print(gff_line_list[int(gene_line_list[941]) - 1 : int(gene_line_list[942]) - 1])

    for i in range(len(gene_line_list) - 1):

        tmp_gff = ''

        for cds in gff_line_list[int(gene_line_list[i]) - 1 : int(gene_line_list[i+1]) - 1]:
            tmp_gff += '\t'.join(cds)

        with open('tmp/busco_gene_' + str(count) + '.gff', 'w') as f:
            f.write(tmp_gff)

        count += 1
    
    tmp_gff = ''

    # print(len(gene_line_list))
    # 942
    # print(gene_line_list[941])
    # 22148
    # print(gff_line_list[22148 - 1])
    # ['scaffold_1146', 'AUGUSTUS', 'gene', '24711', '25194', '0.01', '+', '.', 'ID=169220at6656\n']

    for cds in gff_line_list[gene_line_list[len(gene_line_list) - 1] - 1:]:
        tmp_gff += '\t'.join(cds)
    # print(tmp_gff)

    with open('tmp/busco_gene_' + str(len(gene_line_list) - 1) + '.gff', 'w') as f:
        f.write(tmp_gff)
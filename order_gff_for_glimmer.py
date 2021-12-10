import glob
import sys

gff_in = sys.argv[1]
tmp_gff_file_name = [gff_in]
# tmp_gff_file_name = glob.glob('./tmp/*')

# Version 2021_12_07
# for tmp_gff_file in tmp_gff_file_name:
#     with open(tmp_gff_file, 'r') as f:
#         tmp_list = list()
#         for line in f:
#             line_list = line.split('\t')
#             if line_list[6] == '+':
#                 print(line_list[0] + '\t' + line_list[3] + '\t' + line_list[4])
#             elif line_list[6] == '-':
#                 tmp_list.append([line_list[0], line_list[3], line_list[4]])
#         if len(tmp_list) > 0:
#             tmp_list.reverse()
#             for tmp_list_line in tmp_list:
#                 print(tmp_list_line[0], tmp_list_line[2], tmp_list_line[1])
#         print()        

# Version 2021_12_10
for tmp_gff_file in tmp_gff_file_name:
    with open(tmp_gff_file, 'r') as f:
        tmp_list = list()
        for line in f:
            line_list = line.split('\t')
            if line_list[2] == 'CDS':
                if line_list[6] == '+':
                    print(line_list[0] + '\t' + line_list[3] + '\t' + line_list[4])
                elif line_list[6] == '-':
                    tmp_list.append([line_list[0], line_list[3], line_list[4]])
        if len(tmp_list) > 0:
            tmp_list.reverse()
            for tmp_list_line in tmp_list:
                print(tmp_list_line[0], tmp_list_line[2], tmp_list_line[1])
        print()     
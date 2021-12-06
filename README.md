> USAGE
```
reformat_gff_for_glimmer.sh <gff_ordered>  
```

`glimmer_in.txt` will be created in the current directory.  

> EXAMPLE
```
reformat_gff_for_glimmer.sh /work2/kataoka/gene_prediction_azami/busco_complete_v2_test_ordered.gff > glimmer_in.txt
```


`busco_complete_v2_test_ordered.gff` looks like:  
```
scaffold_1      AUGUSTUS        gene    1130631 1143471 0.01    +       .       ID=131276at6656  
scaffold_1      AUGUSTUS        mRNA    1130631 1143471 0.01    +       .       ID=131276at6656;Parent=131276at6656  
scaffold_1      AUGUSTUS        CDS     1135166 1136518 0.31    +       0       ID=cds.131276at6656;Parent=131276at6656  
scaffold_1      AUGUSTUS        gene    1282808 1313552 0.01    -       .       ID=81413at6656  
scaffold_1      AUGUSTUS        mRNA    1282808 1313552 0.01    -       .       ID=81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1282909 1283108 0.01    -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1287101 1287334 0.04    -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1292813 1293056 0.02    -       0       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1293780 1293835 0.01    -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1298695 1298716 0.01    -       0       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1299300 1299310 0.01    -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1303290 1303536 0.01    -       0       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1307844 1308061 0.6     -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1309738 1310124 0.81    -       2       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        CDS     1313197 1313293 0.27    -       0       ID=cds.81413at6656;Parent=81413at6656  
scaffold_1      AUGUSTUS        gene    1558768 1612634 0.01    -       .       ID=69897at6656  
scaffold_1      AUGUSTUS        mRNA    1558768 1612634 0.01    -       .       ID=69897at6656;Parent=69897at6656  
scaffold_1      AUGUSTUS        CDS     1558768 1558922 0.01    -       2       ID=cds.69897at6656;Parent=69897at6656  
scaffold_1      AUGUSTUS        CDS     1559214 1559226 0.01    -       0       ID=cds.69897at6656;Parent=69897at6656  
scaffold_1      AUGUSTUS        CDS     1563590 1563605 0.01    -       1       ID=cds.69897at6656;Parent=69897at6656  
...  
```

`glimmer_in.txt` looks like:  
```
scaffold_1      1135166 1136518  
  
scaffold_1 1313293 1313197  
scaffold_1 1310124 1309738  
scaffold_1 1308061 1307844  
scaffold_1 1303536 1303290  
scaffold_1 1299310 1299300  
scaffold_1 1298716 1298695  
scaffold_1 1293835 1293780  
scaffold_1 1293056 1292813  
scaffold_1 1287334 1287101  
scaffold_1 1283108 1282909  
  
scaffold_1 1612634 1612594  
scaffold_1 1609471 1609366  
scaffold_1 1609212 1609102  
scaffold_1 1604178 1603921  
...  
```



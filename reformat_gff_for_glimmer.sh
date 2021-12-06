GFF_PATH=$1
TOOLS_DIR=$(cd $(dirname $0);pwd)
CUR_DIR=$(pwd)

mkdir $TOOLS_DIR/tmp
python $TOOLS_DIR/split_gff.py $1
python $TOOLS_DIR/order_gff_for_glimmer.py > $CUR_DIR/glimmer_in.txt
rm -rf tmp
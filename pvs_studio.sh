#!/bin/bash

echo $1
path_name=$1
mkdir /home/huong/projects/VDCT/tmpData/CCPP/pvsstudio/$path_name

make clean
make


for NAME in `find . -name "*.c"`
do
	echo ${NAME%.c}
	pvs-studio --cfg PVS-Studio.cfg --source-file $NAME --i-file ${NAME%.c}.o.PVS-Studio.i --output-file $NAME.log
	plog-converter -a 'GA:1,2' -t json  $NAME.log -o /home/huong/projects/VDCT/tmpData/CCPP/pvsstudio/$path_name/$NAME.json
done

for NAME in `find . -name "*.cpp"`
do
	echo ${NAME%.c}
	pvs-studio --cfg PVS-Studio.cfg --source-file $NAME --i-file ${NAME%.cpp}.o.PVS-Studio.i --output-file $NAME.log
	plog-converter -a 'GA:1,2' -t json  $NAME.log -o /home/huong/projects/VDCT/tmpData/CCPP/pvsstudio/$path_name/$NAME.json
done

rm *.o *.i *.log
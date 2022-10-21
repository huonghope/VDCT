https://github.com/devandi/AnalyzeTool

# Infer
## simple
infer run  -j 1 -- gcc -c CWE15_External_Control_of_System_or_Configuration_Setting__w32_01.c
-j: Run the specified number of analysis jobs simultaneousl

## make with change directory
infer run -o  ./result -j 1 -- make   --directory=./CWE404_Improper_Resource_Shutdown 


# Clang
gcc *.o -o test -lpthread
clang++ -cc1 -analyze -analyzer-checker=alpha -output-file=c_w_temp.xml

clang++ CWE252_Unchecked_Return_Value__char_fgets_01.c
clang -I ../../src/testcasesupport ../../src/testcasesupport/std_thread.c CWE252_Unchecked_Return_Value__char_fgets_01.c
clang++ -cc1 -analyze -analyzer-checker=core,alpha  -I ./1v3/juliet_suite-c-cplus/src/testcasesupport -I /usr/include -I /usr/include/x86_64-linux-gnu/ -I /usr/lib/clang/15/include ./1v3/juliet_suite-c-cplus/testcases/CWE366_Race_Condition_Within_Thread/CWE366_Race_Condition_Within_Thread__global_int_01.c

rm -rf io.c main_linux.cpp main.cpp std_testcase_io.h std_testcase.h std_thread.c std_thread.h testcases.h


o.o std_thread.o -o 
../../build/CWE366
scan-build: Removing directory '/tmp/scan-build-2022-09-22-133127-583164-1' because it contains no reports.


# clang++
clang -Wno-unused-command-line-argument  -I../../src/testcasesupport  --analyze -analyzer-checker=alpha CWE*.cpp
clang -Wno-unused-command-line-argument  -I../../src/testcasesupport  --analyze -Xanalyzer -analyzer-checker=alpha,core CWE*.cpp

clang++ -std=c++11 -stdlib=libc++ main.cpp -Weverything -Reverything --analyze -Xanalyzer -analyzer-output=text -Xanalyzer -analyzer-checker=alpha.cplusplus
clang++ -Wno-unused-command-line-argument  -I../../src/testcasesupport -std=c++11 -stdlib=libc++ CWE*.cpp -Weverything -Reverything --analyze -Xanalyzer -analyzer-output=text -Xanalyzer -analyzer-checker=alpha.cplusplus

# frame

opam install depext
opam depext frama-c
opam install frama-c
eval $(opam env)
frama-c -eva -eva-precision 1 ./main_linux.cpp -cpp-extra-args=-I../../src/testcasesupport/

why3 config detect
/home/huong/projects/VDCT/tmpData/CCPP/infer/infer_CWE773_Missing_Reference_to_Active_File_Descriptor_or_Handle
/home/huong/projects/VDCT/tmpData/CCPP/infer/infer_CWE195_Signed_to_Unsigned_Conversion_Error/report.json
/home/huong/projects/VDCT/tmpData/CCPP/infer/infer_CWE476_NULL_Pointer_Dereference/report.json


-Wno-unused-command-line-argument
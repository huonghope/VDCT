# import dirutils
# import os
# import sys


# class FlawfinderScanner(object):
# 	def __init__(self, config):
# 		self.config = config

# 	# read the existing flaw file in the memory for further use
# 	def run(self, dir, dirName, scanner):
# 	  os.chdir(dir)
# 	  path_file_csv = scanner.getOutFileCsv().replace("#filename", dirName)
# 	  temp_path = 'a'
#     dirutils.file_line_error_header(path_file_csv)
#     # py_common.run_commands([sc.getCmdString(dir, dirName)], True)
#     cmd = sc.getCmdString(dir,dirName)
#     (output, err, exit, time) = dirutils.system_call(cmd, ".") 
#     dirutils.tool_exec_log(temp_path, cmd, output, err, exit)

#     all_lines = output.splitlines()
#     lines = []
#     line_codes = []
#     collect_flag = False
#     for line in all_lines:
#         dec = line.decode("utf-8").strip()
#         if (collect_flag):
#             lines.append(dec)
#             if (len(dec.split(":")) >= 3):
#                 line_codes.append(True)
#             else:
#                 line_codes.append(False)
#         if dec == "FINAL RESULTS:":
#             collect_flag = True
#         if dec == "ANALYSIS SUMMARY:":
#             break

#     sys.stdout = open(path_file_csv, "a")
#     for i in range(0,len(lines)):
#         if (line_codes[i]):
#             a = lines[i].split(":")
#             filename = os.path.basename(a[0])
#             line_no = a[1]
#             error_message = ""
#             j = 2
#             while (j < len(a)):
#                 error_message = error_message + ":" + a[j]
#                 j = j + 1
#             j = i + 1
#             while (j < len(lines)):
#                 if (not line_codes[j]):
#                     error_message += error_message + " " + lines[j].strip()
#                     j = j + 1
#                 else:
#                     break;
#             print(filename, ",", line_no, ",", "\"" + error_message + "\"")
#     sys.stdout = sys.__stdout__ 

    
# if __name__ == '__main__':
#   print("flawfinder Scanner")


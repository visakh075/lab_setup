#!/usr/bin/python
import os
from tokenize import Ignore
paths=os.listdir(".")
projects=[]
libs=[]
lab_lib=os.getcwd()+'/lab_libs'
for element in paths:
	project_path=os.getcwd()+'/'+element
	lib_path=project_path+'/lib'
	obj_path=project_path+'/obj'
	if(os.path.isdir(project_path)):
		# Add to projects
		projects.append(element)
		# Check for lib path
		if(os.path.isdir(lib_path)):
			lib_files=os.listdir(lib_path)
			# check files in the libpath *.c *.cpp *.h
			# ignore this if we have exclusive_lib file
			ignore_list=[]
			ignore_all=False

			if "ignore_all" in lib_files:
				ignore_all=True
				pass
			elif "ignore" in lib_files:
				#print("ignore found in project "+element)
				ignore_file=open(lib_path+"/ignore","r")
				ignore_list=ignore_file.read().splitlines()
				#print(ignore_list)
			
			if(ignore_all==False):
				for lib_file in lib_files:
					if(lib_file.endswith((".c",".cpp",".h"))):
						# add files to lib list
						if(lib_file in ignore_list):
							pass
						else :
							libs.append(lib_path+'/'+lib_file)
# if(os.path.isdir(lab_lib)==False):
# 	os.mkdir(lab_lib)
# return results for bash
for lib in libs:
	print(lib)

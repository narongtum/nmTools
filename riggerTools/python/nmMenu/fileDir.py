import os.path

path = os.path.dirname(os.path.abspath(__file__))
#tmp_path = 'D:\True_Axion\Tools\riggerTools\python\axionMenu'
#newPath = tmp_path.replace(os.sep, '/')
abs_path = os.path.normpath(path)


cut_path = abs_path.replace(r'\python\axionMenu','')
# D:\True_Axion\Tools\riggerTools
print(cut_path)

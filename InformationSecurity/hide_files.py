import ctypes

atrib_hide = 0x02
return_ = ctypes.windll.kernel32.SetFileAttributesW('hide.txt', atrib_hide)

if return_:
   print("file hidden") 
else:
   print("file not hidden") 





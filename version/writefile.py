from datetime import datetime #For answer recording

def write():
  now = datetime.now()
  ho = now.hour
  mi = now.minute
  da = now.day
  mo = now.month
  ye = now.year
  ho = str(ho)
  mi = str(mi)
  da = str(da)
  mo = str(mo)
  ye = str(ye)
  file_handle = open ("record.txt", "a")
  file_handle.write(check)
  file_handle.write(" | ")
  file_handle.write("at ")
  file_handle.write(ho)
  file_handle.write(":")
  file_handle.write(mi)
  file_handle.write(" on ")
  file_handle.write(da)
  file_handle.write("-")
  file_handle.write(mo)
  file_handle.write("-")
  file_handle.write(ye)
  file_handle.write("\n")
  file_handle.close

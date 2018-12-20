#
# * Program: Magic Uneraser v4.1
# * Release: Simple Keygen
# * Created with: Python 3.7.x
#

import hashlib

def generateSerial(name, edition):
  Charset = "5D303E88-0377-4C59-B576-934E71E7F644"
  editions = ["Home", "Office", "Commercial"]
  S = ""
  j = ""
  d = 3
  S = hashlib.md5((name + "Magic Uneraser" + editions[edition] + " Edition" + Charset).upper().encode('utf-8')).hexdigest().upper()
  for i in range(0,16):
    k = ord(S[i]) % 10
    j+=str(k)
    if(len(j)==19):
      break
    if(d==i):
      j+="-"
      d+=4
  return j

name = input("Enter your name: ")
if(name==""):
  print("-> Name can't be empty!")
else:
  splash = """
+-----+---------------------+
| Id  |      Editions       |
+-----+---------------------+
|  1  | Home Edition        |
|  2  | Office Edition      |
|  3  | Commercial Edition  |
+-----+---------------------+
"""
  print(splash)
  edition_id = input("Enter id of the edition to generate key: ")
  if(not edition_id.isdigit()):
    print("-> Enter only numbers.")
  elif(int(edition_id)<=0 or int(edition_id)>3):
    print("-> Enter only id numbers from the list.")
  else:
    print("Registration name: " + name)
    print("Registration key: " + generateSerial(name, int(edition_id)-1))
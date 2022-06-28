
txt = []
with open("test.txt") as infile:
  for line in inline:
    for i in line:
      txt.append(i)
dict = {
'A' : 'Q',
'B' : 'D',
'C' : 'Z',
'D' : 'X',
'E' : 'V',
'F' : 'H',
'G' : 'B',
'H' : 'G',
'I' : 'A',
'J' : 'S',
'K' : 'F',
'L' : 'O',
'M' : 'J',
'N' : 'K',
'0' : 'T',
'P' : 'I',
'Q' : 'P',
'R' : 'W',
'S' : 'N',
'T' : 'R',
'U' : 'E',
'V' : 'L',
'W' : 'C',
'X' : 'U',
'Y' : 'Y',
'Z' : 'M',
}
for i in txt:
  if i in dict.keys():
    print("\033[01;31m%s\033[0m" % dict[i], end = '')
  else:
    print(i, end = '')

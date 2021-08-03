def lol2(date):
  if (int(date[2:4]))%4 == 0 and (int(date[:4]))%400 == 0 :
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
  else:
    mon = [31,28,31,30,31,30,31,31,30,31,30,31]

  fin = 0
  u = int(date[8:10])
  k = int(date[5:7])
  fin += u
  fin += sum(mon[:k-1])
  return fin
  

print(lol2("2019-11-25"))  # what day of the year is this




def lol4(ghosts,target):
  x = abs(target[0])+ abs(target[1])
  y = 0
  for i in range(0,len(ghosts)):
    for j in ghosts[i]:
      if j == ghosts[i][0]:
        y += abs(target[0] - j)
      if j == ghosts[i][1]:
        y += abs(target[1] - j)

    if y <= x :
      return False
      break
    else:
      y = 0
  return True
  
  
print(lol4([[2,3],[7,2],[3,5],[2,5]],[-7,-5]))




def lol4(num):
  x = ""
  while num >= 1000 :
    num -= 1000
    x += "M"
  if num >= 900 and num <= 999 :
    num -= 900
    x += "CM"
  while num >= 500 :
    num -= 500
    x += "D"
  if num >= 400 and num <= 499 :
    num -= 400
    x += "CD"
  while num >= 100 :
    num -= 100
    x += "C"
  if num >= 90 and num <= 99 :
    num -= 90
    x += "XC"
  while num >= 50 :
    num -= 50
    x += "L"
  if num >= 40 and num <= 49 :
    num -= 40
    x += "XL"
  while num >= 10 :
    num -= 10
    x += "X"
  if num == 9 :
    num -= 9
    x += "IX"
  while num >= 5 :
    num -= 5 
    x += "V"
  if num == 4 :
    num -= 4
    x += "IV"
  while num >= 1 :
    num -= 1
    x += "I"

  return x
  
print(lol4(17))     # number to roman numerals




def lol(num):
    y = 0
    M = num.count("M")
    y += 1000*M
    CM = num.count("CM")
    if CM >= 1: 
        y -= 200
    D = num.count("D")
    y += 500*D
    CD = num.count("CD")
    if CD >= 1:
        y -= 200 
    C = num.count("C")
    y += 100*C
    XC = num.count("XC")
    if XC >= 1:
        y -= 20
    L = num.count("L")
    y += 50*L
    XL = num.count("XL")
    if XL >= 1:
        y -= 20
    X = num.count("X")
    y += 10*X
    IX = num.count("IX")
    if IX >= 1:
        y -= 2
    V = num.count("V")
    y += 5*V
    IV = num.count("IV")
    if IV >= 1:
        y -= 2
    I = num.count("I")
    y += 1*I
    return y


print(lol("MCMXCIV"))    # roman numerals to numbers




def lol(num):
    if num == 0 :
      return "Zero"
    g = ["","ten", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    w = ["","one", "two", "three", "four", "five","six", "seven", "eight", "nine",]
    s = ["ten ","eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    y = str(num)
    z = len(y)
    v = ""
    h = 0
    dc = 0
    jk = 0
    dc1 = 0
    jk1 = 0


    for x in range(z-1,-1,-1):
        while x == 9:
            if int(y[0]) == 1:
                v += "one"
                v += " billion "
            else :
                v += "two"
                v += " billion "
            y= y[1:z]
            break
        
        while x == 8:
            v += (w[int(y[0])])
            if int(y[0]) == 0:
              y = y[1:z]
              jk1 += 1
              break
            v += " hundred "
            y = y[1:z]
            break
        
        while x == 7:
            if int(y[0:2]) > 10 and int(y[0:2]) <= 19:
                v += (s[int(y[1])])
                jk += 1

                
            else:
                v += (g[int(y[0])])
                if int(y[0]) == 0:
                  jk1 += 1
            y = y[1:z]
            break

        while x == 6:
            if int(y[0]) == 0:
              jk1 += 1

            if jk1 == 3:
              y = y[1:z]
              break

            if jk == 1:
                v += " million "

            else:
                v += (w[int(y[0])])
                v += " million "
            y = y[1:z]
            break

        while x == 5:
            v += (w[int(y[0])])
            if int(y[0]) == 0 :
              y = y[1:z]
              dc1 += 1
              break
            v += " hundred "
            y = y[1:z]
            break

        
        while x == 4:
            if int(y[0:2]) > 10 and int(y[0:2]) <= 19:
                v += (s[int(y[1])])
                dc += 1
                
            else:
                v += (g[int(y[0])])
                if int(y[0]) == 0:
                  dc1 += 1
            y = y[1:z]
            break

        while x == 3:
            if int(y[0]) == 0:
              dc1 += 1

            if dc1 == 3 :
              y = y[1:z]
              break

            elif dc == 1:
              v += " thousand "
            
            else:
              v += (w[int(y[0])])
              v += " thousand "
            y = y[1:z]
            break

        while x == 2:
            v += (w[int(y[0])])
            if int(y[0]) == 0 :
              y = y[1:z]
              break
            v += " hundred "
            y = y[1:z]
            break

        
        while x == 1:
            if int(y[0:2]) > 10 and int(y[0:2]) <= 19:
                v += (s[int(y[1])])
                h += 1
                
            else:
                v += (g[int(y[0])])
            y = y[1:z]
            break
        
        while x == 0:
            if h == 1:
                break

            else:
                v += (w[int(y[0])])
                break

    do = v.title()
    fn =(do.replace("  "," "))
    return fn.rstrip()
    

print(lol(1711070058))        # numbers to words







def lol9(height):    
    lef = 0
    wat = 0
    du = 0
    if len(height) == 0 or len(height) == 1 or len(height) == 2:
        return 0

    for j in range(0,max(height)):

        while height[0] <= 0  :
            height = height[1:]

        while height [-1] <= 0 :
            height = height[:-1]

        for i in range(0,len(height)):
            x = height[i]
            y = 0

            if x < 0 :
                x = 0

            if x == 0 :
                du += 1

            if x > 0 :
                y = 1

            if y >= 0 : 
                lef += y
                if lef >= y and du >= 1 :
                    wat += 1
                    lef = 0
                    if du > 1:
                        wat += du - 1
                    du = 0

        height = [ x - 1 for x in height] 
    return(wat)
        
        

print(lol9([2,0,3,2,3,0,1,3]))


def lol(height):

    water = 0

    while len(height) > 2 :
        if height.count(max(height)) > 1 :
            x = max(height)
            fi = height.index(x)
            la = len(height) - 1 - height[::-1].index(x)

            water += ((la-fi-1) * x ) - (sum(height[fi+1:la]))
            del height[fi:la]

            print(height)
            print (water)


        else :
            new = sorted(height)
            second = new[-2]
            index1 = height.index(max(height))
            del height[index1]
            height.insert(index1,second)
            print(height)
 
print(lol([0,1,0,2,1,0,1,3,2,1,2,1]))




def lol(nums):
    if nums.count(1) == 0:
        return 1
    else:
        nums.sort()
        nums = list(set(nums))
        nums = nums[nums.index(1):]
        x = 0
        for i in range(len(nums)):
            if nums[i] != 1+i:
                x = (1 + i)
                return x
                break
        if x == 0 :
            return len(nums) + 1
        



print(lol([2147483647,2147483646,2147483645,3,2,1,-1,0,-2147483648]))





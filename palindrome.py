import sys
#Some good test palindromes:
#noon (This has even number of characters)
#racecar (This has odd number)
#A nut for a jar of tuna


def isPalindrome(str):
  #strip whitespace and make lower case.
  str=str.replace(" ", "");
  str=str.lower();
  print(str) 
  beg=0;
  end=len(str)-1;
  
  while beg<end:
    if (str[beg] != str[end]):
       return False;
    beg=beg+1;    
    end = end-1;
  return True

if (sys.version_info[0]<3):
  print("Please run with python 3.x");
  exit(0);

print("Enter a word or sentence to check if it is a palindrome");
print("Type 'quit' to exit");
while True:
  word = input('enter word:');
  if (word == 'quit'): exit(0);
  if isPalindrome(word) == True:
    print("Yes, this is a palindrome!");
  else:
    print("Sorry!");

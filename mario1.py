h = int(input());

while(h<0 or h > 24):
  print("That is an invalid input")
  print('Height: ', end='');
  h = int(input());

for i in range(h):
    print(" "*(h-i)+"#"*(i+1));

value = 6
steps = 0
peak = value
while value != 1:
     if value % 2 == 0:
          value = value // 2
          steps = steps + 1
          if value > peak:
               peak = value
            
        else:
                value = 3*value + 1


while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = r * n + 1
blocks = int(input("Enter the number of blocks: "))
level_counter = 0
bricks_required_per_level = 0
brick_level_count = 1
height = 0
#
# Write your code here.
#	

i = 1
while i < blocks:
    if i == 1:
        level_counter = 1
        bricks_required_per_level = bricks_required_per_level+ 1
        #print("step1")
        i = i + 1
    else:
        i = i + 1
        if brick_level_count < bricks_required_per_level:
            brick_level_count = brick_level_count +1
       #     print("bricklevelcount", brick_level_count)
      #      print("step2")
        else:
            bricks_required_per_level = bricks_required_per_level + 1
            brick_level_count = 0 #reset
            level_counter = level_counter +1
         #   print("bricks required for each level", bricks_required_per_level )
    
height = level_counter
print("The height of the pyramid:", height)

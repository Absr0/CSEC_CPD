# Read input values
n, h = map(int, input().split())
a = list(map(int, input().split()))

# Calculate the required width
width = 0
for height in a:
    if height > h:
        width += 2  # Needs to bend
    else:
        width += 1  # Walks normally
      
print(width)

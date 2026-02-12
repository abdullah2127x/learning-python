# In Python, slicing can be done by using square brackets [ ] after the variable to be sliced. For example:
# text = "Python"

# print(text[0])  # Output: 'P'

# In slicing, the square brackets take up to three arguments:

# 𝗦𝘁𝗮𝗿𝘁 – The index where slicing begins.

# 𝗘𝗻𝗱   – The index where slicing stops (not included).

# 𝗦𝘁𝗲𝗽 –  Step – The number of elements to skip (default is 1).

# It can be Written as:

# 𝘃𝗮𝗿𝗶𝗮𝗯𝗹𝗲[𝘀𝘁𝗮𝗿𝘁:𝗲𝗻𝗱:𝘀𝘁𝗲𝗽]


# The last argument (step) is the hoping how many word will it jump or tell the way of working (forward or reverse)


text = "Python"
# syntax
# text[start:end:step]

# Extract "Pyt"
print(text[0:3])  # Output: 'Pyt'

# Extract "yth" using step 1
print(text[1:4:1])  # Output: 'yth'

# Reverse a string
# if we dont give any number and just write : it will works as start and till end of
print(text[::-1])  # Output: 'nohtyP'

# The last argument (step) is the hoping how many word will it jump or tell the way of working (forward or reverse)

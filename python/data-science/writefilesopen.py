# Write in a file

# File1 = open("/home/mattbellantoni3/rogue-data/readme.md", "w")
# File1.write("This is line A\n")
# File1.write("Write all over")

# loops
# Lines = ["This is a line ", "This is another line ", "This isn't a line "]
# with open("/home/mattbellantoni3/rogue-data/readme.md", "w") as File1:
#     for line in Lines:
#         File1.write(line)

# appends
# Lines = ["Alpha ", "Bravo ", "Charlie "]
# with open("/home/mattbellantoni3/rogue-data/readme.md", "a") as File1:
#     for line in Lines:
#         File1.write(line)

# copy one file to another
# with open("readme.md", "r") as readfile:
#     with open("readme.txt", "w") as writefile:
#         for line in readfile:
#             writefile.write(line)

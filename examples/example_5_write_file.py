lines = [
    "I have eaten",
    "the plums",
    "that were in",
    "the icebox",
]

# Simplest
with open("data/output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

# With .join()
with open("data/output.txt", "w") as file:
    file.write("\n".join(lines))

# With a generator expression
with open("data/output.txt", "w") as file:
    # .writelines doesn't add \n
    file.writelines(line + "\n" for line in lines)

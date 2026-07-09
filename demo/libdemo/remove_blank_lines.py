# Remove blank lines from the given file

FILENAME = "langs.txt"
lines = []
with open(FILENAME, "rt") as f:
    for line in f:
        if len(line.strip()) > 0: # non-blank line
            lines.append(line)

# Write non-blank lines back to the file
with open(FILENAME, "wt") as f:
    for line in lines:
        f.write(line)

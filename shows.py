months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
with open('./shows.txt', 'r') as f:
    for line in f:
        if line.startswith(months):
            print("{}{}".format("<br /><br />", line), end='')
        else:
            print(line, end='')
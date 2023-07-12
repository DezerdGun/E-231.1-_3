with open("Ishodniy_File.txt", "r") as input_file:
    with open("new_file.txt", "w") as output_file:
        for line in input_file:
            words = line.split()
            long_words = [word for word in words if len(word) >= 7]
            output_file.write(" ".join(long_words) + "\n")
import datetime
current_year = datetime.datetime.now().year
print(current_year)
i = int(input())
if (i % 4 == 0 or i % 400 == 0) and i % 100 != 0:
    print("YES")
else:
    print("NO")
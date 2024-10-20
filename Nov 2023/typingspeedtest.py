import time
input("Press enter when you want to start your typing speed test::: ")
start_time = time.time()
user_typing_input = str(input("Type a sentence or paragraph and do it with you best typing speed::: "))
end_time = time.time()
space = 0
for i in user_typing_input:
    if i == " ":
        space = space+1
words = space+1
total_time = end_time-start_time
wpm = words/total_time*60
print(wpm," wpm")
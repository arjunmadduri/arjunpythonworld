array = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def num2word(n):
    if(n==0):
        return ""
    else:
        lastdigit = array[n%10]
        ans = num2word(int(n/10)) + lastdigit + " "
        return ans

n = int(input("Enter a number:"))
print("The Number Entered was: ", n)
print("the word is:", )
print(num2word(n))
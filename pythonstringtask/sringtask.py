1

a="hello"
print(a.upper())

2

b="PYTHON"
print(a.lower())

3

s="hello python"
new_s=s.replace("pthon","hello")
print(new_s)

4

word = "hello"
result = word[1:4]
print(result)  

5
s = "python"
print(s[::-1]) 

6
word = "hello" + " " + "world"
print(word)  

7
h="hi"
print("hi"* 3)

8
cat="concatenate"
print("cat" in "concatenate")   

9

print("banana".count("a"))  

10

print("hello".strip())

11
a="hello"
print("hello".index("o"))

12

print("a,b,c,d".split( "," ))

13

print("".join(["a","b","c"]))

14

print("abcdef"[::2])

15

print("banana".replace("a", "@"))

16

print("hello123".isalnum())

17

a="python"
print(a.capitalize())

18

print("hello world".title())  

19

vowels = str.maketrans("", "", "aeiouAEIOU")
print("python".translate(vowels))

20

word = "madam"
print(word == word[::-1])   

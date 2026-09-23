#You're given two strings that may contain the character '#', which means "backspace": it deletes the character before it (if any).

#Simulate typing both strings, and decide whether the final results are equal.

#Input: s = "ab#c", t = "ad#c"
#Output: true
#both type out to "ac"
#Input: s = "ab##", t = "c#d#"
#Output: true
#both type out to an empty string
#Input: s = "a#c", t = "b"
#Output: false
#s types out to "c", t types out to "b"


class Solution:
    def backspaceCompare(self, s,t):
        stack1 = []
        stack2 = []
        a=True
        o1=""
        o2=""
        for ch in s:
            print(ch)
            if ch == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        o1 = ''.join(stack1)
        print(f"o1 is {o1}")
        for ch in t:
            if ch == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)
        o2=''.join(stack2)
        print(f"o2 is {o2}")
        return(o1==o2)
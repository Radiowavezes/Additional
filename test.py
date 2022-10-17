def longestPalindrome(s: str) -> str:
    def is_palindrome(looking_str: str, index: int = 0) -> bool:
        if int(len(looking_str) / 2) == index:
            return True
        if int(len(looking_str) / 2 + 1) == index:
            return True
        if looking_str[index] != looking_str[-(index + 1)]:
            return False
        return is_palindrome(looking_str, index + 1)
    start = 0
    stop = 1
    recursive_string = ''
    temp = ''
    if len(s) > 1:
        while start < len(s) - 1:
            if is_palindrome(s[start:stop]):
                temp = s[start:stop]
                print(s[start:stop])
                print(stop)
                print(temp)
            if len(temp) > len(recursive_string):
                recursive_string = temp
            stop += 1
            if stop == len(s):
                start += 1
                stop = start + 1
    else:
        recursive_string = s
    return recursive_string

s = 'aabb'
print(longestPalindrome(s))
print(s[3::-1])
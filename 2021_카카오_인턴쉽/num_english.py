def solution(s):
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    num_letter = ''
    answer = ''

    for letter in s:
        if letter.isalpha():
            num_letter += letter
            if num_letter in num_dict:
                answer += str(num_dict[num_letter])
                num_letter = ''
        else:
            answer += letter

    return answer


test1 = solution("one4seveneight")
test2 = solution("23four5six7")
test3 = solution("2three45sixseven")
test4 = solution("123")

print(test1)
print(test2)
print(test3)
print(test4)

# for a in 'one4seven':
#     print(a.isalpha(), type(a))

# num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
#             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# if 'zero' in num_dict:
#     print(num_dict['zero'])

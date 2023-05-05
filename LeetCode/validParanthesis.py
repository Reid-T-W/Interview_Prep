#!/usr/bin/env python3
# class Solutions():
#     def isValid(self, s: str) -> bool:
#         stack_open = []
#         dict = {')':'(', '}':'{', ']':'['}
#         valid = True
#         for bracket in s:
#             dict_value = dict.get(bracket)
#             # Open bracket
#             if dict_value == None:
#                 stack_open.append(bracket)
#             # Closed bracket
#             else:
#                 if len(stack_open) == 0:
#                     valid = False
#                     break
#                 if dict_value != stack_open.pop():
#                     valid = False
#                     break
#         if len(stack_open) != 0:
#             valid = False
#         return valid


# sol = Solutions()
# # str = '({})'
# # str = '(){}[]'
# # str = '{'
# str = '(})'
# print(sol.isValid(str))


class Solutions():
    def isValid(self, s: str) -> bool:
        stack_open = []
        dict = {')':'(', '}':'{', ']':'['}
        valid = True
        for bracket in s:
            dict_value = dict.get(bracket)
            # Closed Bracket
            if dict_value is not None:
                val = stack_open.pop()
                if stack_open is None or dict_value != val:
                    return False
            # Open Bracket
            else:
                stack_open.append(bracket)
        return not stack_open
    
    # str = '(){}[]'

        #     dict_value = dict.get(bracket)
        #     # Open bracket
        #     if dict_value == None:
        #         stack_open.append(bracket)
        #     # Closed bracket
        #     else:
        #         if len(stack_open) == 0:
        #             valid = False
        #             break
        #         if dict_value != stack_open.pop():
        #             valid = False
        #             break
        # if len(stack_open) != 0:
        #     valid = False
        # return valid


sol = Solutions()
# str = '({})'
str = '()'
# str = '{'
# str = '(})'
print(sol.isValid(str))
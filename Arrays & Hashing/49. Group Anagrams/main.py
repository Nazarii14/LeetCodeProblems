# def groupAnagrams(strs):
#     splited = [[j for j in i] for i in strs]
#     result_arr = []
#
#     for i in range(len(splited)):
#         new_temp_arr = []
#         for j in range(i, len(splited)):
#             if sorted(splited[i]) == sorted(splited[j]):
#                 new_temp_arr.append(''.join(splited[j]))
#                 splited.remove(splited[j])
#         result_arr.append(new_temp_arr)
#
#     return [i for i in result_arr if len(i) != 0]
#
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

import collections

ans = collections.defaultdict(list)
print(ans)
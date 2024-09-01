chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

char_count_dict={}
for c in chars:
    if c in char_count_dict:
        char_count_dict[c]+=1
    else:
        char_count_dict[c]=1

result=""
for k,v in char_count_dict.items():
    if v>1:
        result=result+k+str(v)
    else:
        result=result+k
print(result)

# result="".join(f"{k}{v}" if v>1 else k for k,v in char_count_dict.items())
# print(result)

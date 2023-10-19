k=2
strarr = ["tree", "folings", "trashy", "blue", "abcdef", "uvwxyz"]
maximum = 0
larger = ''
for i in range(len(strarr) - k+1):
        
        con = strarr[i] + strarr[i+1]
        length = len(con)
        print(con,"(" ,length,")" ,f"concatenation of strarr{i} and strarr{i+1}" )
        if length > maximum:
            maximum = len(con)
            larger = con
print("longest"  , larger , 'length' , maximum)
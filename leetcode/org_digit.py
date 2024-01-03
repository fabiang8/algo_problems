def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        out = {}
        out["0"] = count["z"]   # count of zeros is count of z
        out["2"] = count["w"]   # count of two is count of w
        out["4"] = count["u"]   # count of four is count of u
        out["6"] = count["x"]   # count of six is count of x
        out["8"] = count["g"]   # count of eight is count of g
        
        
     
        out["3"] = count["h"] - out["8"]  # count of three is total h's - total amount of 8's
        out["5"] = count["f"] - out["4"] # count of five is number of f's - number of fours
        out["7"] = count["s"] - out["6"] # count of seven is amount of s's - count of 6's
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        out["1"] = count["n"] - out["7"] - (2* out["9"]) # count of one is number of n's - total 7's - (2* total 9's)  * because 9 has two n's
        
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)
        
        
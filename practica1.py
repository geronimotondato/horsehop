memo = dict()


def num_ways(code: str, memo: dict):
    if code[0] == "0":
        return 0
    if (memo.get(code)):
        return memo.get(code)
    if(len(code) <= 2):
        if(int(code) > 9 and int(code) < 27):
            return 2
        else:
            return 1
    if(int(code[:2]) > 9 and int(code[:2]) < 27):
        result = num_ways(code[1:], memo) + num_ways(code[2:], memo)
        memo[code] = result
        return result
    else:
        result = num_ways(code[1:], memo)
        memo[code] = result
        return result

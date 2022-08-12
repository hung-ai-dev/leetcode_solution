Recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generator(res: list, n: int, idx: int, par: str, s: int):
            if idx == n:
                if s == 0:
                    res.append(par)
                return
            
            for p, v in zip('()', [1, -1]):
                if s + v >= 0:
                    generator(res, n, idx+1, par+p, s+v)
        res = []
        generator(res, 2*n, 0, '', 0)
        return res

Non recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        mapper = {"0": ')', "1": "("}
        
        for int_par in range(2**(n*2)):
            par = format(int_par, "b").zfill(n*2)
            s, flag = 0, True
            for v in par:
                val = -1 if v == "0" else 1
                s += val
                if s < 0:
                    flag = False
            par = ''.join([mapper[x] for x in par])
            if flag and s == 0:
                res.append(par)
        return res

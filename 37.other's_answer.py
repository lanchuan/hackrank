class Solution(object):
    def solveSudoku(self, board):
        hole = [(i, None, 0) for i, c in enumerate(sum(board, [])) if c == '.']
        ds, fs = set(['.']), set(list("123456789"))
        rs, cs = [set(row)-ds for row in board], [set(col)-ds for col in zip(*board)]
        ss = [[set(sum([board[k][j:j+3] for k in xrange(i, i+3)], [])) - ds\
                                        for j in xrange(0, 9, 3)]\
                                        for i in xrange(0, 9, 3)]
        failed, ptr, n = False, 0, len(hole)
        while ptr < n:
            i, ps, nc = hole[ptr]
            r, c = i//9, i%9
            if failed: rs[r].remove(ps[nc]), cs[c].remove(ps[nc]), ss[r//3][c//3].remove(ps[nc])
            else: ps = list(fs - rs[r] - cs[c] - ss[r//3][c//3])
            if not ps or (failed and nc + 1 == len(ps)):
                ptr, failed = ptr - 1, True
                continue
            nc = nc + 1 if failed else 0
            rs[r].add(ps[nc]), cs[c].add(ps[nc]), ss[r//3][c//3].add(ps[nc])
            hole[ptr] = i, ps, nc
            ptr, failed, board[r][c] = ptr + 1, False, ps[nc]
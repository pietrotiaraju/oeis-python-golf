# A000436

> Generalized Euler numbers c(3,n).
> — [OEIS A000436](https://oeis.org/A000436)

Offset 0: 1, 8, 352, 38528, 7869952, 2583554048, 1243925143552, 825787662368768, 722906928498737152, 806875574817679474688, …

a(n) is the coefficient of x^(2n)/(2n)! in cos(x)/cos(3x).

### Python 3 — 110 bytes

```python
import math
a=[n:=1]
while[print(abs(a[-1]))]:a+=2-sum(math.comb(2*n,2*k)*9**k*a[-k]for k in range(n+1)),;n+=1
```

**How it works**

- Multiply F(x) = cos(x)/cos(3x) = Σ a(n)·x^(2n)/(2n)! by cos(3x) and compare
  the coefficients of x^(2n)/(2n)!: the 2k-th derivative of cos(3x) at 0 is
  (−9)^k and that of cos(x) is (−1)ⁿ, so
  Σ_{k=0}^{n} C(2n, 2k)·(−9)^k·a(n−k) = (−1)ⁿ. For b(n) = (−1)ⁿa(n) the signs
  cancel and b(n) = 1 − Σ_{k=1}^{n} C(2n, 2k)·9^k·b(n−k) (R. J. Mathar's
  formula on the OEIS page). The terms are positive, so a(n) = |b(n)|.
- The list holds b(0), …, b(n−1) when b(n) is built, so `a[-k]` is b(n−k)
  for k ≥ 1. For k = 0, `a[-0]` is `a[0]` = b(0) = 1, which adds 1 to the
  sum; `2-sum(…for k in range(n+1))` is therefore 1 − Σ_{k≥1}, 2 bytes under
  `1-sum(…for k in range(1,n+1))`.
- `a=[n:=1]` stores b(0) = 1 and starts the counter; `while[print(…)]:`
  prints |b| of the newest entry before the next one is appended.

**Notes**

- Keeping the signs, `(-1)**n-sum(math.comb(2*n,2*k)*(-9)**k*a[-k]…)` with
  `n=len(a)` and `print(a[-1])`: 120 bytes. With
  cos(x)/cos(3x) = 1/(2cos(2x) − 1) the recurrence has 4^k in place of 9^k but
  a factor 2 in front: 2 bytes longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s, which takes a tenth of a second here.
- a(716) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there (716 terms, about 22 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |
| 2026-11-06 | Python 3 | 122 | use a shorter math import |
| 2026-11-06 | Python 3 | 120 | remove addition of zero in the binomial argument |
| 2026-11-07 | Python 3 | 110 | signed values (−1)ⁿa(n) and the k = 0 term from `a[0]` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000436), CC BY-SA 4.0.

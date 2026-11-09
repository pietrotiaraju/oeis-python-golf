# A001303

> Stirling numbers of first kind, s(n+3, n), negated.
> — [OEIS A001303](https://oeis.org/A001303)

Offset 1: 6, 50, 225, 735, 1960, 4536, 9450, 18150, 32670, 55770, …

a(n) = |s(n+3, n)| = [n+3, n], the number of permutations of n + 3
elements with exactly n cycles.

### Python 3 — 46 bytes

```python
x=3
while[print((x*~x)**2*~-x*(x-2)//48)]:x+=1
```

**How it works**

- a(n) = C(n+3, 4)·C(n+3, 2) = n(n+1)(n+2)²(n+3)²/48 (formula on the
  OEIS entry). It holds for every n: call the right side P(n). P(0) = 0
  = [3, 0], and
  P(n) − P(n−1) = n(n+1)(n+2)²·((n+3)² − (n−1)(n+1))/48
  = n(n+1)(n+2)²(3n+5)/24 = (n+2)·[n+2, n], using
  [n+2, n] = n(n+1)(n+2)(3n+5)/24 ([A000914](../../A000xxx/A000914/)). The
  Stirling recurrence [n+3, n] = (n+2)·[n+2, n] + [n+2, n−1] gives a(n) the
  same first differences, so a(n) = P(n).
- The loop counter `x` is n + 2, so P = (x−2)(x−1)·x²(x+1)²/48. `~x` is
  −(x+1), so `(x*~x)**2` is x²(x+1)², and `~-x` is x − 1. P is an
  integer, so `//48` is exact. `x` starts at 3, the offset n = 1.
- `print` returns `None` and `[None]` is truthy, so the loop never ends.

**Notes**

- Counting down with y = −x, `(y*~-y)**2*~y*~-~y//48` from `y=-3`, also
  makes 46 bytes. Counting by n
  (`n*-~n*((n+2)*(n+3))**2//48`) or by n + 3 is 49 bytes, like the
  S(n+3, n) record of [A001297](../A001297/) (48, whose offset is 0).
- Running sums: [n+3, n] is the elementary symmetric sum e₃(1, …, n+2),
  and the chain `a=c=6;b=11;n=3` /
  `while[print(c)]:n+=1;c+=n*b;b+=n*a;a+=n` is 54 bytes; adding
  (n+2)·[n+2, n] with the step of A000914 is also 54.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁶/48, far from the 4300-digit int-to-str limit.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001303), CC BY-SA 4.0.

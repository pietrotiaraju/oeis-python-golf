# A001762

> Number of labeled n-vertex dissections of a ball.
> — [OEIS A001762](https://oeis.org/A001762)

Offset 3: 1, 1, 10, 180, 4620, 152880, 6168960, 293025600, 15990004800, 984647664000, …

### Python 3 — 67 bytes

```python
b=v=1
while[print(-~b>>1)]:b=b*v*-~v*(v+11)*9//(v+5)//(4*v+14);v+=3
```

**How it works**

- The entry gives a(n) = C(n, 3)·(3n−9)!/(2n−4)! for n ≥ 4 and a(3) = 1
  separately: at n = 3 the formula f(n) = C(n, 3)·(3n−9)!/(2n−4)! gives
  0!/2! = 1/2 (in the entry's e.g.f. the extra term x³/12 supplies the
  other half).
- For n ≥ 4 the ratio is f(n)/f(n−1) = n/(n−3)·(3n−9)(3n−10)(3n−11)/((2n−4)(2n−5))
  = 3n(3n−10)(3n−11)/((2n−4)(2n−5)), and it also holds from f(3) = 1/2 to
  f(4) = 1. So the program keeps b = 2f(n), an integer (b = 1 at n = 3,
  then 2a(n)), and prints ⌈b/2⌉ = `-~b>>1`: 1 at n = 3, a(n) afterwards.
- The step from n to n + 1 is written with v = 3n − 8 (v = 1 at n = 3, so
  `b=v=1`, and `v+=3` after the step): n + 1 = (v+11)/3, 3n − 7 = v + 1,
  3n − 8 = v and (2n−2)(2n−3) = 2(v+5)(2v+7)/9, which gives
  `b=b*v*-~v*(v+11)*9//(v+5)//(4*v+14)`. The new b is an integer, and two
  floor divisions by positive integers equal one floor division by their
  product, so both are exact.

**Notes**

- Exact integer arithmetic, correct for every n. a(1236) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Stepping t = 3n after the increment, `b=1;t=3` /
  `…t+=3;b=b*(t+6)*(t-4)*(t-5)*9//t//(4*t-6)`, is 69 bytes; with
  i = n − 2, 70. `math.perm(3*n-9,n-5)` would give (3n−9)!/(2n−4)! but fails
  on a negative length at n = 4.
- The b-file has 98 terms (a(3) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly. [A001763](../A001763/) is the rooted
  version.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001762), CC BY-SA 4.0.

# A000074

> Number of odd integers <= 2^n of form x^2 + y^2.
> — [OEIS A000074](https://oeis.org/A000074)

Offset 1: 1, 1, 2, 4, 7, 13, 25, 43, 83, 157, 296, 564, 1083, 2077, 4006, …

### Python 3 — 100 bytes

```python
n=0
while r:=range(1<<-~n//2|2):print(len({max(x*~x+y*~y,-2**n)for x in r for y in r[:x+1]})-1);n+=1
```

**How it works**

- An odd sum of two squares has one odd and one even square. Writing the odd
  root as x+y+1 and the even one as x−y gives
  (x+y+1)² + (x−y)² = **2·(x(x+1) + y(y+1)) + 1**. Every odd sum of two
  squares comes out this way: for v = a² + b² with a odd and b even, take
  x = (a+b−1)/2 and y = (a−b−1)/2. If x or y is negative, −x−1 or −y−1 gives
  the same x(x+1) or y(y+1), so x, y ≥ 0 are enough.
- So the odd sums of two squares are the numbers 2t+1 with
  t = x(x+1) + y(y+1), and 2t+1 ≤ 2ᵏ exactly when t < 2ᵏ⁻¹ (2t+1 is odd and
  2ᵏ is even). a(k) is the number of distinct such t below 2ᵏ⁻¹. (Equivalently,
  t/2 is a sum of two triangular numbers.)
- n counts from 0 and the program prints a(n+1), so the bound is a plain
  `2**n` and the arithmetic stays in integers.
- `~x` is −x−1, so `x*~x+y*~y` is −t. `max(…,-2**n)` sends every t ≥ 2ⁿ to
  the same value −2ⁿ: the set holds −t for each t < 2ⁿ plus that one extra
  value, which `-1` removes. It is the [A000050](../A000050/) `min` trick
  turned upside down: `x*~x+y*~y` is 2 bytes shorter than `x*x+x+y*y+y`,
  and the minus sign on `-2**n` costs one of them back.
- t < 2ⁿ needs x, y < 2^(n/2) ≤ 2^c, where c = ⌈n/2⌉ is `-~n//2`, so x and
  y stay below 2^c. `range(1<<-~n//2|2)` holds them: its length is 2^c + 2
  for c ≥ 2, 3 for c = 0 and 2 for c = 1. t is symmetric in x and y, so y
  runs only up to x (`r[:x+1]`).
- The largest pair, x = y = the last element of the range, gives t ≥ 2ⁿ
  for every n (t = 12 for n = 0, t = 4 for n = 1 and 2), so the extra value
  is always there.
- `while r:=range(…)` names the range in the loop condition; a non-empty
  range is true, so the loop never ends (as in [A000047](../A000047/)).

**Speed**

- Term n+1 costs about |r|²/2 pairs: 2ⁿ⁻¹ for even n and 2ⁿ for odd n. The
  90-byte version used `range(2<<n//2)` for both x and y, which is 2ⁿ⁺²
  pairs for even n and 2ⁿ⁺¹ for odd n.
- The bar is 25 terms in 60 s, and it must come within half the timeout,
  in reference seconds. The 90-byte version needed about 49 s on the GitHub
  runners; on the same local machine this one is 4.7 times faster, about
  10 s. The tight range alone, without `[:x+1]`, is 94 bytes and 2.3 times
  faster, about 21 s: too close to the 30 s limit. The b-file goes to
  n = 50, far beyond any enumeration.

**Notes**

- Even sums of two squares up to 2ⁿ are twice the sums up to 2ⁿ⁻¹, so
  a(n) = A000050(n) − A000050(n−1), the first differences noted on the OEIS
  page.
- `min(x*x+x+y*y+y,2**n)` is 1 byte longer than the `max` form. Filtering
  the A000050 set for odd values, `{v for x in r for y in r if(v:=x*x+y*y)>>n<v%2}`,
  was 3 bytes longer than the 90-byte version.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 90 | first entry |
| 2026-11-08 | Python 3 | 100 | fix: range up to 2^⌈n/2⌉ and y ≤ x, so the bar comes within half the timeout |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000074), CC BY-SA 4.0.

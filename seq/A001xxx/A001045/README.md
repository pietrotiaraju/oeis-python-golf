# A001045

> Jacobsthal sequence (or Jacobsthal numbers): a(n) = a(n-1) + 2*a(n-2), with a(0) = 0, a(1) = 1; also a(n) = nearest integer to 2^n/3.
> — [OEIS A001045](https://oeis.org/A001045)

Offset 0: 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, …

### Python 3 — 29 bytes

```python
x=2
while[print(x//3)]:x+=x-1
```

**How it works**

- The characteristic polynomial of a(n) = a(n−1) + 2a(n−2) is
  t² − t − 2 = (t − 2)(t + 1), and a(0) = 0, a(1) = 1 give the closed form
  a(n) = (2ⁿ − (−1)ⁿ)/3.
- `x` holds 2ⁿ + 1: it starts at 2 = 2⁰ + 1, and `x+=x-1` turns it into
  2x − 1 = 2ⁿ⁺¹ + 1.
- ⌊(2ⁿ + 1)/3⌋ = a(n): for odd n, 2ⁿ + 1 = 3a(n) exactly; for even n,
  2ⁿ + 1 = 3a(n) + 2 and the floor drops the 2. (This is the "nearest
  integer to 2ⁿ/3" of the title.) Exact integers, one variable.

**Notes**

- `x=1` / `while[print(-~x//3)]:x*=2` (x = 2ⁿ, the +1 moved into the print)
  is also 29 bytes.
- Why the update has a −1: printing ⌊x/3⌋ with x = 2ⁿ + d needs d/3 ≥ 1/3
  for odd n and d/3 < 2/3 for even n, so d = 1, and the step x ↦ 2x − d
  has a negative constant. `x-=~x` (2x + 1) would keep x = c·2ⁿ − 1, which
  rounds the wrong way at every odd n.
- Two-variable forms are longer: the Pell-style tuple `a,b=0,1` /
  `while[print(a)]:a,b=b,2*a+b` is 35 bytes, and a(n+1) = 2ⁿ − a(n) as
  `a=0;b=1` / `while[print(a)]:a=b-a;b+=b` is 34 (the shortest a search over
  two-statement in-place loops found).
- Python's 4300-digit int-to-str limit stops the program at a(14286), the
  first term with 4301 digits, after printing a(0) to a(14285).
- The b-file has 3317 terms (a(0) to a(3316), 998 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001045), CC BY-SA 4.0.

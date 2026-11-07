# A000495

> Nearest integer to sinh(n).
> — [OEIS A000495](https://oeis.org/A000495)

Offset 0: 0, 1, 4, 10, 27, 74, 202, 548, 1490, 4052, …

### Python 3 — 88 bytes

```python
n=0
while 1:
 M=d=1;G=2
 while-M%G<2*n**d:M=M*d+2*n**d*(d&1);G*=d;d+=1
 print(M//G);n+=1
```

**How it works**

- The inner loop sums sinh n = Σ_{k odd} nᵏ/k! over a common denominator, as
  the [A000149](../A000149/) program does for eⁿ. With m = d − 1, F = m! and
  N/F the partial sum up to k = m, it keeps M = 2N + F and G = 2F, so
  M/G = N/F + ½ and the rounding is ⌊M/G⌋ = `M//G`. The next term
  multiplies N and F by d and adds nᵈ to N when d is odd, so M becomes
  M·d + 2nᵈ·(d mod 2) and G becomes G·d. `M=d=1;G=2` is m = 0 (N = 0, F = 1).
- `-M%G` over G is the gap from M/G up to the next integer, and 2nᵈ over G
  is n·L with L = nᵐ/m!. The loop stops when the gap is at least n·L.
- That is enough once m ≥ 2n − 1: the omitted terms sum to less than
  Σ_{k>m} nᵏ/k! < L·n/(m + 1 − n) ≤ L. Before that, L ≥ 1 (pair the factors
  of (2n−2)! as i·(2n−1−i) < n²), so n·L ≥ 1 exceeds every gap and the loop
  cannot stop early. So `M//G` is ⌊sinh n + ½⌋.
- The loop always ends: sinh n + ½ is never an integer for n ≥ 1 (otherwise
  eⁿ would be a root of x² − (2k+1)x − 1, against Hermite–Lindemann), so the
  gap tends to a positive limit while n·L tends to 0. For n = 0, 0ᵈ = 0 and
  the test fails at once: 1//2 = 0.

**Notes**

- Other versions: `n**d-(-n)**d` for the new term, also 88 bytes; tracking
  p = 2nᵈ with `p*=n`, 89 bytes; stepping d by 2 with `M=n-~n;G=2;d=1` and
  `d*~-d`, 95 bytes; the earlier N/F form, 113 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The loop runs to m ≈ 2.7n for each n: about 790 terms in 60 s here. The
  b-file has 251 terms (up to a(250)); the bar is the whole b-file in 60 s,
  which takes about 1.3 s.
- a(n) has about 0.43n digits, so the 4300-digit int-to-str limit (near
  n = 9900) is far beyond what a minute reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 113 | first entry |
| 2026-11-07 | Python 3 | 88 | A000149 loop with an odd-term filter and the ½ in M/G |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000495), CC BY-SA 4.0.

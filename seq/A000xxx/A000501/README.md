# A000501

> a(n) = floor(cosh(n)).
> — [OEIS A000501](https://oeis.org/A000501)

Offset 0: 1, 1, 3, 10, 27, 74, 201, 548, 1490, 4051, …

### Python 3 — 83 bytes

```python
n=0
while 1:
 N=F=d=1
 while-N%F<n**d:N=N*d+n**d*(~d&1);F*=d;d+=1
 print(N//F);n+=1
```

**How it works**

- This is the [A000149](../A000149/) program (⌊eⁿ⌋) restricted to the even
  terms of the exponential series: cosh n = Σ_{k even} nᵏ/k!. With m = d − 1,
  F = m! and N/F the partial sum up to k = m; the next step multiplies N and
  F by d and adds nᵈ when d is even (`~d&1` is 1 for even d, 0 for odd).
- `-N%F` over F is the gap from N/F up to the next integer, and nᵈ over F is
  n·L with L = nᵐ/m!. The loop stops when the gap is at least n·L.
- Once m ≥ 2n − 1 the omitted terms sum to less than
  Σ_{k>m} nᵏ/k! < L·n/(m + 1 − n) ≤ L, so cosh n stays below the next integer
  and ⌊cosh n⌋ = `N//F`. Before that, L ≥ 1 (pair the factors of (2n−2)! as
  i·(2n−1−i) < n²), so n·L ≥ 1 exceeds every gap and the loop cannot stop
  early: no separate guard on m is needed.
- cosh n is irrational for n ≥ 1, so the gap tends to a positive limit while
  n·L tends to 0 and the loop ends. For n = 0 the test 0 < 0ᵈ fails at once
  and the program prints 1.

**Notes**

- Other versions: tracking p = nᵈ with `p*=n`, 87 bytes; stepping d by 2,
  `N=F=1;d=0` / `while-N%F<n**d:d+=2;N=N*d*~-d+n**d;F*=d*~-d`, 86 bytes;
  the same with a redundant `d<2*n or` guard, 100 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The loop runs to m ≈ 2.7n for each n: about 760 terms in 60 s here. The
  b-file has 30 terms (up to a(29)); the bar is the whole b-file in 60 s,
  which takes 0.1 s.
- a(n) has about 0.43n digits, so the 4300-digit int-to-str limit (near
  n = 9900) is far beyond what a minute reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 100 | first entry |
| 2026-11-07 | Python 3 | 83 | A000149 loop with an even-term filter, no guard |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000501), CC BY-SA 4.0.

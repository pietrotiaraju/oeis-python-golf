# A001338

> -1 + Sum (k-1)! C(n,k), k = 1..n for n > 0, a(0) = 1.
> — [OEIS A001338](https://oeis.org/A001338)

Offset 0: 1, 0, 2, 7, 23, 88, 414, 2371, 16071, 125672, …

### Python 3 — 48 bytes

```python
a=s=n=0
while[print(abs(s-1))]:a=a*n+1;s+=a;n+=1
```

**How it works**

- Let s(n) = Σ_{k=1}^{n} (k−1)!·C(n,k), so s(0) = 0 (empty sum) and
  a(n) = s(n) − 1 for n > 0. By Pascal's rule
  C(n+1,k) − C(n,k) = C(n,k−1), so
  s(n+1) − s(n) = Σ_{k≥1} (k−1)!·C(n,k−1) = Σ_j j!·C(n,j) = b(n),
  where b is [A000522](../../A000xxx/A000522/): b(n) = Σ n!/(n−j)!,
  b(0) = 1, b(n) = n·b(n−1) + 1. So s is the partial sum
  b(0) + … + b(n−1) (the entry's "Partial sums of A000522").
- The loop prints |s(n) − 1|, then sets a = b(n) = n·a + 1 and adds it
  to s, which gives s(n+1). At n = 0 the old a is multiplied by 0, so `a`
  can start at 0 together with s and n.
- The special value a(0) = 1 comes from `abs`: s(0) − 1 = −1 and
  |−1| = 1, while s(n) ≥ b(0) = 1 for n ≥ 1, so there |s(n) − 1| =
  s(n) − 1.

**Notes**

- Keeping t = s − 1 from the start, `a=n=0;t=-1` /
  `while[print(abs(t:=t+a))]:a=a*n+1;n+=1`, is 49 bytes, as is the body
  `s+=(a:=a*n+1);n+=1`; printing a(0) apart, `print(1);a=n=1;t=0` /
  `while[print(t)]:t+=(a:=a*n+1);n+=1`, is 53.
- Exact integer arithmetic, so the program is right for every n. It stops
  after a(1559): a(1560) is the first term with more than 4300 digits, the
  int-to-str limit of Python 3.11+.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001338), CC BY-SA 4.0.

# A000371

> a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n,k)*2^(2^k).
> — [OEIS A000371](https://oeis.org/A000371)

Offset 0: 2, 2, 10, 218, 64594, 4294642034, 18446744047940725978, …

### Python 3 — 59 bytes

```python
r=[t:=2]
while[print(t)]:r=[t:=r[0]**2]+[t:=t-x for x in r]
```

**How it works**

- With b(k) = 2^(2^k), a(n) is the n-th forward difference Δⁿb(0): the
  inverse binomial transform of b. The program keeps one diagonal of the
  difference table, r = [b(n), Δb(n−1), Δ²b(n−2), …, Δⁿb(0)], whose last
  entry is a(n).
- Adding b(n+1) = b(n)² in front, each next entry is the one before it minus
  the old entry above it, Δʲb(n+1−j) = Δʲ⁻¹b(n+2−j) − Δʲ⁻¹b(n+1−j). That is
  the running walrus `[t:=t-x for x in r]` started at t = `r[0]**2`, and it
  ends with t = Δⁿ⁺¹b(0) = a(n+1), ready to be printed.
- `r=[t:=2]` is the diagonal for n = 0, with t = a(0) = 2.

**Notes**

- Keeping b in its own variable, `p=2;r=[]` +
  `while 1:r=[t:=p]+[t:=t-x for x in r];print(t);p*=p`, is also 59 bytes. The
  recursion Δⁿb(k) = Δⁿ⁻¹b(k+1) − Δⁿ⁻¹b(k) as a lambda is 78, and the sum in
  the name with `math.comb` and `<<2**k` is 92.
- Exact integers, so every printed term is right. The terms grow like
  2^(2^n): a(13) has 2467 digits and a(14) has 4933, so Python's 4300-digit
  int-to-str limit stops the program after a(13) with a `ValueError`. The
  limit is not counted as a failure.
- The b-file has 9 terms (n = 0 to 8) and they print at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000371), CC BY-SA 4.0.

# A001761

> a(n) = (2*n)!/(n+1)!.
> — [OEIS A001761](https://oeis.org/A001761)

Offset 0: 1, 1, 4, 30, 336, 5040, 95040, 2162160, 57657600, 1764322560, …

### Python 3 — 45 bytes

```python
a=n=1
while[print(a)]:n+=1;a=~-n*(4*a-6*a//n)
```

**How it works**

- a(k) = (2k)!/(k+1)! = k!·C(k), with C(k) the Catalan numbers, so
  a(k)/a(k−1) = k·C(k)/C(k−1) = k(4k−2)/(k+1).
- The loop keeps n = k + 1, so that ratio is (n−1)(4n−6)/n and the step is
  a(k) = (n−1)·(4a − 6a/n), the Catalan trick of
  [A000108](../../A000xxx/A000108/). `6*a//n` is exact: 4a − 6a/n equals
  a(k)/k = (k−1)!·C(k), an integer, so 6a/n is one too.
- `a=n=1` starts at a(0) = 1; each pass does `n+=1` and
  `a=~-n*(4*a-6*a//n)`.

**Notes**

- Exact integer arithmetic, correct for every n. a(1310) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Ties at 45 bytes: `a=a*~-n*(4*n-6)//n`, and the walrus
  `a=n*(4*a-6*a//(n:=n+1))` without the separate `n+=1`. Stepping j = 2k,
  `a=1;j=0` / `…j+=2;a=a*j*~-j*2//(j+2)`, is 47; `math.perm` is not
  allowed a negative length, so (2k)!/(k+1)! = P(2k, k−1) needs a detour
  for k = 0 and comes out longer.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001761), CC BY-SA 4.0.

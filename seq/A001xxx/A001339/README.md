# A001339

> a(n) = Sum_{k=0..n} (k+1)! binomial(n,k).
> — [OEIS A001339](https://oeis.org/A001339)

Offset 0: 1, 3, 11, 49, 261, 1631, 11743, 95901, 876809, 8877691, …

### Python 3 — 38 bytes

```python
a=n=1
while[print(-a+(a:=a*n+1))]:n+=1
```

**How it works**

- Let b(n) = Σ_{k=0}^{n} k!·C(n,k) = Σ n!/(n−k)!, which is
  [A000522](../../A000xxx/A000522/), with b(0) = 1 and
  b(n) = n·b(n−1) + 1.
- By Pascal's rule C(n+1,k) − C(n,k) = C(n,k−1), so
  b(n+1) − b(n) = Σ_k k!·C(n,k−1) = Σ_j (j+1)!·C(n,j) = a(n).
  The sequence is the first difference of A000522.
- The loop keeps a = b(n) and a counter one ahead (it holds n + 1):
  `-a` reads the old value, then the walrus makes it
  b(n+1) = (n+1)·b(n) + 1, and the sum printed is b(n+1) − b(n).
  It starts from a = b(0) = 1 with the counter at 1, so both share `a=n=1`.

**Notes**

- The closed form a(n) = n·b(n) + 1 (from the same recurrence), as
  `a=n=0` / `while[print(n*(a:=a*n+1)+1)]:n+=1`, is 39 bytes; the chain
  a(n) = n·a(n−1) + b(n), `a=b=n=0` /
  `while[print(a:=a*n+(b:=b*n+1))]:n+=1`, is 44.
- Exact integer arithmetic, so the program is right for every n. It stops
  after a(1557): a(1558) is the first term with more than 4300 digits, the
  int-to-str limit of Python 3.11+.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001339), CC BY-SA 4.0.

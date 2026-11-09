# A001340

> E.g.f.: 2*exp(x)/(1-x)^3.
> — [OEIS A001340](https://oeis.org/A001340)

Offset 0: 2, 8, 38, 212, 1370, 10112, 84158, 780908, 8000882, 89763320, …

### Python 3 — 43 bytes

```python
a=n=1
while[print(a-n*a+n*(a:=a*n+1))]:n+=1
```

**How it works**

- 2/(1−x)³ = Σ (k+2)(k+1)·x^k = Σ (k+2)!·x^k/k!, so multiplying by
  e^x = Σ x^j/j! gives a(n) = Σ_{k=0}^{n} (k+2)!·C(n,k).
- Let b(n) = Σ_k k!·C(n,k), which is [A000522](../../A000xxx/A000522/):
  b(0) = 1, b(n) = n·b(n−1) + 1. Pascal's rule
  C(n+1,k) − C(n,k) = C(n,k−1) turns a difference of such sums into a
  shift: Σ_k (k+1)!·C(n,k) = b(n+1) − b(n) = n·b(n) + 1, which is
  [A001339](../A001339/), and its difference in turn is
  a(n) = A001339(n+1) − A001339(n) = (n+1)·b(n+1) − n·b(n).
- The loop keeps a = b(n) and a counter one ahead (it holds n + 1).
  `a-n*a` reads the old value first: b(n) − (n+1)·b(n) = −n·b(n). Then
  the walrus makes a = b(n+1) = (n+1)·b(n) + 1, and (n+1)·b(n+1) is
  added, so the line printed is (n+1)·b(n+1) − n·b(n) = a(n).
- It starts from a = b(0) = 1 with the counter at 1: `a=n=1`.

**Notes**

- The closed form a(n) = (n² + n + 1)·b(n) + n + 1, as `a=n=0` /
  `while[print(n*(-~n*(a:=a*n+1)+1)-~a)]:n+=1`, is 48 bytes. The
  two-variable recurrence of [A001341](../A001341/) with the difference
  d(n) = a(n) − a(n−1), d(n+1) = n·d(n) + 3·a(n), is 45:
  `b=n=0;d=2` / `while[print(b:=b+d)]:d=n*d+3*b;n+=1`.
- Exact integer arithmetic, so the program is right for every n. It stops
  after a(1556): a(1557) is the first term with more than 4300 digits, the
  int-to-str limit of Python 3.11+.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001340), CC BY-SA 4.0.

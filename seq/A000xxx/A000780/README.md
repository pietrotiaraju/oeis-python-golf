# A000780

> a(n) = (n+1)!/2 + (n-1)(n-1)!.
> — [OEIS A000780](https://oeis.org/A000780)

Offset 1: 1, 4, 16, 78, 456, 3120, 24480, 216720, 2136960, 23224320, 275788800, …

### Python 3 — 41 bytes

```python
f=q=n=1
while[print(f*q)]:f*=n;n+=1;q-=~n
```

**How it works**

- Factor out (n−1)!: a(n) = (n−1)!·q(n) with
  q(n) = n(n+1)/2 + n − 1 = (n² + 3n − 2)/2 (the OEIS formula), and
  q(n+1) − q(n) = n + 2.
- `f` is (n−1)! and `q` is q(n), so the print is `f*q`. Then `f*=n` and
  `n+=1` step the factorial and the counter, and `q-=~n` adds the new
  n + 1, which is the old n + 2.
- At n = 1 everything is 1: 0! = 1 and q(1) = 1.
- Keeping q as a running sum avoids the polynomial in the print:
  `f=n=1` / `while[print(f*(n*n+3*n-2)//2)]:f*=n;n+=1` is 46 bytes, and
  carrying a(n) itself, a(n+1) = n·(a(n) + (n+2)·(n−1)!), is longer too.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 200 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 1558, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000780), CC BY-SA 4.0.

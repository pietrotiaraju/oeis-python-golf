# A000003

> Number of classes of primitive positive definite binary quadratic forms of
> discriminant D = -4n; or equivalently the class number of the quadratic
> order of discriminant D = -4n.
> — [OEIS A000003](https://oeis.org/A000003)

Offset 1: 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 3, 2, 2, 4, 2, 2, 4, 2, 3, 4, …

### Python 3 — 146 bytes

```python
import math
n=1
while[print(sum(math.gcd(a,b,c)+r<2for a in range(1,n+1)for b in range(-a,a)for c,r in[divmod(b*b+4*n,4*a)]if(c,-b)>=(a,0)))]:n+=1
```

**How it works**

- Every class of positive definite forms ax² + Bxy + cy² contains exactly one
  *reduced* form: |B| ≤ a ≤ c, with B ≥ 0 when |B| = a or a = c (Lagrange,
  Gauss). So a(n) counts reduced forms with B² − 4ac = −4n and
  gcd(a, B, c) = 1.
- The loop variable `b` is −B, so `range(-a,a)` gives B from −a+1 to a: B = a
  is kept and B = −a dropped, as the rule asks.
- `divmod(b*b+4*n,4*a)` gives c and a remainder `r`; the form exists only when
  r = 0 (odd B never divides evenly).
- `(c,-b)>=(a,0)` is "a < c, or a = c and B ≥ 0" in one tuple comparison.
- `math.gcd(a,b,c)+r<2` is true only when r = 0 and the form is primitive,
  so the divisibility test needs no `and`.
- a runs up to n, far past the real bound a ≤ √(4n/3); the extra values of a
  just never satisfy a ≤ c.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`
  (`n+=1` moves into the loop body).

**Notes**

- Each term costs about n² steps, so the program prints about 640 terms a
  minute; the bar for this sequence is 300 terms in 60 s.
- Bounding a with `range(1,isqrt(4*n)+1)` costs 10 bytes more (156, back on
  `from math import*` since it then uses two names) and gives about 6500
  terms a minute.
- `b` running over `range(1-a,a+1)` with the condition `(c,b)>=(a,0)` is the
  same program in 148 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 148 | first entry |
| 2026-11-05 | Python 3 | 147 | `while[print(...)]:` loop |
| 2026-11-05 | Python 3 | 146 | `import math` instead of `from math import*` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000003), CC BY-SA 4.0.

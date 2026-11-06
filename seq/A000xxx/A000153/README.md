# A000153

> a(n) = n*a(n-1) + (n-2)*a(n-2), with a(0) = 0, a(1) = 1.
> — [OEIS A000153](https://oeis.org/A000153)

Offset 0: 0, 1, 2, 7, 32, 181, 1214, 9403, 82508, 808393, 8743994, …

### Python 3 — 46 bytes

```python
n=a=0;s=1
while[print(a)]:a=s-a;s=n*s+3*a;n+=1
```

**How it works**

- At step n the recurrence for the next term is
  a(n+2) = (n+2)·a(n+1) + n·a(n). Keeping the pair (a(n), a(n+1)) gives
  `a,b=b,n*(a+b)+b+b` (48 bytes, the first entry).
- Here the second variable is the sum s = a(n) + a(n+1) instead. The next
  sum is (n+3)·s − 3·a, where the n·a terms cancel, and that is
  n·s + 3·(s − a). Since s − a is exactly the next term, the update splits
  into two short statements: `a=s-a` first, then `s=n*s+3*a` with the new a.
  No tuple assignment and no parentheses: two bytes saved.
- The start (a, s) = (0, 1) is (a(0), a(0) + a(1)); at n = 0 the old s is
  multiplied by 0, so only a = 1 − 0 = 1 matters for the next step.
- `while[print(a)]:` is a byte under `while 1:print(a);`: the one-element
  list `[None]` is truthy.
- Folding the counter into the update with `(n:=n+1)` costs two bytes more
  than `;n+=1`, since n would have to start at −1.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (251 terms) prints at once; the program stops after about 1558 terms,
  when a(n) passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 48 | first entry |
| 2026-11-06 | Python 3 | 46 | track the sum a(n)+a(n+1) instead of a(n+1) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000153), CC BY-SA 4.0.

# A000153

> a(n) = n*a(n-1) + (n-2)*a(n-2), with a(0) = 0, a(1) = 1.
> — [OEIS A000153](https://oeis.org/A000153)

Offset 0: 0, 1, 2, 7, 32, 181, 1214, 9403, 82508, 808393, 8743994, …

### Python 3 — 48 bytes

```python
n=a=0;b=1
while[print(a)]:a,b=b,n*(a+b)+b+b;n+=1
```

**How it works**

- At step n the pair (a, b) holds (a(n), a(n+1)). The recurrence for the
  next term is a(n+2) = (n+2)·a(n+1) + n·a(n), which regroups as
  n·(a+b) + 2b: one product instead of two.
- `b+b` is the same length as `2*b`; shifting the counter instead gives
  n·(a+b) + b − a (counter from 1) or n·(a+b) − 2a (counter from 2),
  both the same length again.
- `while[print(a)]:` is a byte under `while 1:print(a);`: the one-element
  list `[None]` is truthy.
- Folding the counter into the update (`a,b,n=b,…,n+1`) or into the loop
  test (`[print(a),n:=n+1]`) each costs one byte more than `;n+=1`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (251 terms) prints at once; the program stops after about 1558 terms,
  when a(n) passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000153), CC BY-SA 4.0.

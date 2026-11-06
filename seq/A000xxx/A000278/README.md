# A000278

> a(n) = a(n-1) + a(n-2)^2 for n >= 2 with a(0) = 0 and a(1) = 1.
> — [OEIS A000278](https://oeis.org/A000278)

Offset 0: 0, 1, 1, 2, 3, 7, 16, 65, 321, 4546, …

### Python 3 — 35 bytes

```python
a,b=0,1
while[print(a)]:a,b=a+b,a*a
```

**How it works**

- `a` is a(n) and `b` is a(n−1)², so the next term is a+b and the next
  `b` is the square of the current a. The tuple assignment evaluates both
  right-hand sides before storing, so `a*a` still sees the old a.
- At n = 0 the state is a = a(0) = 0 and b = a(−1)² = 1 (the recurrence
  run backwards from a(1) = a(0) + a(−1)² = 1). This is the same state
  update as Peter Luschny's SageMath generator on the OEIS page.
- `while[print(a)]:` prints before each update: `[None]` is a non-empty
  list, so the loop never ends, one byte under `while 1:print(a);`.

**Notes**

- Exact integer arithmetic, correct for every n. The digit count grows by
  a factor of about √2 per term, so the program stops after a(29) (3747
  digits), when a(30) (5153 digits) passes the 4300-digit int-to-str limit
  of Python 3.11+. The bar is the whole b-file (26 terms) in 60 s.
- Starting one step early also gives 35 bytes: with the state (a(n−1),
  a(n)) the extension backwards is a(−1) = −1, a(−2) = ±1, so
  `p=q=-1` / `while 1:p,q=q,q+p*p;print(q)` saves one byte on the setup
  and loses it on the loop, since the print now has to come after the
  update. With the print before the update, equal seeds in either layout
  would both have to be a(0) = 0, and (0, 0) stays at 0 forever.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000278), CC BY-SA 4.0.

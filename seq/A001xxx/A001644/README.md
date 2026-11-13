# A001644

> a(n) = a(n-1) + a(n-2) + a(n-3), a(0)=3, a(1)=1, a(2)=3.
> — [OEIS A001644](https://oeis.org/A001644)

Offset 0: 3, 1, 3, 7, 11, 21, 39, 71, 131, 241, 443, 815, 1499, 2757, 5071, …

### Python 3 — 39 bytes

```python
l=3,1,3
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` holds 3 consecutive terms, a(n) to a(n+2), starting from the
  data's a(0) to a(2) = 3, 1, 3.
- `*l,sum(l)` builds the 4 terms a(n) to a(n+3): the old 3 and
  `sum(l)` = a(n) + a(n+1) + a(n+2), which is a(n+3) by the tribonacci recurrence.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 3, a(n+1) to a(n+3), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(0).
- Integers are exact, so every term is right, for every n.

**Notes**

- This is the program of [A000073](../../A000xxx/A000073/) with the seeds
  3, 1, 3. a(n) is the sum of the n-th powers of the roots of
  x³ = x² + x + 1 (Binet's formula in the entry).
- The three-variable tuple `a=c=3;b=1` / `while[print(a)]:a,b,c=b,c,a+b+c`
  is 41 bytes; the tribonacci update has no shorter chain of in-place
  statements (searched for [A000213](../../A000xxx/A000213/)).
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(16247), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1001 terms (a(0) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001644), CC BY-SA 4.0.

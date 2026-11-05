# A000085

> Number of self-inverse permutations on n letters, also known as involutions; number of standard Young tableaux with n cells.
> — [OEIS A000085](https://oeis.org/A000085)

Offset 0: 1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496, 35696, 140152, 568504, 2390480, 10349536, …

### Python 3 — 40 bytes

```python
a=b=n=1
while[print(a)]:a,b=b,b+n*a;n+=1
```

**How it works**

- The recurrence from the OEIS page: a(0) = a(1) = 1 and
  **a(n) = a(n − 1) + (n − 1)·a(n − 2)**. In an involution on n letters,
  the letter n is either fixed (an involution of the other n − 1 letters)
  or swapped with one of the other n − 1 letters (an involution of the
  remaining n − 2).
- Before each update `a` = a(k), `b` = a(k + 1) and `n` = k + 1, so
  `b+n*a` = a(k + 1) + (k + 1)·a(k) = a(k + 2). The pair shifts one step
  and `n+=1` keeps the invariant.
- `a=b=n=1` is a(0), a(1) and the first multiplier in one chained
  assignment. `while[print(a)]` prints and loops forever because `[None]`
  is a non-empty list.

**Notes**

- Folding the counter into the update, `a,b=b,b+a*(n:=n+1)`, needs n to
  start at 0 (`a=b=1;n=0`), 4 bytes more in all. Growing a list,
  `A+=A[-1]+~-len(A)*A[-2],`, is longer still.
- Exact integer arithmetic, so the program is right for every n.
  a(2835) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit, which is not
  counted as a failure.
- The b-file has 801 terms (n = 0 to 800); all 2835 terms up to the limit
  print in well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000085), CC BY-SA 4.0.

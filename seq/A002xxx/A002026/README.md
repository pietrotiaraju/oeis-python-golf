# A002026

> Generalized ballot numbers (first differences of Motzkin numbers).
> — [OEIS A002026](https://oeis.org/A002026)

Offset 0: 0, 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610, 9713, 26324, 71799, 196938, 542895, 1503312, …

### Python 3 — 51 bytes

```python
e=0;s=k=4
while[print(e)]:s+=3*e+(e:=s-3*s//k);k+=1
```

**How it works**

- a(n) = M(n + 1) − M(n) with M the Motzkin numbers
  ([A001006](../../A001xxx/A001006/)). Their recurrence
  (n + 3)·M(n + 1) = (2n + 3)·M(n) + 3n·M(n − 1) rearranges to
  **(n + 3)·a(n) = n·(M(n) + 3M(n − 1))**, so with s = M(n) + 3M(n − 1)
  and k = n + 3, a(n) = s − 3s/k. Since a(n) is an integer, 3s/k is one
  too, and `s-3*s//k` is exact.
- s moves on as s(n + 1) = M(n + 1) + 3M(n) = s + a(n) + 3·a(n − 1).
  The loop keeps s = s(n + 1), e = a(n) and k = n + 4: it prints e, and
  `s+=3*e+(e:=s-3*s//k)` adds 3·a(n) and the new a(n + 1) to s while
  storing a(n + 1) in e (the right side reads the old s and e).
- Start with a(0) = 0, s(1) = M(1) + 3M(0) = 4 and k = 4.

**Notes**

- Printing the new term inside the `while` header,
  `s=e=1;k=3` / `while[print(d:=s-3*s//k)]:s+=3*e+(e:=d);k+=1`, is
  54 bytes; pairing M(n), M(n + 1) and printing their difference is 59.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 2106 terms (n = 0 to 2105); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 54 | first entry |
| 2026-11-19 | Python 3 | 51 | print the term computed one pass earlier (-3) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002026), CC BY-SA 4.0.

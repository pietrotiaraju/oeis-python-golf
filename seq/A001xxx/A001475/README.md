# A001475

> a(n) = a(n-1) + n * a(n-2), where a(1) = 1, a(2) = 2.
> — [OEIS A001475](https://oeis.org/A001475)

Offset 1: 1, 2, 5, 13, 38, 116, 382, 1310, 4748, 17848, 70076, 284252, 1195240, 5174768, …

### Python 3 — 42 bytes

```python
a=1;b=n=2
while[print(a)]:n+=1;a,b=b,b+n*a
```

**How it works**

- The recurrence of the definition. Before each print `a` = a(k),
  `b` = a(k+1) and `n` = k+1; `n+=1` makes it k+2, so `b+n*a` is
  a(k+1) + (k+2)·a(k) = a(k+2), and the pair shifts.
- The start a(1) = 1, a(2) = 2 with n = 2 is `a=1;b=n=2`. Running the
  recurrence backwards would need a(0) = 1/2, so no phantom start with
  integers works.

**Notes**

- a(n) = [A000085](../A000085/)(n+1)/2, half the number of involutions
  of n+1 points: c(n) = A000085(n+1) satisfies the same
  c(n) = c(n−1) + n·c(n−2) (it is A000085's recurrence shifted), and
  c(1) = 2 = 2·a(1), c(2) = 4 = 2·a(2). Printing `b>>1` from the A000085
  loop is 45 bytes.
- Exact integer arithmetic, so the program is right for every n; the
  4300-digit int-to-str limit stops it at a(2834).
- The b-file has 795 terms (n = 1 to 795); all of them print in well under
  a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001475), CC BY-SA 4.0.

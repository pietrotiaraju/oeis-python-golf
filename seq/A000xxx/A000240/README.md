# A000240

> Rencontres numbers: number of permutations of [n] with exactly one fixed point.
> — [OEIS A000240](https://oeis.org/A000240)

Offset 1: 1, 0, 3, 8, 45, 264, 1855, 14832, 133497, 1334960, …

### Python 3 — 36 bytes

```python
a=n=1
while[print(a*n)]:a=a*n^1;n+=1
```

**How it works**

- Fixing one of the n points and deranging the other n − 1 gives
  a(n) = n·D(n−1), where D is the derangement sequence
  [A000166](../A000166/).
- `a` runs through D(0), D(1), D(2), … with the recurrence
  D(m) = m·D(m−1) xor 1 from the [A000166](../A000166/) record, and the
  loop prints `a*n` before stepping. That is 2 bytes more than A000166.
- Carrying a(n) itself, with a(n+1) = (a(n) xor 1)·(n+1), saves the `*n`
  in the print but needs parentheses in `n+=1;a=(a^1)*n`: also 36 bytes.
  Printing D(n) xor 1, which equals n·D(n−1), costs 38, because the loop
  then has to start at D(1) = 0 with n = 2 (`a=0;n=2`).

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (100 terms) prints at once; the program stops after a(1558), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000240), CC BY-SA 4.0.

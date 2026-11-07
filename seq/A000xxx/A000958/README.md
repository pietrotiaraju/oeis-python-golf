# A000958

> Number of ordered rooted trees with n edges having root of odd degree.
> — [OEIS A000958](https://oeis.org/A000958)

Offset 1: 1, 1, 3, 8, 24, 75, 243, 808, 2742, 9458, 33062, 116868, 417022, …

### Python 3 — 55 bytes

```python
b=c=1;m=2
while[print(b)]:m+=1;b=c+(c:=4*c-6*c//m)-b>>1
```

**How it works**

- The entry gives a(n) = F(n) + F(n+1) with F the Fine numbers
  ([A000957](../A000957/)), and F satisfies C(n) = 2F(n+1) + F(n) for
  n ≥ 1 (C = Catalan numbers). So a(n) = (C(n) + F(n))/2 and
  F(n+1) = C(n) − a(n), which gives a recurrence for a alone:
  **a(n+1) = (C(n+1) + C(n) − a(n))/2**.
- `c` holds C(n) and `m` is n + 2 after its increment, as in
  [A000108](../A000108/): `4*c-6*c//m` is the next Catalan number
  (exact division). The walrus inside the update reads the old C(n)
  first, then stores C(n+1), so one expression uses both.
- Start: a(1) = C(1) = 1 and m = 2.

**Notes**

- Exact integer arithmetic; the division by 2 is exact because
  C(n+1) + C(n) − a(n) = C(n+1) + F(n+1) = 2a(n+1).
- The 4300-digit int-to-str limit of Python 3.11+ stops it after
  a(7152), well past the b-file (1000 terms), which prints in about 0.1 s;
  the bar is the whole b-file.
- Keeping F and printing `c+a>>1` is 57 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000958), CC BY-SA 4.0.

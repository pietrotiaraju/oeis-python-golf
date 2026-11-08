# A001048

> a(n) = n! + (n-1)!.
> — [OEIS A001048](https://oeis.org/A001048)

Offset 1: 2, 3, 8, 30, 144, 840, 5760, 45360, 403200, 3991680, …

### Python 3 — 35 bytes

```python
a=n=1
while[print(a*-~n)]:a*=n;n+=1
```

**How it works**

- n! + (n−1)! = (n−1)!·(n + 1). `a` holds (n−1)!: it starts at 0! = 1 for
  n = 1 and is multiplied by n before n steps, as in
  [A000142](../../A000xxx/A000142/).
- `a*-~n` is a·(n + 1): `-~n` is n + 1 with no parentheses, because the
  unary operators bind tighter than `*`.

**Notes**

- Printing the two factorials as a sum with the walrus,
  `while[print(a+(a:=a*n))]:n+=1`, is a tie (35 bytes); keeping n! and
  printing `a+a//n` is 36.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 100 terms (a(1) to a(100)); the bar is the whole b-file in
  60 s.
- a(1559) is the first term with more than 4300 digits (4303) and Python's
  int-to-str limit stops the printing there; a(1558) has 4300.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001048), CC BY-SA 4.0.

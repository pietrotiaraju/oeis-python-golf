# A001286

> Lah numbers: a(n) = (n-1)*n!/2.
> — [OEIS A001286](https://oeis.org/A001286)

Offset 2: 1, 6, 36, 240, 1800, 15120, 141120, 1451520, 16329600, 199584000, …

### Python 3 — 35 bytes

```python
f=n=1
while[print(n*f)]:n+=1;f*=n+1
```

**How it works**

- The loop variable `n` is k = n − 1 (k = 1, 2, …), and `f` holds
  (k + 1)!/2, that is n!/2. So `n*f` is (n − 1)·n!/2 = a(n). The start
  k = 1, f = 1 = 2!/2 prints a(2) = 1.
- After `n+=1` the new k needs f = (k + 1)!/2, the old value times k + 1,
  which is `f*=n+1`. Everything is exact integer arithmetic, so the program
  is right for every n.
- `while[print(…)]:` prints before each pass: `[None]` is a non-empty list.

**Notes**

- Keeping n itself, `f=1;k=2` / `while[print(~-k*f)]:k+=1;f*=k`, is
  37 bytes; a walrus in the print, `f=1;k=0` /
  `while[print(f*(k:=k+1))]:f*=k+2`, is 39.
- a(1558) is the first term with more than 4300 digits, so there the
  program stops on Python's int-to-str limit (an interpreter limit, not a
  wrong term).
- The b-file has 99 terms (n = 2 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001286), CC BY-SA 4.0.

# A000123

> Number of binary partitions: number of partitions of 2n into powers of 2.
> — [OEIS A000123](https://oeis.org/A000123)

Offset 0: 1, 2, 4, 6, 10, 14, 20, 26, 36, 46, 60, 74, 94, 114, 140, 166, 202, 238, 284, 330, …

### Python 3 — 40 bytes

```python
q=[s:=1]
for x in q:print(s);s+=x;q+=s,s
```

**How it works**

- The program uses the recurrence a(0) = 1, a(n) = a(n−1) + a(⌊n/2⌋)
  from the OEIS entry (proved in [A018819](https://oeis.org/A018819)).
  So each step adds a(⌊n/2⌋), and those increments, for n = 1, 2, 3, …,
  are a(0), a(1), a(1), a(2), a(2), a(3), a(3), …: every term is used
  twice, except a(0), which is used once.
- `q` is that list of increments. It starts as `[1]` (a(0) once), and
  every new term `s` goes onto its end twice (`q+=s,s`).
- `s` holds the current term. Each pass prints it and adds the next
  increment `x`, so that `s` becomes the next term.
- `for x in q` walks a list that keeps growing. Each pass adds two
  increments and uses one, so the loop never runs out and the program
  never stops. When a(n) is computed, the increment it needs is
  a(⌊n/2⌋), which was added long before.
- `q=[s:=1]` sets `s` and `q` in one go: the walrus is 1 byte shorter
  than `s=1;q=[1]`.
- Only integer additions are involved, so every term is exact, for
  every n. `q` grows to about 2n numbers, which is the only memory cost.

**Notes**

- Keeping the sequence itself in a list,
  `a=[1]` + `for x in a:print(x);a+=x+a[len(a)//2],`, is 44 bytes:
  `a[len(a)//2]` costs more than the increment list.
- Taking the increments off the front of the list instead,
  `q=[s:=1]` + `while[print(s)]:s+=q.pop(0);q+=s,s`, is 43 bytes, and
  slower: `pop(0)` shifts the whole list, so the b-file takes about 4 s
  instead of under one.
- The b-file has the 65 537 terms a(0)..a(65536), all printed in under
  a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000123), CC BY-SA 4.0.

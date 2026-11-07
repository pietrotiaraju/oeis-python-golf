# A000523

> a(n) = floor(log_2(n)).
> — [OEIS A000523](https://oeis.org/A000523)

Offset 1: 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, …

### Python 3 — 36 bytes

```python
n=1
while[print(len(bin(n))-3)]:n+=1
```

**How it works**

- For n ≥ 1, `bin(n)` is `0b` followed by ⌊log₂ n⌋ + 1 binary digits, so
  its length minus 3 is ⌊log₂ n⌋.
- `len(bin(n))-3` is 3 bytes under `n.bit_length()-1`.

**Notes**

- Two other 36-byte programs print each value k as a block of 2^k lines:
  the growing queue `l=[0]` / `for k in l:print(k);l+=k+1,k+1` (each k
  read from the list appends two copies of k+1), and
  `k=0` / `while[*map(print,[k]*2**k)]:k+=1`.
- Exact integer arithmetic, so the program is right for every n; binary
  conversion is not subject to the 4300-digit int-to-str limit.
- The b-file has 105 terms (up to a(105)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000523), CC BY-SA 4.0.

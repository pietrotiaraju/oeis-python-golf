# A000133

> Number of Boolean functions of n variables.
> — [OEIS A000133](https://oeis.org/A000133)

Offset 1: 2, 5, 30, 2288, 67172352, 144115192303714304, …

### Python 3 — 41 bytes

```python
v=j=1
while[print((v+2)*j-v)]:v*=j;j*=2*j
```

**How it works**

- OEIS gives a(n) = (2^(2ⁿ) + (2ⁿ − 1)·2^(2^(n−1)+1)) / 2^(n+1)
  (Sean A. Irvine). This is Burnside's lemma for functions counted up to
  complementing any set of inputs (x ↦ x ⊕ a) and complementing the output,
  a group of order 2^(n+1); a brute-force orbit count agrees for n ≤ 4.
- With k = 2^(n−1), the three pieces are powers of two:
  a(n) = 2^(2k−n−1) + 2^k − 2^(k−n).
- The program keeps j = 2^(k−1) and v = 2^(k−n) (an integer, since
  2^(n−1) ≥ n). Then 2^(2k−n−1) = v·j, so a(n) = v·j + 2j − v = (v+2)·j − v.
- From n to n + 1, k doubles: j becomes 2j² and v becomes 2^(2k−n−1) = v·j.
  That is `v*=j;j*=2*j`, in that order. Both start at 1 for n = 1.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`.

**Notes**

- a(n) has about 0.3·2ⁿ digits, so the 11 terms of the b-file print at once;
  the bar is the whole b-file in 60 s.
- a(14) has 4928 digits, so CPython 3.12 stops there with its 4300-digit
  int-to-str limit (an interpreter limit, not counted as a failure).
- Keeping u = 2^k instead of j makes the update `u*=u` shorter, but the
  formula and the start values `v=1;u=2` cost more: 42 bytes at best. The
  direct (u, 4k) form u·(u−2)/(4k) + u is 44 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000133), CC BY-SA 4.0.

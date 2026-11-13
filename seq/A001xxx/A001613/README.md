# A001613

> Delete all odd digits from n.
> — [OEIS A001613](https://oeis.org/A001613)

Offset 0: 0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 0, 0, 2, 0, 4, 0, 6, 0, 8, 0, 20, 2, …

### Python 3 — 61 bytes

```python
n=0
while[print(int(bytes(c for c in b'0%d'%n if~c&1)))]:n+=1
```

**How it works**

- `b'0%d'%n` is the decimal expansion of n as a bytes object, with a 0 in
  front. Iterating over bytes gives the character codes, 48 to 57, and a
  digit is even exactly when its code is (`0` is 48), so `if~c&1` (1 when c
  is even) keeps the even digits and drops the odd ones.
- `int` accepts a bytes object and leading zeros, so `int(bytes(…))` is the
  number the kept digits spell.
- The leading 0 handles numbers with no even digit at all (1, 3, 11, 135, …):
  without it `int(b'')` would raise, with it they give 0, which is what the
  OEIS data shows (a(1) = a(3) = a(11) = 0).
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Other ways to drop the odd digits, each as a whole program:
  `bytes(filter(b'02468'.count,b'0%d'%n))` 66 bytes,
  `(b'0%d'%n).translate(None,b'13579')` 63, `re.sub('[13579]','','0%d'%n)`
  with its import 66, and the recursion f(n) = 10·f(⌊n/10⌋) + d when the
  last digit d is even, f(⌊n/10⌋) when it is odd, 77.
- The program follows the definition for every n.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001613), CC BY-SA 4.0.

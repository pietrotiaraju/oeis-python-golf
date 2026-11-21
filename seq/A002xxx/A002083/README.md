# A002083

> Narayana-Zidek-Capell numbers: a(n) = 1 for n <= 2. Otherwise a(2n) = 2a(2n-1), a(2n+1) = 2a(2n) - a(n).
> — [OEIS A002083](https://oeis.org/A002083)

Offset 1: 1, 1, 1, 2, 3, 6, 11, 22, 42, 84, 165, 330, 654, 1308, 2605, 5210, …

### Python 3 — 48 bytes

```python
a=[1]
while[print(a[-1])]:a+=sum(a[len(a)//2:]),
```

**How it works**

- **Sum rule.** For n ≥ 2, a(n) is the sum of the ⌊n/2⌋ terms before it
  (a formula of the entry). It follows from the definition by induction:
  write S(n) = a(n−⌊n/2⌋) + … + a(n−1). Then S(2) = a(1) = 1 = a(2),
  S(2m) = S(2m−1) + a(2m−1) = 2a(2m−1) = a(2m), and
  S(2m+1) = S(2m) − a(m) + a(2m) = 2a(2m) − a(m) = a(2m+1), each time
  using a(j) = S(j) for the smaller indices.
- **Code.** The list `a` holds a(1), …, a(n−1), so L = len(a) = n − 1 and
  `a[len(a)//2:]` is its last L − ⌊L/2⌋ = ⌊n/2⌋ entries. Their sum is
  appended as a(n), and the loop prints the newest entry.

**Notes**

- The definition itself (`2*a[-1]`, minus `a[n//2]` at odd n) needs the
  index n and the special start a(2) = 1, and is longer.
- Each term costs a sum over half the list; the whole b-file (3325 terms,
  about 1000 digits at the end) takes about a second. The 4300-digit
  int-to-str limit stops the output near n = 14300. The bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002083), CC BY-SA 4.0.

# A000981

> Numbers beginning with letter 'n' in English.
> — [OEIS A000981](https://oeis.org/A000981)

Offset 1: 9, 19, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 900, 901, 902, 903, …

### Python 3 — 59 bytes

```python
n=0
while 1:n+=1;c=f'{n:_}_';c[c[:3:2]=='1_']>'8'!=print(n)
```

**Which names**

- US names as in the OEIS data: 100 is "one hundred", 1900 is "one
  thousand nine hundred" (not "nineteen hundred"), and there is no "and".
- Split n into groups of three digits from the right; every name of
  n ≥ 1000 starts with the name of the leading group, then a scale word,
  so only the leading group matters, whatever the large scales are called
  (see [A000873](../A000873/)).
- The n-words are nine, nineteen, ninety and nine hundred: the leading
  group starts with the digit 9, or it is exactly 19. Every other group
  that starts with 1 reads "one …", "ten", "eleven" or another teen.

**How it works**

- `f'{n:_}_'` writes n with `_` between the groups and one more `_` at the
  end: 19000 → `19_000_`.
- `c[:3:2]` is the first character and the one at index 2; it is `1_`
  exactly when the leading group has two digits and starts with 1. Then
  `c[True]`, the second digit, is tested; otherwise `c[0]`, the leading
  digit. That digit must be 9: `>'8'`, one byte under `=='9'` or `in'9'`.
- `…>'8'!=print(n)` prints only when the test is true (the chain stops at
  the first false comparison), as on the sibling pages
  [A000852](../A000852/), [A000867](../A000867/) and
  [A000870](../A000870/).

**Notes**

- The rule is right for every n, and the program tests every n: about
  110000 terms in 10 s here.
- The b-file has 10000 terms (up to a(10000) = 97887); the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000981), CC BY-SA 4.0.

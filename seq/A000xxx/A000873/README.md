# A000873

> Numbers beginning with letter 'e' in English.
> — [OEIS A000873](https://oeis.org/A000873)

Offset 1: 8, 11, 18, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 800, 801, 802, 803, …

### Python 3 — 67 bytes

```python
n=0
while 1:n+=1;c=f'{n:_}_';c[(k:=c[::2])<'2']in'1:8'<=k!=print(n)
```

**Which names**

- US names as in the OEIS data: 100 is "one hundred" (not "a hundred"),
  1100 is "one thousand one hundred" (not "eleven hundred"), and there is
  no "and".
- Split n into groups of three digits from the right; the leading group k
  has 1 to 3 digits. Every name of n ≥ 1000 starts with the name of k, then
  the scale word. So the first word is that of k: the hundreds digit when k
  has three digits ("eight hundred …"), ten … nineteen when k is 10–19, a
  tens word twenty … ninety when k ≥ 20 has two digits, a digit name
  otherwise.
- The scale words never come first, so this holds whatever the large
  scales are called: short scale, long scale ("one thousand million") or
  the systematic names past vigintillion. The rule, and so the program, is
  right for every n.
- The e-words are eight, eighty, eight hundred (leading digit 8) and
  eleven, eighteen (leading group 11 or 18). A leading 1 otherwise gives
  "one", "ten", "twelve" or another teen, so the test is: leading digit 8,
  or leading digit 1 in a two-digit leading group whose second digit is 1
  or 8.

**How it works**

- `f'{n:_}_'` writes n with `_` between the groups and one more `_` at the
  end: 12345 → `12_345_`. `k=c[::2]` takes characters 0, 2, 4, …: the
  leading digit, then the character at index 2, which is `_` exactly when
  the leading group has two digits.
- `k<'2'` means the leading digit is 1, and then `c[1]` is the second
  digit; otherwise `c[0]` is the leading digit. That character must be in
  `'1:8'`, that is, 1 or 8 (`:` never occurs).
- The same string is the threshold in `'1:8'<=k`: `:` sorts after the
  digits and before `_`. With a leading 1, k = `1_…` (a two-digit group) is
  above it and `1`, `1` + digit are below, so only the groups 11 and 18
  pass; with a leading digit 2–9, k is always above it, so only 8 passes.
- `…<=k!=print(n)` continues the chain: Python evaluates `print(n)` only
  when both tests are true, and then `k!=None` is true too. That is
  `and print(n)` in 2 bytes less, and it saves the space `k and` would
  need.

**Notes**

- The digit-index trick of [A000852](../A000852/) and
  [A000867](../A000867/), `c[c[:3:2]=='1_']in…`, does not work here: the
  digit 1 must pass after a leading 1 in the group 11 but fail as a leading
  digit (one).
- A grouped string with `,` gives another 67-byte form,
  `c=f'{n:,},,';c[-(c[:3]in'18,11,')]in'8,'!=print(n)`: for the groups 11
  and 18 the index −1 picks the final `,`; the doubled `,` keeps `1,` (n = 1)
  from matching inside `11,`, and the stray match `8,1` starts with 8
  anyway. With `import re`, the regular expression
  `re.match('8|1[18],',f'{n:,},')and print(n)` is 69 bytes.
- The program tests every n: about 3.1 million terms in 60 s here, every
  term up to 18999999 (the next one is 8·10⁷).
- The b-file has 10000 terms (up to a(10000) = 86886); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000873), CC BY-SA 4.0.

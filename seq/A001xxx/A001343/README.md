# A001343

> Number of (unordered) ways of making change for n cents using coins of 5, 10, 20, 50, 100 cents.
> — [OEIS A001343](https://oeis.org/A001343)

Offset 0: 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4, …

### Python 3 — 70 bytes

```python
v=1;a=[0]*500
while 1:a+=(v:=v+a[-5*c]for c in b'\n2d');print(v);v=0
```

The coin table holds two raw control bytes (0x05 and 0x14) that a
browser does not show. Byte for byte, the second line is

```text
while 1:a+=(v:=v+a[-5*c]for c in b'<05>\n2d<14>');print(v);v=0
```

where `<05>` stands for the single byte 0x05, and so on. The table lists the
coins: 5, 10 (`\n`), 50 (`2`), 100 (`d`) and 20. With the raw bytes escaped,
`b'\5\n2d\24'`, the program is 73 bytes.

**How it works**

- **Stages.** Number the coin kinds c₁, …, c₅ in the order of the table, and
  let Aⱼ(m) be the number of ways to pay m cents with the first j kinds,
  with Aⱼ(m) = 0 for m < 0; with no coins at all only m = 0 can be paid, so
  A₀(m) = 1 if m = 0 and 0 otherwise. A way either has no coin of kind j, or
  has one, and the rest is a way to pay m − cⱼ, so
  Aⱼ(m) = Aⱼ₋₁(m) + Aⱼ(m − cⱼ), and a(n) = A₅(n). (In series terms each
  stage divides by 1 − x^cⱼ, so the order of the kinds does not matter.)
- **One pass per n.** v starts as A₀(n): `v=1` before the loop for n = 0,
  and `v=0` after each print for every later n. The generator then runs
  through the table: for c = cⱼ, `v:=v+a[-5*c]` adds Aⱼ(n − cⱼ) to v, which
  turns Aⱼ₋₁(n) into Aⱼ(n). A walrus inside a generator binds the outer `v`,
  so after the last coin v = A₅(n) = a(n), which is printed.
- **Reading the list while it grows.** `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between, so each
  Aⱼ(n) is stored before the next stage is computed. When Aⱼ(n) is computed
  `a` holds 500 + 5n + (j − 1) entries, and Aⱼ(n − c) is entry
  500 + 5(n − c) + (j − 1), exactly 5c from the end: `a[-5*c]`. If
  n − c < 0, that entry is one of the 500 leading zeros, as it should be:
  its index lies between 0 (as 500 = 5·100) and 499.
- **Bytes table.** Iterating over `bytes` gives ints, so no `ord` is needed,
  and Python accepts raw control bytes inside a bytes literal (only NUL, the
  line breaks, the backslash and the quote are not allowed there).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- All coins are multiples of 5, so a(n) = 0 unless 5 divides n; the stages
  produce these zeros by themselves. Working in units of 5 cents instead
  (coins 1, 2, 4, 10, 20 with `while v:=1:`) and printing four zeros after
  each term with `print('%d'%v+'\n0'*4)` is 76 bytes.
- Putting a 1 at the front of the zeros instead of `v=1` (with 100 first in
  the table, its stage reads it once, at n = 0) and resetting in the header
  with `while[v:=0]:` is also 70 bytes; counting with an added penny and
  printing the difference `v-a[-6]` of two consecutive totals is 71, the
  comprehension form of [A001301](../A001301/) (offsets 5c minus the slot,
  two of them above 127, so `ord` on a `str`) is 72, and the coins as a
  tuple make 76. The quartic quasi-polynomial of the entry's PARI program is
  far longer.
- The 20 sits last in the table so that its escape `\24` is not followed by
  a digit.
- a(n) ≤ (n + 1)⁴, since the numbers of the four smaller coins fix the
  number of 100s, so the terms stay far below the 4300-digit int-to-str
  limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001343), CC BY-SA 4.0.

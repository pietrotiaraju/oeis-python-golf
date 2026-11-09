# A001314

> Number of (unordered) ways of making change for n cents using coins of 2, 5 (two kinds), 10, 20, 50 cents.
> — [OEIS A001314](https://oeis.org/A001314)

Offset 0: 1, 0, 1, 0, 1, 2, 1, 2, 1, 2, 5, 2, 5, 2, 5, 8, 5, 8, 5, 8, 15, …

### Python 3 — 71 bytes

```python
v=1;a=[0]*300
while 1:a+=(v:=v+a[-6*c]for c in b'\n2');print(v);v=0
```

The coin table holds four raw control bytes (0x02, 0x05, 0x05 and 0x14) that a
browser does not show. Byte for byte, the second line is

```text
while 1:a+=(v:=v+a[-6*c]for c in b'<02><05><05>\n2<14>');print(v);v=0
```

where `<02>` stands for the single byte 0x02, and so on. The table lists the
coins: 2, 5, 5, 10 (`\n`), 50 (`2`) and 20. With the raw bytes escaped,
`b'\2\5\5\n2\24'`, the program is 76 bytes.

**How it works**

- **Stages.** Number the coin kinds c₁, …, c₆ in the order of the table (5
  appears twice, once for each kind), and let Aⱼ(m) be the number of ways to
  pay m cents with the first j kinds, with Aⱼ(m) = 0 for m < 0; with no
  coins at all only m = 0 can be paid, so A₀(m) = 1 if m = 0 and 0
  otherwise. A way either has no coin of kind j, or has one, and the rest is
  a way to pay m − cⱼ, so Aⱼ(m) = Aⱼ₋₁(m) + Aⱼ(m − cⱼ), and a(n) = A₆(n).
  (In series terms each stage divides by 1 − x^cⱼ, so the order of the kinds
  does not matter.)
- **One pass per n.** v starts as A₀(n): `v=1` before the loop for n = 0,
  and `v=0` after each print for every later n. The generator then runs
  through the table: for c = cⱼ, `v:=v+a[-6*c]` adds Aⱼ(n − cⱼ) to v, which
  turns Aⱼ₋₁(n) into Aⱼ(n). A walrus inside a generator binds the outer `v`,
  so after the last coin v = A₆(n) = a(n), which is printed.
- **Reading the list while it grows.** `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between, so each
  Aⱼ(n) is stored before the next stage is computed. When Aⱼ(n) is computed
  `a` holds 300 + 6n + (j − 1) entries, and Aⱼ(n − c) is entry
  300 + 6(n − c) + (j − 1), exactly 6c from the end: `a[-6*c]`. If
  n − c < 0, that entry is one of the 300 leading zeros, as it should be:
  its index lies between 0 (as 300 = 6·50) and 299.
- **Bytes table.** Iterating over `bytes` gives ints, so no `ord` is needed,
  and Python accepts raw control bytes inside a bytes literal (only NUL, the
  line breaks, the backslash and the quote are not allowed there).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The two kinds of 5-cent coin are two stages with the same c = 5, so the
  table holds 5 twice; this is the generating function
  1/((1 − x²)(1 − x⁵)²(1 − x¹⁰)(1 − x²⁰)(1 − x⁵⁰)).
- Putting a 1 at the front of the zeros instead of `v=1` (with 50 first in
  the table, its stage reads it once, at n = 0) and resetting in the header
  with `while[v:=0]:` is also 71 bytes. Counting with an added penny,
  `while v:=1:` as in [A001313](../A001313/), and printing the difference
  `v-a[-7]` of two consecutive totals is 72; the comprehension form of
  [A001301](../A001301/) (offsets 6c minus the slot) is 72, and the coins as
  a tuple make 76.
- The 20 sits last in the table so that its escape `\24` is not followed by
  a digit.
- a(n) ≤ (n + 1)⁵, since the numbers of the five other coins fix the number
  of 2s, so the terms stay far below the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001314), CC BY-SA 4.0.

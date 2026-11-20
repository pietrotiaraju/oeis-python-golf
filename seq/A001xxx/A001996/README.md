# A001996

> Number of partitions of n into parts 2, 3, 4, 5, 6, 7.
> — [OEIS A001996](https://oeis.org/A001996)

Offset 0: 1, 0, 1, 1, 2, 2, 4, 4, 6, 7, 10, 11, 16, 17, 23, 26, 33, 37, 47, 52, 64, 72, …

### Python 3 — 68 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[-i]for i in b'"	%'];print(v-a[-7])
```

The bytes literal holds 4 raw control bytes (0x12, 0x17, 0x09, 0x1A) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<12><17>"<09><1a>%'];print(v-a[-7])
```

where `<12>` stands for the single byte 0x12, and so on.

**How it works**

- **With pennies.** The coin-change template of [A001300](../A001300/)
  counts q(n), the partitions of n into parts 1, …, 7: pennies alone pay n
  in one way, and the coins c₁, …, c₆ = 3, 4, 6, 2, 5, 7 are added one at a
  time with Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ). A partition into parts 1, …, 7
  either has no 1, or dropping one 1 leaves a partition of n − 1, so
  q(n) = a(n) + q(n − 1) and a(n) = q(n) − q(n − 1).
- **One flat list.** `a` starts with 99 zeros and each pass appends row n,
  A₁(n), …, A₆(n). `a+=[…]` evaluates the comprehension before it extends
  `a`, so slot k of row n − c is 6c − k places before the end; for the
  coins in this order that is 18, 23, 34, 9, 26, 37, kept in a bytes
  literal (three of them raw control bytes, the others `"` and `%`, all
  clear of line breaks, the quote and the backslash).
- **The difference.** `while v:=1:` starts each row with A₀(n) = 1 and
  `v:=v+a[-i]` builds and stores the slots, so after the row v = q(n). The
  appended row is the last 6 entries, so `a[-7]` is the last slot of row
  n − 1, q(n − 1) (a leading zero for n = 0), and `print(v-a[-7])` prints
  a(n).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- Starting each row with 1 only at n = 0 instead (`a=[1]+[0]*41`,
  `while[v:=0]:` with the 7 first) costs the same 68 bytes. The closed form
  in the entry has a mod-7 term and is far longer.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001996), CC BY-SA 4.0.

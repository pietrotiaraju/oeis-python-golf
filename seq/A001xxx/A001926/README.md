# A001926

> G.f.: (1+x)^2/[(1-x)^4(1-x-x^2)^3].
> — [OEIS A001926](https://oeis.org/A001926)

Offset 0: 1, 9, 46, 177, 571, 1632, 4270, 10446, 24244, 53942, 115954, 242240, 494087, …

### Python 3 — 67 bytes

```python
a=[0]*99
while v:=1:a+=[v:=v+a[~i]for i in b'	'];print(v)
```

The bytes literal holds 11 raw control bytes (0x14, 0x09, 0x12, 0x07, 0x10,
0x05, 0x05, 0x03, 0x02, 0x01, 0x01) that a browser does not show. Byte for
byte, the second line is

```text
while v:=1:a+=[v:=v+a[~i]for i in b'<14><09><12><07><10><05><05><03><02><01><01>'];print(v)
```

where `<14>` stands for the single byte 0x14, and so on.

**How it works**

- **Definition.** The sequence is defined by its generating function,
  Riordan's (1 + x)²/((1 − x)⁴(1 − x − x²)³) from rook polynomials of
  discordant permutations. The program prints its coefficients, and all
  1001 terms of the b-file agree.
- **Filters.** Read the series as a cascade of filters fed with the all-ones
  series 1/(1 − x): dividing by 1 − x − x² is y(n) = u(n) + y(n − 1) +
  y(n − 2), multiplying by 1 + x is y(n) = u(n) + u(n − 1), and dividing by
  1 − x is a running sum y(n) = u(n) + y(n − 1). The program uses three
  Fibonacci filters, then 1 + x, three running sums and 1 + x again; the
  filters commute, so the order does not matter.
- **One flat list.** As in [A001300](../A001300/), each pass appends row n
  of K = 11 slots (each Fibonacci filter takes two). `a+=[…]` builds the
  whole row before extending `a`, so slot q of row n − r sits rK − q places
  before the end; the leading 99 zeros give the filters zero history.
  `while v:=1:` feeds 1 and `v:=v+a[~i]` adds one earlier slot to the
  running value and stores it, so the last slot is a(n), printed.
- **The slots.** A Fibonacci filter in slots p, p + 1 first adds y(n − 2)
  (slot p + 1 two rows back, 21 − p places) and then y(n − 1) (slot p + 1
  one row back, 10 − p places). A 1 + x slot q adds slot q − 1 of the last
  row (12 − q places), a running-sum slot q adds itself one row back
  (11 − q places). In slot order the distances are 21, 10, 19, 8, 17, 6, 6,
  4, 3, 2, 2.
- **The bytes.** `a[~i]` is `a[-i-1]`, so the bytes hold the distances
  minus one. Whichever filter comes first needs a distance of 10 or 11 (a
  Fibonacci filter in slots 0, 1 reads 21 and 10, a running sum in slot 0
  reads 11), and raw bytes 10–13 are line breaks (11 and 12 also count as
  line breaks for `str.splitlines`); minus one keeps all eleven bytes clear
  of those, the quote and the backslash.

**Notes**

- Feeding the octahedral numbers, the coefficients of (1 + x)²/(1 − x)⁴,
  into three Fibonacci filters held in variables (as
  [A001925](../A001925/) does with one fewer filter) is longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001926), CC BY-SA 4.0.

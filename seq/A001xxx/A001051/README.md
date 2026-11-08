# A001051

> Number of subgroups of order n in orthogonal group O(3).
> — [OEIS A001051](https://oeis.org/A001051)

Offset 1: 1, 3, 1, 5, 1, 5, 1, 7, 1, 5, 1, 8, 1, 5, 1, 7, 1, 5, 1, 7, …

### Python 3 — 65 bytes

```python
n=1
while[print(n%2or 7-n%4-2*(n<5)+[*b'0<x'].count(n))]:n+=1
```

The bytes literal holds four raw control bytes (12 and three times 24)
that a browser does not show. Byte for byte, the program is

```text
n=1
while[print(n%2or 7-n%4-2*(n<5)+[*b'<0c><18><18><18>0<x'].count(n))]:n+=1
```

where `<0c>` stands for the single byte 0x0c, and so on. With those four
bytes escaped (`\f\30\30\30`) the program is 72 bytes.

**How it works**

- **What is counted.** The subgroups are counted up to conjugacy, that is,
  the point groups of order n. Every finite subgroup of O(3) is one of
  three kinds (the classical list, e.g. Conway and Smith, *On Quaternions
  and Octonions*, ch. 3): a rotation group G (cyclic Cₙ, dihedral Dₘ of
  order 2m with m ≥ 2, and the polyhedral groups T, O, I of orders 12, 24,
  60); G × {±I}, of order 2|G|; or, for an index-2 pair H ⊂ G of rotation
  groups, H together with −(G ∖ H), of order |G|. The index-2 pairs are
  (C₂ₘ, Cₘ), (Dₘ, Cₘ), (D₂ₘ, Dₘ) and (O, T).
- **Counting by order.** For odd n only Cₙ exists: 1. For n = 2m there are
  C₂ₘ, Cₘ × {±I} and the group from (C₂ₘ, Cₘ), plus Dₘ and the group from
  (Dₘ, Cₘ) when m ≥ 2; that is 5, or 3 for n = 2. When 4 | n, write
  m = 2k: Dₖ × {±I} and the group from (D₂ₖ, Dₖ) add 2 more when k ≥ 2,
  so 7, or 5 for n = 4. The polyhedral groups add T at 12; O, T × {±I}
  and the group from (O, T) at 24; O × {±I} at 48; I at 60; I × {±I}
  at 120.
- **The program.** `n%2or 7-n%4` is 1 for odd n, 7 for n ≡ 0 and 5 for
  n ≡ 2 (mod 4); `-2*(n<5)` fixes n = 2 and 4. The polyhedral orders sit
  in a bytes literal, 24 three times, and `[*b'…'].count(n)` adds how many
  of them equal n. It is a list count rather than `b'…'.count(n)`, which
  would raise for n > 255.

**Notes**

- Exact; the count rests on the classification above, which is a theorem.
  The OEIS formula (period 1, 5, 1, 7 with the exceptions at 2, 4, 12, 24,
  48, 60, 120) is the same thing.
- `while[print(…)]:n+=1` prints from n = 1 on. The b-file has 10000 terms;
  they print in a fraction of a second, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001051), CC BY-SA 4.0.

# A002115

> Generalized Euler numbers.
> — [OEIS A002115](https://oeis.org/A002115)

Offset 0: 1, 1, 19, 1513, 315523, 136085041, 105261234643, 132705221399353, …

### Python 3 — 73 bytes

```python
r=[t:=1]
while[print(t)]:
 for d in-1,1,-1:r=[t:=t+x for x in[-t]+r[::d]]
```

**How it works**

- **Permutations.** a(n) is the number of permutations of 1..3n whose
  descent set is exactly {3, 6, …, 3n−3}, i.e. up, up, down, up, up,
  down, …: Heinz's Maple program in the entry counts these, and their
  e.g.f. Σ a(n)x^(3n)/(3n)! = 1/Σ (−1)^k x^(3k)/(3k)! is the entry's
  formula (Jovovic; the generalized Euler numbers of the name).
- **Forward count.** Let v_L[k] count such prefixes of length L (the
  pattern cut at L, standardized) ending in their k-th smallest value.
  Adding position L + 1 as an ascent gives v′[k′] = Σ_(k<k′) v[k]
  (k′ = 1..L+1), as a descent Σ_(k≥k′) v[k]. The step from L to L + 1 is a
  descent exactly when 3 divides L, and a(n) = Σ v_(3n).
- **Program.** The comprehension `[t:=t+x for x in[-t]+r[::d]]` is the
  prefix sum with a leading 0 (as in [A000111](../A000111/)); with d = 1
  it is an ascent of r as stored, with d = −1 it reverses first. Storing
  the vector reversed after each descent makes a descent cost one
  reversed pass, and one cycle of (reverse, plain, reverse) passes takes
  L = 3n+1 (stored reversed) to 3n+4: an ascent, an ascent and a descent.
  After a descent the last stored entry is v[1] = Σ v_(3n) = a(n), and
  it is also the final `t`. The start r = [1] is L = 1 (one prefix),
  which already prints a(0) = 1.

**Notes**

- Each term costs three passes over about 3n entries. The b-file has 167
  terms (n = 0 to 166), and the bar is the whole b-file in 60 s, which
  takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002115), CC BY-SA 4.0.

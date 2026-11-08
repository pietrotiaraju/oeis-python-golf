# A001030

> Fixed under 1 -> 21, 2 -> 211.
> — [OEIS A001030](https://oeis.org/A001030)

Offset 1: 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, …

### Python 3 — 37 bytes

```python
l=[2]
for d in l:print(d);l+=*d*[1],2
```

**How it works**

- The morphism sends a letter d to 2 followed by d ones: 1 → 21, 2 → 211.
  Its fixed point w = w₁w₂w₃… (the one starting with 2) is therefore
  w = 2 · 1^w₁ 2 · 1^w₂ 2 · 1^w₃ 2 ⋯, that is, after the first 2 the word
  is the blocks "d ones, then a 2" for d = w₁, w₂, w₃, … in turn.
- The program writes the word into the list `l` while reading it: it
  starts with the leading 2, and each letter d it reads appends the block
  `*d*[1],2` (d ones and a 2). Every block is at least two letters long and
  the loop reads one letter per pass, so the reader never catches up with
  the writer, and `for d in l:` runs forever over the growing list.
- `l+=*d*[1],2` unpacks the ones into a tuple display; a starred item is
  allowed on the right of `+=`, which makes it 1 byte under
  `l+=d*[1]+[2]`.

**Notes**

- No arithmetic beyond list appends; the list holds about 1.4 letters per
  printed term.
- The b-file has 8119 terms (n = 1..8119); they print in well under a
  second, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001030), CC BY-SA 4.0.

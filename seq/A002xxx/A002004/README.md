# A002004

> Davenport-Schinzel numbers of degree 4 on n symbols.
> — [OEIS A002004](https://oeis.org/A002004)

Offset 1: 1, 4, 8, 12, 17, 22, 27, 32, 37, 42, 47, 53, 58, 64, 69, 75, 81, 86, 92, 98, 104, …

### Python 3 — 176 bytes

```python
f=lambda s:max([len(s)]+[f(s+[a])for a in{*range(n)[:len({*s})+1]}-{*s[-1:]}if all(any(c not in x for c in(a,b)*2)for b in{*s}-{a}if(x:=iter(s)))])
n=1
while[print(f([]))]:n+=1
```

**How it works**

- **Which order.** In the 1970 numbering of the entry (Roselle and
  Stanton), a Davenport–Schinzel sequence of degree 4 on n symbols has no
  two equal adjacent terms and no subsequence a, b, a, b, a with a ≠ b;
  in today's notation this is order 3, and a(n) = λ₃(n) is the greatest
  length of such a sequence. The data fixes the reading: a(2) = 4 is
  abab, while with alternations of length 6 forbidden ababa would give 5.
- **Finite.** Keep only the terms x and y of a valid sequence and merge
  equal neighbours: what is left alternates x, y, x, … and has at most 4
  terms (5 would be a forbidden alternation), so it changes at most 3
  times. Each pair of adjacent terms {x, y} of the sequence is such a
  change, so a valid sequence has at most 3·C(n,2) + 1 terms and the
  search below ends.
- **Search.** `f(s)` returns the longest valid extension of the valid
  sequence `s`. Relabel every sequence so that its symbols first appear
  in the order 0, 1, 2, …; this keeps validity and length, so only such
  sequences are built: the next term is a symbol used before or the next
  new one, `range(n)[:len({*s})+1]`, minus the last term `{*s[-1:]}`.
- **The test.** A new last term a creates a forbidden alternation exactly
  when it closes a, b, a, b, a, i.e. when s already contains a, b, a, b
  as a subsequence for some b ≠ a in s. `x:=iter(s)` with `c in x` is the
  usual subsequence test (each `in` consumes the iterator up to the
  match), fresh for every b. Every prefix of a valid sequence is valid,
  so the search reaches every valid sequence, and the maximum of `len(s)`
  is λ₃(n) for every n.

**Notes**

- Exhaustive search with no conjecture: the program is right for every n
  but slow. The number of relabeled valid sequences grows fast (18 thousand
  for n = 5, 880 thousand for n = 6), so n = 5 takes under a second and
  n = 6 about 42 s on a slow PC. The bar is 6 terms with a 120 s timeout.
- The b-file has 21 terms (n = 1 to 21); plain search reaches only the
  first few.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 176 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002004), CC BY-SA 4.0.

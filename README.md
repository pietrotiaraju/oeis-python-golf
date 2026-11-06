# OEIS Python Golf

Shortest known Python programs that generate sequences from the
[OEIS](https://oeis.org/). Every record is run and checked against the
sequence's OEIS b-file, locally and in CI.

New to golfing these? The [golf tricks](TRICKS.md) page collects the
techniques that come up again and again across the sequence pages, each with a
short example and links to the sequences that use it.

## Records

Open a folder for its complete records table, with program sizes in bytes
and the number of terms required within each time limit. Click a sequence
for its code and explanation. The latest records are listed below.

<!-- records:start -->

**609 sequences**, 67776 bytes in all.

| Folder | Sequences |
|---|---|
| [A000000 to A000999](seq/A000xxx/) | 597 |
| [A005000 to A005999](seq/A005xxx/) | 1 |
| [A034000 to A034999](seq/A034xxx/) | 1 |
| [A035000 to A035999](seq/A035xxx/) | 1 |
| [A139000 to A139999](seq/A139xxx/) | 1 |
| [A276000 to A276999](seq/A276xxx/) | 1 |
| [A300000 to A300999](seq/A300xxx/) | 3 |
| [A334000 to A334999](seq/A334xxx/) | 1 |
| [A335000 to A335999](seq/A335xxx/) | 1 |
| [A384000 to A384999](seq/A384xxx/) | 1 |
| [A386000 to A386999](seq/A386xxx/) | 1 |

Latest 20 records:

| Date | Sequence | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | [A000474](seq/A000xxx/A000474/) | 550 | read each matching bit directly while relabeling |
| 2026-11-06 | [A000445](seq/A000xxx/A000445/) | 934 | generate quadratic relations lazily and combine finite maxima |
| 2026-11-06 | [A000421](seq/A000xxx/A000421/) | 369 | enumerate edge multisets and mark their vertex-permutation orbits |
| 2026-11-06 | [A000001](seq/A000xxx/A000001/) | 217 | fix the identity row, fuse the two checks, update the factorial incrementally |
| 2026-11-06 | [A000500](seq/A000xxx/A000500/) | 229 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-06 | [A000492](seq/A000xxx/A000492/) | 228 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-06 | [A000491](seq/A000xxx/A000491/) | 193 | accumulate the five black-partition filters directly |
| 2026-11-06 | [A000483](seq/A000xxx/A000483/) | 101 | flatten the four-column recurrence into one list |
| 2026-11-06 | [A000476](seq/A000xxx/A000476/) | 221 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-06 | [A000470](seq/A000xxx/A000470/) | 229 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-06 | [A000465](seq/A000xxx/A000465/) | 187 | accumulate the four black-partition filters directly |
| 2026-11-06 | [A000448](seq/A000xxx/A000448/) | 319 | use Wilson prime generation and shorten exact threshold expressions |
| 2026-11-06 | [A000446](seq/A000xxx/A000446/) | 370 | use Wilson prime generation, cached lambdas and a shared target |
| 2026-11-06 | [A000440](seq/A000xxx/A000440/) | 228 | shorten numerator padding and pull out the fixed parity sign |
| 2026-11-06 | [A000438](seq/A000xxx/A000438/) | 262 | express the lazy matching generator as a lambda |
| 2026-11-06 | [A000436](seq/A000xxx/A000436/) | 120 | remove addition of zero in the binomial argument |
| 2026-11-06 | [A000428](seq/A000xxx/A000428/) | 111 | reorder the Euler-transform sum and use one coefficient list |
| 2026-11-06 | [A000417](seq/A000xxx/A000417/) | 111 | reorder the Euler-transform sum and use one coefficient list |
| 2026-11-06 | [A000412](seq/A000xxx/A000412/) | 152 | sum the black-partition cases directly and use the divisor recurrence |
| 2026-11-06 | [A000282](seq/A000xxx/A000282/) | 271 | import math for a single prod call |

<!-- records:end -->

## Rules in short

- Print the sequence from its OEIS offset, one term per line, forever.
- CPython 3.12, no flags, no input. Size = file bytes, trailing newline free.
- Plain Python 3 and each "Python 3 + library" are separate categories.
- Correct for every n, with exact arithmetic; hard-coding only with a proof on
  the page.

Full rules and how to send a record: [CONTRIBUTING.md](CONTRIBUTING.md).

## Verify locally

```bash
pip install -r requirements.txt
python tools/verify.py
```

## Why "shortest known"

No record here is proved minimal, and in general none can be:

- A function that returns the length of the shortest program for any output
  cannot exist (the Berry paradox argument behind Kolmogorov complexity).
- Even deciding whether a given program prints a given infinite sequence is
  undecidable (Rice's theorem): a program that prints the sequence but switches
  to 0 once some machine halts prints it exactly when that machine never halts.
- For one specific record of, say, 66 bytes, ruling out every shorter program
  means about 96⁶⁵ ≈ 10¹²⁸ candidates, each needing a proof about its infinite
  output.

So a record stands until someone finds a shorter program.

## Related

- [LODA](https://loda-lang.org/) mines programs for OEIS sequences in its own
  assembly-like language, at a much larger scale and without byte golfing.
- The `%o` lines of each OEIS entry hold readable reference programs.

## License

Programs and tools: [MIT](LICENSE). Sequence names, b-files and other data
come from [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/)
under [CC BY-SA 4.0](https://oeis.org/LICENSE); the pages that quote them are
under CC BY-SA 4.0 too.

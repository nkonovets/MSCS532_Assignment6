# MSCS532 Assignment 6: Medians and Order Statistics & Elementary Data Structures

Part 1 implements randomized quickselect and deterministic selection (median of medians) and compares them on different inputs. Part 2 implements an array, a matrix, a stack, a circular queue, and a singly linked list.
The full report is in [Report/REPORT.md](Report/REPORT.md) (also as a [Word document](Report/assignment_report.docx)).

## Files

- `quick_select.py` – `quickselect_random()` (random pivot) and `quickselect_deterministic()` (median of medians), with `partition()`, `partition_random()` and the three-way `partition_around()`
- `data_structures.py` – `Array`, `Matrix`, `Stack`, `Queue` (circular) and `LinkedList`
- `test_data_structures.py` – a short demo that uses each data structure
- `main.py` – menu to run a selection algorithm on a data file or the data structures demo
- `recorder.py`, `file_parser.py` – timing and file reading helpers (adapted from my previous assignments)
- `data/` – random, sorted, reverse-sorted and repeated lists with 1,000 / 10,000 / 50,000 numbers
- `results.csv` – benchmark results
- `Report/` – the written report

## How to run

Requires Python 3.

```bash
python3 main.py
```

Choose `r` (randomized) or `d` (deterministic) and enter a file such as `data/sorted_large.txt`. The program finds the median and saves the time to `results.csv`. Choose `s` to run the data structures demo.

## Summary of findings

- Both selection algorithms ran in linear time on every input, including sorted and reverse-sorted data.
- Randomized quickselect was three to four times faster on random, sorted and reverse-sorted data (about 5–6 ms vs 15–18 ms at 50,000 numbers).
- On repeated values, the three-way partition made median of medians faster (6.44 ms vs 24.42 ms).
- Array access is O(1) and insertion/deletion O(n); stack and circular queue operations are O(1); linked list insertion at the head is O(1).

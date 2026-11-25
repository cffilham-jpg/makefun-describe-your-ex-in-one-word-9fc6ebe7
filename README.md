# Recalled

[![Competition](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/cffilham-jpg/makefun-describe-your-ex-in-one-word-9fc6ebe7/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/cffilham-jpg/makefun-describe-your-ex-in-one-word-9fc6ebe7/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

An ex with the verdict of a product recall: a fault serious enough to withdraw it.
The submitted artifact contains only the word above, without a caption or newline.

## Candidate review

Scores are editorial estimates from 1 (weak) to 5 (strong), in the judge's priority order: verdict on an ex, comic punch, surprise, craft, recognition. Eligibility gates apply before selection; scores do not override a rejection. Every candidate is below 70 characters.

| Candidate | Characters | Verdict | Punch | Surprise | Craft | Recognition | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Expired | 7 | 5 | 2 | 1 | 5 | 4 | Reject: generic expiration metaphor, too obvious. |
| Recalled | 8 | 5 | 5 | 4 | 5 | 4 | Keep: specific product-recall twist. |
| Buffering | 9 | 3 | 4 | 3 | 5 | 4 | Reject: describes present delay; needs context to become a verdict on an ex. |
| 404 | 3 | 2 | 3 | 2 | 1 | 3 | Reject: an error code, not an English word; requires the missing-person interpretation. |
| Demo | 4 | 2 | 3 | 4 | 5 | 3 | Reject: ambiguous noun; the limited relationship interpretation needs a caption. |
| Returned | 8 | 5 | 4 | 4 | 5 | 4 | Keep: the ex as a returned purchase. |
| Draft | 5 | 2 | 2 | 3 | 5 | 3 | Reject: generic noun; the unfinished-partner interpretation needs explanation. |
| Placeholder | 11 | 5 | 4 | 3 | 5 | 5 | Keep: the partner as a temporary occupant. |
| Unsubscribed | 12 | 3 | 4 | 3 | 5 | 4 | Reject: reads as the speaker's action rather than a description of the ex. |
| Archived | 8 | 5 | 2 | 2 | 5 | 4 | Reject: generic filing-away metaphor without a sharp comic twist. |
| Defective | 9 | 5 | 1 | 1 | 5 | 3 | Reject: plain insult without a twist. |
| Trial | 5 | 2 | 3 | 3 | 5 | 4 | Reject: ambiguous generic noun; needs a free-trial caption to deliver the intended joke. |

**Selection:** Recalled and Returned are the shortest eligible candidates at eight characters. Recalled wins the tie with the sharper, more specific product-fault verdict. Placeholder is longer. No punctuation, invented spelling, or explanation is needed in the entry itself.

## Run

Use Python 3.13 and the standard library only:

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/my-entry python3 main.py
```

The program prints the path to `entry.txt`. It honors `MAKEFUN_OUTPUT_DIR`, defaulting to `out` when unset. If the requested directory cannot be created or the file cannot be written, it writes `entry.txt` inside a new system temporary directory instead. The file contains exactly the UTF-8 bytes `Recalled`, with no trailing newline. No network requests or additional output files are made.

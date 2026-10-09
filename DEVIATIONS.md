# Deviations from NEXT_EXPERIMENT_AND_REVIEW.md / steer_compare_v3.py

None so far. `steer_compare_v3.py` is used exactly as delivered. Supporting
changes made per the task document itself:

- `extract_embeddings.py`: template lists expanded to 16+16 subjects and 10
  prefixes exactly as specified in EXPERIMENT_REVIEW_AND_FIXES.md section
  2.3 (referenced by the task document section 1.3 for the final runs);
  required before the WP4 re-extraction.
- `aggregate.py`: new file, required deliverable of WP6.
- WP1 numerical check scripts run as heredocs (recorded in commands.log and
  repro_check_raw.txt / repro_check_traj.txt); they import the author's
  package and inject the missing `torch.nn.functional` import that their
  `steering/method.py` lacks (their bug, documented in repro_check.md; our
  code is unchanged).

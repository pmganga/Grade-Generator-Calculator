## Grade Generator Calculator

A two-part Python + Bash project for calculating student grades and archiving results.

### Files
- `grade-generator.py` - Interactive grade calculator with validation, GPA, pass/fail logic, and CSV export
- `organizer.sh`       - Bash script that archives all `.csv` files with timestamp and logs everything
- `README.md`           - This file

### Features Implemented
- Full input validation (grade 0-100, positive weights, FA/SA only)
- Weighted grade calculation
- Separate Formative and Summative tracking
- Correct pass/fail logic (>=50% in each category)
- Identifies lowest FA assignment for resubmission
- Exact console output format matching transcript
- CSV export with proper headers
- Bash script creates archive folder, timestamps files, logs content and actions

### Usage
```bash
python3 grade-generator.py
./organizer.sh

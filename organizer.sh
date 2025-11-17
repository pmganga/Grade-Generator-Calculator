#!/bin/bash

# organizer.sh - Archives CSV files with timestamp and logs everything

LOGFILE="organizer.log"
ARCHIVE_DIR="archive"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Create archive directory if it doesn't exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "[$(date)] Created archive directory: $ARCHIVE_DIR" >> "$LOGFILE"
fi

# Find all .csv files in current directory (but not in archive/)
shopt -s nullglob
csv_files=( *.csv )

if [ ${#csv_files[@]} -eq 0 ]; then
    echo "[$(date)] No CSV files found in current directory." >> "$LOGFILE"
    exit 0
fi

echo "[$(date)] Starting archiving process (found ${#csv_files[@]} CSV file(s))" >> "$LOGILE"

for file in "${csv_files[@]}"; do
    # Skip if it's the log file or already in archive
    if [[ "$file" == "$LOGFILE" ]] || [[ "$file" == organizer.log ]]; then
        continue
    fi

    # Generate new filename: insert timestamp before .csv
    base="${file%.csv}"
    new_name="${base}-${TIMESTAMP}.csv"
    
    # Log the action and file content
    echo "----------------------------------------" >> "$LOGFILE"
    echo "[$(date)] Archiving: $file -> archive/$new_name" >> "$LOGFILE"
    echo "File content:" >> "$LOGFILE"
    cat "$file" >> "$LOGFILE"
    echo "----------------------------------------" >> "$LOGFILE"
    echo >> "$LOGFILE"

    # Move and rename
    mv "$file" "$ARCHIVE_DIR/$new_name"
    echo "[$(date)] Successfully archived $file as $new_name" >> "$LOGFILE"
done

echo "[$(date)] Archiving process completed." >> "$LOGFILE"
echo "All CSV files have been archived and logged."

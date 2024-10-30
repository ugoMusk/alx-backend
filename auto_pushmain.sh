#!/usr/bin/env bash

# Add script to .gitignore
echo "git_auto_push_script" >> ../.gitignore

# Find files recursively
find . -type f | while read -r file; do
  # Extract file extension and basename
  extension=$(grep -oE "\.[a-z]{1,5}$" <<< "$file")
  basename=$(basename -s "$extension" "$file")

  # Check if file has changes
  if [ -n "$(git status --porcelain "$file")" ]; then
    # Git operations
    git add "$file"
    git commit -m "Submit solution for the $basename task"
    git push || echo "Git push failed for $file"
    sleep 6
  fi
done

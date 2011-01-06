ls $1| while read file; do perl "../parsing/scripts/rm-id.prl" "$file" > "$file".noid; perl "../parsing/scripts/add-id.prl" "$file".noid > "$file"; rm "$file".noid; done

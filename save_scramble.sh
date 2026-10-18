#!/usr/bin/env bash
# Скрипт: save_scramble.sh
# Призначення: Зберігання скрамблів у jsonl файл
# Автор: Данило
# Дата: 13-11-2025


jsonldir="./final_project/logs"

#---Creating a directory and a file---
if [ ! -d "$jsonldir" ]; then
    mkdir -p "$jsonldir"
fi

jsonl_logfile="$jsonldir/scrambles.jsonl"

#---Fighting with the python JSON output---
time_of_scramble=$(date +"%Y-%m-%d_%H-%M-%S")

py_output=$(py ./final_project/scramble.py)

json_output_py=$(echo "$py_output" | sed -n '/^JSON$/,$ p' | tail -n +2)

json_compact=$(echo "$json_output_py" | jq -c '.') #Making it a single line

json_final=$(echo "$json_compact" | jq --arg ts "$time_of_scramble" '. + {time_of_scramble: $ts}')

#---Writing to JSONL---
echo "$json_final" >> "$jsonl_logfile"
echo "" >> "$jsonl_logfile"



#chmod +x ./final_project/save_scramble.sh
#./final_project/save_scramble.sh
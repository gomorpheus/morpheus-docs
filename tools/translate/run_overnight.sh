#!/bin/bash
# Overnight translation driver.
# Processes all locale batches with `opencode run` agents, $PARALLEL at a time.
# Idempotent: batches with a .done marker are skipped; safe to re-run.
set -u

REPO="/home/destes/Work/morpheus/morpheus-docs"
cd "$REPO" || exit 1
PARALLEL=${PARALLEL:-1}
BATCH_TIMEOUT=${BATCH_TIMEOUT:-2400}
MAX_ATTEMPTS=${MAX_ATTEMPTS:-2}
WORK="tools/translate/work"
MASTER_LOG="$WORK/driver.log"

lang_names() {
  case "$1" in
    es) echo "Spanish|Nota" ;;
    fr) echo "French|Remarque" ;;
    de) echo "German|Hinweis" ;;
    pt) echo "Brazilian Portuguese|Nota" ;;
  esac
}

process_batch() {
  local manifest="$1" lang="$2"
  local base id
  base="$(basename "$manifest" .json)"
  id="${lang}/${base}"
  local done_marker="$WORK/$lang/batches/$base.done"
  [ -f "$done_marker" ] && return 0
  local log="$WORK/$lang/batches/$base.log"
  local read line lang_name note_word prompt
  IFS='|' read -r lang_name note_word <<< "$(lang_names "$lang")"
  prompt="$(sed -e "s|{MANIFEST}|$manifest|" -e "s|{LANG_NAME}|$lang_name|g" -e "s|{NOTE_WORD}|$note_word|" tools/translate/translate_prompt.txt)"

  local attempt=1 ok=0
  local bdir="$WORK/$lang/batches/$base"
  while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
    # clean stale agent outputs from previous attempts
    rm -f "$bdir"/sidecar*.tsv "$bdir"/skip*.tsv
    echo "[$(date '+%H:%M:%S')] START $id attempt=$attempt" >> "$MASTER_LOG"
    timeout "$BATCH_TIMEOUT" opencode run --auto --title "i18n $id" --dir "$REPO" "$prompt" >> "$log" 2>&1
    local rc=$?
    local verify
    verify="$(python3 tools/translate/verify_batch.py "$manifest" 2>&1)"
    echo "[$(date '+%H:%M:%S')] END   $id rc=$rc $verify" >> "$MASTER_LOG"
    if echo "$verify" | grep -q '^remaining=0'; then
      ok=1
      break
    fi
    attempt=$((attempt + 1))
  done
  if [ "$ok" = "1" ]; then
    touch "$done_marker"
    echo "[$(date '+%H:%M:%S')] DONE  $id" >> "$MASTER_LOG"
  else
    echo "[$(date '+%H:%M:%S')] FAILED $id (will be retried on next driver run)" >> "$MASTER_LOG"
  fi
}

# Build the work list (French first), run with bounded parallelism
mapfile -t BATCHES < <(
  for lang in fr es de pt; do
    for m in "$WORK/$lang/batches/batch_"*.json; do
      [ -e "$m" ] || continue
      echo "$lang|$m"
    done
  done
)

pids=()
i=0
while [ "$i" -lt "${#BATCHES[@]}" ]; do
  entry="${BATCHES[$i]}"
  lang="${entry%%|*}"
  manifest="${entry#*|}"
  process_batch "$manifest" "$lang" &
  pids+=($!)
  i=$((i + 1))
  if [ "${#pids[@]}" -ge "$PARALLEL" ]; then
    wait -n
    # drop finished pids
    new=()
    for p in "${pids[@]}"; do
      if kill -0 "$p" 2>/dev/null; then new+=("$p"); fi
    done
    pids=("${new[@]:-}")
    [ -z "${pids[0]:-}" ] && pids=()
  fi
done
wait
echo "[$(date '+%H:%M:%S')] DRIVER FINISHED" >> "$MASTER_LOG"

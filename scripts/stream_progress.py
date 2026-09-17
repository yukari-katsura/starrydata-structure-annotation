#!/usr/bin/env python
"""Turn a claude --output-format stream-json feed into readable terminal progress.

Reads JSON lines on stdin and prints one compact line per meaningful event, so
an unattended run shows that it is working instead of going silent for twenty
minutes. Everything it reads is passed through unchanged only if --tee is given;
normally the caller keeps the raw stream with tee(1) and pipes a copy here.

Emits:
  - each tool use, with a short target (file, command, search)
  - each assistant message, first line only
  - a heartbeat when nothing has happened for a while, so a stall is visible
  - the final result with duration and quota

Usage:  claude -p ... --output-format stream-json --verbose | tee raw.jsonl | stream_progress.py
"""
import json
import os
import select
import sys
import time

IDLE = float(os.environ.get('PROGRESS_IDLE', '45'))   # heartbeat after this many quiet seconds


def short(s, n=64):
    s = ' '.join(str(s).split())
    return s if len(s) <= n else s[:n - 1] + '…'


def target(name, inp):
    """A one-glance description of what a tool call is doing."""
    if not isinstance(inp, dict):
        return ''
    for k in ('file_path', 'path', 'notebook_path'):
        if k in inp:
            return os.path.basename(str(inp[k]))
    if 'command' in inp:
        return short(inp['command'], 70)
    if 'pattern' in inp:
        return f"/{short(inp['pattern'], 40)}/"
    if 'prompt' in inp:
        return short(inp['prompt'], 60)
    if 'description' in inp:
        return short(inp['description'], 60)
    return ''


def main():
    t0 = time.time()
    last = t0
    tools = texts = 0
    quota = None

    def el():
        m, s = divmod(int(time.time() - t0), 60)
        return f'{m:3d}:{s:02d}'

    while True:
        r, _, _ = select.select([sys.stdin], [], [], 5)
        if not r:
            if time.time() - last > IDLE:
                print(f'  {el()}  … working ({tools} tool calls so far)', flush=True)
                last = time.time()
            continue
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line.startswith('{'):
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        t = d.get('type')

        if t == 'assistant':
            for b in d.get('message', {}).get('content', []):
                if b.get('type') == 'tool_use':
                    tools += 1
                    tgt = target(b.get('name', ''), b.get('input'))
                    print(f'  {el()}  {b.get("name","tool"):<8} {tgt}', flush=True)
                    last = time.time()
                elif b.get('type') == 'text':
                    txt = (b.get('text') or '').strip()
                    if txt:
                        texts += 1
                        print(f'  {el()}  » {short(txt.splitlines()[0], 90)}', flush=True)
                        last = time.time()

        elif t == 'rate_limit_event':
            w = d.get('rate_limit_info', {}).get('unifiedWindows', {})
            q = w.get('five_hour', {}).get('utilization')
            if q is not None and q != quota:
                quota = q
                print(f'  {el()}  [quota: five-hour window {q*100:.0f}% used]', flush=True)
                last = time.time()

        elif t == 'result':
            dur = d.get('duration_ms', 0) / 1000
            bad = d.get('is_error')
            print(f'  {el()}  {"FAILED" if bad else "done"} — {tools} tool calls, '
                  f'{texts} messages, {dur/60:.1f} min', flush=True)
            last = time.time()
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (BrokenPipeError, KeyboardInterrupt):
        pass

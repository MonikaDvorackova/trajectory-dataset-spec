import json,sys
REQUIRED={'episode_id','step','observation','action','reward','terminated','truncated','source'}
def validate(rows):
    issues=[];last={}
    for i,r in enumerate(rows):
        missing=REQUIRED-r.keys()
        if missing:issues.append(f'row {i}: missing {sorted(missing)}');continue
        if not isinstance(r['observation'],list) or not isinstance(r['action'],list):issues.append(f'row {i}: observation/action must be arrays')
        ep=r['episode_id'];expected=last.get(ep,-1)+1
        if r['step']!=expected:issues.append(f'row {i}: expected step {expected}, got {r["step"]}')
        last[ep]=r['step']
    return issues
if __name__=='__main__':
    p=sys.argv[1] if len(sys.argv)>1 else 'data/episodes.jsonl';rows=[json.loads(x) for x in open(p,encoding='utf-8') if x.strip()];errors=validate(rows);print(f'rows={len(rows)} issues={len(errors)}');print('\n'.join(errors) if errors else 'schema valid')

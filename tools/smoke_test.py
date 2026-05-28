from pathlib import Path
import subprocess, sys, shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'out' / 'smoke-test'
if OUT.exists():
    shutil.rmtree(OUT)
cmd = [sys.executable, '-m', 'business_case_system.cli', 'build', '--sample', '--out', str(OUT), '--formats', 'md,html,docx']
env = dict(**__import__('os').environ)
env['PYTHONPATH'] = str(ROOT / 'tools' / 'src')
subprocess.run(cmd, cwd=ROOT, env=env, check=True)
expected = ['business_case.md', 'business_case.html', 'business_case.docx']
missing = [name for name in expected if not (OUT / name).exists()]
if missing:
    raise SystemExit(f'Missing expected outputs: {missing}')
print('Smoke test passed: generated Markdown, HTML, and DOCX outputs.')

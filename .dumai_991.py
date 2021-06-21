import sys,shutil,os

runtah=["saya_gans/__pycache__","modul/__pycache__","wibu/__pycache__","saya_gans/ngewe/__pycache__"]

if sys.version[0]!="3":
	exit(" ! harap gunakan python3")

from saya_gans import awokawokawok as kontol
try: [shutil.rmtree(x) for x in runtah]
except: pass
kontol()

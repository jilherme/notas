#!/usr/bin/python3
'''
Atualiza as notas do minicurso de Cálculo com Python para o __site__.

Autor: Pedro H A Konzen - 10/2019
'''

# pacotes do Python
import os

# classes
from sitemap import *
from minicalcpy import *

# pastas temporárias
odir = '.docs'
os.system('rm -rvf '+odir)
os.system('cp -rvf ../docs '+odir)

srcdir = '.src'
os.system('mkdir -p '+srcdir)
os.system('rm -rvf '+srcdir+'/*')

# copia src para pasta temporária
os.system('cp -rvf ../src/* '+srcdir+'/')

# del as notas antigas
os.system('rm -rvf '+odir+'/MiniCalcPy')

# constroi as notas
mini = MiniCalcPy(srcdir,odir)
mini.build()

#fonts
os.system('cp -rvf fonts '+odir+'/MiniCalcPy/')

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/MiniCalcPy/* ../docs/MiniCalcPy/')

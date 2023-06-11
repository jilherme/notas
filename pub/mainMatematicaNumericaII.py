#!/usr/bin/python3
'''
Atualiza as notas de Matemática Numérica II
para o __site__.

Autor: Pedro H A Konzen - 04/2023
'''

# pacotes do Python
import os

# classes
from sitemap import *
from matematicanumericaii import *

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
os.system('rm -rvf ../docs/MatematicaNumericaII')

# constroi as notas
mn = MatematicaNumericaII(srcdir,odir)
mn.build()

# make sitemap.txt
sm = SiteMap(odir)
sm.build()

# publica a atualização
os.system('rsync -av '+odir+'/* ../docs/')

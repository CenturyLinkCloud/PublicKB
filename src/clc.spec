# -*- mode: python -*-
a = Analysis(['clc.py'],
             pathex=['Z:\\keithresar\\clc_git\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='clc.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

# -*- mode: python -*-

def Datafiles(*filenames, **kw):
    import os

    def datafile(path, strip_path=True):
        parts = path.split('/')
        path = name = os.path.join(*parts)
        if strip_path:
            name = os.path.basename(path)
        return name, path, 'DATA'

    strip_path = kw.get('strip_path', True)
    return TOC(
        datafile(filename, strip_path=strip_path)
        for filename in filenames
        if os.path.isfile(filename))


a = Analysis(['clc.py'],
             pathex=['Z:\\keithresar\\clc_git\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas.append(('clc/cacert.pem','clc/cacert.pem', 'DATA'))
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
		  #certfile,
          name='clc-cli.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )

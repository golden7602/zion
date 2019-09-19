# -*- mode: python -*-

block_cipher = None


a = Analysis(['ZionOrder.py'],
             pathex=['e:\\Zion'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas.extend([
    ('PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll', 'src/styles/qwindowsvistastyle.dll', 'BINARY')
])
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ColorProOrderV5.01',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='order_162.ico' )
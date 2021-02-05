# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['labelstrip.py'],
             pathex=['/Users/callum/callum/labelstrip/scripts', '/Users/callum/callum/labelstrip'],
             binaries=[],
             datas=[('/Users/callum/callum/labelstrip/scripts', 'scripts')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='labelstrip',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='scripts/icon.icns')
app = BUNDLE(exe,
             name='labelstrip.app',
             icon='scripts/icon.icns',
             bundle_identifier=None)

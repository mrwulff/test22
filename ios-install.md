iOS Build Environment

Working setup as of Aug 30, 2026.
Do not casually upgrade these versions — this exact combination successfully built and uploaded to App Store Connect.

Virtual environments

The iOS toolchain uses its own Python 3.11 venv:

source ~/venvs/kivy-ios/bin/activate

This is separate from the app's development venv:

~/Documents/test22/.venv311/

The normal test22 development environment is Python 3.11.15 and has Kivy 2.3.1 + KivyMD 2.0.1.dev0 installed.

Do not use buildozer for the iOS build. That's the Android/python-for-Android environment.

kivy-ios location
~/Documents/kivy-ios

Toolchain:

~/venvs/kivy-ios/bin/toolchain

Build output:

~/Documents/kivy-ios/build
~/Documents/kivy-ios/dist

Xcode project:

~/Documents/kivy-ios/schedulara66-ios
Critical pinned versions

The iOS runtime that successfully built:

Python             3.11
Kivy               2.3.1
KivyMD             2.0.1.dev0
materialyoucolor   3.0.4
asyncgui           0.6.3
asynckivy          0.6.4
pyobjus             1.2.4
ios                 1.1

Other important packages:

appdirs             1.4.4
beautifulsoup4      4.15.0
certifi             2026.7.22
charset-normalizer  3.5.1
filetype            1.2.0
humanize            4.16.0
mechanize           0.4.10
python-dateutil     2.9.0.post0
requests            2.34.2
urllib3             2.7.0
webcolors           25.10.0
KivyMD installation

KivyMD was installed from the development/master source and currently reports:

KivyMD 2.0.1.dev0
git-6422e4a

The important dependency is:

toolchain pip install --no-deps "materialyoucolor==3.0.4"

Do not remove materialyoucolor. KivyMD requires it at runtime.

Pillow warning

Pillow is not currently present as an actual package in the iOS runtime tree, despite toolchain pip list still showing its metadata.

Do not reinstall Pillow into the iOS runtime unless we specifically need it.

We removed:

dist/root/python3/lib/python3.11/site-packages/PIL

because its contents caused problems during the iOS build.

Current compiled recipes

Working:

hostopenssl
hostpython3
ios
kivy
libffi
libpng
openssl
pyobjus
python3
sdl2
sdl2_image
sdl2_mixer
sdl2_ttf

Everything else in toolchain status is currently Not built and is unnecessary for the current app.

Copying the application

The generated kivy-ios project contains:

schedulara66-ios/YourApp

Our working copy command is:

PROJECT_DIR="$PWD"

rsync -av --delete \
  --exclude build \
  --exclude dist \
  --exclude .git \
  --exclude .cache \
  --exclude __pycache__ \
  --exclude="*.so" \
  --exclude="*.dylib" \
  --exclude "kivytest311" \
  "/Users/kevinwulff/Documents/test22/" \
  "$PROJECT_DIR/YourApp"
Recreate/check toolchain
cd ~/Documents/kivy-ios
source ~/venvs/kivy-ios/bin/activate

which toolchain
toolchain status

The toolchain should resolve to:

/Users/kevinwulff/venvs/kivy-ios/bin/toolchain
Important

This exact setup successfully:

Built kivy-ios
Built Kivy 2.3.1
Built the SDL2 stack
Installed KivyMD 2.0.1.dev0
Installed materialyoucolor==3.0.4
Built the Schedulara iOS project
Installed it on the physical iPhone
Successfully uploaded the resulting build to App Store Connect
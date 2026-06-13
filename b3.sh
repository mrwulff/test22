#!/bin/bash

set -e

buildozer android debug

APK=$(ls -t bin/*.apk | head -1)

cp "$APK" /mnt/c/Users/kevin/Downloads/latest.apk

powershell.exe -Command "& 'C:\Users\kevin\AppData\Local\Android\Sdk\platform-tools\adb.exe' shell am force-stop org.stagehandit.stagehanditinerary"

powershell.exe -Command "& 'C:\Users\kevin\AppData\Local\Android\Sdk\platform-tools\adb.exe' shell pm clear org.stagehandit.stagehanditinerary"

powershell.exe -Command "& 'C:\Users\kevin\AppData\Local\Android\Sdk\platform-tools\adb.exe' install -r 'C:\Users\kevin\Downloads\latest.apk'"

powershell.exe -Command "& 'C:\Users\kevin\AppData\Local\Android\Sdk\platform-tools\adb.exe' shell monkey -p org.stagehandit.stagehanditinerary -c android.intent.cate>







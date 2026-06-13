#!/bin/bash

set -e

buildozer android debug

APK=$(ls -t bin/*.apk | head -1)

cp "$APK" /mnt/c/Users/kevin/Downloads/latest.apk

ADB="C:\\Users\\kevin\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"

powershell.exe -Command "& '$ADB' shell am force-stop  org.kw.schedulara.kw.schedulara" || true

powershell.exe -Command "& '$ADB' shell pm clear  org.kw.schedulara.kw.schedulara" || true

powershell.exe -Command "& '$ADB' install -r 'C:\Users\kevin\Downloads\latest.apk'"

powershell.exe -Command "& '$ADB' shell monkey -p org.kw.schedulara.kw.schedulara -c android.intent.category.LAUNCHER 1"



#!/usr/bin/env bash
set -euo pipefail
flutter doctor -v
flutter pub get
flutter analyze
flutter test
flutter build apk --debug
echo "Debug APK: build/app/outputs/flutter-apk/app-debug.apk"

# PoseGuru Phase 10 – Testing & Android Build Kit

This kit prepares the integrated Phase 9 Flutter starter for local QA and an Android APK build.

## Can an APK be built from this ZIP?
Not directly from this kit alone. You need Flutter SDK, Android SDK/Android Studio, a complete Flutter project folder, and the Phase 9 source merged into it. This kit includes build commands, smoke-test guidance, permission notes and a release checklist. It does not contain a compiled APK.

## 1. Create/open the Flutter project
Use a current stable Flutter SDK. Copy the Phase 9 `lib/` and `pubspec.yaml` into the project root, then run:
```bash
flutter doctor -v
flutter pub get
flutter analyze
flutter test
```

## 2. Start backend services
Run Phase 7 and Phase 8 backends in separate terminals:
```bash
# Phase 7
uvicorn app:app --reload --host 0.0.0.0 --port 8001

# Phase 8
uvicorn app:app --reload --host 0.0.0.0 --port 8002
```
Phase 6 analysis backend is optional for the current integrated UI because its upload flow is not yet wired into the screens.

## 3. Configure network
In `lib/services/api_config.dart`:
- Android emulator: `http://10.0.2.2:8001` and `http://10.0.2.2:8002`
- iOS simulator: `http://127.0.0.1:<port>`
- Physical phone: use the computer's LAN IP, e.g. `http://192.168.x.x:<port>`

These are development URLs only. Production must use HTTPS and a secured API.

## 4. Android development permission
For local HTTP testing only, see `android_notes/manifest_dev.xml`. Do not ship cleartext HTTP in a release build. Production API must use HTTPS.

## 5. Build a debug APK
```bash
flutter build apk --debug
```
Output:
`build/app/outputs/flutter-apk/app-debug.apk`

## 6. Build a release APK (only after release gates)
```bash
flutter build appbundle --release
```
For Google Play, an Android App Bundle (`.aab`) is normally preferred. Configure signing securely; never commit keystore passwords or signing keys to source control.

## Current known gaps
- The app currently uses a demo user ID, not verified OTP/email authentication.
- Phase 7 is a small rules-based pose catalogue, not trained AI.
- Phase 6 real image recognition is not connected to the integrated setup screen.
- Phase 5 live camera screen is only a camera preview with a 2D placeholder; real AR tracking is not implemented.
- The model illustration is a placeholder; licensed rigged 3D models and animations are absent.
- Photoshoot history write flow and some Phase 8 profile features are not wired in the integrated UI.
- Full multilingual localization, ads integration, privacy consent and production security are not complete.

Do not publish until all release gates in `docs/release_checklist.md` are satisfied.

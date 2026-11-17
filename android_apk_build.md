# Build an installable PoseGuru APK

## What this produces
The included GitHub Actions workflow builds a **debug APK** from the Flutter starter and uploads it as a downloadable workflow artifact. This is for device testing, not Play Store release.

## Steps
1. Extract `PoseGuru_Final_Consolidated_Project.zip`.
2. Create a GitHub repository and upload the contents of the extracted `PoseGuru_Final/` folder to the repository root (so `flutter/` and `.github/` are at the root).
3. The workflow generates the missing Android platform folder automatically before compiling. Open the repository's **Actions** tab.
4. Select **Build PoseGuru Android APK** and choose **Run workflow**. A push to `main` also triggers the workflow.
5. When the workflow succeeds, open that run, scroll to **Artifacts**, and download `poseguru-debug-apk`.
6. Extract the artifact and install `app-debug.apk` on your Android phone. If Android blocks installation, allow installing apps from that source in Android settings.

## Important
- The Flutter starter did not include a generated `android/` platform folder. The workflow now runs `flutter create --platforms=android .` to generate it before compiling.
- This build workflow has been added, but it has **not been executed in this environment**. The APK does not exist yet.
- The current project is a development starter. A successful APK build does not mean all features are production-ready.
- AI vision is in demo mode by default. Live vision requires a server-side API key and configured backend.
- API URLs in the Flutter app may need to be changed from Android emulator addresses to your deployed backend or computer's LAN IP before phone testing.
- The separate 3D reference module is not wired into the main app. It also needs licensed GLB assets and animation clips.
- ARCore/ARKit, verified OTP login, ads and complete translations still require implementation.
- Do not put API secrets inside the Flutter app or APK.
- For Play Store release, configure a release signing key securely and complete privacy, permission and store-policy checks. Do not use a debug APK for public distribution.

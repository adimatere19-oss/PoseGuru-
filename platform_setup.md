# Platform permissions

## Android
In `android/app/src/main/AndroidManifest.xml`, add inside `<manifest>` and outside `<application>`:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Use a physical Android device for camera testing. For a future ARCore build, check the device's ARCore support and follow Google's current ARCore setup requirements. Do not claim AR support on unsupported devices.

## iOS
In `ios/Runner/Info.plist`, add:

```xml
<key>NSCameraUsageDescription</key>
<string>PoseGuru uses the camera to show pose references over your surroundings.</string>
```

Test on a physical iPhone. For a future ARKit build, set the deployment target and device requirements according to Apple's current ARKit documentation.

## Privacy
- Do not upload camera frames unless the user explicitly starts an AI analysis action and is informed.
- The live camera preview in this scaffold stays in the device UI; this code does not send frames to a server.
- Do not save or capture photos from this screen.

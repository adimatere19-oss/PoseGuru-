# Replacing the placeholder with real AR

The included screen is a camera preview plus a 2D placeholder. Production AR requires a native scene renderer.

## Required capabilities
1. Camera background texture.
2. Plane detection (floor/wall) and world tracking.
3. User taps a detected plane to place the reference model.
4. GLB/glTF loading for a licensed, rigged male/female model.
5. Animation clips for each pose, plus transitions.
6. Scale/rotation controls and a reset-anchor action.
7. Optional depth/occlusion where the device supports it.
8. Fallback mode for devices without AR support: show the 3D model on a plain background, not over the live camera.

## Suggested architecture
- `PoseGuideScreen`: UI, pose selection, instructions and controls.
- `Camera/AR adapter`: platform-specific camera/AR implementation.
- `PoseModelRepository`: downloads and caches approved model assets.
- `PoseAnimationController`: maps a selected pose ID to a rig animation.
- `Localization`: translates every instruction and control using the selected app language.

## Platform approach
- Android: integrate ARCore through a maintained Flutter plugin or a small native Kotlin platform view.
- iOS: integrate ARKit through a maintained Flutter plugin or a native Swift platform view.
- Keep the Flutter UI independent of the AR provider behind an interface such as:
  `initialize()`, `placeModel()`, `setPose()`, `setScale()`, `setRotation()`, `dispose()`.

Before selecting a plugin, verify its current maintenance status, supported Flutter version, Android/iOS requirements, and license. Do not add an abandoned plugin solely because an old tutorial uses it.

## Acceptance tests
- Camera permission denied / granted.
- Device has no camera.
- Device does not support AR.
- Plane found and model placed.
- Model remains anchored while the user moves.
- Portrait and landscape.
- Low light and bright outdoor light.
- App backgrounded and resumed.
- No photo capture or upload occurs from the guide screen.

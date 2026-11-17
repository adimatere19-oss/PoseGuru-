# PoseGuru release checklist

## Product and functionality
- [ ] Replace all placeholder model/AR elements with working features or clearly remove them from launch scope.
- [ ] Connect actual vision AI for outfit/background recognition.
- [ ] Expand and review the pose library; verify exactly 10 useful suggestions per request.
- [ ] Connect pose IDs to licensed male/female 3D models and pose animations.
- [ ] Implement real ARCore/ARKit tracking or clearly label the feature as camera guide only.
- [ ] Finish favorite categories, outfit favorites, background history and photoshoot history flows.
- [ ] Implement full localization for every supported language.

## Security and privacy
- [ ] Implement verified mobile OTP and/or email authentication.
- [ ] Replace demo user ID with server-verified identity.
- [ ] Add per-user authorization and HTTPS.
- [ ] Add privacy policy, terms, consent and data deletion/export workflows.
- [ ] Document image processing, retention and third-party AI provider handling.
- [ ] Complete security review and dependency/license review.

## Ads and store
- [ ] Integrate ads in compliance with Google Play policies and applicable consent rules.
- [ ] Do not add paid subscriptions if retaining the confirmed free-with-ads model.
- [ ] Prepare app icon, screenshots, feature graphic and store description.
- [ ] Configure package/application ID and versioning.
- [ ] Configure Android signing and protect keystore credentials.
- [ ] Complete Google Play Data safety form accurately.
- [ ] Test release build on physical devices before submission.

## Important
A successful local APK build does not mean the app is production-ready or approved by Google Play.

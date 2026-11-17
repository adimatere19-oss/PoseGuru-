# PoseGuru manual QA test plan

## Installation and launch
- [ ] Install debug APK on a physical Android phone.
- [ ] App launches without crash.
- [ ] Dark theme, navigation and home tiles render correctly.
- [ ] Back navigation returns to the expected screen.

## Photoshoot setup
- [ ] Solo, Couple, Group and Selfie tiles open the setup screen.
- [ ] Male, Female and Neutral model choices can be selected.
- [ ] Outfit style selection works.
- [ ] Custom scene/location text can be entered.
- [ ] Outfit and background images can be selected from gallery.
- [ ] Cancelling the image picker does not crash the app.

## Pose recommendations
- [ ] Phase 7 API is reachable from the device.
- [ ] Exactly 10 pose cards are returned for each shoot mode.
- [ ] Previous and Next cycle through the cards.
- [ ] Pose instructions show camera framing, body, face, hands and feet guidance.
- [ ] API offline state shows a readable error.
- [ ] Save to Favourites writes to Phase 8 API.

## Favorites and profile
- [ ] Phase 8 API is reachable from the device.
- [ ] Saved poses appear in My Favourite Poses.
- [ ] Empty favorites state is understandable.
- [ ] Profile history empty/error states are understandable.
- [ ] Confirm demo identity is not mistaken for real account login.

## Live camera
- [ ] Camera permission prompt appears.
- [ ] Denying permission shows a clear explanation.
- [ ] Granting permission shows live preview on a physical device.
- [ ] Returning from background and reopening the screen works.
- [ ] No photo is captured or uploaded by the guide screen.
- [ ] Placeholder overlay is clearly not represented as real AR.

## Device and network
- [ ] Test on at least one lower-end and one newer Android device.
- [ ] Test portrait orientation and screen sizes.
- [ ] Test backend unavailable / slow network / airplane mode.
- [ ] Confirm no secret API keys are stored in the Flutter app.

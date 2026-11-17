# Real Vision setup

## Provider
This starter uses OpenAI's Responses API with image inputs from the backend. See the official API docs for current multimodal/Responses guidance: https://platform.openai.com/docs

## Configure
1. Install backend requirements in `backend/phase6_analysis`.
2. Copy `.env.example` to `.env` or set environment variables in your deployment environment.
3. Set `POSEGURU_AI_MODE=live`.
4. Set `OPENAI_API_KEY` on the server only.
5. Set `POSEGURU_VISION_MODEL` to a vision-capable model available to your API project.
6. Start the API on port 8003.

Never put the API key in Flutter, an APK, source control, or a public client configuration. Use a secrets manager in production.

## Test readiness
- `GET /health` should report `vision_provider_ready: true`.
- `POST /analyze` requires a background image and accepts an optional outfit image.
- Live mode returns validated JSON fields; provider errors are returned as a generic 502.
- Demo mode remains the default unless explicitly changed.

## Cost and privacy
Vision API calls are billable according to the model and image detail used. Check current API pricing before launch. Images are transmitted to the configured provider for analysis after the app's consent dialog. Review provider data controls, your privacy policy, retention requirements, and user consent before production.

## Known limits
- Clothing/style labels are visual estimates and may be wrong; users should be able to edit them.
- This does not identify people.
- It does not create or modify the user's final photo.
- Pose suggestions remain the separate Phase 7 rules-based engine, now supplied with detected clothing and scene labels.

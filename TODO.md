# Project Roadmap & TODO

## Current Sprint: v0.1.0 (MVP)

*Goal: Stable real-time pitch detection and range tracking.*

- [x] Implement YIN algorithm wrapper (`core/pitch_detector.py`)
- [x] Basic Movable-Do logic (`core/note_converter.py`)
- [x] Statistical filtering for range tracking (`core/range_tracker.py`)
- [x] Modern PySide6/QML GUI bridge and layout
- [x] Add microphone gain indicator to UI
- [x] Implement manual tonic entry fallback

## Upcoming: v0.2.0 (Song Library)

*Goal: Help users apply their range to real music.*

- [ ] Support MIDI file parsing for song range extraction
- [ ] Simple SQLite database for saving "Favorite Songs"
- [ ] Weighted Key Recommendation strategy (favoring high or low)
- [ ] PDF export for "Session Summaries"

## Vision: v0.3.0+

- [ ] **Setlist Optimizer**: Logic to minimize key changes or vocal strain across a 2-hour set.
- [ ] **Cloud Sync**: Allow users to see their range progress over months/years.
- [ ] **Mobile Companion**: Lite version for stage use (iOS/Android).

## Technical Debt & Polish

- [ ] Replace `sounddevice` with more robust platform-native backends if latency persists.
- [ ] Optimize YIN performance for low-power devices (Raspberry Pi support).
- [ ] Expand unit test coverage to 90%+.
- [ ] Internationalization (i18n) for Solfa syllables (e.g., Fixed-Do locales).

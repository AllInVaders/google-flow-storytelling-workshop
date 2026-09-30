# Google Flow, Gemini Omni & Lyria 3.5 — Incremental Storytelling Workshop

A hands-on workshop for directing **30-second commercials and narrative shorts** using **Google Flow**, **Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`)**, **Nano Banana Pro (`gemini-3-pro-image`)**, **Gemini 3.8 Flash (`gemini-3.8-flash` / `gemini-3.8-flash-tts`)**, and **Lyria 3.5 (`lyria-3.5` / `lyria-3-pro-preview`)**.

- **Live 18-Slide Google Slides Deck**: [Incremental AI Filmmaking: Atomic Prompt Sandbox to 30s Commercial](https://docs.google.com/presentation/d/1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0/edit) ([PDF Snapshot](./slides/google-flow-storytelling-workshop-slides.pdf))
- **Part I — Atomic Prompt Mastery Sandbox**: [`prompts/00-atomic-prompt-sandbox.md`](./prompts/00-atomic-prompt-sandbox.md)
- **Interactive Web Companion**: [`docs/index.html`](./docs/index.html)

---

## Two-Part Workshop Architecture

### Part I: The Atomic Prompt Mastery Sandbox (`30 min`)
Before building a multi-shot commercial, participants enter the **[Atomic Prompt Mastery Sandbox](./prompts/00-atomic-prompt-sandbox.md)** to push **one isolated creative variable at a time** while holding the subject constant:
- **Lab A — Extreme Camera Angles & Motion**: `14mm` worm's-eye vs. `90°` God's-eye knolling (`gemini-3-pro-image`), single-take whip-pan-to-crane choreography (`gemini-omni-1.1-flash`), and **Multi-Turn Conversational Camera Angle Editing**.
- **Lab B — Warmth & Kelvin Color Temperature**: Cold `7500K` blue-hour rain vs. warm `2400K` golden-hour chiaroscuro, dynamic in-shot lighting evolution, and **Conversational Video Relighting** in `gemini-omni-1.1-flash`.
- **Lab C — Radical Aesthetic & Film Stock Styles**: `35mm Kodak Vision3 500T Anamorphic`, `12fps Stop-Motion Clay & Felt Diorama`, `Architectural Sumi-e Ink & Watercolor`, and `1999 Y2K Broadcast CRT`.
- **Lab D — Multi-Object Spatial Lock & Chain-Reaction Physics**: 5-object spatial lock (`gemini-3-pro-image`) and Rube Goldberg domino-to-espresso physics with synchronized foley (`gemini-omni-1.1-flash`).
- **Lab E — Gemini Omni Exclusive Superpowers**: In-video 3D kinetic typography (`"AWAKEN THE CRAFT"`) parted by rising coffee steam, plus Python `interactions.create` multi-turn editing.
- **Lab F — Latest Lyria 3.5 Multimodal Music Sandbox**: `44.1 kHz` stereo tracks from **Text or Image + Text** using `lyria-3.5` / `lyria-3-pro-preview` (with `[Intro]`, `[Verse]`, `[Chorus]`, `[Crescendo]`) and exact 30s loops via `lyria-3-clip-preview`.

### Part II: The 7-Stage Incremental Commercial Build (`90 min`)
Participants start with a **2-sentence story seed** (*"Solis — The 6:00 AM Spark"*) and stack one production layer at a time:

| Stage | Layer Added | Primary Models | Key Deliverable |
| :--- | :--- | :--- | :--- |
| **Stage 0** | **The Story Seed** | `gemini-3.8-flash` | 2-sentence logline + 6-beat emotional arc (`7500K` -> `2700K`) |
| **Stage 1** | **Character & Face Lock** | `gemini-3-pro-image` | 35-word Identity Anchor Block + `5600K` portrait + 4-angle sheet (`[CHAR_MAYA]`, `[CHAR_LEO]`) |
| **Stage 2** | **Scene & Product Lock** | `gemini-3-pro-image` | Empty architectural plates (`[SCENE_STUDIO]`, `[SCENE_CAFE]`) + hero prop (`[PROP_CUP]`) |
| **Stage 3** | **6-Shot Storyboard** | `gemini-3-pro-image` / `gemini-3.1-flash-image` | 6 composited storyboard keyframes + First/Last Frame pairs |
| **Stage 4** | **Gemini Omni Video** | `gemini-omni-1.1-flash` | 6 animated clips via Multi-Reference (up to 5 image refs) & First/Last Frame keyframing (`360p` draft -> `4K`) |
| **Stage 5** | **Dialogue, TTS & Lyria 3.5** | `gemini-omni-1.1-flash` + `gemini-3.8-flash-tts` + `lyria-3.5` | 180° shot-reverse-shot conversation + `Kore` voiceover + `44.1 kHz` multimodal score |
| **Stage 6** | **Omni Conversational Edit & Cut** | `gemini-omni-1.1-flash` | Multi-turn conversational relighting, 10s scene extension (up to 40s), kinetic typography, and final 30s cut |

---

## Repository Structure

```text
google-flow-storytelling-workshop/
├── README.md                                       # Quick-start overview & Two-Part Architecture
├── workshop-guide/
│   ├── 01-instructor-playbook.md                   # Facilitator script, timing, and live demo guide
│   ├── 02-student-incremental-labs.md              # Step-by-step hands-on labs (Part I Sandbox + Part II Stages 0–6)
│   └── 03-cross-platform-translation-guide.md      # Executing in Google Flow, Gemini Omni, Vertex AI, or Runway/Kling
├── prompts/
│   ├── 00-atomic-prompt-sandbox.md                 # Part I: 18 isolated prompt experiments (Angles, Warmth, Style, Physics, Omni, Lyria 3.5)
│   ├── solis-commercial-prompt-library.md          # Part II: Copy-paste prompts for "Solis — The 6:00 AM Spark"
│   └── bonus-story-packs.md                        # 2 extra commercial packs (NovaPay Fintech & Kuntur Outdoor Gear)
├── slides/
│   ├── README.md                                   # 18-slide index & Google Slides link
│   ├── build_flow_workshop_deck.py                 # Google Slides generator script
│   └── google-flow-storytelling-workshop-slides.pdf# PDF snapshot of the 18-slide deck
└── docs/
    └── index.html                                  # Interactive dark-mode Workshop Web Companion
```

## Quick Start

1. **Run Part I (Atomic Prompt Sandbox)**: Open [`prompts/00-atomic-prompt-sandbox.md`](./prompts/00-atomic-prompt-sandbox.md) and test isolated prompts for camera angles, Kelvin warmth, styles, 5-object physics, Gemini Omni conversational edits, and Lyria 3.5 music.
2. **Run Part II (Incremental Production)**: Follow [`workshop-guide/02-student-incremental-labs.md`](./workshop-guide/02-student-incremental-labs.md) and [`prompts/solis-commercial-prompt-library.md`](./prompts/solis-commercial-prompt-library.md) to build the 30-second *"Solis"* commercial from a 2-sentence story seed.
3. **Present with the Slides or Web App**: Open the [18-Slide Google Slides Presentation](https://docs.google.com/presentation/d/1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0/edit) or launch `docs/index.html` in any browser.

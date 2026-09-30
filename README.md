# Google Flow & GenMedia: Incremental Storytelling Workshop

[![Open Google Slides Deck](https://img.shields.io/badge/Google_Slides-16--Slide_Workshop_Deck-F59E0B?style=for-the-badge&logo=googleslides&logoColor=white)](https://docs.google.com/presentation/d/1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0/edit)
[![Launch Google Flow](https://img.shields.io/badge/Google_Flow-Open_Workspace-3B82F6?style=for-the-badge&logo=google&logoColor=white)](https://labs.google/fx/tools/flow)

A hands-on, story-first workshop for building a cohesive **30-second brand commercial** (`"Solis — The 6:00 AM Spark"`) by starting from a 2-sentence narrative seed and incrementally layering **Character Face Consistency**, **Empty Location Plates**, **6-Shot Storyboards**, **Camera Motion**, **Two-Character Dialogue**, and **Timeline Assembly**.

Designed for **Google Flow** (`labs.google/fx/tools/flow` and Enterprise `flow.cloud.google.com`) while remaining 100% portable to **Google AI Studio**, **Vertex AI Studio**, and third-party GenMedia platforms (Runway, Luma Dream Machine, Kling, Midjourney).

---

## High-Level Features

- **7-Stage Incremental "Layer-Cake" Workflow**: Progresses step-by-step from a 2-sentence logline to a finished 6-shot commercial without character drift or hallucinated room geometry.
- **3-Pillar Character Face Consistency**: Combines a verbatim **35-Word Identity Anchor Block**, neutral 5600K studio portraits (`Ingredients`), and a **4-Angle Turnaround Sheet** (`gemini-3-pro-image` / Nano Banana Pro).
- **Two-Character Dialogue & 180° Eyeline Rule**: Shows how to direct Over-the-Shoulder (OTS) and Reverse-Angle shots with synchronized lip-sync (`veo-3.1`), expressive voiceover (`gemini-3.8-flash-tts`), and a 3-part musical score (`lyria-3`).
- **3 Complete Commercial Prompt Packs**: Includes the flagship **Solis Artisan Coffee** commercial plus bonus templates for **Fintech (`NovaPay`)** and **Retail/Apparel (`Kuntur Gear`)** in English and Spanish.
- **16-Slide Google Slides Deck & Web Companion**: Ready-to-present slide deck with facilitator scripts and a zero-build copy-paste prompt portal (`docs/index.html`).

---

## Repository Structure

| Path | Description |
| :--- | :--- |
| [`workshop-guide/01-instructor-playbook.md`](workshop-guide/01-instructor-playbook.md) | 90–120 min Facilitator Run-of-Show, live demo talk tracks, and troubleshooting guide |
| [`workshop-guide/02-student-incremental-labs.md`](workshop-guide/02-student-incremental-labs.md) | Step-by-step Participant Workbook across **Stages 0–6** (Google Flow + Cross-Platform tracks) |
| [`prompts/solis-commercial-prompt-library.md`](prompts/solis-commercial-prompt-library.md) | Copy-paste prompt library, reusable fill-in-the-blank templates, and 2 bonus commercial packs |
| [`slides/`](slides/README.md) | [16-Slide Google Slides Deck](https://docs.google.com/presentation/d/1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0/edit), PDF export, and generator script |
| [`docs/index.html`](docs/index.html) | Interactive web companion with one-click copy buttons for every stage |

---

## Quick Start

1. **Open the Slide Deck**: Launch the [16-Slide Google Slides Presentation](https://docs.google.com/presentation/d/1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0/edit) (or view [`slides/google-flow-storytelling-workshop-slides.pdf`](slides/google-flow-storytelling-workshop-slides.pdf)).
2. **Open Your Workspace**:
   - **Track A (Google Flow)**: Open [Google Flow](https://labs.google/fx/tools/flow) and create a new project.
   - **Track B (Cross-Platform)**: Open [Google AI Studio](https://aistudio.google.com) / Vertex AI Studio (`gemini-3.8-flash`, `gemini-3-pro-image`, `veo-3.1`, `gemini-3.8-flash-tts`, `lyria-3`) or your preferred image/video generator.
3. **Run the 7 Incremental Stages**: Follow [`workshop-guide/02-student-incremental-labs.md`](workshop-guide/02-student-incremental-labs.md) or open `docs/index.html` in your browser for one-click prompt copying:
   - **Stage 0**: Expand the 2-sentence story seed into a 3-Act micro-arc.
   - **Stage 1**: Lock character faces (`[CHAR_MAYA]` & `[CHAR_LEO]`) and a 4-angle turnaround sheet.
   - **Stage 2**: Generate actor-free location plates (`[SCENE_STUDIO]`, `[SCENE_CAFE]`) and the hero prop (`[PROP_CUP]`).
   - **Stage 3**: Composite the 6-shot storyboard and Start/End keyframe pairs.
   - **Stage 4**: Animate camera moves using `Ingredients to Video` and `Frames to Video`.
   - **Stage 5**: Direct the two-character Shot-Reverse-Shot conversation, voiceover, and score.
   - **Stage 6**: Stitch the timeline in `Scenebuilder` using `Extend`, `Jump To`, and J/L audio cuts.

---

## License

Released under the [MIT License](LICENSE).

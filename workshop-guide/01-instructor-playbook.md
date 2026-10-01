# Instructor Playbook: Google Flow & Gemini Omni Storytelling Workshop (90 Min)

> **Target Audience**: Creative Technologists, Filmmakers, Marketers, Designers, and AI Builders  
> **Workspace**: 100% inside **Google Flow** ([labs.google/fx/tools/flow](https://labs.google/fx/tools/flow))  
> **Verified Google Flow Features Used**:
> - **Google Flow Agent** (Conversational story & beat-sheet collaborator)
> - **Characters (`@Maya`, `@Leo`)**: Created once in **Left Sidebar $\rightarrow$ Characters $\rightarrow$ New Character** (locking appearance, name, and bundled **Voice**), then referenced only by **`@Maya`** and **`@Leo`**.
> - **Nano Banana Pro** (`Image` mode — storyboard frames and visual references attached via **`More > Add to Prompt`** or drag-and-drop)
> - **Gemini Omni Flash** (`Video` mode — `4s–10s` clips, **`Video > Ingredients`**, **`Video > Frames` (`+ Add start frame` / `+ Add end frame`)**, **`Save frame`**, `Omni 360p` $\rightarrow$ `720p` 0-credit upscaling, native character voice dialogue, 3-turn conversational **Video Edit**, and **Scenebuilder**)

---

## 1. Workshop Philosophy: Two Simple Parts

Most beginners fail at AI filmmaking because they write a massive paragraph describing a character's face, outfit, room, camera move, and dialogue in every single prompt—causing the model to **re-generate a different person in every clip**.

This workshop fixes that in **two streamlined parts**:

1. **Part I — Prompt Sandbox in Google Flow (25 Minutes)**: Students test **one isolated lever at a time** (Camera Angles, Kelvin Warmth, Visual Styles, and Multi-Object Physics) using `Nano Banana Pro` and `Omni Flash`.
2. **Part II — 5-Step Incremental Story Build (65 Minutes)**: Students build a 30-second commercial (*"Solis Artisan Coffee — The 6:00 AM Spark"*) by creating their characters **once** (`@Maya` and `@Leo`) in Google Flow's **Characters** tab, referencing **`@Maya`** and **`@Leo`** in every prompt, and using **`More > Add to Prompt`**, **`+ Add start/end frame`**, and **`Save frame`** for scene and prop continuity.

---

## 2. Minute-by-Minute Facilitator Run-of-Show (90 Minutes)

| Time | Segment | Instructor Action | Student Deliverable in Google Flow |
| :--- | :--- | :--- | :--- |
| **00:00 – 00:05** | **Welcome & Setup** | Open the 14-slide deck (Slides 01–02). Have everyone open [labs.google/fx/tools/flow](https://labs.google/fx/tools/flow) and create project `00 - Flow Prompt Sandbox`. | Project created; **Omni 360p** draft mode enabled. |
| **00:05 – 00:15** | **Part I · Labs A & B** | Present Slide 03. Run **Lab A** (Worm's-Eye vs. 90° Overhead vs. Whip-Pan) and **Lab B** (7500K Cold Blue vs. 2400K Golden Sunrise + 1-turn Omni Video Edit). | 4 test images + 2 Omni Flash clips + 2 conversational edits. |
| **00:15 – 00:25** | **Part I · Labs C & D** | Present Slide 04. Run **Lab C** (35mm Film vs. 12fps Stop-Motion Clay) and **Lab D** (5-Object Tabletop Lock + Kinetic Text `"AWAKEN THE CRAFT"`). | 3 style variations + 1 kinetic text clip in Omni Flash. |
| **00:25 – 00:35** | **Step 1 · Short Story** | Present Slides 05–06. Create project `Solis - The 6AM Spark`. Use **Google Flow Agent** to turn the 2-sentence story seed into a 5-shot beat sheet. | 5-Shot Beat Sheet inside Google Flow Agent. |
| **00:35 – 00:48** | **Step 2 · Characters** | Present Slides 07–08. **Crucial Teaching Moment**: Create `@Maya` and `@Leo` **once** in `Characters > New Character` (with voices attached). Explain why we never re-describe them. | Locked `@Maya` and `@Leo` in the **Characters** tab with Voices attached. |
| **00:48 – 01:02** | **Step 3 · Storyboard** | Present Slides 09–10. Generate the 5 storyboard images (`Images 3.1–3.5`) in `Image > Nano Banana Pro` using `@Maya`, `@Leo`, and **`More > Add to Prompt`** to keep the cafe and terracotta cup consistent. | 5 consistent storyboard images (`Images 3.1–3.5`). |
| **01:02 – 01:18** | **Step 4 · Video & Voice** | Present Slides 11–12. Switch to `Video > Omni Flash`. Animate Shots 1–5 using **`Video > Frames` (`+ Add start frame` / `+ Add end frame`)** and **`Video > Ingredients`** (`@Maya`, `@Leo` + scene image). | 5 animated `Omni Flash` video clips (`Clips 4.1–4.5`) with spoken dialogue. |
| **01:18 – 01:30** | **Step 5 · Edit & Cut** | Present Slides 13–14. Use **Omni Flash Video Edit** (2 conversational turns) to relight Shot 5 and add the `"SOLIS — AWAKEN THE CRAFT"` title, then assemble in **Scenebuilder** and upscale to `720p`. | Finished 30-second commercial exported from Scenebuilder. |

---

## 3. The 4 Golden Facilitator Callouts

### Callout #1: Stop Re-Generating Characters! (`Create Once -> Refer with @Name`)
- **What to show on screen (Slide 08)**:
  - Open **Left Sidebar $\rightarrow$ Characters $\rightarrow$ New Character**.
  - Paste the physical description of Maya **one single time**, pick her **Warm Alto** voice, name her `Maya`, and click **Done**.
  - Now clear the prompt box and type:
    > `@Maya drinks coffee from the terracotta cup and smiles.`
  - Ask the room: *"Notice how I didn't mention her glasses, freckles, raven hair, or ochre cardigan? Because `@Maya` is already saved as a Google Flow Character! If you paste her description again, you force Flow to invent a brand-new person."*

### Callout #2: How Scene & Object Continuity Actually Works in Google Flow (Slide 09)
- Emphasize to students that in Google Flow's left sidebar (**All media, Images, Videos, Characters, Scenes, Uploads**), only **Characters** (`@Maya`, `@Leo`) and **Voices** (`@Voice`) have named `@` tags—there is no `@Object` or `@Room` tag!
- To reuse a scene, background, or prop image across shots, show the three real Google Flow controls:
  1. Hover over any image in your project and click **`More` ($\vdots$) $\rightarrow$ `Add to Prompt`** (or drag the image tile into the prompt box).
  2. In `Video > Omni Flash`, switch to **`Frames`** and attach your storyboard image as **`+ Add start frame`** (and optionally **`+ Add end frame`**).
  3. Or pause any generated video clip on its last frame and click **`Save frame`** to use that exact frame in your next shot!

### Callout #3: Draft in `Omni 360p`, Upscale Winners to `720p` for 0 Credits
- In the **Video** model dropdown, show students how **Omni 360p** generates in half the credits for rapid testing, and how clicking **Upscale to 720p** on the winning take costs **0 credits**.

### Callout #4: Edit Videos Conversationally Instead of Starting Over
- When a student says *"I love `@Maya`'s expression in Shot 5, but I wish the sunlight were warmer,"* stop them from re-rolling the clip from scratch.
- Have them open the conversational video edit box on that clip and type:
  > `Intensify the warm 2400K golden sunrise beams behind @Maya.`
- Point out that **Omni Flash** supports **up to 3 conversational edit turns** on any clip (up to 10s) while preserving all previous versions in the **History** panel.

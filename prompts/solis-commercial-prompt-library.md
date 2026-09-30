# Master Prompt Library: Incremental Storytelling for Google Flow & GenMedia

This reference library contains **copy-pasteable prompt packs** structured for the **7-Stage Incremental Layer-Cake Method** across **Google Flow** (`labs.google/fx/tools/flow` & `flow.cloud.google.com`), **Google AI Studio / Vertex AI GenMedia**, and **third-party generative video/image platforms**.

---

## Part 1: Universal Prompt Templates (Build Your Own Commercial)

### 1.1 The 35-Word "Identity Anchor Block" Template
Copy and fill out this block once per character. Paste it verbatim into **every** image and video prompt featuring that character to eliminate facial and wardrobe drift:

```text
[NAME], a [AGE]-year-old [ETHNICITY/HERITAGE] [ROLE] with [SKIN_TONE_AND_MICRO_FEATURE, e.g., warm olive skin and subtle nose freckles], [EYE_COLOR_AND_SHAPE], [EXACT_HAIRSTYLE_AND_COLOR], wearing [OUTER_GARMENT_COLOR_AND_FABRIC] over [INNER_GARMENT] and [SIGNATURE_ACCESSORY, e.g., round tortoiseshell glasses].
```

### 1.2 The 4-Angle Face Consistency Turnaround Sheet Template
Run in **`gemini-3-pro-image`** (Nano Banana Pro) or **`gemini-3.1-flash-image`** (Nano Banana 2) at `16:9`:

```text
A 4-panel character reference sheet on a clean neutral grey studio background showing the exact same person in four views:
(1) Front view with a calm neutral expression,
(2) 45-degree three-quarter view with [EMOTION_A],
(3) Side profile looking [DIRECTION],
(4) Front close-up with [EMOTION_B, e.g., a warm genuine smile].
Subject: [PASTE_35_WORD_IDENTITY_ANCHOR_BLOCK]. Identical facial bone structure, hair, and accessories across all four panels, 85mm prime portrait lens, f/2.0, natural skin texture, no text, no labels.
```

### 1.3 The 7-Part Cinematic Video Prompt Formula
```text
[1. SHOT SIZE & ANGLE] + [2. CAMERA MOVEMENT] + [3. IDENTITY ANCHOR BLOCK + SPECIFIC PHYSICAL ACTION] + [4. SCENE & LIGHTING CONTRAST] + [5. LENS & FILM LOOK] + [6. SPOKEN DIALOGUE IN SINGLE QUOTES] + [7. AUDIO: AMBIANCE, SFX & VOICE CUES]
```

---

## Part 2: Flagship Workshop Commercial — "Solis Artisan Coffee: The 6:00 AM Spark"

### Identity & Asset Anchors
* **`[CHAR_MAYA]`**:
  ```text
  Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles across the nose, expressive dark brown eyes, shoulder-length wavy raven hair tied in a loose low clip, wearing an oversized ochre knit cardigan over a white crew-neck tee and round tortoiseshell glasses
  ```
* **`[CHAR_LEO]`**:
  ```text
  Leo, a 45-year-old artisanal barista with a neatly trimmed salt-and-pepper beard, warm crinkles around hazel eyes, wearing a charcoal linen apron over a rolled-sleeve chambray shirt
  ```
* **`[PROP_CUP]`**:
  ```text
  a handcrafted matte terracotta ceramic cappuccino cup resting on a matching saucer, embossed with a minimalist gold sun emblem and the word "SOLIS", topped with rich hazelnut latte art crema
  ```

### Stage-by-Stage Prompt Pack ("Solis")

| Stage | Asset ID | Modality / Mode | Copy-Paste Prompt |
| :-: | :--- | :--- | :--- |
| **0** | `SEED_SOLIS` | Text (`gemini-3.8-flash`) | `Act as a Commercial Film Director. Expand this 2-sentence story seed into a 3-Act 30-second commercial beat sheet for "Solis Artisan Coffee": "At 5:45 AM in a rainy city, an exhausted architect staring at a blank blueprint steps into a glowing corner café. One shared laugh and a warm terracotta cup of espresso reignite her creative spark." Keep it grounded in two characters (Maya, Leo), two locations (rainy studio desk, warm corner café), and one hero prop (matte terracotta Solis cup).` |
| **1A** | `ING_MAYA_PORTRAIT` | Image (`gemini-3-pro-image`) | `Photorealistic cinematic portrait of Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles across the nose, expressive dark brown eyes, shoulder-length wavy raven hair tied in a loose low clip, wearing an oversized ochre knit cardigan over a white crew-neck tee and round tortoiseshell glasses. Neutral studio backdrop with soft 5600K key light, 85mm prime lens, f/2.0, natural skin texture, front three-quarter angle, calm neutral expression, no text.` |
| **1B** | `ING_MAYA_SHEET` | Image (`gemini-3-pro-image`, `16:9`) | `A 4-panel character reference sheet on a clean neutral grey background showing the exact same woman in four views: (1) Front view neutral expression, (2) 45-degree three-quarter view with a tired sigh, (3) Side profile looking down thoughtfully, (4) Front close-up with a warm, genuine smile. Subject: Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles across the nose, expressive dark brown eyes, shoulder-length wavy raven hair tied in a loose low clip, wearing an oversized ochre knit cardigan over a white crew-neck tee and round tortoiseshell glasses. Identical facial structure and glasses across all panels, 85mm lens, no text.` |
| **1C** | `ING_LEO_PORTRAIT` | Image (`gemini-3-pro-image`) | `Photorealistic cinematic portrait of Leo, a 45-year-old artisanal barista with a neatly trimmed salt-and-pepper beard, warm crinkles around hazel eyes, wearing a charcoal linen apron over a rolled-sleeve chambray shirt. Neutral studio backdrop, soft warm key light, 85mm prime lens, f/2.2, natural skin pores, welcoming gentle smile, no text.` |
| **2A** | `ING_SCENE_STUDIO` | Image (`gemini-3-pro-image`, `16:9`) | `Wide establishing interior shot of a minimalist architect's loft desk by a tall rain-streaked industrial window at 5:45 AM before dawn. Empty chair, no people. A drafting lamp casts a cool cyan-blue pool of light over an unrolled blank blueprint, scale ruler, and crumpled sketches. Raindrops trickle down the glass with blurred city streetlights outside. Moody teal-and-slate color grade, 35mm anamorphic lens, shallow depth of field, no text.` |
| **2B** | `ING_SCENE_CAFE` | Image (`gemini-3-pro-image`, `16:9`) | `Medium-wide interior shot of a cozy, wood-paneled artisan espresso bar at dawn. Empty frame with no people. Warm amber Edison bulbs and a polished brass espresso machine gleam with gentle steam rising. Rain is visible outside the fogged front window, contrasting with the rich golden warmth inside. Reclaimed oak counter in the foreground, 35mm cinema lens, Kodak Vision3 500T film look, no text.` |
| **2C** | `ING_PROP_CUP` | Image (`gemini-3-pro-image`, `16:9`) | `Macro studio product photograph of a handcrafted matte terracotta ceramic cappuccino cup resting on a matching terracotta saucer. A minimalist gold embossed sun emblem and the word "SOLIS" are printed cleanly on the front of the cup. Rich velvety hazelnut crema with delicate rosetta latte art on top, a wisp of steam rising. Soft warm rim lighting, neutral dark background, 100mm macro lens.` |
| **4.1** | `VID_SHOT_01` | Video (`Veo 3.1` — *Ingredients to Video*) | `Slow, smooth dolly-in toward a medium close-up of Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles, wavy raven hair in a low clip, round tortoiseshell glasses, and an ochre knit cardigan, sitting at her drafting table by a rain-streaked window at 5:45 AM. She exhales a quiet sigh, taps her wooden pencil twice against the blank blueprint, and glances out at the rain. Cold cyan streetlamp reflections glide across her glasses. Shallow depth of field, 35mm anamorphic lens. Audio: Soft rhythmic rain pattering against window glass, distant thunder, two crisp wooden pencil taps, and a quiet sigh.` |
| **4.2** | `VID_SHOT_02` | Video (`Veo 3.1` — *Ingredients to Video*) | `Smooth lateral tracking shot following Maya, a 29-year-old Latina architect in her ochre knit cardigan and round tortoiseshell glasses, as she pushes open the glass café door from the rainy blue street and steps into the warm golden glow of the artisan espresso bar. A brass door chime rings softly as she shakes raindrops off her umbrella and looks toward the counter with relief. 35mm cinema lens. Audio: Rain sound fading as the wooden door closes, a warm brass shop bell chime, gentle espresso machine hiss.` |
| **4.3** | `VID_SHOT_03` | Video (`Veo 3.1` — *Frames to Video*) | `Macro cinematic tracking shot transitioning smoothly from the first frame to the last frame. Rich, syrupy espresso finishes pouring into the matte terracotta SOLIS cup, forming velvety hazelnut crema. Barista Leo's hand gently lifts the cup, places it onto the reclaimed oak counter, and slides it smoothly toward the foreground camera as a wisp of golden steam curls upward. 100mm macro lens, 60fps slow-motion feel. Audio: Rich espresso extraction hiss, gentle ceramic clink on oak wood, warm fingerpicked acoustic guitar notes entering.` |
| **5.1** | `VID_SHOT_04` | Video (`Veo 3.1` — *Dialogue OTS*) | `Over-the-shoulder medium shot framed from behind Maya's ochre-cardigan shoulder on the left, focusing on Leo, a 45-year-old barista with a neat salt-and-pepper beard and charcoal linen apron positioned on the right of the frame, looking screen-left with a warm, knowing smile. As his hand rests beside the steaming terracotta SOLIS cup on the counter, Leo speaks clearly in a warm, grounded baritone voice: 'Rough night with the blueprints? Start with this—the lines always follow.' Warm amber café lighting, 50mm lens, natural lip sync. Audio: Cozy café ambiance, soft rain outside, and Leo speaking in a warm baritone: 'Rough night with the blueprints? Start with this—the lines always follow.'` |
| **5.2** | `VID_SHOT_05` | Video (`Veo 3.1` — *Dialogue Reverse*) | `Reverse-angle medium close-up of Maya, a 29-year-old Latina architect with warm olive skin, round tortoiseshell glasses, and ochre knit cardigan positioned on the left of the frame, looking screen-right toward the barista. She wraps both hands around the warm terracotta SOLIS cup, inhales the rising steam, and her tired expression melts into a genuine, relieved smile. She replies softly with a light chuckle: 'You just saved the whole skyline, Leo.' Warm golden key light, 50mm prime lens, natural lip sync. Audio: Gentle café murmur and Maya speaking in a warm, relieved voice with a subtle laugh: 'You just saved the whole skyline, Leo.'` |
| **6.1** | `VID_SHOT_06` | Video (`Veo 3.1` — *Scenebuilder Jump To / Frames*) | `Smooth push-in tilting down over Maya's shoulder at her studio desk as warm golden sunrise streams through the wet window, illuminating the steaming terracotta SOLIS cup beside her blueprint. Maya's charcoal pencil sweeps across the paper in one confident motion, completing a soaring architectural bridge arch. Warm golden-hour cinema grade, 35mm lens. Audio: Uplifting acoustic guitar and strings crescendo, crisp charcoal sketching stroke on heavy paper, followed by warm voiceover: 'Solis. Awaken the craft.'` |

---

## Part 3: Bonus Story Pack #1 (Fintech / SMB) — "NovaPay: The Market Rainstorm"

Use this incremental story pack to demonstrate a **Fintech / Digital Payments** commercial:

* **Stage 0 (2-Sentence Seed)**:
  > *"When a sudden downpour knocks out the old wired card terminal at an outdoor flower market, a worried florist nearly loses her biggest anniversary bouquet order. With one tap on her smartphone using NovaPay, the payment clears in a second and both customer and florist share a relieved laugh under the awning."*
* **Stage 1 (Character Identity Anchors)**:
  - **`[CHAR_ELENA]` (Florist)**: `Elena, a 38-year-old botanical shop owner with sun-kissed bronze skin, a friendly dimple on her left cheek, curly chestnut hair tucked under a sage-green canvas bucket hat, wearing a denim work apron over a cream linen shirt`
  - **`[CHAR_MARCO]` (Customer)**: `Marco, a 32-year-old groom-to-be with fair skin, short tousled dark blond hair, wearing a navy trench coat beaded with raindrops, holding a wrapped bouquet of white peonies`
* **Stage 2 (Scene & Product Ingredients)**:
  - **`[SCENE_STALL]`**: `Vibrant covered open-air flower market stall under a striped canvas awning during a spring rainstorm, buckets of white peonies and eucalyptus, warm string lights glowing against misty rain, 35mm lens, no people.`
  - **`[PROP_PHONE]`**: `Close-up of a sleek matte-slate smartphone screen displaying a glowing emerald checkmark and the clean white logo "NOVAPAY — Approved" with contactless wave ripples.`
* **Stage 5 (Shot-Reverse-Shot Conversation Prompts)**:
  - **Shot 4 (Marco, on left looking screen-right)**:
    ```text
    Medium close-up of Marco, a 32-year-old man in a rain-beaded navy trench coat holding white peonies on the left of the frame, looking screen-right with a sympathetic smile as he holds up his contactless card: 'No power on the terminal? Tell me you have a backup—my anniversary dinner is in twenty minutes.'
    ```
  - **Shot 5 (Elena, on right looking screen-left)**:
    ```text
    Reverse-angle medium close-up of Elena, a 38-year-old florist in a sage-green canvas hat and denim apron on the right of the frame, looking screen-left with a confident grin as she holds out her smartphone: 'Tap right here on my phone—NovaPay doesn't care about the rain.' Audio: Crisp contactless payment chime and both laughing over the sound of rain.
    ```

---

## Part 4: Bonus Story Pack #2 (Retail / Outdoor) — "Kuntur Gear: The Ridge at Dawn"

Use this incremental story pack to demonstrate an **Outdoor Apparel / Retail** commercial:

* **Stage 0 (2-Sentence Seed)**:
  > *"Shivering at a windy 4,800-meter mountain pass before sunrise, a young wildlife photographer struggles to steady her camera lens. Her veteran mountain guide zips up her copper-orange Kuntur thermal shell, and together they capture the first golden condor flight across the ridge."*
* **Stage 1 (Character Identity Anchors)**:
  - **`[CHAR_SOFIA]` (Photographer)**: `Sofia, a 26-year-old Andean wildlife photographer with warm copper-tan skin, high cheekbones, braided black hair under a charcoal merino beanie, wearing a vibrant burnt-orange Kuntur technical alpine shell jacket with matte black waterproof zippers`
  - **`[CHAR_MATEO]` (Guide)**: `Mateo, a 52-year-old veteran mountain guide with weathered bronze skin, deep laugh lines, silver stubble, wearing dark glacier sunglasses and a slate-grey alpine parka`

---

## Part 5: Cross-Platform Execution Cheat Sheet

| Workshop Step | Google Flow (`labs.google/fx/tools/flow`) | Google AI Studio / Vertex GenMedia | Runway Gen-4 / Luma / Kling / Midjourney |
| :--- | :--- | :--- | :--- |
| **Story Seed** | Flow Agent / Gemini Brainstorming | `gemini-3.8-flash` (`thinking_level="low"`) | Any LLM chat |
| **Character & Face Lock** | **Ingredients Panel** $\rightarrow$ Create & Pin Character | `gemini-3-pro-image` (4-Panel Turnaround Sheet) | Midjourney `--cref` / Runway Act-One / Character Ref |
| **Scene & Product Plates** | **Ingredients Panel** $\rightarrow$ Create & Pin Scene/Prop | `gemini-3-pro-image` (`16:9` empty plates) | Text-to-Image `16:9` clean plates |
| **Storyboard Keyframes** | Combine Ingredients into Still Frames | `gemini-3-pro-image` with 3 reference images | Multi-Image Reference / Image Compositing |
| **Multi-Asset Animation** | **Ingredients to Video** (up to 3 refs, Veo 3.1) | `veo-3.1` / `gemini-omni-1.1-flash` (`reference_images`) | Multi-Subject Image-to-Video |
| **Exact Start $\rightarrow$ End Motion** | **Frames to Video** (First Frame + Last Frame) | `veo-3.1` / `gemini-omni-1.1-flash` (`first_frame`, `last_frame`) | Start/End Keyframe Interpolation |
| **Dialogue & Voiceover** | Veo 3.1 Native Audio (`'spoken line'`) | Veo 3.1 Native Audio + `gemini-3.8-flash-tts` (`Kore`, `Charon`) | Lip-Sync tool + TTS audio track |
| **Timeline Continuity** | **Scenebuilder** (`Extend`, `Jump To`) | Video Extension API + NLE Timeline | Extend Clip + CapCut / Premiere / DaVinci |

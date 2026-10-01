# Part I: Google Flow Prompt Sandbox (Labs A–D)

> **Purpose**: Before building a full multi-shot story, spend 25 minutes in **Google Flow** ([labs.google/fx/tools/flow](https://labs.google/fx/tools/flow)) testing **one isolated visual or motion lever at a time**. By holding the subject constant and changing only one variable per prompt, you see immediately how **Nano Banana Pro** (Image) and **Gemini Omni Flash** (Video) respond to camera geometry, color temperature, artistic styles, and multi-object physics.

---

## How to Run the Sandbox in Google Flow

1. Open **[Google Flow](https://labs.google/fx/tools/flow)** and click **+ New Project** $\rightarrow$ name it `00 - Flow Prompt Sandbox`.
2. In the bottom prompt bar:
   - Select **Image** $\rightarrow$ **Nano Banana Pro** (`16:9`) to test static framing, lighting, and styles.
   - Select **Video** $\rightarrow$ **Omni Flash** (`16:9`, `6s` or `8s`) to test camera motion, physics, and conversational video edits.
   - **Pro Tip**: Select **Omni 360p** while experimenting to generate drafts at half the credit cost, then click **Upscale to 720p** (0 credits) on your favorite clips!

---

## Lab A: Extreme Camera Angles & Motion Geometry

Hold the subject constant (*a brass espresso machine on an oak counter in a sunlit cafe*) and change **only the camera angle and movement**.

### Prompt A.1 — Extreme Worm's-Eye Low Angle (`Image > Nano Banana Pro`)

```text
Extreme low-angle worm's-eye view looking straight up from the surface of a reclaimed oak counter at a towering vintage brass espresso machine, 14mm ultra-wide lens, dramatic vertical perspective lines converging toward the ceiling, golden morning sunlight streaming through tall factory windows, shallow depth of field, photorealistic commercial photography.
```

### Prompt A.2 — 90° Top-Down Overhead Flat-Lay (`Image > Nano Banana Pro`)

```text
90-degree top-down bird's-eye view looking straight down at a reclaimed oak counter with a vintage brass espresso machine, a terracotta ceramic cup, a linen napkin, and scattered roasted coffee beans arranged in balanced geometric symmetry, 50mm lens, soft diffused overhead daylight, crisp commercial product photography.
```

### Prompt A.3 — Single-Take Whip-Pan to Macro Close-Up (`Video > Omni Flash`, `6s`)

```text
Dynamic camera starting in a wide establishing shot of a sunlit industrial-chic cafe, then executing a fast whip-pan right and smooth dolly-in to an extreme macro close-up of dark espresso pouring from a brass portafilter into a matte terracotta cup, golden crema swirling, realistic steam rising, natural espresso pouring and cafe room-tone audio.
```

### Prompt A.4 — Conversational Camera Angle Edit (`Omni Flash Video Edit` — Turn 1)

Click the video generated in **Prompt A.3**, select the **Edit Video** prompt box in Google Flow, and type:

```text
Change the camera movement to a slow, steady 180-degree eye-level orbit around the brass espresso machine while keeping the pouring espresso and rising steam identical.
```

---

## Lab B: Warmth, Color Temperature & Relighting

Hold the composition constant (*an architect's drafting desk by a rain-streaked window*) and shift **only the Kelvin color temperature and lighting mood**.

### Prompt B.1 — Cold 7500K Pre-Dawn Isolation (`Image > Nano Banana Pro`)

```text
Medium wide shot of an architect's drafting desk beside a tall rain-streaked glass window at 5:45 AM, cold 7500K blue-hour ambient light, muted slate-blue shadows, a single unlit brass desk lamp, a blank white blueprint roll, melancholic and quiet mood, 35mm lens, photorealistic cinema still.
```

### Prompt B.2 — Warm 2400K Golden Sunrise Breakthrough (`Image > Nano Banana Pro`)

```text
Medium wide shot of an architect's drafting desk beside a tall glass window at 6:15 AM, warm 2400K golden-hour sunrise beams cutting through morning mist, glowing amber rim light on the wooden desk, long dramatic shadows, warm brass desk lamp switched on, hopeful and inspiring mood, 35mm lens, photorealistic cinema still.
```

### Prompt B.3 — Real-Time Cold-to-Warm Lighting Shift (`Video > Omni Flash`, `8s`)

```text
Fixed-tripod medium shot of an architect's drafting desk by a rain-streaked window. Over 8 seconds, the lighting transitions smoothly from cold 7500K blue pre-dawn shadows into warm 2400K golden sunrise beams flooding across the desk and illuminating a steaming terracotta coffee cup, gentle rain fading into morning birdsong.
```

### Prompt B.4 — Conversational Relighting (`Omni Flash Video Edit` — Turn 1)

Select the video from **Prompt B.3** and apply a 1-turn conversational video edit in Google Flow:

```text
Change the lighting to cozy 2200K warm amber candlelight at night with soft golden bokeh reflections on the window glass.
```

---

## Lab C: Visual Styles & Mediums

Keep the exact same scene (*a barista pouring latte art into a terracotta cup*) and swap **only the artistic medium**.

### Prompt C.1 — 35mm Anamorphic Kodak Vision3 Film (`Image > Nano Banana Pro`)

```text
Close-up of hands pouring steamed milk into a matte terracotta coffee cup to form a rosette latte art pattern, shot on 35mm Kodak Vision3 500T film, 2.39:1 anamorphic lens, horizontal amber lens flare, organic silver-halide film grain, rich halation on warm highlights, shallow depth of field.
```

### Prompt C.2 — 12fps Stop-Motion Felt & Clay Diorama (`Video > Omni Flash`, `6s`)

```text
Handcrafted stop-motion animation at 12 frames per second of a miniature clay barista pouring cotton-wool steam and glossy resin espresso into a tiny terracotta clay mug on a balsa-wood counter, visible thumbprints on the clay, stitched felt apron texture, warm miniature stage lighting, playful tactile charm.
```

### Prompt C.3 — Architectural Ink & Watercolor Concept Sketch (`Image > Nano Banana Pro`)

```text
Expressive architectural concept illustration of a barista pouring coffee at an oak counter, hand-drawn black fountain-pen ink linework with loose burnt-sienna, warm ochre, and Prussian-blue watercolor washes on textured cold-press cotton paper, visible pencil construction lines.
```

---

## Lab D: Combining Objects, Physics & Kinetic Typography

Push **Nano Banana Pro** and **Gemini Omni Flash** to compose multiple distinct objects with exact spatial placement, cause-and-effect physics, and clean in-video text.

### Prompt D.1 — 5-Object Spatial Lock (`Image > Nano Banana Pro`)

```text
Crisp 45-degree tabletop product shot on a reclaimed oak counter containing five exact objects: (1) a matte terracotta cup embossed with 'SOLIS' in the center, (2) antique brass compass calipers to the left, (3) a rolled white architectural blueprint behind the cup, (4) round tortoiseshell eyeglasses resting on the blueprint, and (5) a sprig of fresh green rosemary to the right, warm morning side-light, 50mm lens.
```

### Prompt D.2 — Multi-Object Physics Chain Reaction (`Video > Omni Flash`, `8s`)

```text
Continuous macro tracking shot across an oak drafting table: a single roasted coffee bean rolls down a wooden ruler, tips a brass balance scale, which gently nudges a glass carafe to pour a dark ribbon of coffee into a matte terracotta 'SOLIS' cup as golden steam rises into a warm sunbeam, realistic clinking and pouring sound effects.
```

### Prompt D.3 — In-Video Kinetic Brand Typography (`Video > Omni Flash`, `6s`)

```text
Cinematic close-up of a steaming matte terracotta cup embossed with 'SOLIS' on an oak counter in golden morning sunlight. As the translucent white steam rises into the warm air, clean minimalist gold serif typography reading 'AWAKEN THE CRAFT' forms naturally in the center of the frame above the cup, soft acoustic chord and gentle cafe ambiance.
```

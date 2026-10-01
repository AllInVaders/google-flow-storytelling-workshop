# Student Hands-On Lab Guide: Google Flow & Gemini Omni Storytelling

Welcome to the **Google Flow & Gemini Omni Storytelling Workshop**! Every lab in this guide runs directly inside **[Google Flow](https://labs.google/fx/tools/flow)**.

- **Part I (25 Min)**: **Prompt Sandbox (Labs A–D)** — Test camera angles, warmth, visual styles, and multi-object physics in isolation.
- **Part II (65 Min)**: **5-Step Incremental Story Build** — Produce a 30-second commercial (*"Solis Artisan Coffee — The 6:00 AM Spark"*) from a 2-sentence story seed using **`@Maya`** and **`@Leo`** character references, **Nano Banana Pro**, **Gemini Omni Flash**, and **Scenebuilder**.

---

## Part I: Google Flow Prompt Sandbox (Labs A–D)

### Workspace Setup
1. Open **[labs.google/fx/tools/flow](https://labs.google/fx/tools/flow)** and click **+ New Project** $\rightarrow$ name it `00 - Flow Prompt Sandbox`.
2. In the bottom prompt box, switch between:
   - **Image $\rightarrow$ Nano Banana Pro** (`16:9`) for still frames.
   - **Video $\rightarrow$ Omni Flash** (`16:9`, `6s` or `8s`, **Omni 360p** draft mode) for video clips.

---

### Lab A: Camera Angles & Motion Geometry
Keep the subject identical (*a brass espresso machine on an oak counter*) and test how camera geometry changes power and intimacy:

1. **Worm's-Eye Low Angle (`Image > Nano Banana Pro`)**:
   ```text
   Extreme low-angle worm's-eye view looking straight up from the surface of a reclaimed oak counter at a towering vintage brass espresso machine, 14mm ultra-wide lens, dramatic vertical perspective lines converging toward the ceiling, golden morning sunlight streaming through tall factory windows, shallow depth of field, photorealistic commercial photography.
   ```
2. **90° Overhead Flat-Lay (`Image > Nano Banana Pro`)**:
   ```text
   90-degree top-down bird's-eye view looking straight down at a reclaimed oak counter with a vintage brass espresso machine, a terracotta ceramic cup, a linen napkin, and scattered roasted coffee beans arranged in balanced geometric symmetry, 50mm lens, soft diffused overhead daylight, crisp commercial product photography.
   ```
3. **Single-Take Whip-Pan (`Video > Omni Flash`, `6s`)**:
   ```text
   Dynamic camera starting in a wide establishing shot of a sunlit industrial-chic cafe, then executing a fast whip-pan right and smooth dolly-in to an extreme macro close-up of dark espresso pouring from a brass portafilter into a matte terracotta cup, golden crema swirling, realistic steam rising, natural espresso pouring and cafe room-tone audio.
   ```
4. **1-Turn Camera Edit (`Omni Flash Video Edit`)**: Click the video from #3, select **Edit Video**, and type:
   ```text
   Change the camera movement to a slow, steady 180-degree eye-level orbit around the brass espresso machine while keeping the pouring espresso and rising steam identical.
   ```

---

### Lab B: Warmth, Color Temperature & Relighting
Test how Kelvin color temperature tells an emotional story before any actor speaks:

1. **7500K Cold Blue Pre-Dawn (`Image > Nano Banana Pro`)**:
   ```text
   Medium wide shot of an architect's drafting desk beside a tall rain-streaked glass window at 5:45 AM, cold 7500K blue-hour ambient light, muted slate-blue shadows, a single unlit brass desk lamp, a blank white blueprint roll, melancholic and quiet mood, 35mm lens, photorealistic cinema still.
   ```
2. **2400K Warm Golden Sunrise (`Image > Nano Banana Pro`)**:
   ```text
   Medium wide shot of an architect's drafting desk beside a tall glass window at 6:15 AM, warm 2400K golden-hour sunrise beams cutting through morning mist, glowing amber rim light on the wooden desk, long dramatic shadows, warm brass desk lamp switched on, hopeful and inspiring mood, 35mm lens, photorealistic cinema still.
   ```
3. **Real-Time Cold-to-Warm Transition (`Video > Omni Flash`, `8s`)**:
   ```text
   Fixed-tripod medium shot of an architect's drafting desk by a rain-streaked window. Over 8 seconds, the lighting transitions smoothly from cold 7500K blue pre-dawn shadows into warm 2400K golden sunrise beams flooding across the desk and illuminating a steaming terracotta coffee cup, gentle rain fading into morning birdsong.
   ```
4. **1-Turn Relighting Edit (`Omni Flash Video Edit`)**: Click the video from #3, select **Edit Video**, and type:
   ```text
   Change the lighting to cozy 2200K warm amber candlelight at night with soft golden bokeh reflections on the window glass.
   ```

---

### Lab C: Visual Styles & Mediums
Render the exact same action across three distinct visual mediums:

1. **35mm Anamorphic Film (`Image > Nano Banana Pro`)**:
   ```text
   Close-up of hands pouring steamed milk into a matte terracotta coffee cup to form a rosette latte art pattern, shot on 35mm Kodak Vision3 500T film, 2.39:1 anamorphic lens, horizontal amber lens flare, organic silver-halide film grain, rich halation on warm highlights, shallow depth of field.
   ```
2. **12fps Stop-Motion Clay & Felt (`Video > Omni Flash`, `6s`)**:
   ```text
   Handcrafted stop-motion animation at 12 frames per second of a miniature clay barista pouring cotton-wool steam and glossy resin espresso into a tiny terracotta clay mug on a balsa-wood counter, visible thumbprints on the clay, stitched felt apron texture, warm miniature stage lighting, playful tactile charm.
   ```
3. **Architectural Ink & Watercolor (`Image > Nano Banana Pro`)**:
   ```text
   Expressive architectural concept illustration of a barista pouring coffee at an oak counter, hand-drawn black fountain-pen ink linework with loose burnt-sienna, warm ochre, and Prussian-blue watercolor washes on textured cold-press cotton paper, visible pencil construction lines.
   ```

---

### Lab D: Combining Objects, Physics & Kinetic Text
1. **5-Object Spatial Lock (`Image > Nano Banana Pro`)**:
   ```text
   Crisp 45-degree tabletop product shot on a reclaimed oak counter containing five exact objects: (1) a matte terracotta cup embossed with 'SOLIS' in the center, (2) antique brass compass calipers to the left, (3) a rolled white architectural blueprint behind the cup, (4) round tortoiseshell eyeglasses resting on the blueprint, and (5) a sprig of fresh green rosemary to the right, warm morning side-light, 50mm lens.
   ```
2. **Multi-Object Chain Reaction (`Video > Omni Flash`, `8s`)**:
   ```text
   Continuous macro tracking shot across an oak drafting table: a single roasted coffee bean rolls down a wooden ruler, tips a brass balance scale, which gently nudges a glass carafe to pour a dark ribbon of coffee into a matte terracotta 'SOLIS' cup as golden steam rises into a warm sunbeam, realistic clinking and pouring sound effects.
   ```
3. **In-Video Kinetic Typography (`Video > Omni Flash`, `6s`)**:
   ```text
   Cinematic close-up of a steaming matte terracotta cup embossed with 'SOLIS' on an oak counter in golden morning sunlight. As the translucent white steam rises into the warm air, clean minimalist gold serif typography reading 'AWAKEN THE CRAFT' forms naturally in the center of the frame above the cup, soft acoustic chord and gentle cafe ambiance.
   ```

---

## Part II: 5-Step Incremental Commercial Build in Google Flow

Create a new project in **[Google Flow](https://labs.google/fx/tools/flow)** named `Solis - The 6AM Spark`.

---

### Step 1: Start With a 2-Sentence Story & 5-Shot Beat Sheet

Open the **Google Flow Agent** panel inside your project and paste:

```text
We are creating a 30-second commercial in Google Flow for 'Solis Artisan Coffee' titled 'The 6:00 AM Spark.'
Story Seed: At 5:45 AM on a rainy morning, exhausted architect Maya stares at a blank blueprint in her cold studio until she walks into a warm neighborhood cafe where barista Leo slides her a steaming terracotta cup of Solis coffee. One sip sparks her creativity and transforms her blank page into a sunlit bridge design.

Break this story into a concise 5-shot beat sheet for Google Flow:
- Shot 1 (Studio - Creative Block, 6s)
- Shot 2 (Cafe Arrival - Transition from Cold Rain to Warm Glow, 6s)
- Shot 3 (The Craft - Leo Pours & Slides the Solis Cup, 6s)
- Shot 4 (Dialogue - Leo's Encouragement, 6s)
- Shot 5 (Dialogue, First Sip & Creative Spark Finale, 6s)
For each shot, list only: Shot #, Setting (@Studio or @Cafe), Characters (@Maya, @Leo), Action, and Lighting Shift.
```

---

### Step 2: Create Characters (`@Maya`, `@Leo`) & Scene Ingredients Once

> **⚠️ Critical Rule**: In Google Flow, you create a character **once** in **Characters $\rightarrow$ New Character**. After you click **Done**, **never re-describe their physical appearance again**! In every future prompt, simply type **`@Maya`** or **`@Leo`** (e.g., `"@Maya drinks coffee"`).

#### 2A. Create Your Two Characters (`Left Sidebar > Characters > New Character`)

1. **Create `@Maya`**:
   - Click **Characters** $\rightarrow$ **New Character**.
   - Paste this description **once** and click **Generate**:
     ```text
     29-year-old Latina architect with warm olive skin, subtle freckles across the nose, shoulder-length wavy raven hair pinned in a loose low clip, round tortoiseshell eyeglasses, wearing a mustard-ochre ribbed knit cardigan over a crisp white crew-neck tee, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
     ```
   - Enter Character Name: **`Maya`**
   - Click **Select a voice** $\rightarrow$ pick a **Warm Female Alto** $\rightarrow$ **Add to Character** $\rightarrow$ **Done**.

2. **Create `@Leo`**:
   - Click **Characters** $\rightarrow$ **New Character**.
   - Paste this description **once** and click **Generate**:
     ```text
     42-year-old artisan barista with medium-brown skin, silver-flecked short curly hair, neatly trimmed beard, warm smile lines around the eyes, wearing a washed indigo denim apron over a charcoal henley with rolled sleeves, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
     ```
   - Enter Character Name: **`Leo`**
   - Click **Select a voice** $\rightarrow$ pick a **Warm Male Baritone** $\rightarrow$ **Add to Character** $\rightarrow$ **Done**.

#### 2B. Create Your Three Scene & Prop Ingredients (`Image > Nano Banana Pro`)

Generate these three assets in **Image $\rightarrow$ Nano Banana Pro** (`16:9`) and name them `Studio`, `Cafe`, and `SolisCup`:

1. **`@Studio`**:
   ```text
   Empty architectural studio loft at 5:45 AM before dawn, wide establishing shot, rain-streaked floor-to-ceiling industrial glass window overlooking a misty blue-hour city skyline, tilted birchwood drafting table with a blank white blueprint roll, brass desk lamp turned off, cold 7000K slate-blue lighting, 24mm lens, no people.
   ```
2. **`@Cafe`**:
   ```text
   Empty neighborhood artisan coffee shop interior at 6:00 AM, reclaimed oak counter in the foreground, gleaming vintage brass espresso machine, warm 2700K Edison pendant bulbs glowing against exposed brick, rain visible on the front glass window, inviting golden-amber atmosphere, 35mm lens, no people.
   ```
3. **`@SolisCup`**:
   ```text
   Product close-up of a handcrafted matte terracotta ceramic cappuccino cup with a cream ceramic interior resting on a matching terracotta saucer, subtle minimalist embossed wordmark 'SOLIS' on the front of the cup, rich dark espresso with velvety hazelnut-brown microfoam rosette latte art, soft studio lighting.
   ```

---

### Step 3: Build Storyboard Frames Using `@Maya` & `@Leo` (`Image > Nano Banana Pro`)

In **Image $\rightarrow$ Nano Banana Pro** (`16:9`), type `@` in the prompt box to select your saved Characters and Ingredients. Notice how short and clean every prompt is!

1. **Frame 3.1 (Shot 1 — Studio Block)**:
   ```text
   @Maya sitting at the drafting desk inside @Studio at 5:45 AM, leaning on her elbow and staring tiredly at the blank white blueprint, holding a charcoal pencil loosely, cold blue pre-dawn window light, medium shot, 35mm lens.
   ```
2. **Frame 3.2 (Shot 2 — Cafe Arrival)**:
   ```text
   @Maya stepping inside @Cafe out of the morning rain, looking toward the warm glowing espresso counter with quiet relief, cool blue rain outside the door contrasting with warm golden light inside, medium wide shot, 35mm lens.
   ```
3. **Frame 3.3 (Shot 3 Start Frame — Leo Pours)**:
   ```text
   @Leo standing behind the oak counter in @Cafe, pulling a fresh espresso shot from the brass machine into @SolisCup as aromatic steam rises, warm 2700K pendant lighting, medium shot, 50mm lens.
   ```
4. **Frame 3.4 (Shot 3 End Frame — Cup Slid to Maya)**:
   ```text
   Close-up on the oak counter in @Cafe as @Leo's hand finishes sliding the steaming @SolisCup into the foreground in front of @Maya, warm golden morning light catching the rising steam, shallow depth of field, 50mm lens.
   ```
5. **Frame 3.5 (Shot 5 Frame — Maya's First Sip)**:
   ```text
   Medium close-up of @Maya in @Cafe wrapping both hands around @SolisCup, inhaling the warm steam with her eyes brightening in a moment of sudden creative inspiration, warm 2400K golden sunrise light streaming across the counter, 50mm lens.
   ```

---

### Step 4: Animate Video & Dialogue in Google Flow (`Video > Omni Flash`)

Switch the prompt bar to **Video $\rightarrow$ Omni Flash** (`16:9`, `6s`).

1. **Clip 4.1 — Shot 1 (`Ingredients` or `+ Add start frame` with Frame 3.1)**:
   ```text
   Slow push-in medium shot of @Maya sitting at the drafting table in @Studio, rubbing her temple and tapping her charcoal pencil against the blank white blueprint while rain patters softly against the cold blue window glass.
   ```
2. **Clip 4.2 — Shot 2 (`Ingredients` or `+ Add start frame` with Frame 3.2)**:
   ```text
   Smooth tracking shot following @Maya as she walks into @Cafe, shaking a drop of rain from her sleeve and walking up to the warm sunlit oak espresso bar, gentle door chime and cozy cafe ambiance.
   ```
3. **Clip 4.3 — Shot 3 (`Frames Mode`: attach Frame 3.3 as `+ Add start frame` and Frame 3.4 as `+ Add end frame`)**:
   ```text
   Smooth camera tilt and follow as @Leo finishes pouring rich crema into @SolisCup and slides the steaming cup smoothly across the oak counter in @Cafe toward @Maya, espresso machine hiss and ceramic saucer slide audio.
   ```
4. **Clip 4.4 — Shot 4: Leo Speaks (`Ingredients`: `@Leo`, `@Maya`, `@Cafe`, `@SolisCup`)**:
   ```text
   Over-the-shoulder medium shot from behind @Maya on the left, focusing on @Leo on the right looking screen-left across the counter in @Cafe with a warm smile. @Leo says: "Rough night with the blueprints? Start with this."
   ```
5. **Clip 4.5 — Shot 5: Maya Drinks Coffee & Replies (`Ingredients`: `@Maya`, `@Cafe`, `@SolisCup`)**:
   ```text
   Reverse-angle medium close-up of @Maya on the left looking screen-right in @Cafe. @Maya drinks coffee from @SolisCup, lowers the cup with a warm inspired smile, and says: "You just saved the whole skyline, Leo."
   ```

---

### Step 5: Conversational Video Editing (`Omni Flash`) & Scenebuilder

1. **Turn 1 Conversational Edit on Clip 4.5**: Click **Clip 4.5** $\rightarrow$ **Edit Video** $\rightarrow$ enter:
   ```text
   Intensify the warm 2400K golden sunrise beams streaming through the window behind @Maya and make the rising coffee steam from @SolisCup glow softly in the backlight.
   ```
2. **Turn 2 Conversational Edit on Clip 4.5**: In the same edit thread, enter:
   ```text
   In the final 2 seconds as the steam rises, fade in clean minimalist gold serif text in the upper center reading 'SOLIS — AWAKEN THE CRAFT'.
   ```
3. **Assemble in Scenebuilder**:
   - Click **More ($\vdots$) $\rightarrow$ Add to Scene** on **Clips 4.1 through 4.5**.
   - Open **Scenebuilder**, trim the clip handles so `@Leo`'s question flows right into `@Maya` drinking coffee and replying, click **Upscale to 720p** (0 credits) on any draft clips, and click **Download**!

# Part II: "Solis Artisan Coffee — The 6:00 AM Spark" (Google Flow Prompt Library)

> **100% Real Google Flow + Gemini Omni Flash Workflow**: Every prompt in this library runs directly inside **[Google Flow](https://labs.google/fx/tools/flow)** using **only existing, verified Google Flow features**:
> - **Google Flow Agent** (Conversational story & beat-sheet brainstorming)
> - **Characters (`@Maya`, `@Leo`)**: Created once in **Left Sidebar $\rightarrow$ Characters $\rightarrow$ New Character** (with bundled **Voice**), then referenced as **`@Maya`** and **`@Leo`** in every prompt.
> - **Adding Existing Images to Prompts (`More > Add to Prompt` / `Video > Ingredients` / `Video > Frames`)**: In Google Flow, only **Characters** (`@Maya`, `@Leo`) and **Voices** (`@Voice`) use `@Name` tags. To reference a scene, prop, or storyboard frame image, hover over the image tile and click **`More` ($\vdots$) $\rightarrow$ `Add to Prompt`** (or drag the image into the prompt box / **`+ Add start frame`** / **`+ Add end frame`**) and describe it in plain natural English!
> - **Gemini Omni Flash** (`Video` mode — `4s–10s` clips, `Omni 360p` $\rightarrow$ `720p` 0-credit upscale, `Save frame`, 3-turn conversational **Video Edit**, and **Scenebuilder**).

---

## ⚠️ The 2 Golden Rules of Referencing in Google Flow

### Rule 1: Create Characters Once $\rightarrow$ Refer ONLY by `@Maya` & `@Leo`
In Google Flow, you **never** repeat a character's physical description across scene prompts. Repeating physical traits causes the model to **re-generate a different person** in every shot.
1. Create the character **once** in **Left Sidebar $\rightarrow$ Characters $\rightarrow$ New Character** (locking their appearance, name, and voice).
2. In every storyboard and video prompt afterwards, simply type **`@Maya`** or **`@Leo`** and describe what they do!

### Rule 2: How to Reference Scene & Prop Images (No Fake `@Object` Tags!)
Google Flow's left sidebar has **All media, Images, Videos, Characters, Scenes, and Uploads**—there is **no** `@Object` or `@Location` tag feature. Instead, to keep a room or coffee cup consistent across shots:
- Hover over an existing image in your project and click **`More` ($\vdots$) $\rightarrow$ `Add to Prompt`** (or drag the image tile into the prompt box).
- In **Video $\rightarrow$ Omni Flash**, attach your storyboard image using **`Video > Frames` (`+ Add start frame` / `+ Add end frame`)** or **`Video > Ingredients` (`Add` button)**, or pause a video clip and click **`Save frame`** to use that frame in the next shot.

| ❌ Wrong (Re-Generating Characters or Fake `@Object` Tags) | ✅ Right (100% Real Google Flow Workflow) |
| :--- | :--- |
| *"A 29-year-old Latina architect with olive skin, freckles, raven hair, and glasses drinks from `@SolisCup` in `@Cafe`..."* | Attach the cafe frame via **`More > Add to Prompt`** (or **`+ Add start frame`**) and type:<br>**`@Maya drinks coffee from the terracotta cup and smiles.`** |

---

## Step 1: Story Seed & 5-Shot Beat Sheet (`Google Flow Agent`)

Open **Google Flow** ([labs.google/fx/tools/flow](https://labs.google/fx/tools/flow)) $\rightarrow$ **+ New Project** (`Solis - The 6AM Spark`) $\rightarrow$ open the **Google Flow Agent** panel and paste:

### Prompt 1.1 — 2-Sentence Story Seed to 5-Shot Beat Sheet

```text
We are creating a 30-second commercial in Google Flow for 'Solis Artisan Coffee' titled 'The 6:00 AM Spark.'
Story Seed: At 5:45 AM on a rainy morning, exhausted architect Maya stares at a blank blueprint in her cold studio until she walks into a warm neighborhood cafe where barista Leo slides her a steaming terracotta cup of Solis coffee. One sip sparks her creativity and transforms her blank page into a sunlit bridge design.

Break this story into a concise 5-shot beat sheet for Google Flow:
- Shot 1 (Studio - Creative Block, 6s)
- Shot 2 (Cafe Arrival - Transition from Cold Rain to Warm Glow, 6s)
- Shot 3 (The Craft - Leo Pours & Slides the Terracotta Cup, 6s)
- Shot 4 (Dialogue - Leo's Encouragement, 6s)
- Shot 5 (Dialogue, First Sip & Creative Spark Finale, 6s)
For each shot, list only: Shot #, Setting, Characters (@Maya, @Leo), Action, and Lighting Shift.
```

---

## Step 2: Create Locked Characters Once (`Characters > New Character`)

Click **Characters** (left sidebar) $\rightarrow$ **New Character**. Run each prompt **one single time** to create your cast:

### Character 1 — `@Maya`

- **Character Name**: `Maya`
- **Voice Selection**: Click **Select a voice** $\rightarrow$ choose a **Warm, Natural Female Alto** $\rightarrow$ **Add to Character** $\rightarrow$ **Done**
- **One-Time Character Creation Prompt**:

```text
29-year-old Latina architect with warm olive skin, subtle freckles across the nose, shoulder-length wavy raven hair pinned in a loose low clip, round tortoiseshell eyeglasses, wearing a mustard-ochre ribbed knit cardigan over a crisp white crew-neck tee, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
```

### Character 2 — `@Leo`

- **Character Name**: `Leo`
- **Voice Selection**: Click **Select a voice** $\rightarrow$ choose a **Warm, Friendly Male Baritone** $\rightarrow$ **Add to Character** $\rightarrow$ **Done**
- **One-Time Character Creation Prompt**:

```text
42-year-old artisan barista with medium-brown skin, silver-flecked short curly hair, neatly trimmed beard, warm smile lines around the eyes, wearing a washed indigo denim apron over a charcoal henley with rolled sleeves, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
```

---

## Step 3: Generate Scene & Storyboard Images (`Image > Nano Banana Pro`)

Switch the bottom prompt bar to **Image** $\rightarrow$ **Nano Banana Pro** (`16:9`).
- Notice how we **never re-describe Maya or Leo**—we only type **`@Maya`** and **`@Leo`**!
- **Pro Tip (`More > Add to Prompt`)**: Once you generate **Image 3.2** (the warm cafe interior), hover over that image tile and click **`More` ($\vdots$) $\rightarrow$ `Add to Prompt`** (or drag the image into the prompt box) when generating **Images 3.3, 3.4, and 3.5** so Google Flow uses the exact same cafe counter and terracotta cup as a visual reference!

### Image 3.1 — Shot 1 Storyboard Frame (Maya's Cold Studio)

```text
@Maya sitting at a birchwood drafting desk in an architectural studio loft at 5:45 AM, leaning on her elbow and staring tiredly at a blank white blueprint roll, rain-streaked glass window behind her, cold 7000K blue pre-dawn lighting, medium shot, 35mm lens.
```

### Image 3.2 — Shot 2 Storyboard Frame (Maya Enters the Warm Cafe)

```text
@Maya stepping inside a warm neighborhood artisan coffee shop out of the morning rain, looking toward a reclaimed oak counter with a gleaming vintage brass espresso machine, warm 2700K Edison pendant bulbs glowing against exposed brick, medium wide shot, 35mm lens.
```

### Image 3.3 — Shot 3 Start Frame (Leo Pours into the Terracotta Cup)

- **Optional Reference Image**: Click **`More > Add to Prompt`** on **Image 3.2** to keep the same cafe background.

```text
@Leo standing behind the reclaimed oak counter in the warm artisan coffee shop, pulling a fresh espresso shot from the vintage brass espresso machine into a matte terracotta cappuccino cup embossed with 'SOLIS' as aromatic steam rises, warm 2700K pendant lighting, medium shot, 50mm lens.
```

### Image 3.4 — Shot 3 End Frame (Leo Slides the Terracotta Cup to Maya)

- **Reference Image**: Click **`More > Add to Prompt`** on **Image 3.3** so the oak counter and terracotta cup match Image 3.3!

```text
Close-up on the reclaimed oak counter in the warm coffee shop as @Leo's hand finishes sliding the steaming matte terracotta 'SOLIS' cappuccino cup into the foreground in front of @Maya, warm golden morning light catching the rising steam, shallow depth of field, 50mm lens.
```

### Image 3.5 — Shot 5 Storyboard Frame (Maya's First Sip & Spark)

- **Reference Image**: Click **`More > Add to Prompt`** on **Image 3.4**.

```text
Medium close-up of @Maya at the oak cafe counter wrapping both hands around the steaming matte terracotta 'SOLIS' cappuccino cup, inhaling the warm steam with her eyes brightening in sudden creative inspiration, warm 2400K golden sunrise light streaming across the counter, 50mm lens.
```

---

## Step 4: Animate Video & Dialogue in Google Flow (`Video > Omni Flash`)

Switch the prompt bar to **Video** $\rightarrow$ **Omni Flash** (`16:9`, `6s`).
- **Draft Fast**: Select **Omni 360p** while experimenting, then click **Upscale to 720p** (0 credits) on your winning takes.
- **Two Real Ways to Animate in Google Flow**:
  1. **`Video > Frames` (`+ Add start frame` / `+ Add end frame`)**: Drag a storyboard image from Step 3 into **`+ Add start frame`** (and optionally a second image into **`+ Add end frame`**) so the video begins on that exact frame.
  2. **`Video > Ingredients`**: Type **`@Maya`** and **`@Leo`** in the prompt (their bundled voices automatically speak any dialogue lines!), and optionally click **`Add`** under the prompt box (or drag an image tile from your project) to attach a scene/prop reference image.

### Clip 4.1 — Shot 1: Creative Block in the Studio (`6s`)

- **How to Set Up in Flow**: Choose **`Video > Frames`** and attach **Image 3.1** as **`+ Add start frame`** (or use **`Video > Ingredients`** with **`@Maya`** + **Image 3.1**).
- **Prompt**:

```text
Slow push-in medium shot of @Maya sitting at the drafting desk in the cold rainy studio, rubbing her temple and tapping her charcoal pencil against the blank white blueprint while rain patters softly against the window glass.
```

### Clip 4.2 — Shot 2: Entering the Warm Cafe (`6s`)

- **How to Set Up in Flow**: Choose **`Video > Frames`** and attach **Image 3.2** as **`+ Add start frame`** (or use **`Video > Ingredients`** with **`@Maya`** + **Image 3.2**).
- **Prompt**:

```text
Smooth tracking shot following @Maya as she walks into the warm coffee shop out of the rain, shaking a drop of water from her sleeve and approaching the sunlit oak espresso bar, gentle door chime and cozy cafe ambiance.
```

### Clip 4.3 — Shot 3: The Craft (`Video > Frames`: Start + End Frame, `6s`)

- **Start Frame (`+ Add start frame`)**: Attach **Image 3.3** (`@Leo` pouring espresso into the terracotta cup).
- **End Frame (`+ Add end frame`)**: Attach **Image 3.4** (`@Leo` sliding the cup across the oak counter to `@Maya`).
- **Prompt**:

```text
Smooth camera tilt and follow as @Leo finishes pouring rich crema into the matte terracotta 'SOLIS' cup and slides the steaming cup smoothly across the oak counter toward @Maya, espresso machine hiss and ceramic saucer slide audio.
```

### Clip 4.4 — Shot 4: Leo Speaks (`Video > Ingredients` + Bundled Voice, `6s`)

- **How to Set Up in Flow**: Choose **`Video > Ingredients`**, type **`@Leo`** and **`@Maya`**, and drag **Image 3.4** into the prompt box as a location/prop ingredient.
- **Prompt (180° Rule — Leo on Right Looking Screen-Left)**:

```text
Over-the-shoulder medium shot from behind @Maya on the left, focusing on @Leo on the right looking screen-left across the oak espresso counter with a warm smile. @Leo says: "Rough night with the blueprints? Start with this."
```

### Clip 4.5 — Shot 5: Maya Drinks Coffee & Replies (`Video > Ingredients` + Bundled Voice, `6s`)

- **How to Set Up in Flow**: Choose **`Video > Ingredients`**, type **`@Maya`**, and attach **Image 3.5** as a visual ingredient (or use **`Video > Frames`** with **Image 3.5** as **`+ Add start frame`**).
- **Prompt (180° Rule — Maya on Left Looking Screen-Right)**:

```text
Reverse-angle medium close-up of @Maya on the left looking screen-right at the warm oak counter. @Maya drinks coffee from the terracotta cup, lowers the cup with a warm inspired smile, and says: "You just saved the whole skyline, Leo."
```

> **Pro Tip — Chaining Shots with `Save frame`**: Want to continue right from the end of Clip 4.5? Pause Clip 4.5 on its final frame in Google Flow, click **`Save frame`**, and attach that saved image as **`+ Add start frame`** for your next generation!

---

## Step 5: Conversational Video Editing (`Omni Flash`) & Scenebuilder

In Google Flow, **Gemini Omni Flash** lets you conversationally edit any generated video clip (up to `10s` long) for **up to 3 turns** without losing your actor's performance, and then stitch your final cut in **Scenebuilder**.

### Edit 5.1 — Turn 1: Intensify Golden Sunrise Lighting on Clip 4.5

Select **Clip 4.5** in Google Flow, open the conversational video edit prompt, and enter:

```text
Intensify the warm 2400K golden sunrise beams streaming through the cafe window behind @Maya and make the rising coffee steam glow softly in the backlight.
```

### Edit 5.2 — Turn 2: Add Brand Title Overlay on Clip 4.5

In the same conversational edit thread (Turn 2 of 3), enter:

```text
In the final 2 seconds as the steam rises, fade in clean minimalist gold serif text in the upper center reading 'SOLIS — AWAKEN THE CRAFT'.
```

### 5.3 — Assemble & Export in Google Flow Scenebuilder

1. Hover over your 5 finished clips (**Clips 4.1 $\rightarrow$ 4.5**), click **`More` ($\vdots$)** $\rightarrow$ **`Add to Scene`**.
2. Open **Scenebuilder** (`Scenes` in the left sidebar) to arrange the timeline in order (`Shot 1 -> Shot 2 -> Shot 3 -> Shot 4 -> Shot 5`).
3. Drag the clip handles to trim dead air at the start or end of each dialogue line so `@Leo`'s question flows naturally into `@Maya`'s sip and reply.
4. Click **`Upscale to 720p`** (0 credits on Omni Flash) on any remaining 360p draft clips, preview the full 30-second commercial, and click **`Download`**.

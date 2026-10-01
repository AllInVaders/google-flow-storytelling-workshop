# Part II: "Solis Artisan Coffee — The 6:00 AM Spark" (Google Flow Prompt Library)

> **100% Google Flow + Gemini Omni Flash Workflow**: Every prompt in this library is designed to run directly inside **[Google Flow](https://labs.google/fx/tools/flow)** using **Google Flow Agent**, **Characters (`@Maya`, `@Leo`)**, **Ingredients (`@Studio`, `@Cafe`, `@SolisCup`)**, **Nano Banana Pro** (Images), **Gemini Omni Flash** (Video & Native Audio), and **Scenebuilder**.

---

## ⚠️ The #1 Rule of Characters in Google Flow

In Google Flow, you **never** repeat a character's physical description across multiple prompts. Repeating physical traits causes the model to **re-generate a slightly different person** in every shot.

1. **Create the Character ONCE** in **Left Sidebar $\rightarrow$ Characters $\rightarrow$ New Character** (locking their face, outfit, name, and voice).
2. **ONLY Refer to `@CharacterName` Afterwards**: In every storyboard and video prompt that follows, simply type **`@Maya`** or **`@Leo`** and describe **what they do** (e.g., `"@Maya drinks coffee"`).

| ❌ Wrong (Re-Generating the Character) | ✅ Right (Google Flow `@Character` Reference) |
| :--- | :--- |
| *"A 29-year-old Latina architect with olive skin, freckles, raven hair in a clip, tortoiseshell glasses, and an ochre cardigan drinks coffee..."* | **`@Maya drinks coffee from @SolisCup, inhales the warm steam, and smiles.`** |

---

## Step 1: Story Seed & 5-Shot Beat Sheet (`Google Flow Agent`)

Open **Google Flow** $\rightarrow$ **+ New Project** (`Solis - The 6AM Spark`) $\rightarrow$ open the **Google Flow Agent** panel and paste:

### Prompt 1.1 — 2-Sentence Story Seed to 5-Shot Beat Sheet

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

## Step 2: Create Characters & Scene Ingredients Once

### 2A. Create Locked Characters (`Characters > New Character`)

Click **Characters** (left sidebar) $\rightarrow$ **New Character**. Run these prompts **once** to create your cast:

#### Character 1 — `@Maya`

- **Character Name**: `Maya`
- **Voice Selection**: Click **Select a voice** $\rightarrow$ choose a **Warm, Natural Female Alto** $\rightarrow$ **Add to Character**
- **One-Time Character Creation Prompt**:

```text
29-year-old Latina architect with warm olive skin, subtle freckles across the nose, shoulder-length wavy raven hair pinned in a loose low clip, round tortoiseshell eyeglasses, wearing a mustard-ochre ribbed knit cardigan over a crisp white crew-neck tee, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
```

#### Character 2 — `@Leo`

- **Character Name**: `Leo`
- **Voice Selection**: Click **Select a voice** $\rightarrow$ choose a **Warm, Friendly Male Baritone** $\rightarrow$ **Add to Character**
- **One-Time Character Creation Prompt**:

```text
42-year-old artisan barista with medium-brown skin, silver-flecked short curly hair, neatly trimmed beard, warm smile lines around the eyes, wearing a washed indigo denim apron over a charcoal henley with rolled sleeves, neutral 5600K studio lighting, clean slate-gray background, photorealistic portrait.
```

---

### 2B. Create Scene & Product Ingredients (`Image > Nano Banana Pro`)

Switch the prompt bar to **Image** $\rightarrow$ **Nano Banana Pro** (`16:9`). Generate these three empty world/prop assets and name them in your project library so you can tag them with `@`:

#### Ingredient 1 — `@Studio` (Maya's Rainy Drafting Studio)

```text
Empty architectural studio loft at 5:45 AM before dawn, wide establishing shot, rain-streaked floor-to-ceiling industrial glass window overlooking a misty blue-hour city skyline, tilted birchwood drafting table with a blank white blueprint roll, brass desk lamp turned off, cold 7000K slate-blue lighting, 24mm lens, no people.
```

#### Ingredient 2 — `@Cafe` (Solis Roastery Interior)

```text
Empty neighborhood artisan coffee shop interior at 6:00 AM, reclaimed oak counter in the foreground, gleaming vintage brass espresso machine, warm 2700K Edison pendant bulbs glowing against exposed brick, rain visible on the front glass window, inviting golden-amber atmosphere, 35mm lens, no people.
```

#### Ingredient 3 — `@SolisCup` (Hero Product Prop)

```text
Product close-up of a handcrafted matte terracotta ceramic cappuccino cup with a cream ceramic interior resting on a matching terracotta saucer, subtle minimalist embossed wordmark 'SOLIS' on the front of the cup, rich dark espresso with velvety hazelnut-brown microfoam rosette latte art, soft studio lighting.
```

---

## Step 3: Build Storyboard Frames Using `@Maya` & `@Leo` (`Image > Nano Banana Pro`)

Now generate the key storyboard frames in **Image** $\rightarrow$ **Nano Banana Pro** (`16:9`). Notice how we **never re-describe Maya or Leo**—we just tag **`@Maya`**, **`@Leo`**, **`@Studio`**, **`@Cafe`**, and **`@SolisCup`**!

### Frame 3.1 — Shot 1 Start Frame (Creative Block)

```text
@Maya sitting at the drafting desk inside @Studio at 5:45 AM, leaning on her elbow and staring tiredly at the blank white blueprint, holding a charcoal pencil loosely, cold blue pre-dawn window light, medium shot, 35mm lens.
```

### Frame 3.2 — Shot 2 Frame (Entering the Warm Cafe)

```text
@Maya stepping inside @Cafe out of the morning rain, looking toward the warm glowing espresso counter with quiet relief, cool blue rain outside the door contrasting with warm golden light inside, medium wide shot, 35mm lens.
```

### Frame 3.3 — Shot 3 Start Frame (Leo Pours the Espresso)

```text
@Leo standing behind the oak counter in @Cafe, pulling a fresh espresso shot from the brass machine into @SolisCup as aromatic steam rises, warm 2700K pendant lighting, medium shot, 50mm lens.
```

### Frame 3.4 — Shot 3 End Frame (Cup Slid Across the Counter)

```text
Close-up on the oak counter in @Cafe as @Leo's hand finishes sliding the steaming @SolisCup into the foreground in front of @Maya, warm golden morning light catching the rising steam, shallow depth of field, 50mm lens.
```

### Frame 3.5 — Shot 5 Frame (Maya's First Sip & Spark)

```text
Medium close-up of @Maya in @Cafe wrapping both hands around @SolisCup, inhaling the warm steam with her eyes brightening in a moment of sudden creative inspiration, warm 2400K golden sunrise light streaming across the counter, 50mm lens.
```

---

## Step 4: Animate Video & Dialogue in Google Flow (`Video > Omni Flash`)

Switch the prompt bar to **Video** $\rightarrow$ **Omni Flash** (`16:9`, `6s`).
- **Draft Fast**: Use **Omni 360p** while testing, then click **Upscale to 720p** (0 credits) on your winning takes.
- **Voice Consistency**: Because you bundled voices into `@Maya` and `@Leo` in Step 2A, **Omni Flash** automatically uses their locked voices for dialogue!

### Clip 4.1 — Shot 1: Creative Block in the Studio (`Ingredients Mode`, `6s`)

- **Referenced Assets**: `@Maya`, `@Studio` (or attach `Frame 3.1` as **+ Add start frame**)
- **Prompt**:

```text
Slow push-in medium shot of @Maya sitting at the drafting table in @Studio, rubbing her temple and tapping her charcoal pencil against the blank white blueprint while rain patters softly against the cold blue window glass.
```

### Clip 4.2 — Shot 2: Entering Solis Cafe (`Ingredients Mode`, `6s`)

- **Referenced Assets**: `@Maya`, `@Cafe` (or attach `Frame 3.2` as **+ Add start frame**)
- **Prompt**:

```text
Smooth tracking shot following @Maya as she walks into @Cafe, shaking a drop of rain from her sleeve and walking up to the warm sunlit oak espresso bar, gentle door chime and cozy cafe ambiance.
```

### Clip 4.3 — Shot 3: The Craft (`Frames Mode: Start + End Frame`, `6s`)

- **Start Frame**: Attach `Frame 3.3` (`+ Add start frame`)
- **End Frame**: Attach `Frame 3.4` (`+ Add end frame`)
- **Prompt**:

```text
Smooth camera tilt and follow as @Leo finishes pouring rich crema into @SolisCup and slides the steaming cup smoothly across the oak counter in @Cafe toward @Maya, espresso machine hiss and ceramic saucer slide audio.
```

### Clip 4.4 — Shot 4: Leo Speaks (`Ingredients Mode + Bundled Voice`, `6s`)

- **Referenced Assets**: `@Leo`, `@Maya`, `@Cafe`, `@SolisCup`
- **Prompt (180° Rule — Leo on Right Looking Screen-Left)**:

```text
Over-the-shoulder medium shot from behind @Maya on the left, focusing on @Leo on the right looking screen-left across the counter in @Cafe with a warm smile. @Leo says: "Rough night with the blueprints? Start with this."
```

### Clip 4.5 — Shot 5: Maya Drinks Coffee & Replies (`Ingredients Mode + Bundled Voice`, `6s`)

- **Referenced Assets**: `@Maya`, `@Cafe`, `@SolisCup` (or attach `Frame 3.5` as **+ Add start frame**)
- **Prompt (180° Rule — Maya on Left Looking Screen-Right)**:

```text
Reverse-angle medium close-up of @Maya on the left looking screen-right in @Cafe. @Maya drinks coffee from @SolisCup, lowers the cup with a warm inspired smile, and says: "You just saved the whole skyline, Leo."
```

> **Tip — Chaining Shots with `Save Frame`**: Want a seamless cut from Clip 4.5 into a bonus drawing shot? Pause Clip 4.5 on its final frame, click **Save frame** in Google Flow, and attach that saved frame as **+ Add start frame** for your next Omni Flash generation!

---

## Step 5: Conversational Video Editing (`Omni Flash`) & Scenebuilder

With **Gemini Omni Flash** in Google Flow, you can conversationally edit any generated video clip for **up to 3 turns** without losing the character's performance, and then assemble your final cut in **Scenebuilder**.

### Edit 5.1 — Turn 1: Intensify Golden Sunrise Lighting on Clip 4.5

Select **Clip 4.5** in Google Flow, click **Edit Video**, and enter:

```text
Intensify the warm 2400K golden sunrise beams streaming through the window behind @Maya and make the rising coffee steam from @SolisCup glow softly in the backlight.
```

### Edit 5.2 — Turn 2: Add Brand Title Overlay on Clip 4.5

In the same conversational edit thread (Turn 2 of 3), enter:

```text
In the final 2 seconds as the steam rises, fade in clean minimalist gold serif text in the upper center reading 'SOLIS — AWAKEN THE CRAFT'.
```

### 5.3 — Assemble & Export in Google Flow Scenebuilder

1. Hover over your 5 finished clips (**Clips 4.1 $\rightarrow$ 4.5**), click **More ($\vdots$)** $\rightarrow$ **Add to Scene**.
2. Open **Scenebuilder** in Google Flow to arrange the timeline in order (`Shot 1 -> Shot 2 -> Shot 3 -> Shot 4 -> Shot 5`).
3. Drag the clip handles to trim dead air at the start or end of each dialogue line so `@Leo`'s line flows naturally into `@Maya`'s sip and reply.
4. Click **Upscale to 720p** (0 credits on Omni Flash) on any remaining 360p draft clips, preview the full 30-second commercial, and click **Download**.

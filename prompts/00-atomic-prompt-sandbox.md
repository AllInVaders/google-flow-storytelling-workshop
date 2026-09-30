# Part I: The Atomic Prompt Mastery Sandbox (Pre-Production Warm-Up)

> **When to Run This Section**: Run this as **Part I (20-minute Pre-Work or Warm-Up Lab)** before starting the 7-stage incremental commercial production—or right between **Stage 0 (Story Seed)** and **Stage 1 (Character Lock)**.
>
> **Core Philosophy — Isolate One Variable at a Time**:
> Before combining characters, sets, storyboards, and dialogue into a full commercial, great AI directors test **individual, atomic prompt characteristics** in isolation. By keeping the subject simple and pushing **one specific dimension** to the extreme—**Camera Angle**, **Warmth & Lighting**, **Visual Style**, **Multi-Object Composition**, **Conversational Video Editing**, or **Multimodal Music**—you discover the exact vocabulary that unlocks the best results in **Gemini Image (`gemini-3-pro-image` / `gemini-3.1-flash-image`)**, **Gemini Omni (`gemini-omni-1.1-flash`)**, and **Lyria 3.5 (`lyria-3.5` / `lyria-3-pro-preview`)**.

---

## Quick Model Reference for the Sandbox

| Modality | Recommended Model ID | Why We Use It in This Lab |
| :--- | :--- | :--- |
| **Image Generation (Precision & Text)** | `gemini-3-pro-image` (*Nano Banana Pro*) | Best-in-class multi-object spatial accuracy, lens geometry, and crisp typography |
| **Image Generation (Fast Iteration)** | `gemini-3.1-flash-image` (*Nano Banana 2*) | Rapid style/lighting A/B testing with adjustable thinking |
| **Video Generation & Conversational Editing** | **`gemini-omni-1.1-flash`** (*Gemini Omni Flash* / `omni`) | **Primary Video Model**: Text/Image/Video-to-Video, multi-turn conversational editing (`interactions.create`), First/Last frame keyframing, 360p draft -> 4K upscaling, kinetic typography sync, and native audio |
| **Music & Multimodal Audio Scoring** | **`lyria-3.5`** / **`lyria-3-pro-preview`** / **`lyria-3-clip-preview`** | **Latest Lyria Stack**: 44.1 kHz stereo music from **Text or Image + Text**, full song structure (`lyria-3.5` / `lyria-3-pro-preview`), or locked 30s commercial clips (`lyria-3-clip-preview`) |

---

## Lab A: Testing Extreme Camera Angles & Perspective Shifts

Most prompts fail to look cinematic because they default to a flat, eye-level medium shot. In this test, we keep the subject constant and push **camera angle, lens focal length, and continuous camera choreography**.

### A.1 — Image Prompt: Extreme Worm's-Eye Architectural Lookup (`14mm Ultra-Wide`)
*Run in Google Flow Images or `gemini-3-pro-image`:*
```text
Extreme worm's-eye view photograph taken from ground level with the camera resting directly on wet dark cobblestone pavement, looking straight up at 85 degrees toward a towering brutalist glass-and-brass coffee roastery at dawn. In the immediate foreground, 5 inches from the lens, a single matte terracotta espresso cup sits on the wet stone beside a puddle reflecting the soaring building above. 14mm ultra-wide rectilinear lens, dramatic converging vertical lines, crisp deep depth of field, no text.
```

### A.2 — Image Prompt: 90° Overhead "God's-Eye" Knolling Flat-Lay (`50mm Prime`)
*Run in Google Flow Images or `gemini-3-pro-image`:*
```text
Exact 90-degree overhead bird's-eye flat-lay photograph looking straight down onto a dark walnut architect's drafting table. Arranged in precise geometric knolling alignment: (1) an unrolled cyan architectural bridge blueprint in the center, (2) a matte terracotta cappuccino cup with rosetta latte art in the top-right corner, (3) round tortoiseshell glasses and a brass compass on the left, and (4) a hand in an ochre knit sleeve reaching in from the bottom edge holding a charcoal pencil. 50mm lens, zero perspective distortion, soft directional top-left window light.
```

### A.3 — Video Prompt (`gemini-omni-1.1-flash`): Single-Take Whip-Pan & Crane-Up Choreography
*Run in Gemini Omni (`gemini-omni-1.1-flash`) or Google Flow Video:*
```text
One continuous cinematic shot, no jump cuts. Start on an extreme low-angle macro view at counter height of a barista's hand tamping espresso grounds with a heavy brass tamper. The camera then whip-pans smoothly to the right in one fluid motion across the reclaimed oak counter, following a steaming matte terracotta cup as it slides toward an architect in tortoiseshell glasses, and cranes straight up into a high-angle overhead view looking down as she wraps both hands around the cup. Warm amber Edison lighting, 35mm lens, 24fps. Audio: Crisp metallic tamp click, smooth ceramic slide across wood, warm café murmur.
```

### A.4 — Gemini Omni Conversational Camera Angle Edit (Multi-Turn Follow-Up)
*After generating A.3 in `gemini-omni-1.1-flash` (via AI Studio / Interactions API / Flow Agent), send this follow-up turn without rewriting the prompt:*
```text
Keep the exact same character, espresso bar, cup movement, and audio, but change the camera movement to a slow 180-degree orbital arc shot at eye level that circles smoothly around the terracotta cup as steam rises.
```

---

## Lab B: Testing Warmth, Color Temperature (Kelvin) & Volumetric Light

Lighting is the fastest way to tell an emotional story without dialogue. Run **B.1** and **B.2** side-by-side: notice how changing **only the lighting & Kelvin temperature keywords** completely flips the mood of the exact same room.

### B.1 — Image Prompt: Cold 7500K Pre-Dawn Isolation (Teal & Cyan Shadow)
```text
Medium shot of a minimalist studio desk by a tall rain-streaked industrial window. Lit exclusively by cold 7500K pre-dawn blue-hour overcast sky and a flickering cyan fluorescent streetlamp outside. Deep moody slate-blue shadows, wet cold condensation on the window glass, desaturated somber color palette, solitary atmosphere, 35mm anamorphic lens.
```

### B.2 — Image Prompt: Warm 2400K Golden Sanctuary (Amber Chiaroscuro & Halation)
```text
Medium shot of the exact same minimalist studio desk by a tall industrial window, now bathed in rich 2400K golden-hour sunrise and a warm vintage brass desk lamp. Golden volumetric sunbeams cut through floating dust motes and rising coffee steam, casting long warm amber and honey-gold shadows across the wooden desk. Soft warm halation around highlights, cozy inviting atmosphere, 35mm anamorphic lens.
```

### B.3 — Video Prompt (`gemini-omni-1.1-flash`): Real-Time Cold-to-Warm Lighting Evolution
```text
Static medium-wide shot of a rain-streaked architect's loft desk in cold 7500K blue pre-dawn shadow. Over 6 seconds, storm clouds outside the tall window part rapidly as a blazing 3000K golden sunrise breaks through, sweeping a warm diagonal beam of sunlight across the desk, illuminating a steaming terracotta espresso cup and turning the room from cold cyan to glowing amber. Volumetric light rays in the rising steam. Audio: Distant rain fading out as a warm, resonant morning acoustic chord swells.
```

### B.4 — Gemini Omni Conversational Relight (Multi-Turn Follow-Up)
*After generating any video clip in `gemini-omni-1.1-flash`, test conversational relighting:*
```text
Keep the subject, framing, and camera motion identical, but relight the entire scene to warm 2200K candlelight with soft golden rim lighting and gentle chiaroscuro shadows.
```

---

## Lab C: Testing Radical Aesthetic & Film Stock Styles

Test how **Gemini Image** and **Gemini Omni 1.1 Flash** lock onto tactile textures, historical film stocks, and non-photorealistic art directions.

### C.1 — Style 1 (Image): 1970s 35mm Kodak Vision3 500T Anamorphic Cinema
```text
Cinematic film still of a bustling rainy corner espresso bar at night seen through a wet glass window. Shot on 35mm Kodak Vision3 500T motion picture film with Panavision C-Series anamorphic lenses. Characteristic organic film grain, warm red-orange halation around glowing tungsten streetlamps, vertical oval bokeh in the rain droplets, and a subtle horizontal blue anamorphic lens flare.
```

### C.2 — Style 2 (Image & Omni Video): Tactile Stop-Motion Felt & Sculpted Clay Diorama
```text
Handcrafted miniature stop-motion diorama of a cozy corner coffee shop in the rain. Every element is built from tactile physical craft materials: the barista and architect are sculpted from matte polymer clay with visible subtle thumbprint textures; the rising espresso steam is made of wispy needle-felted merino wool; the rain droplets on the window are clear blown glass beads; the counter is balsa wood. Lit by warm miniature LED practical bulbs, 100mm macro tilt-shift lens with shallow depth of field. (For Gemini Omni Video: animate at a charming 12fps stop-motion frame cadence as the clay barista slides the miniature cup across the counter.)
```

### C.3 — Style 3 (Image & Omni Video): Architectural Sumi-e Ink & Bleeding Watercolor
```text
Expressive architectural concept illustration of a woman drinking espresso at a café counter while a suspension bridge forms in the steam above her cup. Drawn with crisp black technical Sumi-e fountain-pen ink lines on rough cold-press 300gsm cotton watercolor paper, layered with translucent washes of burnt sienna, warm ochre, and Prussian blue watercolor that bleed organically into the paper fibers.
```

### C.4 — Style 4 (Gemini Omni Video): Retro 1999 Y2K Broadcast & Chrome Aesthetic
```text
Create an 8-second 16:9 retro 1999 Y2K commercial clip for an espresso bar. Fast zoom-in with a fisheye lens on a chrome espresso machine pulling a shot into a terracotta cup against a glossy cobalt-blue cyclorama backdrop with a hard white spotlight circle. High-key frontal studio light, candy amber, cobalt, and polished chrome palette; authentic 1999 broadcast television look with soft highlight bloom, subtle VHS chroma bleed, fine tape grain, and upbeat 120-BPM breakbeat percussive audio.
```

---

## Lab D: Combining Multiple Objects & Chain-Reaction Physics

A classic stress test for any generative model is **multi-object spatial composition** (putting 4–5 distinct items in exact relative positions without merging their attributes) and **multi-object physical cause-and-effect**.

### D.1 — Image Prompt: 5-Object Spatial & Material Lock (`gemini-3-pro-image`)
```text
High-resolution studio tabletop composition on a slab of dark green Connemara marble featuring five distinct objects in exact spatial positions:
(1) Center: a matte terracotta ceramic cappuccino cup with the word "SOLIS" embossed in gold leaf on the front;
(2) Left of the cup: a pair of round tortoiseshell eyeglasses with raindrops on the lenses;
(3) Right of the cup: a vintage brushed-brass mechanical pocket watch open to 6:00;
(4) Foreground: three whole roasted Arabica coffee beans resting on the corner of a folded cyan blueprint;
(5) Background: a translucent fluted glass carafe filled with cold water catching a warm diagonal sunbeam.
Each material—matte terracotta, tortoiseshell acetate, brushed brass, paper, and fluted glass—is rendered with distinct physical accuracy. 85mm lens, f/5.6.
```

### D.2 — Video Prompt (`gemini-omni-1.1-flash`): Multi-Object Chain-Reaction Physics
*Showcases Gemini Omni's world-knowledge physics simulation:*
```text
Continuous smooth macro tracking shot following a precision chain reaction across a wooden café counter: a polished brass marble rolls down a grooved oak ruler, gently taps a row of three white brown-sugar dominoes which topple in sequence, nudging a brass spoon that tips into a matte terracotta cup filled with dark espresso, sending a delicate ripple across the golden crema as a wisp of steam curls upward. Realistic gravity, momentum, and fluid surface tension. 60fps smooth motion, warm studio lighting. Audio: Rolling metallic hum, three soft crisp sugar-cube clicks, a gentle ceramic clink, and liquid swirl.
```

---

## Lab E: Gemini Omni Exclusive Superpowers (Kinetic Text & Conversational Remix)

Unlike legacy text-to-video pipelines, **Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`)** natively synchronizes **on-screen kinetic typography** with physical motion and supports **multi-turn conversational editing** via the Interactions API.

### E.1 — Video Prompt (`gemini-omni-1.1-flash`): In-Video Kinetic Typography Sync
```text
Macro cinematic close-up of a steaming matte terracotta cappuccino cup resting on a dark oak table in warm golden morning light. As a thick, velvety plume of golden steam rises from the cup toward the top of the frame, clean minimalist 3D gold serif letters reading "AWAKEN THE CRAFT" materialize in mid-air above the rim. The rising coffee steam physically swirls around and parts through the 3D gold letters, casting soft warm reflections on the typography. 85mm macro lens. Audio: Warm resonant cello swell and gentle café steam hiss.
```

### E.2 — Multi-Turn Conversational Video Editing Workflow (Python SDK / Interactions API)
```python
import base64
from google import genai

client = genai.Client()

# Turn 1: Fast 360p/720p Draft Generation in Gemini Omni 1.1 Flash
turn1 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=(
        "Medium tracking shot of an architect in an ochre cardigan walking along a "
        "rain-slicked city sidewalk at dawn toward a glowing corner café. 35mm lens."
    ),
)
with open("shot_draft.mp4", "wb") as f:
    f.write(base64.b64decode(turn1.output_video.data))

# Turn 2: Conversational Edit — Keep motion & character, change weather & angle
turn2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=turn1.id,
    input=(
        "Keep the exact same character and walking pace, but change the lighting to "
        "warm golden sunrise breaking through the buildings and add a glowing neon "
        "'SOLIS' sign in the café window."
    ),
)
with open("shot_refined.mp4", "wb") as f:
    f.write(base64.b64decode(turn2.output_video.data))
```

---

## Lab F: Latest Lyria 3.5 & Lyria 3 Pro Multimodal Music Sandbox

As of late 2026, Google's **Lyria 3.5 (`lyria-3.5`)**, **Lyria 3 Pro (`lyria-3-pro-preview`)**, and **Lyria 3 Clip (`lyria-3-clip-preview`)** produce **44.1 kHz high-fidelity stereo audio** and support **multimodal inputs (Text + Image!)** via the Interactions API.

### F.1 — Exact 30-Second Commercial Instrumental Bed (`lyria-3-clip-preview` / `lyria-3.5`)
```text
30-second cinematic commercial soundtrack in 44.1kHz stereo, 92 BPM, instrumental only.
[0:00–0:08 Intro]: Sparse, melancholic solo felt piano with soft room reverb, evoking a cold rainy 5:45 AM morning.
[0:08–0:20 Main Groove]: A warm, fingerpicked acoustic guitar and upright bass enter on a gentle upbeat groove, adding cozy artisan café warmth.
[0:20–0:30 Crescendo Outro]: Uplifting chamber strings (cello and violin) swell into a bright, inspiring major-key resolution that lands cleanly at 0:29 with a warm acoustic harmonic tail.
```

### F.2 — Full Song with Structural Tags & Expressive Vocals (`lyria-3.5` / `lyria-3-pro-preview`)
```text
Warm indie-folk commercial anthem, 96 BPM, 44.1kHz stereo, intimate female lead vocal with brushed drums, upright bass, and warm acoustic guitar.
[Intro]
(Gentle fingerpicked acoustic guitar and soft rain ambience)
[Verse 1]
Five forty-five on a windowpane,
Blueprints waiting in the morning rain.
[Chorus]
One warm spark in the terracotta cup,
Golden sunrise waking the skyline up.
Solis in the morning light,
Every line falls into sight.
[Outro]
(Warm cello and acoustic guitar harmonic fade)
```

### F.3 — Multimodal Image-to-Music Scoring (`lyria-3.5` with Image Input)
*Pass any image generated in **Lab B.1 (Cold Rain)** or **Lab B.2 (Warm Sunrise)** directly into `lyria-3.5`:*
```python
import base64
from google import genai
from google.genai import types

client = genai.Client()

with open("warm_sunrise_studio.png", "rb") as f:
    img_bytes = f.read()

interaction = client.interactions.create(
    model="lyria-3.5",
    input=[
        types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
        "Compose a 30-second instrumental commercial soundtrack that matches the exact lighting, warmth, and emotional mood of this image. 44.1kHz stereo.",
    ],
)
with open("image_scored_track.mp3", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

---

## Sandbox Takeaway Checklist (Before Moving to Part II)

1. **Camera Angles**: Did you see how specifying `14mm worm's-eye lookup`, `90-degree overhead flat-lay`, or `single-take whip-pan` immediately breaks out of generic "eye-level AI video"?
2. **Warmth & Kelvin Lighting**: Did you see how shifting from `7500K cold cyan blue-hour` to `2400K golden sunrise chiaroscuro` tells an emotional story before a single word is spoken?
3. **Gemini Omni Conversational Editing**: Instead of starting from scratch when a video clip is 80% right, use a conversational follow-up turn in `gemini-omni-1.1-flash` to relight or re-angle the shot!
4. **Ready for Part II**: Now let's take these exact atomic skills and layer them incrementally to produce our 30-second commercial: **"Solis — The 6:00 AM Spark"**!

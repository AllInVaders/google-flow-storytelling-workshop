# Google Flow & Gemini Omni Flash Quick-Reference Cheat Sheet

> **Workspace**: [https://labs.google/fx/tools/flow](https://labs.google/fx/tools/flow)  
> **Official Help Center**: [support.google.com/flow](https://support.google.com/flow)

---

## 1. The Golden Rule of Characters (`@CharacterName`)

In Google Flow, you **never** repeat a character's physical description in scene prompts.

1. **Create Once**: Click **Characters** (left sidebar) $\rightarrow$ **New Character** $\rightarrow$ enter the visual description once $\rightarrow$ click **Generate** $\rightarrow$ enter the character name (`Maya`, `Leo`) $\rightarrow$ click **Select a voice** $\rightarrow$ **Add to Character** $\rightarrow$ **Done**.
2. **Refer Only by `@Name` Afterwards**: In every Image or Video prompt, simply type **`@Maya`** or **`@Leo`** and describe their action.

| Task | Prompt Box Input |
| :--- | :--- |
| **Create `Maya` (Done Once in `Characters > New Character`)** | `29-year-old Latina architect with warm olive skin, subtle freckles, wavy raven hair in a low clip, round tortoiseshell eyeglasses, mustard-ochre knit cardigan, neutral studio lighting.` |
| **Use `@Maya` in a Storyboard or Video Prompt** | `@Maya drinks coffee from @SolisCup and smiles.` |
| **Use `@Maya` + `@Leo` in a Two-Shot** | `Over-the-shoulder shot from behind @Maya on the left looking at @Leo on the right in @Cafe. @Leo says: "Rough night with the blueprints? Start with this."` |

---

## 2. Google Flow `@` Tags & Asset Types

Type **`@`** inside the Google Flow prompt bar (or drag any tile from your project grid into the prompt box) to reference saved project assets:

| Tag Type | How to Create in Google Flow | Example Usage in Prompt |
| :--- | :--- | :--- |
| **`@Character`** | Left Sidebar $\rightarrow$ **Characters** $\rightarrow$ **New Character** (locks face, outfit & voice). | `@Maya sits at the desk staring at a blank blueprint.` |
| **`@Ingredient`** | Generate an empty set or product prop in **Image $\rightarrow$ Nano Banana Pro** (or upload an image) and name it in your library. | `@Leo pours espresso into @SolisCup inside @Cafe.` |
| **`@Voice`** | Left Sidebar $\rightarrow$ **Voices** $\rightarrow$ **New Voice** (or bundle directly inside a `@Character`). | `@Maya speaks in her warm alto voice.` |

---

## 3. Gemini Omni Flash Video Modes & Controls

Select **Video $\rightarrow$ Omni Flash** in the bottom prompt bar:

| Feature | How It Works in Google Flow | Best Used For |
| :--- | :--- | :--- |
| **Clip Durations (`4s`, `6s`, `8s`, `10s`)** | Choose clip duration in the prompt settings menu before generating. | `6s` for standard commercial cuts; `8s–10s` for longer continuous camera moves or dialogue. |
| **Draft & Upscale (`Omni 360p` $\rightarrow$ `720p`)** | Select **Omni 360p** to generate drafts at half the credit cost, then click **Upscale to 720p** (**0 credits**) on your favorite clip. | Rapid prompt exploration in Part I Sandbox and Step 4 takes. |
| **Frames (`+ Add start frame` / `+ Add end frame`)** | Attach a starting image—or both a start and end image—to guide exact motion interpolation. | Precision actions like `@Leo` pouring espresso (`Frame 3.3`) and sliding `@SolisCup` (`Frame 3.4`). |
| **Save Frame (`Save frame`)** | Pause any video clip on its final frame and click **Save frame** to turn that exact frame into a new image asset. | Chaining continuous multi-shot sequences by attaching the saved frame as the next clip's **+ Add start frame**. |
| **Conversational Video Edit (Up to 3 Turns)** | Click any generated video clip (up to `10s`), choose **Edit Video**, and describe what to change in natural language. | Relighting a shot (`"Change to 2400K golden sunrise"`) or adding kinetic text (`"Add gold text 'SOLIS'"`) without losing the actor's performance. |
| **Scenebuilder (`Add to Scene`)** | Hover over any clip $\rightarrow$ **More ($\vdots$)** $\rightarrow$ **Add to Scene**, then open **Scenebuilder** to reorder, trim handles, and export. | Assembling Shots 1–5 into the final 30-second commercial. |

---

## 4. Camera & Lighting Prompt Cheat Sheet

| Lever | Prompt Keywords for Google Flow (`Nano Banana Pro` & `Omni Flash`) |
| :--- | :--- |
| **Camera Angles** | `Extreme worm's-eye low angle (14mm)`, `Eye-level medium close-up (50mm)`, `Over-the-shoulder (OTS) shot`, `90-degree top-down flat-lay` |
| **Camera Motion** | `Slow dolly push-in`, `Smooth tracking shot`, `180-degree orbit`, `Single-take whip-pan to macro close-up` |
| **Color Temperature** | `Cold 7500K blue-hour pre-dawn shadows`, `Neutral 5600K studio daylight`, `Warm 2700K Edison amber glow`, `2400K golden sunrise rim light` |
| **180° Dialogue Rule** | **Shot A**: `Behind @Maya on the left, focusing on @Leo on the right looking screen-left` $\rightarrow$ **Shot B**: `Reverse-angle of @Maya on the left looking screen-right` |

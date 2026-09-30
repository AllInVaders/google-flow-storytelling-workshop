#!/usr/bin/env python3
"""Builds the 18-Slide Native Editable Google Slides Deck for the Google Flow, Gemini Omni & Lyria 3.5 Storytelling Workshop.

Features:
- Part I: Atomic Prompt Mastery Sandbox (Camera Angles, Kelvin Warmth, Aesthetic Styles, 5-Object Physics, Omni Conversational Editing, Lyria 3.5 Multimodal Music)
- Part II: 7-Stage Incremental Commercial Production ("Solis — The 6:00 AM Spark") powered by Gemini Omni 1.1 Flash (`gemini-omni-1.1-flash`) and Lyria 3.5 (`lyria-3.5`)
- Single-word classic Material Icons (`bolt`, `hub`, `code`, `check`, `warning`, `security`, `key`, `cloud`, `lock`, `psychology`, `star`)
- Clickable link pills pointing to `https://github.com/AllInVaders/google-flow-storytelling-workshop`, `https://labs.google/fx/tools/flow`, and `https://aistudio.google.com?model=gemini-omni-1.1-flash`
- Tripartite speaker notes (`[PURPOSE]`, `[VERBAL SCRIPT]`, `[TRANSITION]`) on 100% of slides
"""

import json
import os
import subprocess

GSLIDES = "/google/bin/releases/gemini-agents-gslides/gslides"
DEFAULT_PRES_ID = "1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0"
GITHUB_REPO = "https://github.com/AllInVaders/google-flow-storytelling-workshop"
GITHUB_BLOB = "https://github.com/AllInVaders/google-flow-storytelling-workshop/blob/main"
FLOW_URL = "https://labs.google/fx/tools/flow"
OMNI_STUDIO_URL = "https://aistudio.google.com?model=gemini-omni-1.1-flash"

BG_CANVAS = "#0B1120"
BG_CARD = "#111827"
BG_PREVIEW = "#070E1A"
BG_PILL = "#1E293B"
BG_BANNER = "#064E3B"
TEXT_WHITE = "#FFFFFF"
TEXT_SECONDARY = "#CBD5E1"
TEXT_MUTED = "#94A3B8"
TEXT_SKY = "#38BDF8"
TEXT_MINT = "#A7F3D0"

ACCENT_AMBER = "#F59E0B"
ACCENT_BLUE = "#3B82F6"
ACCENT_PURPLE = "#8B5CF6"
ACCENT_CYAN = "#06B6D4"
ACCENT_GREEN = "#10B981"
ACCENT_RED = "#EF4444"


def add_header(ops, sid, category, title, subtitle, slide_num, total_slides=18):
    """Adds slide header, slide counter, and clickable GitHub repository pill."""
    ops.append({"op": "set-background", "slide": sid, "color": BG_CANVAS})
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": category.upper(),
        "x": 40,
        "y": 15,
        "width": 395,
        "height": 18,
        "font_family": "Roboto",
        "font_size": 8.8,
        "bold": True,
        "color": TEXT_SKY,
    })
    ops.append({
        "op": "add-shape",
        "slide": sid,
        "shape_type": "RECTANGLE",
        "x": 438,
        "y": 13,
        "width": 202,
        "height": 20,
        "background_color": BG_PILL,
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": "AllInVaders/google-flow-storytelling-workshop",
        "x": 440,
        "y": 15,
        "width": 198,
        "height": 16,
        "font_family": "Roboto",
        "font_size": 7.0,
        "bold": True,
        "color": TEXT_SKY,
        "alignment": "center",
        "link": GITHUB_REPO,
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": f"Slide {slide_num:02d}/{total_slides:02d}",
        "x": 643,
        "y": 15,
        "width": 47,
        "height": 18,
        "font_family": "Roboto",
        "font_size": 8.5,
        "bold": True,
        "color": TEXT_MUTED,
        "alignment": "right",
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": title,
        "x": 40,
        "y": 33,
        "width": 640,
        "height": 28,
        "font_family": "Roboto",
        "font_size": 15.2,
        "bold": True,
        "color": TEXT_WHITE,
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": subtitle,
        "x": 40,
        "y": 61,
        "width": 640,
        "height": 24,
        "font_family": "Roboto",
        "font_size": 9.6,
        "color": TEXT_SECONDARY,
    })


def add_takeaway_banner(ops, sid, text, url=None):
    """Adds bottom emerald takeaway banner at y=345 using single-word Material Icon 'check'."""
    ops.append({
        "op": "add-shape",
        "slide": sid,
        "shape_type": "RECTANGLE",
        "x": 40,
        "y": 345,
        "width": 640,
        "height": 32,
        "background_color": BG_BANNER,
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": "check",
        "x": 42,
        "y": 350,
        "width": 40,
        "height": 22,
        "font_family": "Material Icons",
        "font_size": 15,
        "color": TEXT_MINT,
        "alignment": "center",
    })
    tb = {
        "op": "add-textbox",
        "slide": sid,
        "text": text,
        "x": 78,
        "y": 351,
        "width": 592,
        "height": 22,
        "font_family": "Roboto",
        "font_size": 8.8,
        "bold": True,
        "color": TEXT_MINT,
    }
    if url:
        tb["link"] = url
    ops.append(tb)


def add_three_cards(ops, sid, cards):
    """3-Card Column Layout."""
    xs = [40, 260, 480]
    col_w = 200
    for idx, c in enumerate(cards):
        cx = xs[idx]
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": col_w,
            "height": 235,
            "background_color": BG_CARD,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": col_w,
            "height": 4,
            "background_color": c["accent"],
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": c["icon"],
            "x": cx + 12,
            "y": 104,
            "width": 176,
            "height": 24,
            "font_family": "Material Icons",
            "font_size": 20,
            "color": c["accent"],
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": c["title"],
            "x": cx + 10,
            "y": 128,
            "width": 180,
            "height": 26,
            "font_family": "Roboto",
            "font_size": 10.5,
            "bold": True,
            "color": TEXT_WHITE,
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": c["body"],
            "x": cx + 10,
            "y": 156,
            "width": 180,
            "height": 132,
            "font_family": "Roboto",
            "font_size": 8.6,
            "color": TEXT_SECONDARY,
            "line_spacing": 122,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx + 10,
            "y": 296,
            "width": 180,
            "height": 24,
            "background_color": BG_PILL,
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": c["link_label"],
            "x": cx + 12,
            "y": 300,
            "width": 176,
            "height": 18,
            "font_family": "Roboto",
            "font_size": 8.3,
            "bold": True,
            "color": TEXT_SKY,
            "alignment": "center",
            "link": c["link_url"],
        })


def add_five_pipeline(ops, sid, steps):
    """5-Card Phase Pipeline Layout."""
    xs = [40, 170, 300, 430, 560]
    col_w = 120
    for idx, s in enumerate(steps):
        cx = xs[idx]
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": col_w,
            "height": 235,
            "background_color": BG_CARD,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": col_w,
            "height": 4,
            "background_color": s["accent"],
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": s["icon"],
            "x": cx + 10,
            "y": 103,
            "width": 100,
            "height": 22,
            "font_family": "Material Icons",
            "font_size": 18,
            "color": s["accent"],
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": s["title"],
            "x": cx + 6,
            "y": 126,
            "width": 108,
            "height": 26,
            "font_family": "Roboto",
            "font_size": 9.0,
            "bold": True,
            "color": TEXT_WHITE,
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": s["body"],
            "x": cx + 8,
            "y": 154,
            "width": 104,
            "height": 134,
            "font_family": "Roboto",
            "font_size": 8.1,
            "color": TEXT_SECONDARY,
            "line_spacing": 118,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx + 5,
            "y": 296,
            "width": 110,
            "height": 24,
            "background_color": BG_PILL,
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": s["link_label"],
            "x": cx + 6,
            "y": 300,
            "width": 108,
            "height": 18,
            "font_family": "Roboto",
            "font_size": 7.6,
            "bold": True,
            "color": TEXT_SKY,
            "alignment": "center",
            "link": s["link_url"],
        })


def add_grid_2x2(ops, sid, items):
    """2x2 Grid Layout."""
    coords = [(40, 95), (370, 95), (40, 218), (370, 218)]
    for idx, item in enumerate(items):
        cx, cy = coords[idx]
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": cy,
            "width": 310,
            "height": 112,
            "background_color": BG_CARD,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": cy,
            "width": 310,
            "height": 4,
            "background_color": item["accent"],
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": item["icon"],
            "x": cx + 2,
            "y": cy + 8,
            "width": 44,
            "height": 24,
            "font_family": "Material Icons",
            "font_size": 18,
            "color": item["accent"],
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": item["title"],
            "x": cx + 44,
            "y": cy + 9,
            "width": 256,
            "height": 22,
            "font_family": "Roboto",
            "font_size": 10.1,
            "bold": True,
            "color": TEXT_WHITE,
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": item["body"],
            "x": cx + 12,
            "y": cy + 33,
            "width": 286,
            "height": 48,
            "font_family": "Roboto",
            "font_size": 8.5,
            "color": TEXT_SECONDARY,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx + 10,
            "y": cy + 83,
            "width": 290,
            "height": 21,
            "background_color": BG_PILL,
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": item["link_label"],
            "x": cx + 12,
            "y": cy + 86,
            "width": 286,
            "height": 16,
            "font_family": "Roboto",
            "font_size": 8.0,
            "bold": True,
            "color": TEXT_SKY,
            "alignment": "center",
            "link": item["link_url"],
        })


def add_split_case_study(ops, sid, left_card, right_card, bottom_preview):
    """Split Top Cards + Bottom Copy-Paste Prompt Preview Box."""
    for cx, card in [(40, left_card), (370, right_card)]:
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": 310,
            "height": 105,
            "background_color": BG_CARD,
        })
        ops.append({
            "op": "add-shape",
            "slide": sid,
            "shape_type": "RECTANGLE",
            "x": cx,
            "y": 95,
            "width": 310,
            "height": 4,
            "background_color": card["accent"],
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": card["icon"],
            "x": cx + 2,
            "y": 103,
            "width": 44,
            "height": 24,
            "font_family": "Material Icons",
            "font_size": 18,
            "color": card["accent"],
            "alignment": "center",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": card["title"],
            "x": cx + 44,
            "y": 104,
            "width": 256,
            "height": 20,
            "font_family": "Roboto",
            "font_size": 10.0,
            "bold": True,
            "color": TEXT_WHITE,
            "alignment": "left",
        })
        ops.append({
            "op": "add-textbox",
            "slide": sid,
            "text": card["body"],
            "x": cx + 12,
            "y": 128,
            "width": 286,
            "height": 66,
            "font_family": "Roboto",
            "font_size": 8.4,
            "color": TEXT_SECONDARY,
        })
    ops.append({
        "op": "add-shape",
        "slide": sid,
        "shape_type": "RECTANGLE",
        "x": 40,
        "y": 208,
        "width": 640,
        "height": 128,
        "background_color": BG_PREVIEW,
    })
    ops.append({
        "op": "add-shape",
        "slide": sid,
        "shape_type": "RECTANGLE",
        "x": 40,
        "y": 208,
        "width": 640,
        "height": 3,
        "background_color": bottom_preview["accent"],
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": bottom_preview["title"],
        "x": 52,
        "y": 214,
        "width": 410,
        "height": 18,
        "font_family": "Roboto",
        "font_size": 9.3,
        "bold": True,
        "color": TEXT_SKY,
    })
    ops.append({
        "op": "add-shape",
        "slide": sid,
        "shape_type": "RECTANGLE",
        "x": 470,
        "y": 213,
        "width": 198,
        "height": 19,
        "background_color": BG_PILL,
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": bottom_preview["link_label"],
        "x": 472,
        "y": 215,
        "width": 194,
        "height": 15,
        "font_family": "Roboto",
        "font_size": 8.0,
        "bold": True,
        "color": TEXT_SKY,
        "alignment": "center",
        "link": bottom_preview["link_url"],
    })
    ops.append({
        "op": "add-textbox",
        "slide": sid,
        "text": bottom_preview["code"],
        "x": 52,
        "y": 233,
        "width": 616,
        "height": 98,
        "font_family": "Roboto Mono",
        "font_size": 7.5,
        "color": TEXT_WHITE,
        "line_spacing": 112,
    })


def build_all_slides(existing_slide_ids=None):
    ops = []
    if existing_slide_ids:
        # Add Slide 1 first so presentation never has 0 slides, then delete old slides
        ops.append({"op": "add-slide", "layout": "BLANK", "id": "SLIDE_01"})
        for old_id in existing_slide_ids:
            ops.append({"op": "delete-element", "element": old_id})
    else:
        ops.append({"op": "add-slide", "layout": "BLANK", "id": "SLIDE_01"})
        ops.append({"op": "delete-element", "element": "p"})

    # =========================================================================
    # SLIDE 01: Hero Cover — Two-Part Workshop Roadmap (Atomic Sandbox + Production)
    # =========================================================================
    sid = "SLIDE_01"
    add_header(
        ops,
        sid,
        "Google Flow · Gemini Omni 1.1 Flash · Lyria 3.5 · Storytelling Workshop",
        "Incremental AI Filmmaking: Atomic Prompt Sandbox to 30s Commercial",
        "Part I tests isolated prompt characteristics (Angles, Warmth, Style, Physics); Part II builds a commercial with Gemini Omni.",
        1,
    )
    add_five_pipeline(ops, sid, [
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Part I · Sandbox",
            "body": "• Isolated Prompt Lab\n• Extreme Camera Angles\n• 7500K vs 2400K Warmth\n• 5-Object Physics Lock\n• Omni Multi-Turn Edit",
            "link_label": "Atomic Sandbox ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Stages 0–1 · Cast",
            "body": "• 2-Sentence Story Seed\n• 3-Act Micro-Arc\n• 35-Word Identity Block\n• Neutral 5600K Portrait\n• 4-Angle Turnaround",
            "link_label": "Stage 0–1 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Stages 2–3 · Board",
            "body": "• Empty Location Plates\n• Hero Product ('SOLIS')\n• 6-Shot Storyboard\n• First/Last Frame Pairs\n• Continuity Bridges",
            "link_label": "Stage 2–3 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Stage 4 · Omni Video",
            "body": "• gemini-omni-1.1-flash\n• Up to 5 Image + 3 Vid Refs\n• First/Last Keyframing\n• 360p Draft -> 4K Upscale\n• Conversational Tuning",
            "link_label": "Stage 4 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "Stages 5–6 · Finale",
            "body": "• 180° Eyeline Dialogue\n• gemini-3.8-flash-tts\n• Lyria 3.5 (Img+Text)\n• 10s Extend (up to 40s)\n• Kinetic Text & Edit",
            "link_label": "Prompt Library ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Full Workshop Repo, Atomic Sandbox & Prompts: https://github.com/AllInVaders/google-flow-storytelling-workshop",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Introduce the Two-Part Workshop Architecture: Part I (Atomic Prompt Mastery Sandbox) followed by Part II (7-Stage Incremental Commercial Production powered by Gemini Omni 1.1 Flash and Lyria 3.5).\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Welcome to the Google Flow, Gemini Omni, and Lyria 3.5 Storytelling Workshop. Today's workshop is divided into two hands-on parts. In Part I, we enter the Atomic Prompt Sandbox to push single, isolated characteristics to the limit—camera angles, Kelvin warmth, styles, and multi-object physics. Then in Part II, we start with a two-sentence story seed and incrementally pile on characters, sets, storyboards, Gemini Omni video generation, two-person dialogue, and Lyria 3.5 music.\"\n\n"
            "[TRANSITION]\n"
            "Let's look at why we separate atomic prompt testing from incremental production."
        ),
    })

    # =========================================================================
    # SLIDE 02: Why "One Giant Prompt" Fails vs. Atomic Sandbox + Layer-Cake
    # =========================================================================
    sid = "SLIDE_02"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Core Methodology · Atomic Calibration + Incremental Layering",
        "Why Single-Prompt Video Fails vs. Our Two-Part Production Method",
        "Test isolated creative levers in Part I, then stack locked layers incrementally in Part II with Gemini Omni 1.1 Flash.",
        2,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "warning",
            "accent": ACCENT_RED,
            "title": "The 'One Giant Prompt' Trap (Point A)",
            "body": "• Trying to test angles, lighting, style, and story in a single prompt.\n• Protagonist's face, glasses, and jacket mutate in every clip.\n• Regenerating a take from scratch destroys an 85% great performance.\n• Two speaking characters look away from each other.",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "Atomic Sandbox + Layer-Cake Pipeline (Point B)",
            "body": "• Part I: Isolate & master 1 variable per prompt (Angles, Warmth, Style).\n• Part II: Lock story -> Lock faces -> Lock empty sets -> Storyboard.\n• Animate & edit conversationally in gemini-omni-1.1-flash (up to 5 refs).\n• Score from Text + Image in Lyria 3.5 (44.1 kHz stereo).",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "Two-Part Workshop Progression (Google Flow + Gemini Omni 1.1 Flash + Lyria 3.5)",
            "link_label": "Facilitator Playbook ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
            "code": (
                "Part I  (Atomic Sandbox)     -> Push 1 isolated lever at a time: Camera Angles | Kelvin Warmth | Styles | 5-Object Physics\n"
                "Stage 0–1 (Story & Cast)     -> 2-sentence seed (gemini-3.8-flash) + 35-word Identity Anchor + 4-Angle Sheet (gemini-3-pro-image)\n"
                "Stage 2–3 (Stage & Board)    -> Empty Location Plates ([SCENE_STUDIO], [SCENE_CAFE]) + [PROP_CUP] + 6 Storyboard Keyframes\n"
                "Stage 4–5 (Omni Video & Aud) -> gemini-omni-1.1-flash (Multi-Ref & First/Last Frame) + 180° Dialogue + gemini-3.8-flash-tts + lyria-3.5\n"
                "Stage 6   (Omni Edit & Cut)  -> Multi-turn conversational video editing + 10s scene extension (up to 40s) + Kinetic Typography"
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Rule #1: Calibrate isolated variables in the Atomic Sandbox first; then layer character, set, and motion in production.",
        f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Explain why isolating variables in Part I (Atomic Sandbox) makes Part II (Incremental Commercial Production) dramatically more predictable.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"When creators jump straight into a 30-second commercial, they change five things at once and can't tell why a shot failed. That's why we start with Part I—our Atomic Prompt Sandbox—where we hold the subject constant and push one variable at a time: camera angle, Kelvin warmth, visual style, or multi-object physics. Once you feel how Gemini Image and Gemini Omni respond to each lever, Part II's incremental build becomes effortless.\"\n\n"
            "[TRANSITION]\n"
            "Let's jump right into Part I and test our first two isolated characteristics: Camera Angles and Kelvin Warmth."
        ),
    })

    # =========================================================================
    # SLIDE 03: Part I (1/3) — Atomic Sandbox: Camera Angles & Kelvin Warmth
    # =========================================================================
    sid = "SLIDE_03"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part I · Atomic Prompt Mastery Sandbox (Labs A & B)",
        "Testing Isolated Variables: Extreme Camera Angles & Kelvin Warmth",
        "Hold the subject constant and push camera perspective or Kelvin color temperature to the extreme in Image & Omni Video.",
        3,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Lab A: Extreme Camera Angles & Whip-Pan",
            "body": "• Worm's-Eye (14mm): Camera on wet cobblestones looking up 85°.\n• God's-Eye (90° Overhead): Flat-lay knolling on walnut desk.\n• Omni Single-Take: Low-angle tamp -> whip-pan right -> crane up.\n• Omni Conversational Edit: Re-angle to 180° orbit in 1 turn!",
        },
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Lab B: Warmth & Kelvin Color Temperature",
            "body": "• Cold 7500K Blue-Hour: Cyan streetlamp, slate shadows, isolation.\n• Warm 2400K Sunrise: Honey-gold sunbeams, volumetric steam.\n• Omni Dynamic Shift: Clouds part to turn 7500K room into 3000K gold.\n• Omni Conversational Relight: Flip cold rain to 2200K candlelight!",
        },
        {
            "accent": ACCENT_AMBER,
            "title": "Copy-Paste Prompts A.3 + A.4 — Single-Take Whip-Pan & Conversational Edit",
            "link_label": "Open Atomic Sandbox ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
            "code": (
                "[TURN 1 - INITIAL GENERATION]: One continuous cinematic shot, no jump cuts. Start on an extreme low-angle macro view at counter height\n"
                "of a barista's hand tamping espresso with a heavy brass tamper. The camera whip-pans smoothly right across the oak counter, following\n"
                "a steaming terracotta cup as it slides toward an architect in tortoiseshell glasses, and cranes up into a high-angle overhead view.\n"
                "[TURN 2 - CONVERSATIONAL EDIT]: Keep the exact character, cup movement, and audio, but change the camera to a slow 180° eye-level orbit."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Notice Turn 2: With Gemini Omni 1.1 Flash, you can change the camera angle or relight a video conversationally without starting over!",
        OMNI_STUDIO_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Run Hands-On Labs A and B from the Atomic Prompt Sandbox, testing extreme camera angles and Kelvin warmth shifts.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Open prompts/00-atomic-prompt-sandbox.md. First, look at Lab A: instead of letting the model pick a boring eye-level shot, we test a 14mm worm's-eye lookup on wet cobblestones, a 90-degree overhead flat-lay, and a continuous whip-pan-to-crane shot in Gemini Omni 1.1 Flash. Then in Turn 2, we ask Gemini Omni conversationally to keep the exact scene but orbit 180 degrees around the cup. Next, in Lab B, compare 7500K blue-hour coldness against 2400K golden sunrise warmth.\"\n\n"
            "[TRANSITION]\n"
            "Now let's test Visual Styles and Multi-Object Physics in Labs C and D."
        ),
    })

    # =========================================================================
    # SLIDE 04: Part I (2/3) — Atomic Sandbox: Visual Styles & Multi-Object Physics
    # =========================================================================
    sid = "SLIDE_04"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part I · Atomic Prompt Mastery Sandbox (Labs C & D)",
        "Testing Radical Film Styles, 5-Object Spatial Lock & Chain Physics",
        "Push tactile material styles and multi-object spatial/physical interactions in Nano Banana Pro & Gemini Omni 1.1 Flash.",
        4,
    )
    add_grid_2x2(ops, sid, [
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "Lab C.1 · 35mm Kodak Vision3 500T Anamorphic",
            "body": "• Panavision C-Series anamorphic lenses + organic 35mm grain.\n• Warm red-orange halation around glowing tungsten streetlamps, vertical oval bokeh, and horizontal blue streak flare.",
            "link_label": "Style Prompts C.1–C.4 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "psychology",
            "accent": ACCENT_PURPLE,
            "title": "Lab C.2 · 12fps Stop-Motion Clay & Felt Diorama",
            "body": "• Sculpted matte polymer clay figures with subtle thumbprints.\n• Needle-felted merino wool espresso steam + blown-glass raindrops on a balsa wood counter at 12fps shutter cadence.",
            "link_label": "Stop-Motion Prompt ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Lab D.1 · 5-Object Spatial Lock (`gemini-3-pro-image`)",
            "body": "• Center: Terracotta cup embossed with gold 'SOLIS'.\n• Left: Tortoiseshell glasses. Right: Brass watch at 6:00.\n• Foreground: 3 coffee beans on blueprint. Back: Fluted glass carafe.",
            "link_label": "5-Object Prompt D.1 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_GREEN,
            "title": "Lab D.2 · Chain-Reaction Physics (`gemini-omni-1.1-flash`)",
            "body": "• Brass marble rolls down oak ruler -> taps 3 brown-sugar dominoes -> nudges brass spoon into terracotta espresso cup -> ripples golden crema with synchronized foley.",
            "link_label": "Physics Prompt D.2 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Multi-Object Secret: Number each object (1)–(5) with explicit spatial prepositions (Center, Left, Right, Foreground, Background).",
        f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Demonstrate how to lock distinct visual styles (35mm film, stop-motion clay, watercolor) and combine 5 distinct objects without attribute bleeding.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Lab C, we test how specific material and lens vocabulary transforms the entire medium—from 35mm Kodak 500T film halation to a 12-frames-per-second stop-motion diorama made of polymer clay and felted wool. In Lab D, we stress-test multi-object composition: by numbering our five objects and anchoring each to a spatial zone, Nano Banana Pro renders every texture cleanly, while Gemini Omni simulates a full Rube Goldberg chain reaction.\"\n\n"
            "[TRANSITION]\n"
            "Now let's test Gemini Omni's kinetic typography and the latest Lyria 3.5 multimodal music models in Labs E and F."
        ),
    })

    # =========================================================================
    # SLIDE 05: Part I (3/3) — Kinetic Typography & Latest Lyria 3.5 Music Lab
    # =========================================================================
    sid = "SLIDE_05"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part I · Atomic Prompt Mastery Sandbox (Labs E & F)",
        "Gemini Omni Kinetic Typography & Lyria 3.5 Multimodal Music Lab",
        "Render in-video 3D typography that reacts to steam in Gemini Omni, and score images in 44.1 kHz stereo with Lyria 3.5.",
        5,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_BLUE,
            "title": "Lab E: In-Video Kinetic Typography (`gemini-omni-1.1-flash`)",
            "body": "• Gemini Omni synchronizes legible on-screen text with physical motion.\n• Prompt 3D gold serif letters ('AWAKEN THE CRAFT') to materialize above the cup as rising coffee steam physically swirls and parts through the letters!",
        },
        {
            "icon": "star",
            "accent": ACCENT_PURPLE,
            "title": "Lab F: Latest Lyria 3.5 & 3 Pro (`lyria-3.5` / `lyria-3-pro-preview`)",
            "body": "• 44.1 kHz high-fidelity stereo audio from Text OR Image + Text!\n• Pass a cold-rain or warm-sunrise image directly to lyria-3.5.\n• Use structural tags ([Intro], [Verse], [Chorus], [Crescendo]) or lyria-3-clip-preview for exact 30s commercial beds.",
        },
        {
            "accent": ACCENT_PURPLE,
            "title": "Copy-Paste Lab E.1 (Omni Kinetic Text) & Lab F.1 (`lyria-3.5` 44.1kHz Commercial Score)",
            "link_label": "Copy Labs E & F ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
            "code": (
                "[OMNI KINETIC TEXT]: Macro close-up of a steaming matte terracotta cappuccino cup on dark oak in golden light. As velvety steam rises,\n"
                "minimalist 3D gold serif letters reading \"AWAKEN THE CRAFT\" materialize above the rim; rising steam physically swirls through the letters.\n"
                "[LYRIA 3.5 SCORE]: 30-second commercial soundtrack in 44.1kHz stereo, 92 BPM: [0:00-0:08 Intro] Sparse felt piano & rain;\n"
                "[0:08-0:20 Groove] Warm fingerpicked acoustic guitar & upright bass; [0:20-0:30 Crescendo] Uplifting chamber strings in major key."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Lyria 3.5 Multimodal Secret: Pass your storyboard keyframe image + text prompt into lyria-3.5 so the music matches the exact lighting mood!",
        f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Showcase Gemini Omni's kinetic typography synchronization and introduce the latest Lyria 3.5 / Lyria 3 Pro / Lyria 3 Clip music models.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Before we finish Part I, look at two game-changing capabilities. First, Gemini Omni 1.1 Flash can render legible 3D kinetic typography inside the video that physically interacts with rising steam. Second, with the latest Lyria 3.5 and Lyria 3 Pro models, we get 44.1 kHz stereo music with full structural control, vocals or instrumentals, and multimodal image-to-music—meaning you can feed your storyboard frame directly into Lyria 3.5 to score the visual mood!\"\n\n"
            "[TRANSITION]\n"
            "Now let's review how Gemini Omni 1.1 Flash powers our video architecture across Google Flow and AI Studio."
        ),
    })

    # =========================================================================
    # SLIDE 06: Platform Architecture — Why Focus on Gemini Omni 1.1 Flash
    # =========================================================================
    sid = "SLIDE_06"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Video & Audio Architecture · Gemini Omni 1.1 Flash + Google Flow",
        "Why We Focus on Gemini Omni (`gemini-omni-1.1-flash`) for Video Production",
        "Combining multimodal reference fusion, conversational video editing, keyframe interpolation, and 360p-to-4K scaling.",
        6,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "1. Multimodal References\n(Up to 5 Img + 3 Vid)",
            "body": "• Simultaneously pass Text + up to 5 Image References + up to 3 Video References (3s).\n• Lock Character A + Character B + Set + Hero Prop in one shot with native synchronized audio.",
            "link_label": "Open Gemini Omni ↗",
            "link_url": OMNI_STUDIO_URL,
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "2. Conversational Editing\n& First/Last Keyframes",
            "body": "• Multi-turn chat editing via Interactions API: swap lighting, angles, or props while keeping the take.\n• First & Last Frame anchoring interpolates smooth camera transitions.",
            "link_label": "Open Google Flow ↗",
            "link_url": FLOW_URL,
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "3. 360p -> 4K Upscaling\n& 40s Scene Extension",
            "body": "• Rapidly prototype choreography in 360p ($0.034/s) or 720p, then upscale winning takes to 1080p/4K.\n• Extend clips in 3–10s increments up to 40 seconds total.",
            "link_label": "Cross-Platform Matrix ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "2026 Model Stack: gemini-3.8-flash (Story) · gemini-3-pro-image (Ingredients) · gemini-omni-1.1-flash (Video) · gemini-3.8-flash-tts · lyria-3.5",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Explain the architectural advantages of Gemini Omni 1.1 Flash as the primary video generation and editing model alongside Google Flow.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Why are we centering our video workflow on Gemini Omni 1.1 Flash? Three reasons: first, it accepts up to five reference images and three reference videos simultaneously; second, it supports multi-turn conversational video editing alongside First and Last Frame keyframing; and third, you can draft rapidly at 360p, extend scenes in 10-second increments up to 40 seconds, and upscale your final cut to 4K.\"\n\n"
            "[TRANSITION]\n"
            "Now let's begin Part II: building our 30-second commercial 'Solis — The 6:00 AM Spark' starting with Stage 0."
        ),
    })

    # =========================================================================
    # SLIDE 07: Part II · Stage 0 — The 2-Sentence Micro-Story Seed
    # =========================================================================
    sid = "SLIDE_07"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 0 (Layer 1 of 7): Narrative Foundation",
        "Start with a 2-Sentence Story Seed & Expand to a 3-Act Micro-Arc",
        "Constrain the commercial to 30 seconds, 2 characters, 2 contrasting Kelvin lighting worlds, and 1 hero prop.",
        7,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "psychology",
            "accent": ACCENT_AMBER,
            "title": "The 2-Sentence Seed ('Solis — The 6:00 AM Spark')",
            "body": "\"At 5:45 AM in a rainy city, an exhausted architect staring at a blank blueprint steps into a glowing corner café. One shared laugh and a warm terracotta cup of espresso reignite her creative spark.\"",
        },
        {
            "icon": "star",
            "accent": ACCENT_CYAN,
            "title": "3-Act Visual & Kelvin Lighting Arc (30 Seconds)",
            "body": "• Act I (0–8s): 7500K Cold Cyan Rain — Maya stuck at her studio desk.\n• Act II (8–22s): 2700K Warm Amber Glow — Leo slides the Solis cup across the counter; a 2-line conversation.\n• Act III (22–30s): 3000K Golden Sunrise — Maya sketches the bridge arch.",
        },
        {
            "accent": ACCENT_AMBER,
            "title": "Copy-Paste Prompt 0.1 — Expand Story Seed (Run in Flow Agent / gemini-3.8-flash)",
            "link_label": "Copy Prompt 0.1 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "Act as a Commercial Film Director. I have a two-sentence story seed for a 30-second brand commercial for 'Solis Artisan Coffee':\n"
                "\"At 5:45 AM in a rainy city, an exhausted architect staring at a blank blueprint steps into a glowing corner café.\n"
                "One shared laugh and a warm terracotta cup of espresso reignite her creative spark.\"\n"
                "Expand this seed into a tight 3-Act Micro-Story (Act I: The Creative Block, Act II: The Warm Encounter, Act III: The Spark Reignited).\n"
                "Keep it grounded in 2 characters (Maya, architect; Leo, barista), 2 locations, and 1 hero prop (matte terracotta Solis cup)."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Color & Mood Arc: 7500K Cold Pre-Dawn Rain (Problem) -> 2700K Warm Edison Café (Connection) -> Golden Sunrise (Transformation).",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Demonstrate how a 2-sentence story seed is expanded into a constrained 3-act commercial beat sheet.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Notice how we apply our Kelvin lighting lesson from Part I directly to our story structure: Act I is 7500K cold cyan rain at 5:45 AM; Act II is 2700K warm amber Edison light inside Leo's corner café; and Act III is golden morning sunrise flooding Maya's studio desk.\"\n\n"
            "[TRANSITION]\n"
            "Now let's lock Maya and Leo's faces in Stage 1 so they never drift across our 6 shots."
        ),
    })

    # =========================================================================
    # SLIDE 08: Stage 1 — Character Generation & The Face Consistency Formula
    # =========================================================================
    sid = "SLIDE_08"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 1 (Layer 2 of 7): Character & Face Consistency",
        "The 3-Pillar System for Zero Face Drift in Gemini Omni & Google Flow",
        "Combine a verbatim 35-word Identity Anchor Block, a neutral 5600K studio portrait, and a 4-Angle Turnaround Sheet.",
        8,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "code",
            "accent": ACCENT_AMBER,
            "title": "Pillar 1 · The 35-Word\nIdentity Anchor Block",
            "body": "• Never write 'a young woman' in Shot 1 and 'Maya' in Shot 2.\n• Lock 5 traits: Age/Heritage + Skin micro-feature (freckles/crinkles) + Hair clip + Eyewear + Outer/Inner Wardrobe.\n• Paste verbatim into every shot.",
            "link_label": "Anchor Templates ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Pillar 2 · Neutral 5600K\nCharacter Ingredient",
            "body": "• Generate your master portrait on a clean neutral grey backdrop with soft 5600K studio light (85mm, f/2.0).\n• Avoid colored neon light in reference portraits so lighting adapts cleanly to any scene.",
            "link_label": "Stage 1 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Pillar 3 · The 4-Angle\nTurnaround Sheet",
            "body": "• Prompt Nano Banana Pro (gemini-3-pro-image) for a 4-panel sheet in one 16:9 frame: Front, 45°, Profile, Smiling Close-Up.\n• Pass angle-matched panels into gemini-omni-1.1-flash (supports up to 5 image refs!).",
            "link_label": "Turnaround Prompt ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Pro Tip: Distinct accessories (round tortoiseshell glasses + ochre knit cardigan) act as high-weight visual anchors in Gemini Omni.",
        f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the 3-pillar technique that guarantees facial and wardrobe consistency in Gemini Omni and Google Flow.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"To guarantee zero face drift in Gemini Omni and Google Flow, we combine three pillars: a verbatim 35-word Identity Anchor Block, a neutral 5600K studio portrait, and a 4-angle turnaround sheet generated in Nano Banana Pro. Because Gemini Omni accepts up to five reference images per call, you can feed both front and 45-degree angles simultaneously.\"\n\n"
            "[TRANSITION]\n"
            "Let's copy and run the character prompts for Maya and Leo right now."
        ),
    })

    # =========================================================================
    # SLIDE 09: Live Lab #1 — Character & Face Consistency Prompts
    # =========================================================================
    sid = "SLIDE_09"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 1 Hands-On Lab · Character Ingredients (`[CHAR_MAYA]` & `[CHAR_LEO]`)",
        "Live Lab #1: Generating Locked Character Portraits & Turnaround Sheets",
        "Run these prompts in `gemini-3-pro-image` (Nano Banana Pro) or Google Flow's Ingredients Panel and pin both characters.",
        9,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Protagonist Anchor: `[CHAR_MAYA]` (Architect)",
            "body": "\"Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles across the nose, expressive dark brown eyes, shoulder-length wavy raven hair tied in a loose low clip, wearing an oversized ochre knit cardigan over a white crew-neck tee and round tortoiseshell glasses.\"",
        },
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "Co-Star Anchor: `[CHAR_LEO]` (Barista)",
            "body": "\"Leo, a 45-year-old artisanal barista with a neatly trimmed salt-and-pepper beard, warm crinkles around hazel eyes, wearing a charcoal linen apron over a rolled-sleeve chambray shirt. Neutral studio backdrop, soft warm key light, 85mm prime lens.\"",
        },
        {
            "accent": ACCENT_PURPLE,
            "title": "Copy-Paste Prompt 1.2 — 4-Angle Face Consistency Sheet (`gemini-3-pro-image`)",
            "link_label": "Open Web Prompt Deck ↗",
            "link_url": f"{GITHUB_BLOB}/docs/index.html",
            "code": (
                "A 4-panel character reference sheet on a clean neutral grey background showing the exact same woman in four views:\n"
                "(1) Front view neutral expression, (2) 45-degree three-quarter view with a tired sigh,\n"
                "(3) Side profile looking down thoughtfully, (4) Front close-up with a warm, genuine smile.\n"
                "Subject: Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles across the nose, expressive dark brown eyes,\n"
                "shoulder-length wavy raven hair tied in a loose low clip, wearing an oversized ochre knit cardigan and round tortoiseshell glasses."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "In Google Flow / AI Studio: Generate Maya & Leo in Nano Banana Pro -> Save as reference assets for Gemini Omni 1.1 Flash.",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the exact copy-paste prompts for generating Maya, Leo, and Maya's 4-panel turnaround sheet.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Copy Prompts 1.1, 1.2, and 1.3 into Google Flow's Ingredients creator or AI Studio with Nano Banana Pro. Once generated, pin Maya and Leo to your asset library.\"\n\n"
            "[TRANSITION]\n"
            "Now that our two actors are cast and locked, let's build our empty location plates and the Solis terracotta cup in Stage 2."
        ),
    })

    # =========================================================================
    # SLIDE 10: Stage 2 — Scene & Product World Generation
    # =========================================================================
    sid = "SLIDE_10"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 2 (Layer 3 of 7): Environments & Hero Product",
        "Build the Stage Before Calling the Actors: Empty Plates & Product Lock",
        "Generate actor-free Location Ingredients and a macro Product Ingredient so room layouts and brand logos stay rock-solid.",
        10,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Scene Ingredient A\n`[SCENE_STUDIO]` (7500K)",
            "body": "• Minimalist architect's loft desk at 5:45 AM before dawn.\n• Tall rain-streaked industrial window + cool 7500K cyan drafting lamp.\n• Explicitly prompt: 'Empty chair, no people' so the plate is clean.",
            "link_label": "Prompt 2.1 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Scene Ingredient B\n`[SCENE_CAFE]` (2700K)",
            "body": "• Cozy wood-paneled artisan espresso bar at dawn.\n• Warm 2700K amber Edison bulbs, brass espresso machine, oak counter.\n• Fogged rainy window in background for visual contrast.",
            "link_label": "Prompt 2.2 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "Object Ingredient\n`[PROP_CUP]` (Hero Product)",
            "body": "• Handcrafted matte terracotta ceramic cup + saucer.\n• Minimalist gold embossed sun emblem and clean word 'SOLIS'.\n• Generated in Nano Banana Pro (gemini-3-pro-image) for exact typography.",
            "link_label": "Prompt 2.3 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Why 'Empty Chair, No People'? If a location plate already contains a random person, the video model will fight your Character Ingredient.",
        f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Explain why location plates must be generated empty (without people) and how to lock product typography.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 2, always include 'Empty chair, no people' in your Scene Ingredients so Gemini Omni never has to overwrite a random background person with Maya or Leo.\"\n\n"
            "[TRANSITION]\n"
            "Let's run the three Stage 2 prompts to populate our asset library with both sets and the hero cup."
        ),
    })

    # =========================================================================
    # SLIDE 11: Live Lab #2 — Scene & Product Ingredient Prompts
    # =========================================================================
    sid = "SLIDE_11"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 2 Hands-On Lab · Scene & Object Ingredients",
        "Live Lab #2: Generating `[SCENE_STUDIO]`, `[SCENE_CAFE]` & `[PROP_CUP]`",
        "Create and pin these 3 visual assets so your project holds all 5 core building blocks of the commercial.",
        11,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Prompt 2.1 — Cold Rainy Studio (`[SCENE_STUDIO]`)",
            "body": "\"Wide establishing interior shot of a minimalist architect's loft desk by a tall rain-streaked industrial window at 5:45 AM before dawn. Empty chair, no people. A drafting lamp casts a cool 7500K cyan-blue pool of light over an unrolled blank blueprint and scale ruler. 35mm anamorphic lens.\"",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Prompt 2.2 — Warm Corner Café (`[SCENE_CAFE]`)",
            "body": "\"Medium-wide interior shot of a cozy, wood-paneled artisan espresso bar at dawn. Empty frame with no people. Warm 2700K amber Edison bulbs and a polished brass espresso machine gleam with gentle steam rising. Rain outside fogged window, reclaimed oak counter in foreground.\"",
        },
        {
            "accent": ACCENT_GREEN,
            "title": "Copy-Paste Prompt 2.3 — Hero Product Ingredient (`[PROP_CUP]` in Nano Banana Pro)",
            "link_label": "Copy Stage 2 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "Macro studio product photograph of a handcrafted matte terracotta ceramic cappuccino cup resting on a matching terracotta saucer.\n"
                "A minimalist gold embossed sun emblem and the word \"SOLIS\" are printed cleanly on the front of the cup.\n"
                "Rich velvety hazelnut crema with delicate rosetta latte art on top, a wisp of steam rising.\n"
                "Soft warm rim lighting, neutral dark studio background, 100mm macro lens."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Checkpoint: You now have 5 locked Ingredients — [CHAR_MAYA], [CHAR_LEO], [SCENE_STUDIO], [SCENE_CAFE], and [PROP_CUP].",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Guide participants through generating the two empty location plates and the Solis terracotta cup ingredient.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Run Prompts 2.1, 2.2, and 2.3 now. With Maya, Leo, the Studio, the Café, and the Solis Cup generated, we have all five visual building blocks ready for storyboarding.\"\n\n"
            "[TRANSITION]\n"
            "Let's assemble our 6-shot visual storyboard in Stage 3."
        ),
    })

    # =========================================================================
    # SLIDE 12: Stage 3 — Visual Storyboarding & Continuity Bridges
    # =========================================================================
    sid = "SLIDE_12"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 3 (Layer 4 of 7): Visual Storyboarding",
        "The 6-Shot Commercial Storyboard & Reference Combination Matrix",
        "Lock framing, Kelvin lighting transitions, and First/Last keyframe pairs in still images before generating video.",
        12,
    )
    add_grid_2x2(ops, sid, [
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Shots 1 & 2 · Act I -> Act II Threshold (0–10s)",
            "body": "• Shot 1: [CHAR_MAYA] + [SCENE_STUDIO] — Medium close-up at 5:45 AM; cold 7500K cyan rain reflects on her glasses.\n• Shot 2: [CHAR_MAYA] + [SCENE_CAFE] — Tracking shot stepping out of blue rain into warm 2700K amber café glow.",
            "link_label": "Keyframes 3.1 & 3.2 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "Shot 3 · Hero Product First -> Last Pair (10–15s)",
            "body": "• First Frame: Espresso pouring in dual streams into the matte terracotta SOLIS cup.\n• Last Frame: Leo's hand sliding the steaming SOLIS cup across the oak counter toward the camera.",
            "link_label": "Keyframe Pair 3.3 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Shots 4 & 5 · Two-Character Conversation (15–25s)",
            "body": "• Shot 4 (OTS): [CHAR_LEO] on right looking screen-left over Maya's shoulder (+ [SCENE_CAFE] + [PROP_CUP]).\n• Shot 5 (Reverse): [CHAR_MAYA] on left looking screen-right, holding the SOLIS cup and smiling.",
            "link_label": "Keyframes 3.4 & 3.5 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_GREEN,
            "title": "Shot 6 · Act III Spark Reignited Finale (25–30s)",
            "body": "• First Frame: Golden sunrise hits the studio desk as Maya sets the SOLIS cup beside the blank blueprint.\n• Last Frame: High-angle over shoulder as her pencil sweeps a bold bridge arch + Kinetic 'SOLIS' title.",
            "link_label": "Keyframe Pair 3.6 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Gemini Omni Advantage: Pass up to 5 reference images per shot (e.g., Leo + Maya + Café + SOLIS Cup in Shot 4)!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Map out all 6 shots of the 30-second commercial and show which Ingredients combine in each shot.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Here is our complete 6-shot commercial storyboard. Every single shot is a deterministic combination of our 5 locked assets. Notice how Shots 3 and 6 use First and Last Frame pairs for keyframe interpolation in Gemini Omni.\"\n\n"
            "[TRANSITION]\n"
            "Let's look at the exact prompts for compositing these storyboard keyframes."
        ),
    })

    # =========================================================================
    # SLIDE 13: Live Lab #3 — Storyboard Keyframe Compositing
    # =========================================================================
    sid = "SLIDE_13"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 3 Hands-On Lab · Compositing Keyframes & First/Last Pairs",
        "Live Lab #3: Generating Storyboard Stills Before Animating Video",
        "Combine Character + Scene references into still frames to verify composition and prepare First/Last frames for Gemini Omni.",
        13,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Keyframe 3.1 — Shot 1 Start Still (Maya + Studio)",
            "body": "Attach [CHAR_MAYA] + [SCENE_STUDIO]: Maya sits at the rain-streaked architect's desk at 5:45 AM resting her chin on her hand, staring at the blank blueprint. Cool 7500K cyan window light reflects on her tortoiseshell glasses.",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Keyframe 3.3 — Shot 3 First & Last Frame Pair",
            "body": "• First Frame: Macro shot under brass portafilter pouring espresso into the terracotta SOLIS cup.\n• Last Frame: Leo's hand sliding the steaming SOLIS cup across the reclaimed oak counter into foreground close-up.",
        },
        {
            "accent": ACCENT_CYAN,
            "title": "Copy-Paste Prompt 3.1 — Composited Storyboard Keyframe (Multi-Image Reference)",
            "link_label": "All 6 Keyframe Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "Using the character reference for Maya and the studio location reference:\n"
                "Medium close-up cinema still of Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles,\n"
                "wavy raven hair in a low clip, round tortoiseshell glasses, and an ochre knit cardigan, sitting at the rain-streaked\n"
                "architect's desk at 5:45 AM. She rests her chin on her hand, staring at the blank blueprint with a tired expression.\n"
                "Cool cyan-blue pre-dawn window light reflects on her glasses. 35mm anamorphic lens."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Why generate First & Last frames for Shot 3? Because Gemini Omni's keyframe anchoring guarantees the SOLIS logo lands sharply!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to composite reference ingredients into storyboard stills and Start/End frame pairs.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"By generating both the First Frame (espresso pouring) and the Last Frame (Leo sliding the cup toward the lens) as still images first, Gemini Omni 1.1 Flash's keyframe interpolation smoothly bridges the motion between them while keeping the gold SOLIS logo razor-sharp.\"\n\n"
            "[TRANSITION]\n"
            "Now let's move to Stage 4 and animate our shots with Gemini Omni 1.1 Flash."
        ),
    })

    # =========================================================================
    # SLIDE 14: Stage 4 — Video Generation with Gemini Omni 1.1 Flash
    # =========================================================================
    sid = "SLIDE_14"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 4 (Layer 5 of 7): Gemini Omni Video Directing",
        "Animating with `gemini-omni-1.1-flash`: Multi-Ref, Keyframes & 4K",
        "Combine up to 5 image references, First/Last Frame keyframing, 360p fast prototyping, and conversational edits.",
        14,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "Mode A · Multi-Reference\nVideo (Up to 5 Img Refs)",
            "body": "• Pass [CHAR_MAYA] + [SCENE_STUDIO] + [PROP_CUP] into gemini-omni-1.1-flash (or Flow Ingredients to Video).\n• Best for natural acting & continuous camera moves (Shots 1, 2, 4, 5).",
            "link_label": "Open Gemini Omni ↗",
            "link_url": OMNI_STUDIO_URL,
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Mode B · First & Last\nFrame Keyframing",
            "body": "• Anchor both First Frame + Last Frame in gemini-omni-1.1-flash (or Flow Frames to Video).\n• Perfect for camera orbits, macro product reveals, and match cuts (Shots 3 & 6).",
            "link_label": "Stage 4 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "code",
            "accent": ACCENT_PURPLE,
            "title": "Draft at 360p -> Edit\nConversationally -> 4K",
            "body": "• Step 1: Generate fast 360p/720p draft (3s–10s).\n• Step 2: Refine lighting or angle via multi-turn chat.\n• Step 3: Upscale winning take to crisp 1080p or 4K at 24fps!",
            "link_label": "Prompt Formula ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Gemini Omni Workflow: Draft at 360p ($0.034/s) -> Conversational Edit -> Upscale final hero shot to 4K!",
        OMNI_STUDIO_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the 3-mode video production workflow in Gemini Omni 1.1 Flash: Multi-Reference Video, First/Last Frame Keyframing, and 360p-to-4K conversational iteration.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 4, we unleash Gemini Omni 1.1 Flash. Use Multi-Reference Video for open-ended acting in Shots 1, 2, 4, and 5; use First and Last Frame Keyframing for exact product transitions in Shots 3 and 6; and iterate at 360p before upscaling your winning take to 4K.\"\n\n"
            "[TRANSITION]\n"
            "Let's copy and run our Gemini Omni video prompts for Shots 1, 2, and 3."
        ),
    })

    # =========================================================================
    # SLIDE 15: Live Lab #4 — Gemini Omni Video Prompts (Shots 1–3)
    # =========================================================================
    sid = "SLIDE_15"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 4 Hands-On Lab · Animating Shots 1, 2 & 3 in `gemini-omni-1.1-flash`",
        "Live Lab #4: Running Multi-Reference & First/Last Frame Video",
        "Generate the opening creative block (Shot 1), the café entrance (Shot 2), and the macro espresso slide (Shot 3).",
        15,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "Shot 1 — Multi-Ref Video (`gemini-omni-1.1-flash`)",
            "body": "• Attach Refs: [CHAR_MAYA] + [SCENE_STUDIO]\n• Camera: Slow, smooth dolly-in toward medium close-up.\n• Action: Maya exhales a quiet sigh, taps her wooden pencil twice on the blank blueprint, glances at the rain.",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Shot 3 — First & Last Frame Keyframing",
            "body": "• First Frame: Espresso pouring into SOLIS cup.\n• Last Frame: Leo's hand sliding SOLIS cup to foreground.\n• Camera: 100mm macro tracking shot, 60fps slow-motion feel with rising golden steam.",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "Copy-Paste Prompt 4.1 — Shot 1 Video (`gemini-omni-1.1-flash` with Native Synchronized Audio)",
            "link_label": "Copy Shots 1–3 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "Slow, smooth dolly-in toward a medium close-up of Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles,\n"
                "wavy raven hair in a low clip, round tortoiseshell glasses, and an ochre knit cardigan, sitting at her drafting table by a\n"
                "rain-streaked window at 5:45 AM. She exhales a quiet sigh, taps her wooden pencil twice against the blank blueprint, and\n"
                "glances out at the rain. Cold 7500K cyan streetlamp reflections glide across her glasses. 35mm anamorphic lens.\n"
                "Audio: Soft rhythmic rain pattering against window glass, distant thunder, two crisp wooden pencil taps, and a quiet sigh."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Gemini Omni natively generates synchronized rain, wooden pencil taps, and espresso extraction foley with every video clip!",
        OMNI_STUDIO_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the executable Gemini Omni video prompts for Shots 1–3.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Run Prompt 4.1 with Maya and the Studio attached, and Prompt 4.3 with our Shot 3 First and Last frames. Gemini Omni natively generates the synchronized foley sound effects—two wooden pencil taps on paper and rain against glass.\"\n\n"
            "[TRANSITION]\n"
            "Now we reach Stage 5: piling on two-character dialogue, Gemini 3.8 Flash TTS, and our Lyria 3.5 multimodal musical score."
        ),
    })

    # =========================================================================
    # SLIDE 16: Stage 5 — Directing Two-Character Dialogue & Lyria 3.5 Score
    # =========================================================================
    sid = "SLIDE_16"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 5 (Layer 6 of 7): Dialogue, TTS & Lyria 3.5 Music",
        "Directing Two-Character Conversations & Multimodal Scoring in Lyria 3.5",
        "Combine the 180° Eyeline Rule, Gemini Omni lip-sync, Gemini 3.8 Flash TTS, and Lyria 3.5 (44.1 kHz Text + Image scoring).",
        16,
    )
    add_grid_2x2(ops, sid, [
        {
            "icon": "hub",
            "accent": ACCENT_AMBER,
            "title": "1. The 180° Eyeline Rule (Shot-Reverse-Shot)",
            "body": "• To make two clips look like a real conversation, lock opposite screen directions:\n• Shot 4 (Leo): Positioned on RIGHT of frame, looking SCREEN-LEFT.\n• Shot 5 (Maya): Positioned on LEFT of frame, looking SCREEN-RIGHT.",
            "link_label": "180° Rule Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_BLUE,
            "title": "2. Gemini Omni Native Lip-Sync Dialogue",
            "body": "• Put spoken words in single quotes ('...') right after vocal tone:\n• \"Leo speaks in a warm baritone: 'Rough night with the blueprints?'\"\n• Keep dialogue to 8–12 words per 6–8s clip (~2 words/sec).",
            "link_label": "Dialogue Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "psychology",
            "accent": ACCENT_PURPLE,
            "title": "3. Studio Voiceover (`gemini-3.8-flash-tts`)",
            "body": "• Use gemini-3.8-flash-tts with expressive voices (Kore, Charon, Aoede, Puck, Fenrir) for the brand tagline.\n• Supports affective tags: [sigh], [short pause].",
            "link_label": "TTS Prompt 5.3 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "4. Latest Lyria 3.5 Score (`lyria-3.5` / `lyria-3-pro`)",
            "body": "• Pass Keyframe 3.3 Image + Text into lyria-3.5 (or lyria-3-clip-preview) for 44.1 kHz stereo music: sparse felt piano (0–8s) -> warm acoustic guitar (8–20s) -> strings crescendo (20–30s).",
            "link_label": "Lyria 3.5 Prompt ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Audio Stack: gemini-omni-1.1-flash (Lip-Sync + Foley) + gemini-3.8-flash-tts (Voiceover) + lyria-3.5 (44.1kHz Multimodal Score).",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the 180-degree camera axis rule for two-character conversations and the upgraded 3-part audio stack (Gemini Omni native lip-sync, Gemini 3.8 Flash TTS, and Lyria 3.5).\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 5, we combine the 180-degree eyeline rule with our upgraded audio stack: Gemini Omni 1.1 Flash renders Leo and Maya's lip-synced dialogue, Gemini 3.8 Flash TTS delivers the studio narrator tagline in the 'Kore' voice, and Lyria 3.5 takes both our text prompt and Keyframe 3.3 image to compose a 44.1 kHz stereo score.\"\n\n"
            "[TRANSITION]\n"
            "Let's run the Shot 4, Shot 5, TTS, and Lyria 3.5 prompts right now."
        ),
    })

    # =========================================================================
    # SLIDE 17: Live Lab #5 — Two-Character Conversation & Lyria 3.5 Prompts
    # =========================================================================
    sid = "SLIDE_17"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 5 Hands-On Lab · Shot-Reverse-Shot Dialogue & Lyria 3.5",
        "Live Lab #5: Directing Leo & Maya's Conversation + Lyria 3.5 Score",
        "Run Shot 4 (OTS on Leo) and Shot 5 (Reverse on Maya) in `gemini-omni-1.1-flash`, then score with `lyria-3.5`.",
        17,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Shot 4: Leo Speaks (Looking Screen-Left)",
            "body": "Over-the-shoulder medium shot from behind Maya's ochre shoulder on the left, focusing on Leo on the right looking screen-left with a warm smile. Leo speaks in a warm baritone: 'Rough night with the blueprints? Start with this—the lines always follow.'",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "Shot 5: Maya Replies (Looking Screen-Right)",
            "body": "Reverse-angle medium close-up of Maya on the left looking screen-right. She wraps both hands around the terracotta SOLIS cup, inhales the steam, smiles, and replies softly: 'You just saved the whole skyline, Leo.'",
        },
        {
            "accent": ACCENT_PURPLE,
            "title": "Copy-Paste Prompts 5.2, 5.3 & 5.4 — Omni Reverse Shot + `gemini-3.8-flash-tts` + `lyria-3.5`",
            "link_label": "Copy Stage 5 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "[SHOT 5 - gemini-omni-1.1-flash]: Reverse-angle medium close-up of Maya on the left looking screen-right, holding the terracotta SOLIS cup.\n"
                "She smiles and replies softly: 'You just saved the whole skyline, Leo.' Warm golden key light, 50mm lens.\n"
                "[TTS - gemini-3.8-flash-tts (Kore)]: \"[sigh] Every bold idea starts before the sun rises. [short pause] Solis. Awaken the craft.\"\n"
                "[SCORE - lyria-3.5 (44.1kHz)]: [0:00-0:08] Sparse felt piano & rain -> [0:08-0:20] Warm acoustic guitar -> [0:20-0:30] Strings crescendo."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Verify Across Shots 4 & 5: Leo looks left -> Maya looks right -> The terracotta SOLIS cup sits on the oak counter between them.",
        OMNI_STUDIO_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the copy-paste conversation prompts for Shot 4, Shot 5, Gemini 3.8 Flash TTS, and Lyria 3.5.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Copy Prompts 5.1 through 5.4. Watch how Shot 4 frames Leo over Maya's ochre-cardigan shoulder on the left, and Shot 5 flips the camera to Maya on the left looking right. Then generate the voiceover with gemini-3.8-flash-tts and the 44.1 kHz score with lyria-3.5.\"\n\n"
            "[TRANSITION]\n"
            "Finally, let's move to Stage 6 to apply Gemini Omni conversational edits, 10s scene extensions, and kinetic typography."
        ),
    })

    # =========================================================================
    # SLIDE 18: Stage 6 — Omni Conversational Edit, 40s Extend & Repo Wrap-Up
    # =========================================================================
    sid = "SLIDE_18"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Stage 6 (Layer 7 of 7): Conversational Edit, Extend & Resources",
        "Finishing with Gemini Omni Conversational Edit, 40s Extend & Repo",
        "Refine takes conversationally, extend clips up to 40s, sync kinetic brand text, and explore all 3 commercial packs on GitHub.",
        18,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "bolt",
            "accent": ACCENT_BLUE,
            "title": "1. Omni Conversational\nEdit & 40s Extension",
            "body": "• Multi-turn edit on Shot 5: intensify 2700K golden rim light & steam without losing Maya's acting.\n• Extend in 3–10s increments (up to 40s) as Maya takes her first sip!",
            "link_label": "Prompt 6.1 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "2. Shot 6 Finale with\nKinetic Typography",
            "body": "• Maya's charcoal pencil sweeps a bold bridge arch in golden sunrise.\n• Clean gold serif text 'SOLIS — AWAKEN THE CRAFT' materializes in the rising coffee steam (4K upscale).",
            "link_label": "Prompt 6.2 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "code",
            "accent": ACCENT_GREEN,
            "title": "3. GitHub Repo & 3\nFull Commercial Packs",
            "body": "• Part I Atomic Prompt Sandbox\n• Pack 1: Solis Artisan Coffee\n• Pack 2: NovaPay Fintech\n• Pack 3: Kuntur Outdoor Gear\n• Interactive Web Portal",
            "link_label": "Open GitHub Repo ↗",
            "link_url": GITHUB_REPO,
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Star & Fork the Updated Workshop Repo: https://github.com/AllInVaders/google-flow-storytelling-workshop",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to finish the commercial using Gemini Omni conversational editing, 10s scene extension, kinetic typography, and J/L cuts, and share the GitHub repo links.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 6, we use Gemini Omni's conversational editing to boost the golden rim light on Shot 5, extend her reaction by 4 seconds, and render Shot 6 with kinetic gold typography reading 'SOLIS — AWAKEN THE CRAFT' synced to the rising steam. Everything we covered today—both Part I's Atomic Prompt Sandbox and Part II's 7-stage incremental build—is live in our GitHub repository!\"\n\n"
            "[TRANSITION]\n"
            "Thank you, and happy filmmaking with Google Flow, Gemini Omni 1.1 Flash, and Lyria 3.5!"
        ),
    })

    return ops


def get_existing_slide_ids(pres_id):
    cmd = [GSLIDES, "readonly", "info", pres_id, "--json"]
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0:
        return None
    try:
        data = json.loads(res.stdout)
        slides = data.get("slides", [])
        return [s.get("objectId") for s in slides if s.get("objectId")]
    except Exception:
        return None


def main():
    pres_id = os.environ.get("PRES_ID", DEFAULT_PRES_ID)
    existing_ids = get_existing_slide_ids(pres_id)
    if existing_ids:
        print(f"1. Updating existing Google Slides presentation in-place: {pres_id} ({len(existing_ids)} old slides)...")
    else:
        print("1. Creating new Google Slides presentation via gslides CLI...")
        create_cmd = [
            GSLIDES,
            "mutate",
            "create",
            "--title",
            "Google Flow, Gemini Omni & Lyria 3.5: Incremental Storytelling Workshop",
            "--json",
        ]
        res = subprocess.run(create_cmd, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout.strip())
        pres_id = data.get("presentationId") or data.get("id")
        existing_ids = ["p"]

    ops = build_all_slides(existing_ids)
    batch_file = "/tmp/flow_workshop_slides_batch.json"
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(ops, f, indent=2)

    print(f"2. Executing batch update ({len(ops)} operations across 18 slides)...")
    batch_cmd = [GSLIDES, "mutate", "batch", pres_id, "-f", batch_file, "--json"]
    subprocess.run(batch_cmd, capture_output=True, text=True, check=True)
    print("Batch completed successfully!")
    print(f"PRESENTATION_URL=https://docs.google.com/presentation/d/{pres_id}/edit")

    with open("/tmp/flow_workshop_pres_id.txt", "w", encoding="utf-8") as f:
        f.write(pres_id)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Builds the 14-Slide Native Editable Google Slides Deck for the Google Flow & Gemini Omni Storytelling Workshop.

Features:
- 100% Focused on Google Flow (https://labs.google/fx/tools/flow), Gemini Omni Flash, and Nano Banana Pro
- Part I: Google Flow Prompt Sandbox (Labs A–D: Camera Angles, Kelvin Warmth, Visual Styles, Multi-Object Physics & Kinetic Text)
- Part II: 5-Step Incremental Story Build ("Solis — The 6:00 AM Spark") with proper @Maya and @Leo Character Referencing (Create Once -> Refer with @Name)
- Single-word classic Material Icons (bolt, hub, code, check, warning, security, key, cloud, lock, psychology, star)
- Clickable link pills pointing to https://github.com/AllInVaders/google-flow-storytelling-workshop and https://labs.google/fx/tools/flow
- Tripartite speaker notes ([PURPOSE], [VERBAL SCRIPT], [TRANSITION]) on 100% of slides
"""

import json
import os
import subprocess

GSLIDES = "/google/bin/releases/gemini-agents-gslides/gslides"
DEFAULT_PRES_ID = "1RvTUXHZ1RYTo92FfgsawQ3dUK2bK1DDbZAPO0LVwhl0"
GITHUB_REPO = "https://github.com/AllInVaders/google-flow-storytelling-workshop"
GITHUB_BLOB = "https://github.com/AllInVaders/google-flow-storytelling-workshop/blob/main"
FLOW_URL = "https://labs.google/fx/tools/flow"

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


def add_header(ops, sid, category, title, subtitle, slide_num, total_slides=14):
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
        ops.append({"op": "add-slide", "layout": "BLANK", "id": "SLIDE_01"})
        for old_id in existing_slide_ids:
            ops.append({"op": "delete-element", "element": old_id})
    else:
        ops.append({"op": "add-slide", "layout": "BLANK", "id": "SLIDE_01"})
        ops.append({"op": "delete-element", "element": "p"})

    # =========================================================================
    # SLIDE 01: Hero Cover — Two-Part Google Flow & Gemini Omni Roadmap
    # =========================================================================
    sid = "SLIDE_01"
    add_header(
        ops,
        sid,
        "Google Flow · Gemini Omni Flash · Nano Banana Pro · Workshop",
        "Google Flow & Gemini Omni: Incremental Storytelling Workshop",
        "Part I tests isolated prompt levers in Google Flow; Part II builds a 30s commercial with @Maya & @Leo.",
        1,
    )
    add_five_pipeline(ops, sid, [
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Part I · Sandbox",
            "body": "• Labs A–D in Flow\n• Camera Angles\n• 7500K vs 2400K\n• Visual Styles\n• Multi-Object Physics",
            "link_label": "Prompt Sandbox ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Steps 1–2 · Cast",
            "body": "• 2-Sentence Seed\n• 5-Shot Beat Sheet\n• Create @Maya Once\n• Create @Leo Once\n• @Studio & @Cafe",
            "link_label": "Step 1–2 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Step 3 · Board",
            "body": "• Nano Banana Pro\n• Prompt Only with @Maya & @Leo\n• No Re-Generation\n• Start/End Frames",
            "link_label": "Step 3 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "psychology",
            "accent": ACCENT_CYAN,
            "title": "Step 4 · Omni",
            "body": "• Video > Omni Flash\n• @Character + @Voice\n• Start/End Frames\n• 180° Dialogue Rule\n• 360p -> 720p Free",
            "link_label": "Step 4 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "Step 5 · Cut",
            "body": "• 3-Turn Video Edit\n• Conversational Relighting\n• Kinetic Brand Text\n• Scenebuilder Export",
            "link_label": "Prompt Library ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "100% Google Flow Workspace: Create @Characters Once -> Refer by @Name -> Animate & Edit in Gemini Omni Flash!",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Welcome attendees and introduce the simplified Two-Part Google Flow & Gemini Omni Flash Storytelling Workshop.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Welcome! Today we are working 100% inside Google Flow powered by Nano Banana Pro for images and Gemini Omni Flash for video. In Part I, we'll spend 25 minutes in our Prompt Sandbox testing isolated camera angles, warmth, styles, and physics. In Part II, we'll build a 30-second commercial by creating @Maya and @Leo once and referencing them across 5 simple steps.\"\n\n"
            "[TRANSITION]\n"
            "Let's look at why this two-part method prevents character drift in Google Flow."
        ),
    })

    # =========================================================================
    # SLIDE 02: Core Method — Sandbox Testing + Incremental Layering
    # =========================================================================
    sid = "SLIDE_02"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Workshop Methodology · Why One-Shot Prompts Fail",
        "How Google Flow Works: Sandbox Testing + Incremental Layering",
        "Test isolated levers first; then create @Characters once and build your commercial scene by scene.",
        2,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "warning",
            "accent": ACCENT_RED,
            "title": "The 'Re-Generation'\nTrap (What Fails)",
            "body": "• Writing a huge paragraph that re-describes your hero's face and outfit in every prompt.\n• Result: Google Flow generates a brand-new person in every clip!",
            "link_label": "See Slide 08 Fix ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Part I: Prompt Sandbox\n(Labs A–D, 25 Min)",
            "body": "• Hold the subject constant and test ONE variable per prompt.\n• Master Camera Angles, Kelvin Warmth, Visual Styles, and Physics in Omni Flash.",
            "link_label": "Open Sandbox Labs ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "Part II: Create Once,\nRefer with @Name",
            "body": "• Create @Maya & @Leo ONCE in Characters > New Character.\n• In every scene prompt, just type '@Maya drinks coffee'—face, outfit & voice stay locked!",
            "link_label": "Open Student Labs ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Golden Rule: Never re-describe a saved character in Google Flow—create @Maya once and only refer to @Maya!",
        f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Explain the core mistake beginners make in Google Flow (re-describing characters in every prompt) and how our two-part structure solves it.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"The #1 mistake people make in Google Flow is re-pasting a character's physical description in every scene prompt. When you do that, you're asking the model to re-generate a new person every time! Instead, we create @Maya once in the Characters tab, and from that moment on, we only refer to @Maya by name.\"\n\n"
            "[TRANSITION]\n"
            "Before we create our cast, let's warm up in Part I with Labs A and B."
        ),
    })

    # =========================================================================
    # SLIDE 03: Part I (1/2) — Sandbox Labs A & B: Angles & Kelvin Warmth
    # =========================================================================
    sid = "SLIDE_03"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part I · Google Flow Prompt Sandbox (Labs A & B)",
        "Sandbox Labs A & B: Camera Angles & Kelvin Lighting Warmth",
        "Keep the subject constant in Google Flow and test extreme camera geometry and color temperature.",
        3,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Lab A: Camera Angles & Motion (A.1 – A.4)",
            "body": "• A.1 Worm's-Eye Low Angle (14mm lens looking straight up)\n• A.2 90° Overhead Flat-Lay (geometric tabletop symmetry)\n• A.3 Single-Take Whip-Pan to Macro (Omni Flash, 6s)\n• A.4 1-Turn Video Edit: 'Change to slow 180° eye-level orbit'",
        },
        {
            "icon": "star",
            "accent": ACCENT_BLUE,
            "title": "Lab B: Kelvin Warmth & Relighting (B.1 – B.4)",
            "body": "• B.1 Cold 7500K Blue-Hour Isolation (5:45 AM pre-dawn)\n• B.2 Warm 2400K Golden Sunrise Breakthrough (amber rim light)\n• B.3 8s Real-Time Cold-to-Warm Lighting Shift (Omni Flash)\n• B.4 1-Turn Video Edit: 'Change lighting to 2200K candlelight'",
        },
        {
            "accent": ACCENT_AMBER,
            "title": "Copy-Paste in Google Flow (Video > Omni Flash, 6s–8s, Omni 360p)",
            "link_label": "Copy Labs A & B ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
            "code": (
                "[LAB A.3 - Whip-Pan]: Dynamic camera starting in a wide shot of a sunlit cafe, then executing a fast whip-pan right and dolly-in\n"
                "to an extreme macro close-up of dark espresso pouring into a matte terracotta cup, golden crema swirling, realistic steam rising.\n"
                "[LAB B.3 - Sunrise Shift]: Fixed-tripod medium shot of an architect's desk by a rain-streaked window. Over 8s, lighting transitions\n"
                "smoothly from cold 7500K blue pre-dawn shadows into warm 2400K golden sunrise beams illuminating a steaming terracotta cup."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Pro Tip: Test prompts in 'Omni 360p' at half the credit cost, then click 'Upscale to 720p' for 0 credits!",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Guide students through Sandbox Labs A (Camera Angles) and B (Kelvin Warmth & Relighting) in Google Flow.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Open Google Flow and create project '00 - Flow Prompt Sandbox'. In Lab A, we test extreme 14mm worm's-eye angles, 90-degree flat-lays, and a single-take whip-pan in Omni Flash. In Lab B, we shift our drafting desk from cold 7500K blue-hour shadows to warm 2400K golden sunrise beams, and test a 1-turn conversational video edit.\"\n\n"
            "[TRANSITION]\n"
            "Now let's test Visual Styles and Multi-Object Physics in Labs C and D."
        ),
    })

    # =========================================================================
    # SLIDE 04: Part I (2/2) — Sandbox Labs C & D: Styles, Objects & Physics
    # =========================================================================
    sid = "SLIDE_04"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part I · Google Flow Prompt Sandbox (Labs C & D)",
        "Sandbox Labs C & D: Visual Styles, Multi-Object Lock & Physics",
        "Swap artistic mediums on the same scene and test 5-object spatial locks and kinetic typography in Omni Flash.",
        4,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "psychology",
            "accent": ACCENT_PURPLE,
            "title": "Lab C: Visual Style Transfer (C.1 – C.3)",
            "body": "• C.1 35mm Anamorphic Film (Kodak Vision3, halation, grain)\n• C.2 12fps Stop-Motion Clay & Felt Diorama (Omni Flash, 6s)\n• C.3 Architectural Fountain-Pen Ink & Watercolor Wash\n• Same action (barista pouring latte art), 3 tactile worlds!",
        },
        {
            "icon": "hub",
            "accent": ACCENT_GREEN,
            "title": "Lab D: Combining Objects & Physics (D.1 – D.3)",
            "body": "• D.1 5-Object Tabletop Lock (Cup, Calipers, Blueprint, Glasses, Rosemary)\n• D.2 Rube Goldberg Espresso Chain Reaction (Omni Flash, 8s)\n• D.3 In-Video Kinetic Text: 'AWAKEN THE CRAFT' in rising steam",
        },
        {
            "accent": ACCENT_PURPLE,
            "title": "Copy-Paste in Google Flow (Video > Omni Flash, 6s)",
            "link_label": "Copy Labs C & D ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
            "code": (
                "[LAB C.2 - Stop-Motion]: Handcrafted stop-motion animation at 12 frames per second of a miniature clay barista pouring cotton-wool\n"
                "steam and glossy resin espresso into a tiny terracotta clay mug on a balsa-wood counter, visible thumbprints on the clay.\n"
                "[LAB D.3 - Kinetic Text]: Close-up of a steaming matte terracotta cup embossed with 'SOLIS' in golden sunlight. As translucent\n"
                "white steam rises, clean minimalist gold serif typography reading 'AWAKEN THE CRAFT' forms naturally above the cup."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Takeaway: Specify tactile material nouns ('cotton-wool steam', 'balsa-wood') and explicit left/center/right anchors.",
        f"{GITHUB_BLOB}/prompts/00-atomic-prompt-sandbox.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Run Sandbox Labs C (Visual Styles) and D (Multi-Object Composition, Physics & Kinetic Typography) in Google Flow.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Lab C, watch how Omni Flash turns a barista pouring coffee into a 12-frames-per-second stop-motion clay diorama with cotton-wool steam. In Lab D, we lock 5 distinct objects on a tabletop and render kinetic gold serif typography ('AWAKEN THE CRAFT') directly inside the rising coffee steam.\"\n\n"
            "[TRANSITION]\n"
            "Now let's review all the Gemini Omni Flash tools inside Google Flow before starting Part II."
        ),
    })

    # =========================================================================
    # SLIDE 05: Why We Use Gemini Omni Flash in Google Flow
    # =========================================================================
    sid = "SLIDE_05"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Core Engine · Gemini Omni Flash Inside Google Flow",
        "Why We Use Gemini Omni Flash in Google Flow",
        "One unified model in Google Flow for @Character locks, Start/End Frames, Voice dialogue, and 3-turn video edits.",
        5,
    )
    add_grid_2x2(ops, sid, [
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "1. Native @Character, @Ingredient & @Voice Locks",
            "body": "Type @ in the Google Flow prompt box to combine @Maya, @Leo, @Studio, @Cafe, and @SolisCup—with their bundled character voices automatically synced to spoken lines.",
            "link_label": "Flow Cheat Sheet ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "2. Flexible 4s–10s Clips & 360p -> 720p Upscale",
            "body": "Generate 4s, 6s, 8s, or 10s clips in 16:9 or 9:16. Prototype in Omni 360p at half the credit cost, then click Upscale to 720p for 0 credits on your winning takes.",
            "link_label": "Open Google Flow ↗",
            "link_url": FLOW_URL,
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "3. Start/End Frames & Save Frame Chaining",
            "body": "Attach + Add start frame and + Add end frame for exact motion transitions, or pause any clip and click Save frame to chain the next shot seamlessly.",
            "link_label": "Step 4 Video Labs ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "4. 3-Turn Conversational Video Editing",
            "body": "Click Edit Video on any Omni Flash clip (up to 10s) to change camera angles, relight to golden hour, or add brand titles across up to 3 conversational turns.",
            "link_label": "Step 5 Edit Labs ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "All video generation, dialogue lip-sync, ambient SFX, and conversational edits in this workshop run on Omni Flash!",
        f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Summarize the four capabilities of Gemini Omni Flash inside Google Flow that power Part II.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Everything in Part II runs on Gemini Omni Flash inside Google Flow: native @Character, @Ingredient, and @Voice references, 4-to-10-second clips with free 360p-to-720p upscaling, Start and End Frame interpolation, and up to 3 turns of conversational video editing.\"\n\n"
            "[TRANSITION]\n"
            "Let's create our Part II project and start Step 1: our 2-sentence story seed."
        ),
    })

    # =========================================================================
    # SLIDE 06: Step 1 — Start With a 2-Sentence Story & 5-Shot Beat Sheet
    # =========================================================================
    sid = "SLIDE_06"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 1 of 5: Short Story Seed & Beat Sheet",
        "Step 1: Start With a 2-Sentence Story & 5-Shot Beat Sheet",
        "Use the built-in Google Flow Agent to turn a 2-sentence story into a 5-shot commercial plan.",
        6,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "psychology",
            "accent": ACCENT_AMBER,
            "title": "The 2-Sentence Story Seed ('Solis — The 6AM Spark')",
            "body": "\"At 5:45 AM on a rainy morning, exhausted architect Maya stares at a blank blueprint in her cold studio until she walks into a warm cafe where barista Leo slides her a steaming terracotta cup of Solis coffee. One sip sparks her creativity.\"",
        },
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "The 5-Shot Commercial Beat Sheet (30s Total)",
            "body": "• Shot 1 (6s): @Maya stuck at desk in cold @Studio (7000K)\n• Shot 2 (6s): @Maya enters warm @Cafe out of the rain\n• Shot 3 (6s): @Leo pours & slides @SolisCup across counter\n• Shot 4 (6s): @Leo speaks -> Shot 5 (6s): @Maya sips & replies",
        },
        {
            "accent": ACCENT_AMBER,
            "title": "Copy-Paste Prompt 1.1 — Run in the Google Flow Agent Panel",
            "link_label": "Copy Prompt 1.1 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "We are creating a 30-second commercial in Google Flow for 'Solis Artisan Coffee' titled 'The 6:00 AM Spark.'\n"
                "Story Seed: At 5:45 AM on a rainy morning, exhausted architect Maya stares at a blank blueprint in her cold studio until she walks\n"
                "into a warm neighborhood cafe where barista Leo slides her a steaming terracotta cup of Solis coffee. One sip sparks her creativity.\n"
                "Break this story into a concise 5-shot beat sheet listing: Shot #, Setting (@Studio/@Cafe), Characters (@Maya/@Leo), Action & Lighting."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Step 1 Deliverable: A clear 5-shot beat sheet where emotional change is visually driven by Cold Blue -> Warm Gold.",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to start a project in Google Flow using a 2-sentence story seed and the Google Flow Agent.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Create a new project in Google Flow called 'Solis - The 6AM Spark' and open the Google Flow Agent panel. Paste Prompt 1.1 to turn our 2-sentence story seed into a 5-shot beat sheet. Notice how the emotional arc is carried by our color temperature shift from 7000K cold blue rain to 2400K golden sunrise.\"\n\n"
            "[TRANSITION]\n"
            "Now comes the most important step in Google Flow: creating @Maya and @Leo properly in Step 2A."
        ),
    })

    # =========================================================================
    # SLIDE 07: Step 2A — Create Characters Once (@Maya & @Leo)
    # =========================================================================
    sid = "SLIDE_07"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 2A of 5: Google Flow Characters (@Maya & @Leo)",
        "Step 2A: Create Characters Once in Characters > New Character",
        "Lock each character's visual appearance, name, and voice ONCE—never re-describe their appearance again!",
        7,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "1. Open Characters\n> New Character",
            "body": "• In the left sidebar of Google Flow, click Characters -> New Character.\n• Enter the detailed physical description ONE time under neutral 5600K studio light and click Generate.",
            "link_label": "Official Flow Docs ↗",
            "link_url": "https://support.google.com/flow/answer/16935308#flowcharacters",
        },
        {
            "icon": "psychology",
            "accent": ACCENT_PURPLE,
            "title": "2. Name & Attach\nCharacter Voice",
            "body": "• Name your characters 'Maya' and 'Leo'.\n• Click Select a voice -> pick Warm Alto for Maya & Warm Baritone for Leo -> click Add to Character -> Done.",
            "link_label": "Step 2A Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "3. Refer ONLY by\n@Maya and @Leo",
            "body": "• In every storyboard and video prompt from now on, simply type @Maya or @Leo!\n• Example: '@Maya drinks coffee and smiles.'\n• Flow keeps her face, glasses, cardigan & voice!",
            "link_label": "See Side-by-Side ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Google Flow Character Rule: Describe once in 'New Character' -> Reference everywhere else using only '@Maya' & '@Leo'!",
        f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the official Google Flow Characters workflow (Left Sidebar -> Characters -> New Character -> Name + Voice -> Done).\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Let's make sure everyone uses Google Flow Characters the right way. Click 'Characters' in the left sidebar, then 'New Character'. Paste Maya's physical description ONCE, name her 'Maya', attach her Warm Alto voice, and click Done. Do the same for 'Leo'. Once they are saved, you NEVER paste their physical descriptions again!\"\n\n"
            "[TRANSITION]\n"
            "Let's look at the side-by-side comparison on Slide 08 and run the character creation prompts."
        ),
    })

    # =========================================================================
    # SLIDE 08: Live Lab — Creating @Maya & @Leo vs. The "Re-Generation" Mistake
    # =========================================================================
    sid = "SLIDE_08"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Step 2A Hands-On Lab · Right vs. Wrong Character Prompting in Flow",
        "Live Lab: Creating @Maya Once vs. The 'Re-Generation' Mistake",
        "Once @Maya and @Leo are created, your scene prompts should only describe their actions—never their faces!",
        8,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "warning",
            "accent": ACCENT_RED,
            "title": "❌ WRONG: Re-Describing Maya in Scene Prompts",
            "body": "\"A 29-year-old Latina architect with olive skin, freckles, raven hair in a clip, tortoiseshell glasses, and an ochre cardigan drinks coffee...\"\n-> Forces Google Flow to re-generate a DIFFERENT woman every shot!",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "✅ RIGHT: Referencing @Maya in Scene Prompts",
            "body": "1. Create Maya once in Characters > New Character.\n2. In Shots 1–5, only type:\n\"@Maya drinks coffee from @SolisCup, inhales the warm steam, and smiles.\"\n-> 100% locked face, glasses, cardigan, and voice!",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "One-Time Creation Prompts (Run ONCE in Left Sidebar > Characters > New Character)",
            "link_label": "Copy @Maya & @Leo ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[CREATE @Maya ONCE (Voice: Warm Alto)]: 29-year-old Latina architect with warm olive skin, subtle freckles across the nose,\n"
                "wavy raven hair pinned in a low clip, round tortoiseshell eyeglasses, mustard-ochre ribbed knit cardigan over white crew-neck tee.\n"
                "[CREATE @Leo ONCE (Voice: Warm Baritone)]: 42-year-old artisan barista with medium-brown skin, silver-flecked short curly hair,\n"
                "neatly trimmed beard, warm smile lines, wearing a washed indigo denim apron over a charcoal henley with rolled sleeves."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Lab Check: Confirm both '@Maya' and '@Leo' appear in your Characters tab with their Voices attached before moving on!",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Contrast the wrong way (re-describing characters in scene prompts) against the right way (creating @Maya once and prompting '@Maya drinks coffee').\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Look at the two cards at the top. On the left is what NOT to do: repeating '29-year-old Latina architect with olive skin and glasses' in your scene prompts re-generates a new person. On the right is how Google Flow works: create @Maya once using the bottom box, and then just type '@Maya drinks coffee from @SolisCup and smiles.'\"\n\n"
            "[TRANSITION]\n"
            "Now let's create our three empty scene and product Ingredients in Step 2B."
        ),
    })

    # =========================================================================
    # SLIDE 09: Step 2B — Create Reusable Scene & Product Ingredients
    # =========================================================================
    sid = "SLIDE_09"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 2B of 5: Scene & Prop Ingredients (@Studio, @Cafe, @SolisCup)",
        "Step 2B: Create Reusable Scene & Product Ingredients",
        "Generate empty architectural sets and your hero product prop in Image > Nano Banana Pro so you can tag them with @.",
        9,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "cloud",
            "accent": ACCENT_BLUE,
            "title": "Empty Sets: @Studio (7000K) & @Cafe (2700K)",
            "body": "• Generate both sets with 'no people' so the background geometry stays consistent across cuts.\n• @Studio: Cold 7000K rain-streaked loft.\n• @Cafe: Warm 2700K oak counter & brass espresso machine.",
        },
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "Hero Product Prop: @SolisCup",
            "body": "• Handcrafted matte terracotta cappuccino cup with a cream interior and embossed 'SOLIS' wordmark.\n• Saving it as @SolisCup keeps the cup identical when @Leo pours and @Maya drinks!",
        },
        {
            "accent": ACCENT_CYAN,
            "title": "Copy-Paste Ingredient Prompts — Run in Image > Nano Banana Pro (16:9)",
            "link_label": "Copy Set Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[@Studio]: Empty architectural studio loft at 5:45 AM, rain-streaked glass window overlooking misty city skyline, birchwood drafting\n"
                "table with blank white blueprint roll, brass desk lamp turned off, cold 7000K slate-blue lighting, 24mm lens, no people.\n"
                "[@Cafe]: Empty neighborhood artisan coffee shop at 6:00 AM, reclaimed oak counter, gleaming vintage brass espresso machine, warm\n"
                "2700K Edison pendant bulbs against exposed brick, 35mm lens, no people.  [@SolisCup]: Matte terracotta cup embossed with 'SOLIS'."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "You now have 5 reusable Google Flow building blocks: @Maya, @Leo, @Studio, @Cafe, and @SolisCup!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Generate the three environment and prop Ingredients (@Studio, @Cafe, @SolisCup) in Google Flow using Nano Banana Pro.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Next, switch the prompt bar to Image -> Nano Banana Pro and generate our three non-character Ingredients: @Studio, @Cafe, and @SolisCup. Generating empty sets with 'no people' gives us rock-solid background plates that we can combine with @Maya and @Leo in Step 3.\"\n\n"
            "[TRANSITION]\n"
            "Now let's combine our @Characters and @Ingredients into 5 storyboard frames in Step 3."
        ),
    })

    # =========================================================================
    # SLIDE 10: Step 3 — Build Storyboard Frames Using @Maya, @Leo & @Cafe
    # =========================================================================
    sid = "SLIDE_10"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 3 of 5: Storyboard Frames (Image > Nano Banana Pro)",
        "Step 3: Build Storyboard Frames Using @Maya, @Leo & @Cafe",
        "Combine your saved @ assets into 5 storyboard stills—including a Start & End Frame pair for Shot 3!",
        10,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Short, Clean Prompts Using @ References",
            "body": "• Type @ in the prompt box (or drag tiles from your asset grid) to combine @Maya + @Studio or @Leo + @Cafe + @SolisCup.\n• Validate framing and lighting on fast images before spending video credits.",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Start + End Frame Pair for Shot 3 (Frames 3.3 & 3.4)",
            "body": "• Frame 3.3 (Start): @Leo pouring espresso into @SolisCup.\n• Frame 3.4 (End): @Leo's hand sliding @SolisCup across the counter in front of @Maya.\n• Ready for Omni Flash Frames interpolation!",
        },
        {
            "accent": ACCENT_PURPLE,
            "title": "Copy-Paste Storyboard Prompts 3.1 – 3.5 (Image > Nano Banana Pro, 16:9)",
            "link_label": "Copy Step 3 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[Frame 3.1]: @Maya sitting at the drafting desk inside @Studio at 5:45 AM, staring tiredly at the blank white blueprint, 35mm lens.\n"
                "[Frame 3.2]: @Maya stepping inside @Cafe out of the morning rain, looking toward the warm glowing espresso counter, 35mm lens.\n"
                "[Frame 3.3 Start]: @Leo standing behind the oak counter in @Cafe, pulling a fresh espresso shot into @SolisCup, 50mm lens.\n"
                "[Frame 3.4 End]: Close-up on the oak counter in @Cafe as @Leo's hand finishes sliding the steaming @SolisCup in front of @Maya."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Notice how clean Step 3 is: zero physical descriptions—just @Maya, @Leo, @Studio, @Cafe, and @SolisCup!",
        f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Generate the 5 storyboard frames in Nano Banana Pro using only @Character and @Ingredient tags.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Look at the storyboard prompts at the bottom of Slide 10. Every single prompt is one crisp sentence using @Maya, @Leo, @Studio, @Cafe, and @SolisCup! We also generate Frame 3.3 and Frame 3.4 as a Start and End Frame pair for Shot 3.\"\n\n"
            "[TRANSITION]\n"
            "With our storyboard locked, let's switch to Video -> Omni Flash in Step 4 to animate Shots 1, 2, and 3."
        ),
    })

    # =========================================================================
    # SLIDE 11: Step 4 — Animate Shots in Google Flow (Video > Omni Flash)
    # =========================================================================
    sid = "SLIDE_11"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 4A of 5: Animating Shots 1–3 (Video > Omni Flash)",
        "Step 4A: Animate Shots in Google Flow (Video > Omni Flash)",
        "Use @Character + @Ingredient references for Shots 1–2, and + Add start/end frame for Shot 3.",
        11,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_CYAN,
            "title": "Clips 4.1 & 4.2: Ingredients Mode (@Maya + Set)",
            "body": "• Select Video > Omni Flash (6s, Omni 360p draft).\n• Reference @Maya + @Studio for Shot 1 and @Maya + @Cafe for Shot 2 (or attach Frame 3.1 / 3.2 as + Add start frame).",
        },
        {
            "icon": "hub",
            "accent": ACCENT_AMBER,
            "title": "Clip 4.3: Frames Mode (Start Frame -> End Frame)",
            "body": "• Click + Add start frame (Frame 3.3) and + Add end frame (Frame 3.4).\n• Omni Flash smoothly interpolates @Leo pouring espresso and sliding @SolisCup to @Maya!",
        },
        {
            "accent": ACCENT_CYAN,
            "title": "Copy-Paste Video Prompts 4.1 – 4.3 (Video > Omni Flash, 6s)",
            "link_label": "Copy Step 4A Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[Clip 4.1 - Shot 1]: Slow push-in medium shot of @Maya sitting at the drafting table in @Studio, rubbing her temple and tapping\n"
                "her charcoal pencil against the blank white blueprint while rain patters softly against the cold blue window glass.\n"
                "[Clip 4.2 - Shot 2]: Smooth tracking shot following @Maya as she walks into @Cafe, walking up to the warm sunlit espresso bar.\n"
                "[Clip 4.3 - Shot 3 (Start 3.3 + End 3.4)]: Smooth tilt as @Leo finishes pouring into @SolisCup and slides it across @Cafe to @Maya."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Pro Tip: Pause any clip on its final frame and click 'Save frame' to use it as the '+ Add start frame' for your next shot!",
        f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Demonstrate animating Shots 1, 2, and 3 in Google Flow using Gemini Omni Flash Ingredients mode and Start/End Frames mode.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Switch the prompt box to Video -> Omni Flash. For Shots 1 and 2, we simply tag @Maya with @Studio and @Cafe. For Shot 3, we attach Frame 3.3 as our Start Frame and Frame 3.4 as our End Frame so Omni Flash connects Leo's pour directly into sliding @SolisCup across the oak counter.\"\n\n"
            "[TRANSITION]\n"
            "Now let's animate Shots 4 and 5 with spoken two-character dialogue in Step 4B."
        ),
    })

    # =========================================================================
    # SLIDE 12: Step 4B — Directing Two-Character Dialogue (@Leo & @Maya)
    # =========================================================================
    sid = "SLIDE_12"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 4B of 5: Spoken Dialogue & The 180° Eyeline Rule",
        "Step 4B: Directing Two-Character Dialogue (@Leo & @Maya)",
        "Omni Flash uses @Leo and @Maya's bundled voices while the 180° rule makes them look at each other.",
        12,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Clip 4.4 — Shot 4: @Leo Speaks (Looking Left)",
            "body": "• Over-the-shoulder from behind @Maya on the left, focusing on @Leo on the right looking screen-left.\n• @Leo speaks in his bundled Warm Baritone voice:\n\"Rough night with the blueprints? Start with this.\"",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "Clip 4.5 — Shot 5: @Maya Drinks Coffee & Replies",
            "body": "• Reverse-angle medium close-up of @Maya on the left looking screen-right.\n• @Maya drinks coffee from @SolisCup, smiles, and replies in her bundled Warm Alto voice!",
        },
        {
            "accent": ACCENT_GREEN,
            "title": "Copy-Paste Dialogue Prompts 4.4 & 4.5 (Video > Omni Flash, 6s)",
            "link_label": "Copy Step 4B Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[Clip 4.4 - Shot 4]: Over-the-shoulder medium shot from behind @Maya on the left, focusing on @Leo on the right looking\n"
                "screen-left across the counter in @Cafe with a warm smile. @Leo says: \"Rough night with the blueprints? Start with this.\"\n"
                "[Clip 4.5 - Shot 5]: Reverse-angle medium close-up of @Maya on the left looking screen-right in @Cafe. @Maya drinks coffee\n"
                "from @SolisCup, lowers the cup with a warm inspired smile, and says: \"You just saved the whole skyline, Leo.\""
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Look at Clip 4.5: '@Maya drinks coffee from @SolisCup... and says: ...' — zero character re-generation!",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach how to direct a natural two-character conversation in Omni Flash using @Leo and @Maya's bundled voices and the 180-degree eyeline rule.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Look at how simple and powerful Clips 4.4 and 4.5 are. In Clip 4.4, @Leo looks screen-left and speaks in his saved baritone voice. In Clip 4.5, we literally write: '@Maya drinks coffee from @SolisCup, lowers the cup with a warm inspired smile, and says: You just saved the whole skyline, Leo.' Because @Maya is a saved Flow Character, her face, outfit, and alto voice stay 100% consistent!\"\n\n"
            "[TRANSITION]\n"
            "Finally, let's move to Step 5 to polish Clip 4.5 with Omni conversational editing and assemble our cut in Scenebuilder."
        ),
    })

    # =========================================================================
    # SLIDE 13: Step 5 — Omni Conversational Video Editing & Scenebuilder
    # =========================================================================
    sid = "SLIDE_13"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Part II · Step 5 of 5: Conversational Video Edit & Final Assembly",
        "Step 5: Omni Conversational Video Editing & Scenebuilder",
        "Refine Clip 4.5 across 2 conversational turns in Omni Flash, then assemble & export in Scenebuilder.",
        13,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "psychology",
            "accent": ACCENT_BLUE,
            "title": "Omni Conversational Video Edit (Up to 3 Turns)",
            "body": "• Click Clip 4.5 -> Edit Video.\n• Turn 1: Intensify the warm 2400K golden sunrise beams.\n• Turn 2: Fade in gold serif text 'SOLIS — AWAKEN THE CRAFT' in the rising steam—without losing @Maya's performance!",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "Assemble & Export in Google Flow Scenebuilder",
            "body": "• Hover over Clips 4.1–4.5 -> More (⋮) -> Add to Scene.\n• Open Scenebuilder to order Shots 1–5 and trim dialogue handles.\n• Click Upscale to 720p (0 credits) on all clips and Download!",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "Copy-Paste Conversational Edit Prompts 5.1 & 5.2 (Omni Flash Video Edit)",
            "link_label": "Copy Step 5 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
            "code": (
                "[Edit 5.1 - Turn 1 (Relight Clip 4.5)]: Intensify the warm 2400K golden sunrise beams streaming through the window behind\n"
                "@Maya and make the rising coffee steam from @SolisCup glow softly in the backlight.\n"
                "[Edit 5.2 - Turn 2 (Brand Title Overlay)]: In the final 2 seconds as the steam rises, fade in clean minimalist gold serif text\n"
                "in the upper center reading 'SOLIS — AWAKEN THE CRAFT'."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "All previous versions of edited clips remain safe in your Google Flow 'History' panel!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to apply multi-turn conversational video edits in Gemini Omni Flash and assemble the final 30-second commercial in Scenebuilder.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Step 5, instead of re-generating Shot 5 from scratch, click Edit Video on Clip 4.5. In Turn 1, we intensify the 2400K golden sunrise backlight. In Turn 2, we fade in 'SOLIS — AWAKEN THE CRAFT' as the steam rises. Then add all 5 clips to Scenebuilder, trim the handles, upscale to 720p for 0 credits, and download your commercial!\"\n\n"
            "[TRANSITION]\n"
            "Let's wrap up on Slide 14 with our 5 Google Flow Golden Rules and GitHub repository links."
        ),
    })

    # =========================================================================
    # SLIDE 14: Workshop Recap, Golden Rules & GitHub Repository
    # =========================================================================
    sid = "SLIDE_14"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Workshop Wrap-Up · Golden Rules & Resources",
        "Recap: The 5 Golden Rules of Google Flow & Gemini Omni",
        "Everything we built today—plus 2 bonus commercial packs—is ready to clone in the GitHub repository.",
        14,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Rules 1 & 2:\n@Characters & Sets",
            "body": "1. Create @Maya & @Leo ONCE in Characters > New Character (with Voice).\n2. Never re-describe them—only type '@Maya drinks coffee' in @Studio or @Cafe!",
            "link_label": "Flow Cheat Sheet ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/03-google-flow-cheatsheet.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Rules 3 & 4:\nFrames & Omni Edit",
            "body": "3. Prototype in Omni 360p, use Start/End Frames & Save Frame, and upscale to 720p for 0 credits.\n4. Use 3-turn Video Editing instead of re-rolling good acting!",
            "link_label": "Solis Prompt Library ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "code",
            "accent": ACCENT_GREEN,
            "title": "Rule 5: Explore the\nGitHub Repository",
            "body": "• Part I Sandbox (Labs A–D)\n• Part II Solis Coffee Prompts\n• Bonus: NovaPay & Kuntur\n• Interactive Web Companion\n• 14-Slide Deck & PDF",
            "link_label": "Open GitHub Repo ↗",
            "link_url": GITHUB_REPO,
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Star & Clone the Workshop Repo: https://github.com/AllInVaders/google-flow-storytelling-workshop",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Summarize the 5 Golden Rules of Google Flow & Gemini Omni Flash and share the GitHub repository.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"To recap our 5 Golden Rules: (1) Test isolated levers in the Sandbox first; (2) Create @Maya and @Leo once in the Characters tab and only refer to them by @Name thereafter; (3) Lock empty sets as @Ingredients; (4) Use Omni 360p drafts, Start/End Frames, and free 720p upscaling; and (5) Use 3-turn conversational video editing and Scenebuilder to finish your film. All prompts are live on GitHub!\"\n\n"
            "[TRANSITION]\n"
            "Thank you, and happy filmmaking in Google Flow!"
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
            "Google Flow & Gemini Omni: Incremental Storytelling Workshop",
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

    print(f"2. Executing batch update ({len(ops)} operations across 14 slides)...")
    batch_cmd = [GSLIDES, "mutate", "batch", pres_id, "-f", batch_file, "--json"]
    subprocess.run(batch_cmd, capture_output=True, text=True, check=True)
    print("Batch completed successfully!")
    print(f"PRESENTATION_URL=https://docs.google.com/presentation/d/{pres_id}/edit")

    with open("/tmp/flow_workshop_pres_id.txt", "w", encoding="utf-8") as f:
        f.write(pres_id)


if __name__ == "__main__":
    main()

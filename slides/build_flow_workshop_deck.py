#!/usr/bin/env python3
"""Builds the 16-Slide Native Editable Google Slides Deck for the Google Flow & GenMedia Storytelling Workshop.

Features:
- Clean dark-mode executive cards (5-Card Pipeline, 3-Card Columns, 2x2 Grid, Split Prompt Preview)
- Single-word classic Material Icons (`bolt`, `hub`, `code`, `check`, `warning`, `security`, `key`, `cloud`, `lock`, `psychology`, `star`)
- Clickable link pills pointing to `https://github.com/AllInVaders/google-flow-storytelling-workshop` and `https://labs.google/fx/tools/flow`
- Tripartite speaker notes (`[PURPOSE]`, `[VERBAL SCRIPT]`, `[TRANSITION]`) + copy-paste prompts on 100% of slides
"""

import json
import re
import subprocess

GSLIDES = "/google/bin/releases/gemini-agents-gslides/gslides"
GITHUB_REPO = "https://github.com/AllInVaders/google-flow-storytelling-workshop"
GITHUB_BLOB = "https://github.com/AllInVaders/google-flow-storytelling-workshop/blob/main"
FLOW_URL = "https://labs.google/fx/tools/flow"
AISTUDIO_URL = "https://aistudio.google.com"

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


def add_header(ops, sid, category, title, subtitle, slide_num, total_slides=16):
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
        "font_size": 15.5,
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
        "font_size": 9.8,
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
            "font_size": 10.2,
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


def build_all_slides():
    ops = [
        {"op": "delete-element", "element": "i0"},
        {"op": "delete-element", "element": "i1"},
    ]

    # =========================================================================
    # SLIDE 01: Hero Cover & Incremental Layer-Cake Roadmap (`p`)
    # =========================================================================
    sid = "p"
    add_header(
        ops,
        sid,
        "Google Flow & GenMedia · Hands-On Storytelling Workshop",
        "Incremental AI Filmmaking: From a 2-Sentence Story to a 30s Commercial",
        "Start with a tiny narrative seed and pile on Character Face Lock, Empty Sets, Storyboards, Motion, Dialogue & Scenebuilder.",
        1,
    )
    add_five_pipeline(ops, sid, [
        {
            "icon": "psychology",
            "accent": ACCENT_AMBER,
            "title": "00 · Story Seed",
            "body": "• 2-Sentence Logline\n• 3-Act Micro-Arc\n• 2 Characters Max\n• 2 Locations + 1 Prop\n• Cold -> Warm Shift",
            "link_label": "Stage 0 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "01 · Face Lock",
            "body": "• 35-Word Anchor Block\n• Neutral 5600K Portrait\n• 4-Angle Turnaround\n• Character Ingredients\n• Zero Identity Drift",
            "link_label": "Stage 1 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "02–03 · Set & Board",
            "body": "• Empty Location Plates\n• Hero Product Macro\n• 6-Shot Storyboard\n• Start/End Frame Pairs\n• Continuity Bridges",
            "link_label": "Stage 2-3 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_CYAN,
            "title": "04 · Camera & Motion",
            "body": "• Ingredients to Video\n• Frames to Video\n• 7-Part Prompt Formula\n• Anamorphic & Macro\n• Veo 3.1 Physics",
            "link_label": "Stage 4 Lab ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "05–06 · Talk & Edit",
            "body": "• 180° Eyeline Rule\n• Shot-Reverse-Shot\n• Native Lip-Sync + TTS\n• Scenebuilder Extend\n• Jump To & J/L Cuts",
            "link_label": "Prompt Library ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Full Workshop Repo, Facilitator Script & Copy-Paste Prompts: https://github.com/AllInVaders/google-flow-storytelling-workshop",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Introduce the 7-Stage Incremental Story Layer-Cake (Snowball) methodology for Google Flow and cross-platform GenMedia.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Welcome to the Google Flow and GenMedia Storytelling Workshop. Today we are going to build a 30-second commercial called 'Solis — The 6:00 AM Spark.' Instead of typing one giant prompt and hoping for the best, we will start with a two-sentence story seed and incrementally pile on characters, face consistency, location plates, storyboards, camera motion, two-person dialogue, and timeline assembly.\"\n\n"
            "[TRANSITION]\n"
            "Let's first understand why single-prompt video generation breaks down and how our incremental workflow solves it."
        ),
    })

    # =========================================================================
    # SLIDE 02: Why "One Giant Prompt" Fails vs. The Incremental Layer-Cake
    # =========================================================================
    sid = "SLIDE_02"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Core Methodology · Why Incremental Layering Wins",
        "Why Single-Prompt Video Fails vs. The Layer-Cake Production Pipeline",
        "Separating story, character identity, empty sets, and camera physics eliminates character drift across every platform.",
        2,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "warning",
            "accent": ACCENT_RED,
            "title": "The 'One Giant Prompt' Trap (Point A)",
            "body": "• Typing 'Make a 30s coffee commercial' into a single prompt box.\n• Protagonist's face, glasses, and jacket mutate in every clip.\n• Background room geometry and product logos hallucinate.\n• Two speaking characters look away from each other.",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "The Incremental Layer-Cake Method (Point B)",
            "body": "• Lock 2-sentence story -> Lock faces -> Lock empty sets -> Storyboard.\n• Combine up to 3 pinned Ingredients per shot in Google Flow.\n• Use Start/End Frames for deterministic product transitions.\n• Direct 2-character conversations using the 180-Degree Rule.",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "Incremental Layering Equation (Google Flow + Any GenMedia Platform)",
            "link_label": "Facilitator Playbook ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
            "code": (
                "Layer 0 (Story Seed)        -> 2 sentences + 3-Act lighting contrast (Cold Cyan -> Warm Amber -> Sunrise)\n"
                "Layer 1 (Identity Lock)     -> 35-word verbatim Identity Anchor Block + Neutral 5600K Portrait / 4-Angle Sheet\n"
                "Layer 2 (Stage & Prop)      -> Empty Location Plates ([SCENE_STUDIO], [SCENE_CAFE]) + Hero Product ([PROP_CUP])\n"
                "Layer 3 (Visual Storyboard) -> 6 Composited Keyframes (Start & End Frame pairs before rendering video)\n"
                "Layer 4-6 (Motion + Audio)  -> Ingredients-to-Video + Frames-to-Video + 180° Shot-Reverse-Shot Dialogue + Scenebuilder"
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Rule #1 of AI Filmmaking: Never invent your character, your room, and your camera move for the first time in the same video prompt.",
        f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Contrast the common beginner mistake (single monolithic prompt) against the modular film-set workflow used in Google Flow.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"When most creators open a video model, they try to describe the story, the actor's face, the coffee shop, and the camera movement all at once. In the next shot, the actor's face drifts and the coffee shop looks completely different. By separating our production into incremental layers—just like a real film set—we lock the actors and sets first, then animate.\"\n\n"
            "[TRANSITION]\n"
            "Let's look at how these layers map directly to the Google Flow workspace and to other GenMedia platforms."
        ),
    })

    # =========================================================================
    # SLIDE 03: Google Flow Workspace & Cross-Platform Architecture
    # =========================================================================
    sid = "SLIDE_03"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Platform Architecture · Write Once, Execute Anywhere",
        "Mapping the Workshop to Google Flow & Universal GenMedia Platforms",
        "Every workshop exercise runs natively in Google Flow while mapping 1:1 to Vertex AI, AI Studio, Runway, Luma, and Midjourney.",
        3,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "lock",
            "accent": ACCENT_AMBER,
            "title": "1. Ingredients Panel\n(Asset & Identity Vault)",
            "body": "• Google Flow: Create or upload Character, Scene, and Object Ingredients (Nano Banana Pro / Imagen).\n• Cross-Platform: Generate a 4-Angle Character Turnaround Sheet + Empty Location Plates as reference images.",
            "link_label": "Open Google Flow ↗",
            "link_url": FLOW_URL,
        },
        {
            "icon": "bolt",
            "accent": ACCENT_BLUE,
            "title": "2. Dual Video Engines\n(Ingredients vs. Frames)",
            "body": "• Ingredients to Video: Blend up to 3 references (Character + Set + Prop) with Veo 3.1 camera prompts.\n• Frames to Video: Lock exact First Frame + Last Frame to interpolate smooth macro transitions.",
            "link_label": "Google AI Studio ↗",
            "link_url": AISTUDIO_URL,
        },
        {
            "icon": "hub",
            "accent": ACCENT_GREEN,
            "title": "3. Scenebuilder Timeline\n(Extend, Jump To & Audio)",
            "body": "• Extend: Lengthen a clip seamlessly from its final frames.\n• Jump To: Bridge a character into a new scene/angle.\n• Audio: Veo 3.1 native lip-sync + Gemini 3.8 Flash TTS + Lyria 3 score.",
            "link_label": "Cross-Platform Matrix ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Model Stack: gemini-3.8-flash (Story) · gemini-3-pro-image (Nano Banana Pro) · veo-3.1 · gemini-3.8-flash-tts · lyria-3",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Orient participants to the three core workspaces in Google Flow (Ingredients, Video Generation Modes, Scenebuilder) and their cross-platform equivalents.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Google Flow gives us three superpowers in one browser tab: the Ingredients Panel to pin our characters, sets, and products; two video generation modes—Ingredients to Video and Frames to Video powered by Veo 3.1; and Scenebuilder to extend and sequence clips. And if you run this in Vertex AI, AI Studio, or Runway, the exact same reference images and prompts work seamlessly.\"\n\n"
            "[TRANSITION]\n"
            "Let's begin hands-on with Stage 0: writing our two-sentence micro-story seed."
        ),
    })

    # =========================================================================
    # SLIDE 04: Stage 0 — The 2-Sentence Micro-Story Seed
    # =========================================================================
    sid = "SLIDE_04"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 0 · Incremental Layer 1 of 7: Narrative Foundation",
        "Start with a 2-Sentence Story Seed & Expand to a 3-Act Micro-Arc",
        "Constrain the commercial to 30 seconds, 2 characters, 2 contrasting locations, and 1 hero prop before generating visuals.",
        4,
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
            "title": "3-Act Visual & Lighting Arc (30 Seconds)",
            "body": "• Act I (0–8s): Cold Cyan Rain — Maya stuck at her studio desk.\n• Act II (8–22s): Warm Amber Glow — Leo slides the Solis cup across the counter; a 2-line conversation.\n• Act III (22–30s): Golden Sunrise — Maya sketches the bridge arch.",
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
        "Color & Mood Arc: Cold Cyan Pre-Dawn Rain (Problem) -> Warm Amber Edison Café (Connection) -> Golden Sunrise (Transformation).",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Demonstrate how a 2-sentence story seed is expanded into a constrained 3-act commercial beat sheet.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Every great commercial is built on a clear contrast. Our story seed is just two sentences: Maya is an architect stuck on a blank blueprint at 5:45 AM in the cold rain; she steps into Leo's glowing corner café, shares a laugh over a terracotta cup of Solis espresso, and returns at sunrise to draw her bridge. Notice how we constrain the world to two characters, two locations, and one prop.\"\n\n"
            "[TRANSITION]\n"
            "Now that we know who Maya and Leo are, how do we make sure their faces look identical in every shot? Welcome to Stage 1."
        ),
    })

    # =========================================================================
    # SLIDE 05: Stage 1 — Character Generation & The Face Consistency Formula
    # =========================================================================
    sid = "SLIDE_05"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 1 · Incremental Layer 2 of 7: Character & Face Consistency",
        "The 3-Pillar System for Zero Face Drift Across Shots & Platforms",
        "Combine a verbatim 35-word Identity Anchor Block, a neutral 5600K studio portrait, and a 4-Angle Turnaround Sheet.",
        5,
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
            "body": "• Prompt Nano Banana Pro (gemini-3-pro-image) for a 4-panel sheet in one 16:9 frame: Front, 45°, Profile, Smiling Close-Up.\n• Crop panels to feed angle-matched references on any platform!",
            "link_label": "Turnaround Prompt ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Pro Tip: Distinct accessories (round tortoiseshell glasses + ochre knit cardigan) act as high-weight visual anchors for video models.",
        f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the 3-pillar technique that guarantees facial and wardrobe consistency in Google Flow and external tools.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Why do faces drift in AI video? Because users rely on a single image reference with a vague text prompt, or they generate a reference portrait with heavy neon shadows that bleed into later shots. Our 3-pillar fix combines a verbatim 35-word Identity Anchor Block, a neutral 5600K studio portrait pinned in Google Flow's Ingredients Panel, and a 4-angle turnaround sheet for cross-platform angle matching.\"\n\n"
            "[TRANSITION]\n"
            "Let's copy and run the exact character prompts for Maya and Leo right now."
        ),
    })

    # =========================================================================
    # SLIDE 06: Live Lab #1 — Character & Face Consistency Prompts
    # =========================================================================
    sid = "SLIDE_06"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 1 Hands-On Lab · Character Ingredients (`[CHAR_MAYA]` & `[CHAR_LEO]`)",
        "Live Lab #1: Generating Locked Character Portraits & Turnaround Sheets",
        "Run these prompts in Google Flow's Ingredients Panel (or Nano Banana Pro / gemini-3-pro-image) and pin both characters.",
        6,
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
        "In Google Flow: Open 'Ingredients' -> Create Ingredient -> Generate Maya & Leo -> Pin both to your project asset library.",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the exact copy-paste prompts for generating Maya, Leo, and Maya's 4-panel turnaround sheet.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Copy Prompt 1.1 and 1.3 into Google Flow's Ingredients creator—or Prompt 1.2 into Gemini 3 Pro Image if you want the 4-angle sheet. Notice how specific the landmarks are: 'subtle freckles across the nose', 'wavy raven hair tied in a loose low clip', 'round tortoiseshell glasses', and 'oversized ochre knit cardigan.' Once generated, pin Maya and Leo to your Ingredients tray.\"\n\n"
            "[TRANSITION]\n"
            "Now that our two actors are cast and locked, we need to build the sets and the hero coffee cup in Stage 2."
        ),
    })

    # =========================================================================
    # SLIDE 07: Stage 2 — Scene & Product World Generation
    # =========================================================================
    sid = "SLIDE_07"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 2 · Incremental Layer 3 of 7: Environments & Hero Product",
        "Build the Stage Before Calling the Actors: Empty Plates & Product Lock",
        "Generate actor-free Location Ingredients and a macro Product Ingredient so room layouts and brand logos stay rock-solid.",
        7,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Scene Ingredient A\n`[SCENE_STUDIO]` (Act I)",
            "body": "• Minimalist architect's loft desk at 5:45 AM before dawn.\n• Tall rain-streaked industrial window + cool cyan-blue drafting lamp.\n• Explicitly prompt: 'Empty chair, no people' so the plate is clean.",
            "link_label": "Prompt 2.1 ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Scene Ingredient B\n`[SCENE_CAFE]` (Act II)",
            "body": "• Cozy wood-paneled artisan espresso bar at dawn.\n• Warm amber Edison bulbs, brass espresso machine, reclaimed oak counter.\n• Fogged rainy window in background for visual contrast.",
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
            "\"In Stage 2, we think like production designers. If you generate a coffee shop that already has a random person standing behind the counter, and then you try to insert Leo, the model gets confused. Always include 'Empty chair, no people' in your Scene Ingredients. And for our hero product, we use Nano Banana Pro to render the matte terracotta cup with the exact gold 'SOLIS' logo.\"\n\n"
            "[TRANSITION]\n"
            "Let's run the three Stage 2 prompts to populate our Ingredients tray with both sets and the hero cup."
        ),
    })

    # =========================================================================
    # SLIDE 08: Live Lab #2 — Scene & Product Ingredient Prompts
    # =========================================================================
    sid = "SLIDE_08"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 2 Hands-On Lab · Scene & Object Ingredients",
        "Live Lab #2: Generating `[SCENE_STUDIO]`, `[SCENE_CAFE]` & `[PROP_CUP]`",
        "Create and pin these 3 visual assets so your Ingredients library holds all 5 core building blocks of the commercial.",
        8,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Prompt 2.1 — Cold Rainy Studio (`[SCENE_STUDIO]`)",
            "body": "\"Wide establishing interior shot of a minimalist architect's loft desk by a tall rain-streaked industrial window at 5:45 AM before dawn. Empty chair, no people. A drafting lamp casts a cool cyan-blue pool of light over an unrolled blank blueprint and scale ruler. 35mm anamorphic lens.\"",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Prompt 2.2 — Warm Corner Café (`[SCENE_CAFE]`)",
            "body": "\"Medium-wide interior shot of a cozy, wood-paneled artisan espresso bar at dawn. Empty frame with no people. Warm amber Edison bulbs and a polished brass espresso machine gleam with gentle steam rising. Rain outside fogged window, reclaimed oak counter in foreground.\"",
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
        "Checkpoint: You now have 5 pinned Ingredients — [CHAR_MAYA], [CHAR_LEO], [SCENE_STUDIO], [SCENE_CAFE], and [PROP_CUP].",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Guide participants through generating the two empty location plates and the Solis terracotta cup ingredient.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Run Prompts 2.1, 2.2, and 2.3 now. Look at the visual contrast between Scene A (moody teal and cyan rain) and Scene B (warm amber Kodak 500T film glow). By pinning these three assets alongside Maya and Leo, we have all five ingredients needed to storyboard the entire commercial.\"\n\n"
            "[TRANSITION]\n"
            "Before we touch video generation, let's assemble our 6-shot visual storyboard in Stage 3."
        ),
    })

    # =========================================================================
    # SLIDE 09: Stage 3 — Visual Storyboarding & Continuity Bridges
    # =========================================================================
    sid = "SLIDE_09"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 3 · Incremental Layer 4 of 7: Visual Storyboarding",
        "The 6-Shot Commercial Storyboard & Ingredient Combination Matrix",
        "Lock framing, lighting transitions, and Start/End keyframe pairs in still images before spending video compute.",
        9,
    )
    add_grid_2x2(ops, sid, [
        {
            "icon": "cloud",
            "accent": ACCENT_CYAN,
            "title": "Shots 1 & 2 · Act I -> Act II Threshold (0–10s)",
            "body": "• Shot 1: [CHAR_MAYA] + [SCENE_STUDIO] — Medium close-up at 5:45 AM; cold cyan rain reflects on her glasses.\n• Shot 2: [CHAR_MAYA] + [SCENE_CAFE] — Tracking shot stepping out of blue rain into warm amber café glow.",
            "link_label": "Keyframes 3.1 & 3.2 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_AMBER,
            "title": "Shot 3 · Hero Product Start -> End Pair (10–15s)",
            "body": "• First Frame: Espresso pouring in dual streams into the matte terracotta SOLIS cup.\n• Last Frame: Leo's hand sliding the steaming SOLIS cup across the oak counter toward the camera.",
            "link_label": "Keyframe Pair 3.3 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_PURPLE,
            "title": "Shots 4 & 5 · Two-Character Conversation (15–25s)",
            "body": "• Shot 4 (OTS): [CHAR_LEO] on right looking screen-left over Maya's shoulder.\n• Shot 5 (Reverse): [CHAR_MAYA] on left looking screen-right, holding the SOLIS cup and smiling.",
            "link_label": "Keyframes 3.4 & 3.5 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_GREEN,
            "title": "Shot 6 · Act III Spark Reignited Finale (25–30s)",
            "body": "• First Frame: Golden sunrise hits the studio desk as Maya sets the SOLIS cup beside the blank blueprint.\n• Last Frame: High-angle over shoulder as her charcoal pencil sweeps a bold bridge arch.",
            "link_label": "Keyframe Pair 3.6 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Storyboarding Rule: Every shot combines at most 3 Ingredients (Character + Location + Prop) for maximum model adherence.",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Map out all 6 shots of the 30-second commercial and show which Ingredients combine in each shot.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Here is our complete 6-shot commercial storyboard. Notice how every single shot is just a combination of the 5 ingredients we already created: Shot 1 combines Maya and the Studio; Shot 2 combines Maya and the Café; Shot 3 combines Leo, the Café, and the Solis Cup using a First and Last Frame pair; Shots 4 and 5 are our Over-the-Shoulder conversation; and Shot 6 brings Maya and the Solis Cup back to the sunlit studio.\"\n\n"
            "[TRANSITION]\n"
            "Let's look at how to prompt composite storyboard keyframes and Start/End frame pairs."
        ),
    })

    # =========================================================================
    # SLIDE 10: Live Lab #3 — Storyboard Keyframe Compositing
    # =========================================================================
    sid = "SLIDE_10"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 3 Hands-On Lab · Compositing Keyframes & Start/End Pairs",
        "Live Lab #3: Generating Storyboard Stills Before Animating Video",
        "Combine Character + Scene references into still frames to verify composition and prepare First/Last frames for Veo 3.1.",
        10,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "lock",
            "accent": ACCENT_BLUE,
            "title": "Keyframe 3.1 — Shot 1 Start Still (Maya + Studio)",
            "body": "Attach [CHAR_MAYA] + [SCENE_STUDIO]: Maya sits at the rain-streaked architect's desk at 5:45 AM resting her chin on her hand, staring at the blank blueprint. Cool cyan window light reflects on her tortoiseshell glasses.",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Keyframe 3.3 — Shot 3 Start & End Frame Pair",
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
        "Why generate Start & End frames for Shot 3? Because 'Frames to Video' guarantees the SOLIS logo lands sharply in the final frame!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to composite reference ingredients into storyboard stills and Start/End frame pairs.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"When you want a hero product shot to end in a crystal-clear close-up with an exact brand logo, never leave the ending to chance. By generating both the First Frame (espresso pouring) and the Last Frame (Leo sliding the cup toward the lens) as still images first, Google Flow's Frames to Video mode will smoothly bridge the motion between them.\"\n\n"
            "[TRANSITION]\n"
            "Now let's move to Stage 4 and bring our storyboard to life with camera movement and Veo 3.1 physics."
        ),
    })

    # =========================================================================
    # SLIDE 11: Stage 4 — Animating with Ingredients-to-Video & Frames-to-Video
    # =========================================================================
    sid = "SLIDE_11"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 4 · Incremental Layer 5 of 7: Motion & Camera Directing",
        "Mastering 'Ingredients to Video', 'Frames to Video' & Camera Syntax",
        "Once visuals are anchored in references, dedicate your video prompt to camera movement, physical action, and sound.",
        11,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "Mode A · Ingredients\nto Video (Up to 3 Refs)",
            "body": "• Upload [CHAR_MAYA] + [SCENE_STUDIO] + [PROP_CUP].\n• Best for natural acting, subtle facial expressions, and continuous camera moves (Shots 1, 2, 4, 5).\n• Always include the 35-word Identity Anchor Block.",
            "link_label": "Open Google Flow ↗",
            "link_url": FLOW_URL,
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Mode B · Frames to\nVideo (First + Last)",
            "body": "• Upload First Frame + Last Frame.\n• Veo 3.1 interpolates camera travel, lighting shift, and fluid physics between the two keyframes.\n• Best for product reveals & match cuts (Shots 3 & 6).",
            "link_label": "Stage 4 Guide ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "code",
            "accent": ACCENT_PURPLE,
            "title": "The 7-Part Cinematic\nVideo Prompt Formula",
            "body": "1. Shot Size & Angle\n2. Camera Movement (dolly-in, tracking)\n3. Identity Anchor + Action\n4. Scene & Lighting\n5. Lens (35mm anamorphic)\n6. Dialogue in 'quotes'\n7. Audio / SFX cues",
            "link_label": "Prompt Formula ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Camera Vocabulary That Works Best in Veo 3.1: 'Slow smooth dolly-in', 'Lateral tracking shot', 'Over-the-shoulder', 'Macro push-in'.",
        f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Explain when to use Ingredients to Video vs. Frames to Video in Google Flow, and introduce the 7-part video prompt structure.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 4, we choose between Google Flow's two flagship video modes: use Ingredients to Video when you want open-ended acting with up to three reference assets, and use Frames to Video when you want an exact transition from a First Frame to a Last Frame. Follow the 7-part prompt formula so camera movement and physical action come first.\"\n\n"
            "[TRANSITION]\n"
            "Let's copy and run our video generation prompts for Shots 1, 2, and 3."
        ),
    })

    # =========================================================================
    # SLIDE 12: Live Lab #4 — Motion & Camera Directing Prompts (Shots 1–3)
    # =========================================================================
    sid = "SLIDE_12"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 4 Hands-On Lab · Animating Shots 1, 2 & 3 in Veo 3.1",
        "Live Lab #4: Running 'Ingredients to Video' & 'Frames to Video'",
        "Generate the opening creative block (Shot 1), the café entrance (Shot 2), and the macro espresso slide (Shot 3).",
        12,
    )
    add_split_case_study(
        ops,
        sid,
        {
            "icon": "hub",
            "accent": ACCENT_BLUE,
            "title": "Shot 1 Setup — Ingredients to Video (`Veo 3.1`)",
            "body": "• Attach Ingredients: [CHAR_MAYA] + [SCENE_STUDIO]\n• Camera: Slow, smooth dolly-in toward medium close-up.\n• Action: Maya exhales a quiet sigh, taps her wooden pencil twice on the blank blueprint, glances at the rain.",
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "Shot 3 Setup — Frames to Video (`First` -> `Last`)",
            "body": "• First Frame: Espresso pouring into SOLIS cup.\n• Last Frame: Leo's hand sliding SOLIS cup to foreground.\n• Camera: 100mm macro tracking shot, 60fps slow-motion feel with rising golden steam.",
        },
        {
            "accent": ACCENT_BLUE,
            "title": "Copy-Paste Prompt 4.1 — Shot 1 Video ('Ingredients to Video' with Native Audio)",
            "link_label": "Copy Shots 1–3 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "Slow, smooth dolly-in toward a medium close-up of Maya, a 29-year-old Latina architect with warm olive skin, subtle freckles,\n"
                "wavy raven hair in a low clip, round tortoiseshell glasses, and an ochre knit cardigan, sitting at her drafting table by a\n"
                "rain-streaked window at 5:45 AM. She exhales a quiet sigh, taps her wooden pencil twice against the blank blueprint, and\n"
                "glances out at the rain. Cold cyan streetlamp reflections glide across her glasses. 35mm anamorphic lens.\n"
                "Audio: Soft rhythmic rain pattering against window glass, distant thunder, two crisp wooden pencil taps, and a quiet sigh."
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Notice the 'Audio:' cue at the end: Veo 3.1 natively synthesizes synchronized rain, pencil taps, and espresso extraction SFX.",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the executable video prompts for Shots 1–3 demonstrating Ingredients-to-Video and Frames-to-Video.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Let's run Prompt 4.1 in Ingredients to Video with Maya and the Studio attached, and Prompt 4.3 in Frames to Video with our Shot 3 First and Last frames. Notice how adding a dedicated 'Audio:' line at the bottom tells Veo 3.1 to generate the exact foley sound effects—two wooden pencil taps on paper and rain against glass.\"\n\n"
            "[TRANSITION]\n"
            "Now we reach Stage 5: piling on spoken dialogue and directing a two-character conversation."
        ),
    })

    # =========================================================================
    # SLIDE 13: Stage 5 — Directing Two-Character Dialogue & The 180° Rule
    # =========================================================================
    sid = "SLIDE_13"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 5 · Incremental Layer 6 of 7: Dialogue, Conversation & Audio",
        "How to Direct Believable Two-Character Conversations in AI Video",
        "Combine the 180-Degree Eyeline Rule, single-quoted dialogue prompts, Gemini 3.8 Flash TTS, and Lyria 3 music.",
        13,
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
            "title": "2. Veo 3.1 Native Lip-Sync Dialogue Syntax",
            "body": "• Put spoken words in single quotes ('...') right after vocal tone:\n• \"Leo speaks in a warm, grounded baritone voice: 'Rough night with the blueprints?'\"\n• Keep dialogue to 8–12 words per 6–8s clip (~2 words/sec).",
            "link_label": "Dialogue Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "psychology",
            "accent": ACCENT_PURPLE,
            "title": "3. Expressive Voiceover (`gemini-3.8-flash-tts`)",
            "body": "• For narrator taglines or cross-platform dubbing, use gemini-3.8-flash-tts with expressive voices (Kore, Charon, Aoede, Puck, Fenrir).\n• Supports affective tags: [sigh], [short pause].",
            "link_label": "TTS Prompt 5.3 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "star",
            "accent": ACCENT_GREEN,
            "title": "4. Custom 30s Commercial Score (`lyria-3`)",
            "body": "• Prompt Lyria 3 for a 3-part dynamic arc: sparse felt piano (0–8s) -> warm acoustic guitar on café chime (9–20s) -> uplifting strings crescendo (21–30s) in 48kHz stereo.",
            "link_label": "Lyria 3 Prompt ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Golden Rule for Lip-Sync: Never exceed 12–14 spoken words in an 8-second clip so the character's cadence feels natural and unhurried.",
        f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Teach the 180-degree camera axis rule for two-character conversations and the 3-part audio stack (Veo 3.1 native dialogue, Gemini 3.8 Flash TTS, and Lyria 3).\n\n"
            "[VERBAL SCRIPT]\n"
            "\"When two AI characters talk to each other in separate clips, why do they often look like they're talking to a wall? Because the prompt didn't lock screen direction. In Shot 4, we place Leo on the right of the frame looking screen-left over Maya's shoulder. In Shot 5, we place Maya on the left of the frame looking screen-right. When you cut those two clips together, their eyes lock across the counter!\"\n\n"
            "[TRANSITION]\n"
            "Let's run the exact Shot 4 and Shot 5 conversation prompts right now."
        ),
    })

    # =========================================================================
    # SLIDE 14: Live Lab #5 — Two-Character Conversation Prompts (Shots 4 & 5)
    # =========================================================================
    sid = "SLIDE_14"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 5 Hands-On Lab · Shot-Reverse-Shot Dialogue in Veo 3.1",
        "Live Lab #5: Directing Leo & Maya's Café Counter Conversation",
        "Run Shot 4 (Over-the-Shoulder on Leo) and Shot 5 (Reverse Close-Up on Maya) with synchronized spoken dialogue.",
        14,
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
            "title": "Copy-Paste Prompt 5.2 & 5.3 — Maya's Reverse Shot + Gemini 3.8 Flash TTS Tagline",
            "link_label": "Copy Stage 5 Prompts ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
            "code": (
                "[SHOT 5 - VEO 3.1]: Reverse-angle medium close-up of Maya, a 29-year-old Latina architect with warm olive skin, round\n"
                "tortoiseshell glasses, and ochre knit cardigan on the left of the frame, looking screen-right. She wraps both hands around\n"
                "the terracotta SOLIS cup, smiles, and replies softly: 'You just saved the whole skyline, Leo.' Warm golden key light, 50mm.\n"
                "[VOICEOVER - gemini-3.8-flash-tts (Voice: Kore)]: \"[sigh] Every bold idea starts before the sun rises. [short pause] Solis. Awaken the craft.\""
            ),
        },
    )
    add_takeaway_banner(
        ops,
        sid,
        "Verify Across Shots 4 & 5: Leo looks left -> Maya looks right -> The terracotta SOLIS cup sits on the oak counter between them.",
        FLOW_URL,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide the copy-paste conversation prompts for Shot 4, Shot 5, and the Gemini 3.8 Flash TTS brand tagline.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"Copy Prompt 5.1 and Prompt 5.2 into Google Flow. Watch how Shot 4 frames Leo over Maya's ochre-cardigan shoulder on the left, and Shot 5 flips the camera to Maya on the left looking right. Then generate the final narrator voiceover using gemini-3.8-flash-tts with the expressive 'Kore' voice.\"\n\n"
            "[TRANSITION]\n"
            "Now let's bring all 6 shots into Google Flow's Scenebuilder in Stage 6 to finish our 30-second commercial."
        ),
    })

    # =========================================================================
    # SLIDE 15: Stage 6 — Scenebuilder Assembly (`Extend`, `Jump To` & J/L Cuts)
    # =========================================================================
    sid = "SLIDE_15"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Stage 6 · Incremental Layer 7 of 7: Scenebuilder Timeline Assembly",
        "Finishing the Commercial with `Extend`, `Jump To` & J/L Audio Cuts",
        "Stitch your 6 shots in Scenebuilder, lengthen emotional reactions, and bridge Maya back to her sunlit studio.",
        15,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "bolt",
            "accent": ACCENT_BLUE,
            "title": "1. Scenebuilder `Extend`\n(Lengthen Reaction Beats)",
            "body": "• Select the end of Shot 5 in Scenebuilder and click 'Extend'.\n• Prompt: 'Continue seamlessly as Maya takes her first slow sip from the terracotta SOLIS cup; her eyes widen with sudden inspiration.'",
            "link_label": "Prompt 6.1 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "hub",
            "accent": ACCENT_AMBER,
            "title": "2. Scenebuilder `Jump To`\n(Scene Match-Cut Finale)",
            "body": "• From the end of Shot 5, click 'Jump To' (or use Frames to Video) for Shot 6.\n• Transitions Maya and the SOLIS cup directly into golden sunrise at her studio desk as she sketches the bridge arch.",
            "link_label": "Prompt 6.2 ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
        },
        {
            "icon": "check",
            "accent": ACCENT_GREEN,
            "title": "3. The J-Cut / L-Cut\nPro Editing Secret",
            "body": "• Never cut audio and video on the exact same millisecond.\n• Let the last 0.5s of Leo's line ('the lines always follow...') trail over the visual cut to Shot 6 as Maya's pencil touches the paper!",
            "link_label": "Editing Checklist ↗",
            "link_url": f"{GITHUB_BLOB}/workshop-guide/01-instructor-playbook.md",
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Final Output: A cohesive 30-second commercial with locked character faces, consistent product branding, and two-way dialogue!",
        f"{GITHUB_BLOB}/workshop-guide/02-student-incremental-labs.md",
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Show how to use Scenebuilder's Extend and Jump To features plus J/L audio cuts to assemble the final 30-second commercial.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"In Stage 6, we assemble our 6 clips inside Scenebuilder. First, we use Extend on Shot 5 so Maya has time to take a sip after her line. Next, we use Jump To to transition her back to the sunlit studio for Shot 6. Finally, apply a classic L-cut by letting Leo's voice trail half a second into Shot 6 as Maya's charcoal pencil draws the bridge arch.\"\n\n"
            "[TRANSITION]\n"
            "Let's wrap up with our bonus industry templates and the GitHub repository links."
        ),
    })

    # =========================================================================
    # SLIDE 16: Workshop Resources, Bonus Templates & GitHub Repository
    # =========================================================================
    sid = "SLIDE_16"
    ops.append({"op": "add-slide", "layout": "BLANK", "id": sid})
    add_header(
        ops,
        sid,
        "Workshop Wrap-Up · Templates, Prompt Library & GitHub Repo",
        "Build Your Own Brand Story: Resources & Bonus Industry Templates",
        "Clone the workshop repository to access all Stage 0–6 prompts, two bonus commercial packs, and the web companion.",
        16,
    )
    add_three_cards(ops, sid, [
        {
            "icon": "code",
            "accent": ACCENT_BLUE,
            "title": "GitHub Repository &\nInteractive Web Portal",
            "body": "• Complete Facilitator Playbook\n• Student Incremental Workbook\n• Interactive Copy-Paste Web App (docs/index.html)\n• Universal Prompt Templates",
            "link_label": "Open GitHub Repo ↗",
            "link_url": GITHUB_REPO,
        },
        {
            "icon": "bolt",
            "accent": ACCENT_AMBER,
            "title": "3 Ready-to-Run\nCommercial Story Packs",
            "body": "• Pack 1: Solis Artisan Coffee (Architect + Barista)\n• Pack 2: NovaPay Fintech (Florist + Groom in Rainstorm)\n• Pack 3: Kuntur Outdoor Gear (Photographer + Andean Guide)",
            "link_label": "Master Prompt Library ↗",
            "link_url": f"{GITHUB_BLOB}/prompts/solis-commercial-prompt-library.md",
        },
        {
            "icon": "cloud",
            "accent": ACCENT_GREEN,
            "title": "Launch Google Flow &\nGoogle AI Studio",
            "body": "• Google Flow Workspace: labs.google/fx/tools/flow\n• Enterprise Flow: flow.cloud.google.com\n• Google AI Studio: aistudio.google.com",
            "link_label": "Launch Google Flow ↗",
            "link_url": FLOW_URL,
        },
    ])
    add_takeaway_banner(
        ops,
        sid,
        "Star & Fork the Workshop Repository: https://github.com/AllInVaders/google-flow-storytelling-workshop",
        GITHUB_REPO,
    )
    ops.append({
        "op": "set-notes",
        "slide": sid,
        "text": (
            "[PURPOSE]\n"
            "Provide participants with all links to the GitHub repository, bonus story templates (Fintech & Retail), and Google Flow workspace.\n\n"
            "[VERBAL SCRIPT]\n"
            "\"You now have the complete 7-stage incremental storytelling framework. In the GitHub repository, you'll find every prompt we ran today for Solis Coffee, plus two bonus commercial story packs for Fintech (NovaPay) and Retail (Kuntur Gear), along with our fill-in-the-blank Identity Anchor templates so you can build your own brand story immediately.\"\n\n"
            "[TRANSITION]\n"
            "Thank you, and happy filmmaking in Google Flow!"
        ),
    })

    return ops


def main():
    print("1. Creating new Google Slides presentation via gslides CLI...")
    create_cmd = [
        GSLIDES,
        "mutate",
        "create",
        "--title",
        "Google Flow & GenMedia: Incremental Storytelling Workshop (Playbook & Prompts)",
        "--json",
    ]
    res = subprocess.run(create_cmd, capture_output=True, text=True, check=True)
    out_text = res.stdout.strip()
    print("Create output:", out_text)
    try:
        data = json.loads(out_text)
        pres_id = data.get("presentationId") or data.get("id")
    except Exception:
        pres_id = None
    if not pres_id:
        m = re.search(r"([a-zA-Z0-9_-]{25,})", out_text)
        pres_id = m.group(1)

    print(f"Created Presentation ID: {pres_id}")
    ops = build_all_slides()
    batch_file = "/tmp/flow_workshop_slides_batch.json"
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(ops, f, indent=2)

    print(f"2. Executing batch update ({len(ops)} operations across 16 slides)...")
    batch_cmd = [GSLIDES, "mutate", "batch", pres_id, "-f", batch_file, "--json"]
    subprocess.run(batch_cmd, capture_output=True, text=True, check=True)
    print("Batch completed successfully!")
    print(f"PRESENTATION_URL=https://docs.google.com/presentation/d/{pres_id}/edit")

    with open("/tmp/flow_workshop_pres_id.txt", "w", encoding="utf-8") as f:
        f.write(pres_id)


if __name__ == "__main__":
    main()

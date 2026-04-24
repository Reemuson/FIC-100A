<p align="center" width="100%">
  <img alt="Logo" width="33%" src="Logos/logo-wordmark-colour.png">
</p>

<h1 align="center">${BOARD_NAME}</h1>

<p align="center" width="100%">
  <a href="${GIT_URL}/actions/workflows/ci.yaml">
    <img alt="CI Badge" src="${GIT_URL}/actions/workflows/ci.yaml/badge.svg?branch=">
  </a>
</p>

<p align="center" width="100%">
    <img src="Images/board_image.png">
</p>

***

<p align="center">
  <img alt="3D Top Angled" src="${png_3d_viewer_angled_top_outpath}" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img alt="3D Bottom Angled" src="${png_3d_viewer_angled_bottom_outpath}" width="45%">
</p>

***

## SPECIFICATIONS

| Parameter | Value | 
| --- | --- |
| Dimensions | ${bb_w_mm} × ${bb_h_mm} mm |

***

## PRODUCT IDENTIFICATION

Public model identifier: **FIC-100A**

Recommended description: **USB IR Adapter compatible with selected Fluke multimeters**

This project uses a simple function-based product numbering style. `FIC` identifies the Fluke-compatible infrared cable family, and `100A` identifies this product generation.

This project is an independent, third-party design compatible with selected Fluke instruments. It is not made by, endorsed by, sponsored by, or affiliated with Fluke Corporation. Fluke is a trademark of Fluke Corporation.

***

## DIRECTORY STRUCTURE

    .
    ├─ Computations       # Misc calculations
    ├─ HTML               # HTML files for generated webpage
    ├─ Images             # Pictures and renders
    │
    ├─ kibot_resources    # External resources for KiBot
    │  ├─ colors          # Color theme for KiCad
    │  ├─ fonts           # Fonts used in the project
    │  ├─ scripts         # External scripts used with KiBot
    │  └─ templates       # Templates for KiBot generated reports
    │
    ├─ kibot_yaml         # KiBot YAML config files
    ├─ KiRI               # KiRI (PCB diff viewer) files
    │
    ├─ lib                # KiCad footprint and symbol libraries
    │  ├─ 3d_models       # Component 3D models
    │  ├─ lib_fp          # Footprint libraries
    │  └─ lib_sym         # Symbol libraries
    │
    ├─ Logos              # Logos
    │
    ├─ Manufacturing      # Assembly and fabrication documents
    │  ├─ Assembly        # Assembly documents (BoM, pos, notes)
    │  │
    │  └─ Fabrication     # Fabrication documents (ZIP, notes)
    │     ├─ Drill Tables # CSV drill tables
    │     └─ Gerbers      # Gerbers
    │
    ├─ Report             # Reports for ERC/DRC
    ├─ Schematic          # PDF of schematic
    ├─ Templates          # Title block templates
    ├─ Testing
    │  └─ Testpoints      # Testpoints tables      
    │
    └─ Variants           # Outputs for assembly variants

## LEGAL

This repository contains open hardware design files, protected project branding, and third-party workflow content.

- The primary hardware licence is the CERN Open Hardware Licence Version 2 - Weakly Reciprocal (`CERN-OHL-W-2.0`). See `LICENSE`.
- Project-specific scope notes, branding exclusions, compatibility wording, non-affiliation wording, and safety notes are in `NOTICE.md`.
- Third-party copyright and licence notices are preserved in `THIRD_PARTY_NOTICES.md`.

This project is an independent, third-party design compatible with selected Fluke instruments. It is not made by, endorsed by, sponsored by, or affiliated with Fluke Corporation. Fluke is a trademark of Fluke Corporation.

This is a hardware/electronics project. Anyone building, modifying, testing, selling, or using the design is responsible for verifying isolation, creepage and clearance, electrical safety, regulatory compliance, and fitness for purpose.

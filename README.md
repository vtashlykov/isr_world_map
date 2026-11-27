# Global Incoherent Scatter Radar (ISR) Inventory & Map Atlas

A geospatial catalog and map generator for **24 Incoherent Scatter Radar (ISR)** facilities around the world, covering their locations, operational status, operating periods, frequency bands, and antenna architectures.

The repository includes English and Russian map scripts, high-resolution map outputs, and 24 local SVG assets with illustrative radar images.

---

## 📌 Project Overview

Incoherent Scatter Radars (ISRs) probe the Earth's upper atmosphere, ionosphere, and magnetosphere. The catalog covers:
- **14 active facilities** currently conducting upper-atmosphere observations.
- **7 decommissioned facilities**, preserving historically significant systems such as Arecibo, Sondrestrom, Saint-Santin, Nançay, Malvern, Sodankylä, and Kiruna.
- **3 next-generation facilities** in the **EISCAT_3D** multi-static phased-array network: Skibotn, Kaiseniemi, and Karesuvanto.

### Map features

- Geographic site markers use distinct colors and shapes for active, decommissioned, and next-generation radars.
- Callouts combine radar names, locations, operating periods, frequencies, antenna descriptions, and local illustrative antenna images, linked to site coordinates.
- English and Russian scripts generate localized versions of the map.
- The optional `--hide-decommissioned` flag removes decommissioned sites and updates the legend. In this mode, EISCAT_3D callouts move to separate positions over Europe, use leader arrows, and omit the A/B/C cluster labels.
- Each script writes a 1200 dpi map and a 100 dpi PNG preview. The English map is `global_isr_radar_map.png`; the Russian map is `Глобальная_карта_радаров_НР.png`. Both scripts write `global_isr_radar_map_preview.png`.

---

## 🗺️ Global ISR Map Preview

[![Global ISR Radar Map](global_isr_radar_map_preview.png)](global_isr_radar_map.png)

*The preview is downsized for Markdown compatibility. Click it to open the full-resolution map.*

---

## 📊 Cataloged Radar Facilities Inventory

The global catalog splits operational characteristics across three detailed parameters: **Operational Status & Years**, **Frequency Band**, and **Antenna System Type**.

| # | Facility Name | Location / Country | Coordinates | Operational Status & Timeline | Frequency Band | Antenna System Type | SVG Asset |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **1** | Arecibo Observatory | Puerto Rico | 18.34° N, 66.75° W | Decommissioned (1963–2020) | UHF (430 MHz) | Fixed Spherical Reflector Dish (Ø305 m) | `Arecibo.svg` |
| **2** | Jicamarca Radio Obs. (JRO) | Peru | 11.95° S, 76.87° W | Active (Since 1961) | VHF (50 MHz) | Planar Crossed-Dipole Field Array (300×300 m) | `Jicamarca_Radar.svg` |
| **3** | Millstone Hill ISR | Massachusetts, USA | 42.62° N, 71.49° W | Active (Since 1960) | UHF (440.2 MHz) | Steerable Parabolic Dish (Ø46 m) & Zenith Dish (Ø68 m) | `Millstone_Hill.svg` |
| **4** | PFISR (Poker Flat) | Alaska, USA | 65.13° N, 147.47° W | Active (Since 2007) | UHF (449 MHz) | Active Solid-State Phased Array (128 AMISR Panels) | `PFISR_Radar.svg` |
| **5** | Resolute Bay (RISR / AMISR) | Nunavut, Canada | 74.73° N, 94.91° W | Active (Since 2009) | UHF (449 MHz) | Dual-Face Active Solid-State Phased Array (AMISR) | `AMISR_Rocket_Bay_Radar.svg` |
| **6** | Sondrestrom Radar | Greenland | 66.99° N, 50.95° W | Decommissioned (1982–2018) | L-Band / UHF (1290 MHz) | Fully Steerable Parabolic Dish (Ø32 m) | `Sondrestrom_Radar.svg` |
| **7** | Saint-Santin Transmitter | France | 44.65° N, 2.19° E | Decommissioned (1963–1987) | UHF (935 MHz) | Continuous-Wave (CW) Cassegrain Dish (Ø52 m) | `Saint_Santin_Transmitter.svg` |
| **8** | Nançay Receiver | France | 47.38° N, 6.50° E | Decommissioned (1963–1987) | UHF (935 MHz, Rx) | Parabolic Reflector Array (300×35 m) | `Nancy_Receiver.svg` |
| **9** | Malvern ISR | Worcestershire, UK | 52.11° N, 2.32° W | Decommissioned (1968–1975) | UHF (400 / 1200 MHz) | Multi-static Steerable Parabolic Dish Network | `Malvern_BW.svg` |
| **10** | EISCAT Tromsø | Norway | 69.59° N, 19.23° E | Active (Since 1981) | UHF (931 MHz) / VHF (224 MHz) | Steerable Parabolic Dish (Ø32 m) & Cylinder (120×40 m) | `EISCAT_Tromso_Radar.svg` |
| **11** | EISCAT Sodankylä | Finland | 67.36° N, 26.63° E | Decommissioned (Since 1981) | UHF (931 MHz, receiver) | Fully Steerable Parabolic Dish (Ø32 m) | `EISCAT_Sodankyla_Radar.svg` |
| **12** | EISCAT Svalbard (ESR) | Svalbard, Norway | 78.15° N, 16.03° E | Active (Since 1996) | UHF (500 MHz) | Dual Dishes (Ø31 m Steerable & Ø42 m Fixed Field-Aligned) | `EISCAT_Svalbard_Radar.svg` |
| **13** | EISCAT Kiruna | Kiruna, Sweden | 67.86° N, 20.44° E | Decommissioned (1981–2023) | UHF (931 MHz) | Fully Steerable Parabolic Antenna (Ø32 m) | `EISCAT_Kiruna.svg` |
| **14** | EISCAT_3D Skibotn | Norway | 69.34° N, 20.31° E | Next-Gen (Commissioning from 2024) | VHF (233 MHz) | Active Phased Array Transceiver (~10,900 dipoles) | `EISCAT3D_Skibotn.svg` |
| **15** | EISCAT_3D Kaiseniemi | Sweden | 68.27° N, 19.45° E | Next-Gen (Commissioning from 2024) | VHF (233 MHz, receiver) | Active Phased Array Receiver (~5,000 dipoles) | `EISCAT3D_Kaiseniemi.svg` |
| **16** | EISCAT_3D Karesuvanto | Finland | 68.48° N, 22.52° E | Next-Gen (Commissioning from 2024) | VHF (233 MHz, receiver) | Active Phased Array Receiver (~5,000 dipoles) | `EISCAT3D_Karesuvanto.svg` |
| **17** | Kharkiv ISR | Ukraine | 49.68° N, 36.29° E | Active (Since 1970s) | VHF (158 MHz) | Zenith-Facing Reflector (Ø100 m) & Steerable Reflector (Ø25 m) | `Kharkiv.svg` |
| **18** | Irkutsk ISR | Russia | 52.88° N, 103.27° E | Active (Since 1993) | VHF (154–162 MHz) | Linear Sectoral Horn Array (246×12 m) | `Irkutsk.svg` |
| **19** | MU Radar | Shigaraki, Japan | 34.85° N, 136.11° E | Active (Since 1984) | VHF (46.5 MHz) | Circular Active Phased Array (Ø103 m, 475 Yagi elements) | `MU_Radar.svg` |
| **20** | Equatorial Atmosphere Radar (EAR) | Sumatra, Indonesia | 0.20° S, 100.32° E | Active (Since 2001) | VHF (47.0 MHz) | Circular Active Phased Array (Ø110 m, 560 Yagi elements) | `EAR.svg` |
| **21** | Sanya ISR (SYISR) | Hainan, China | 18.30° N, 109.60° E | Active (Since 2020) | UHF (430–450 MHz) | Active Digital Phased Array (40×40 m, 8,320 channels) | `Sanya.svg` |
| **22** | Qujing ISR (QJISR) | Yunnan, China | 25.60° N, 103.80° E | Active (Since 2014) | UHF (500 MHz) | Fully Steerable Parabolic Dish (Ø29 m) | `Quijing.svg` |
| **23** | ALTAIR | Kwajalein Atoll | 9.40° N, 167.48° E | Active (Since 1970) | Dual VHF (160 MHz) / UHF (422 MHz) | Fully Steerable Parabolic Dish (Ø46 m) | `ALTAIR.svg` |
| **24** | PANSY Radar | Syowa, Antarctica | 69.00° S, 39.58° E | Active (Since 2011) | VHF (47.0 MHz) | Active Phased Array (1,045 Yagi Dipole Elements) | `PANSY.svg` |

---

## 📁 Repository Structure

```
.
├── plot_global_isr_map.py            # English map rendering script
├── plot_global_isr_map_ru.py         # Russian map rendering script
├── global_isr_radar_map.png           # English 1200 dpi map
├── Глобальная_карта_радаров_НР.png    # Russian 1200 dpi map
├── global_isr_radar_map_preview.png   # 100 dpi preview (written by either script)
├── radar_svg_files/                   # 24 SVG radar-image assets
└── README.md                          # Project documentation and source acknowledgments
```

---

## 🚀 Quick Start & Installation

### Requirements
- Python 3.10+
- `geopandas`
- `matplotlib`
- `pillow`
- `cairosvg`
- `numpy`
- `pyogrio`

### Setup & Execution
```bash
pip install geopandas matplotlib pillow cairosvg numpy pyogrio
python3 plot_global_isr_map.py
python3 plot_global_isr_map_ru.py
```

The first command generates an English-labeled map; the second generates a Russian-labeled map. By default, both include decommissioned radars. Add `--hide-decommissioned` to either command to omit them:

```bash
python3 plot_global_isr_map.py --hide-decommissioned
python3 plot_global_isr_map_ru.py --hide-decommissioned
```

The script downloads Natural Earth country boundaries at runtime, so an internet connection is required.

---

## 🙏 Acknowledgments & Sources

### 1. Scientific Source Materials & Literature
This project relies on historical, technical, and architectural documentation provided across scientific publications and research institutes:
- **Sanya ISR (SYISR)**: Yue et al. (2024), *'The Sanya Incoherent Scatter Radar Tristatic System and Initial Experiments'*, *Space Weather*.
- **Equatorial Atmosphere Radar (EAR) & MU Radar**: Research Institute for Sustainable Humanosphere (RISH), Kyoto University, and CPEA Project records.
- **US Incoherent Scatter Radars**: MIT Lincoln Laboratory, MIT Haystack Observatory historical records (Erickson et al.), and NSF facility reports.
- **EISCAT & EISCAT_3D Facilities**: EISCAT Scientific Association technical specifications for Tromsø, Sodankylä, ESR, and EISCAT_3D (Skibotn, Kaiseniemi, Karesuvanto).
- **French & UK Historical Facilities**: Copernicus HGSS records on Saint-Santin, Nançay, and Malvern Radar History Society archives.
- **Kharkiv & Jicamarca Facilities**: Kharkiv Institute of Ionosphere & Jicamarca Radio Observatory technical publications.

### 2. Instruments & Software Tools Used
- **Gemini Notebook & Generative Image Engine**: Used to render illustrative antenna images from reference photographs. The Gemini watermark is retained as provenance for generated imagery; it is part of the rendered output, not added by the map script.
- **SVG image format**: Each `.svg` asset embeds a PNG image as Base64, making the file self-contained but not truly vector artwork. Base64 adds about 33% to the embedded image payload: the 24 assets contain about 56.5 MB of PNG data encoded as about 75.4 MB of Base64. External PNG files could avoid this encoding overhead, but would require keeping a separate image file alongside each SVG.
- **CairoSVG & Pillow**: Vector SVG conversion, scaling, and composite annotation handling.
- **GeoPandas & Matplotlib**: Spatial data processing, Natural Earth map projection, and custom `AnnotationBbox` leader-arrow callout layout engine.
- **Natural Earth Data**: Low-resolution global administrative boundary dataset (`naturalearth_lowres`).

---

## 📜 License

This project is open-source under the MIT License.

import argparse
import io
import os
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cairosvg
from PIL import Image

parser = argparse.ArgumentParser(description="Plot the global ISR radar map.")
parser.add_argument(
    "--hide-decommissioned",
    action="store_true",
    help="Exclude decommissioned radars from the map.",
)
args = parser.parse_args()

plt.style.use("seaborn-v0_8-whitegrid")

WORLD_BOUNDARIES_URL = "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(WORLD_BOUNDARIES_URL)

RADAR_SITES = [
    # Americas & Greenland
    {"name": "Arecibo Observatory", "loc": "Puerto Rico", "lat": 18.34, "lon": -66.75, "status": "Decommissioned", "years": "1963–2020", "freq": "430 MHz (UHF)", "type": "Spherical reflector (Ø305 m)", "img": "radar_svg_files/Arecibo.svg", "xytext": (-100, 10)},
    {"name": "Jicamarca (JRO)", "loc": "Peru", "lat": -11.95, "lon": -76.87, "status": "Active", "years": "Since 1961", "freq": "50 MHz (VHF)", "type": "Planar dipole array (300×300 m)", "img": "radar_svg_files/Jicamarca_Radar.svg", "xytext": (-120, -15)},
    {"name": "Millstone Hill", "loc": "USA", "lat": 42.62, "lon": -71.49, "status": "Active", "years": "Since 1960", "freq": "440.2 MHz (UHF)", "type": "Steerable reflector (Ø46 m) / zenith-facing reflector (Ø68 m)", "img": "radar_svg_files/Millstone_Hill.svg", "xytext": (-100, 38)},
    {"name": "Poker Flat (PFISR)", "loc": "Alaska, USA", "lat": 65.13, "lon": -147.47, "status": "Active", "years": "Since 2007", "freq": "449 MHz (UHF)", "type": "Active AMISR phased array (128 panels)", "img": "radar_svg_files/PFISR_Radar.svg", "xytext": (-160, 44)},
    {"name": "Resolute Bay (RISR)", "loc": "Canada", "lat": 74.73, "lon": -94.91, "status": "Active", "years": "Since 2009", "freq": "449 MHz (UHF)", "type": "Dual-panel AMISR phased array", "img": "radar_svg_files/AMISR_Rocket_Bay_Radar.svg", "xytext": (-118, 76)},
    {"name": "Sondrestrom", "loc": "Greenland", "lat": 66.99, "lon": -50.95, "status": "Decommissioned", "years": "1982–2018", "freq": "1290 MHz (L-band)", "type": "Fully steerable reflector (Ø32 m)", "img": "radar_svg_files/Sondrestrom_Radar.svg", "xytext": (-75, 76)},
    
    # Europe & Arctic
    {"name": "Saint-Santin", "loc": "France", "lat": 44.65, "lon": 2.19, "status": "Decommissioned", "years": "1963–1987", "freq": "935 MHz (UHF)", "type": "Bistatic CW reflector (Ø52 m)", "img": "radar_svg_files/Saint_Santin_Transmitter.svg", "xytext": (-30, 20)},
    {"name": "Nançay Receiver", "loc": "France", "lat": 47.38, "lon": 6.50, "status": "Decommissioned", "years": "1963–1987", "freq": "935 MHz (UHF, receiver)", "type": "Segmented reflector (300×35 m)", "img": "radar_svg_files/Nancy_Receiver.svg", "xytext": (10, 20)},
    {"name": "Malvern", "loc": "United Kingdom", "lat": 52.11, "lon": -2.32, "status": "Decommissioned", "years": "1968–1975", "freq": "400 / 1200 MHz (UHF)", "type": "Multistatic reflector antennas", "img": "radar_svg_files/Malvern_BW.svg", "xytext": (-30, 40)},
    {"name": "Tromsø (EISCAT)", "loc": "Norway", "lat": 69.59, "lon": 19.23, "status": "Active", "years": "Since 1981", "freq": "931 MHz / 224 MHz", "type": "Steerable reflector (Ø32 m) / cylinder (120×40 m)", "img": "radar_svg_files/EISCAT_Tromso_Radar.svg", "xytext": (-3, 83)},
    {"name": "Sodankylä (EISCAT)", "loc": "Finland", "lat": 67.36, "lon": 26.63, "status": "Decommissioned", "years": "Since 1981", "freq": "931 MHz (receiver)", "type": "Fully steerable reflector (Ø32 m)", "img": "radar_svg_files/EISCAT_Sodankyla_Radar.svg", "xytext": (70, 68)},
    {"name": "Svalbard (ESR)", "loc": "Svalbard", "lat": 78.15, "lon": 16.03, "status": "Active", "years": "Since 1996", "freq": "500 MHz (UHF)", "type": "Two parabolic antennas (Ø31 m / Ø42 m)", "img": "radar_svg_files/EISCAT_Svalbard_Radar.svg", "xytext": (38, 83)},
    {"name": "Kiruna (EISCAT)", "loc": "Kiruna, Sweden", "lat": 67.86, "lon": 20.44, "status": "Decommissioned", "years": "1981–2023", "freq": "931 MHz (UHF)", "type": "Fully steerable parabolic antenna (Ø32 m)", "img": "radar_svg_files/EISCAT_Kiruna.svg", "xytext": (-30, 65)},

    # EISCAT-3D Cluster
    {"cluster_label": "A", "label_offset": (-18, 15), "name": "EISCAT_3D Skibotn", "loc": "Norway", "lat": 69.34, "lon": 20.31, "status": "Next-Gen", "years": "Commissioning from 2024", "freq": "233 MHz (VHF)", "type": "Active phased array (~10,900 dipoles, Tx/Rx)", "img": "radar_svg_files/EISCAT3D_Skibotn.svg", "xytext": (-93, -60)},
    {"cluster_label": "B", "label_offset": (-18, -16), "name": "EISCAT_3D Kaiseniemi", "loc": "Sweden", "lat": 68.27, "lon": 19.45, "status": "Next-Gen", "years": "Commissioning from 2024", "freq": "233 MHz (VHF, receiver)", "type": "Receive phased array (~5,000 dipoles)", "img": "radar_svg_files/EISCAT3D_Kaiseniemi.svg", "xytext": (-52, -60)},
    {"cluster_label": "C", "label_offset": (10, -12), "name": "EISCAT_3D Karesuvanto", "loc": "Finland", "lat": 68.48, "lon": 22.52, "status": "Next-Gen", "years": "Commissioning from 2024", "freq": "233 MHz (VHF, receiver)", "type": "Receive phased array (~5,000 dipoles)", "img": "radar_svg_files/EISCAT3D_Karesuvanto.svg", "xytext": (-7, -60)},

    # Eastern Europe & Asia
    {"name": "Kharkiv ISR", "loc": "Ukraine", "lat": 49.68, "lon": 36.29, "status": "Active", "years": "Since the 1970s", "freq": "158 MHz (VHF)", "type": "Zenith-facing reflector (Ø100 m) / steerable reflector (Ø25 m)", "img": "radar_svg_files/Kharkiv.svg", "xytext": (60, 45)},
    {"name": "Irkutsk ISR", "loc": "Russia", "lat": 52.88, "lon": 103.27, "status": "Active", "years": "Since 1993", "freq": "154–162 MHz (VHF)", "type": "Linear sectoral horn array (246×12 m)", "img": "radar_svg_files/Irkutsk.svg", "xytext": (125, 68)},
    {"name": "MU Radar", "loc": "Japan", "lat": 34.85, "lon": 136.11, "status": "Active", "years": "Since 1984", "freq": "46.5 MHz (VHF)", "type": "Circular phased array (Ø103 m, 475 Yagi antennas)", "img": "radar_svg_files/MU_Radar.svg", "xytext": (160, 48)},
    {"name": "Equatorial Atmosphere Radar (EAR)", "loc": "Indonesia", "lat": -0.20, "lon": 100.32, "status": "Active", "years": "Since 2001", "freq": "47.0 MHz (VHF)", "type": "Circular phased array (Ø110 m, 560 Yagi antennas)", "img": "radar_svg_files/EAR.svg", "xytext": (80, -22)},
    {"name": "Sanya ISR (SYISR)", "loc": "China", "lat": 18.30, "lon": 109.60, "status": "Active", "years": "Since 2020", "freq": "430–450 MHz (UHF)", "type": "Digital phased array (40×40 m, 8,320 channels)", "img": "radar_svg_files/Sanya.svg", "xytext": (140, 10)},
    {"name": "Qujing ISR (QJISR)", "loc": "China", "lat": 25.60, "lon": 103.80, "status": "Active", "years": "Since 2014", "freq": "500 MHz (UHF)", "type": "Steerable parabolic reflector (Ø29 m)", "img": "radar_svg_files/Quijing.svg", "xytext": (78, 20)},

    # Pacific & Antarctica
    {"name": "ALTAIR", "loc": "Kwajalein Atoll", "lat": 9.40, "lon": 167.48, "status": "Active", "years": "Since 1970", "freq": "160 MHz (VHF) / 422 MHz (UHF)", "type": "Fully steerable parabolic reflector (Ø46 m)", "img": "radar_svg_files/ALTAIR.svg", "xytext": (155, -25)},
    {"name": "PANSY Radar", "loc": "Antarctica", "lat": -69.00, "lon": 39.58, "status": "Active", "years": "Since 2011", "freq": "47.0 MHz (VHF)", "type": "Active phased array (1,045 Yagi dipoles)", "img": "radar_svg_files/PANSY.svg", "xytext": (62, -60)}
]

STATUS_COLORS = {
    "Active": "#10b981",       # Emerald Green
    "Decommissioned": "#ef4444", # Red
    "Next-Gen": "#3b82f6"       # Blue
}

STATUS_MARKERS = {
    "Active": "o",
    "Decommissioned": "s",
    "Next-Gen": "^"
}

visible_sites = [
    site for site in RADAR_SITES
    if not args.hide_decommissioned or site["status"] != "Decommissioned"
]
EISCAT_3D_HIDDEN_XYTEXT = {
    "A": (-10, 35),
    "B": (-15, 60),
    "C": (25, 30),
}

fig, ax = plt.subplots(figsize=(32, 20), facecolor="#f8fafc")
ax.set_facecolor("#dbeafe")

world.plot(ax=ax, color="#cbd5e1", edgecolor="#334155", linewidth=1.1)

ax.set_xlim(-180, 180)
ax.set_ylim(-75, 92)
ax.set_xticks(np.arange(-180, 181, 30))
ax.set_yticks(np.arange(-60, 91, 30))
ax.set_xticklabels([f"{abs(x)}°W" if x<0 else (f"{x}°E" if x>0 else "0°") for x in np.arange(-180, 181, 30)], fontsize=13, fontweight="bold", color="#334155")
ax.set_yticklabels([f"{abs(y)}°S" if y<0 else (f"{y}°N" if y>0 else "0°") for y in np.arange(-60, 91, 30)], fontsize=13, fontweight="bold", color="#334155")
ax.grid(True, linestyle="--", color="#94a3b8", alpha=0.7, linewidth=0.8)

ax.set_title("Global Incoherent Scatter Radar (ISR) Network", fontsize=24, fontweight="bold", color="#0f172a", pad=22, loc="left")

for site in visible_sites:
    st = site["status"]
    color = STATUS_COLORS[st]
    marker = STATUS_MARKERS[st]
    cluster_label = site.get("cluster_label")
    show_cluster_label = bool(cluster_label) and not args.hide_decommissioned
    image_xytext = site["xytext"]
    if args.hide_decommissioned and cluster_label:
        image_xytext = EISCAT_3D_HIDDEN_XYTEXT[cluster_label]
    
    ax.scatter(site["lon"], site["lat"], c=color, marker=marker, s=200, edgecolor="black", linewidth=1.6, zorder=8)

    if show_cluster_label:
        ax.annotate(
            cluster_label,
            (site["lon"], site["lat"]),
            xytext=site["label_offset"],
            textcoords="offset points",
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#1d4ed8",
            bbox=dict(boxstyle="circle,pad=0.28", facecolor="white", edgecolor="#1d4ed8", linewidth=1.5),
            zorder=10,
        )
    
    if os.path.exists(site["img"]):
        svg_png = cairosvg.svg2png(url=site["img"])
        raw_img = Image.open(io.BytesIO(svg_png))
        thumb = raw_img.resize((260, 175), Image.Resampling.LANCZOS)
        imagebox = OffsetImage(thumb, zoom=0.60)
        imagebox.image.axes = ax
        
        ab = AnnotationBbox(
            imagebox,
            (site["lon"], site["lat"]),
            xybox=image_xytext,
            xycoords="data",
            boxcoords="data",
            pad=0.35,
            arrowprops=None if show_cluster_label else dict(
                    arrowstyle="-|>",
                    mutation_scale=2.25,
                    connectionstyle="arc3,rad=0.15",
                    color=color,
                    linewidth=2.2
                ),
            bboxprops=dict(edgecolor=color, linewidth=2.8, facecolor="white", alpha=0.98)
        )
        ax.add_artist(ab)
        
        tx, ty = image_xytext
        if show_cluster_label:
            badge_text = f"{cluster_label} · {site['name']} [{site['loc']}]\n{site['years']} | {site['freq']}"
        else:
            badge_text = f"{site['name']} [{site['loc']}]\n{site['years']} | {site['freq']}"
        ax.text(tx, ty + 8.5, badge_text, fontsize=10.5, fontweight="bold", color="#0f172a", ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=color, linewidth=1.6, alpha=0.95), zorder=12)

status_legend = [
    ("Active", "#047857", "Active radar systems"),
    ("Decommissioned", "#b91c1c", "Decommissioned / retired radar systems"),
    ("Next-Gen", "#1d4ed8", "Next-generation EISCAT_3D facilities"),
]
status_counts = {
    status: sum(site["status"] == status for site in visible_sites)
    for status in STATUS_COLORS
}
legend_patches = [
    mpatches.Patch(
        facecolor=STATUS_COLORS[status],
        edgecolor=edge_color,
        label=f"{label} ({status_counts[status]})",
    )
    for status, edge_color, label in status_legend
    if status_counts[status]
]
legend = ax.legend(handles=legend_patches, loc="lower left", bbox_to_anchor=(0.01, 0.02), frameon=True, facecolor="white", edgecolor="#475569", fontsize=13, title="ISR radar operational status", title_fontsize=16)
legend.get_frame().set_linewidth(2.0)
ax.add_artist(legend)

cluster_legend_patches = [
    mpatches.Patch(facecolor="white", edgecolor="#1d4ed8", label=f"{site['cluster_label']} — {site['name']} ({site['loc']})")
    for site in visible_sites if not args.hide_decommissioned and "cluster_label" in site
]

#cluster_legend = ax.legend(
#    handles=cluster_legend_patches,
#    loc="lower right",
#    bbox_to_anchor=(0.99, 0.02),
#    frameon=True,
#    facecolor="white",
#    edgecolor="#1d4ed8",
#    fontsize=10,
#    title="EISCAT_3D markers",
#    title_fontsize=11,
#)
#cluster_legend.get_frame().set_linewidth(1.5)

out_img = "global_isr_radar_map.png"
preview_img = "global_isr_radar_map_preview.png"
plt.savefig(out_img, dpi=1200, bbox_inches="tight")
plt.savefig(preview_img, dpi=100, bbox_inches="tight", format="png")
plt.close(fig)

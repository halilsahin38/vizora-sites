#!/usr/bin/env bash
# Maakt een Etsy-productvideo (≈12 s, 1600x1280, geen geluid) van listing-images/*.png
# Gebruik: tools/make-video.sh products/<map>
set -euo pipefail
dir="$1"; out="$dir/listing-video.mp4"
mapfile -t imgs < <(ls "$dir"/listing-images/*.png | sort)
D=1.9; F=0.4   # seconden per beeld, overgangsduur
args=(); filt=""
for i in "${!imgs[@]}"; do
  args+=(-loop 1 -t "$D" -i "${imgs[$i]}")
  filt+="[$i:v]scale=1600:1280,setsar=1,fps=30,zoompan=z='min(zoom+0.0009,1.06)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1600x1280:fps=30,format=yuv420p[v$i];"
done
prev="v0"; off=$(echo "$D - $F" | bc)
for ((i=1; i<${#imgs[@]}; i++)); do
  filt+="[$prev][v$i]xfade=transition=fade:duration=$F:offset=$off[x$i];"
  prev="x$i"; off=$(echo "$off + $D - $F" | bc)
done
ffmpeg -y -loglevel error "${args[@]}" -filter_complex "${filt%;}" -map "[$prev]" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -movflags +faststart "$out"
echo "Wrote $out"

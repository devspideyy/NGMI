"""Builds out/viewer/index.html: a three.js viewer for every GLB in out/props/models."""
import csv, json, os, sys
sys.argv = [sys.argv[0], "--no-render"]
import props  # registry only; main() is not run on import

rows = {r["name"][3:]: r for r in csv.DictReader(open("out/props/PROP_LIST.csv"))}
data = []
for i, e in enumerate(props.R):
    sheet, name, fn, origin, view, note = e[:6]
    r = rows.get(name)
    if not r:
        continue
    item = dict(n=name, s=sheet, note=note, t=int(r["triangles"]),
                d=[round(float(r["size_x_m"]), 3), round(float(r["size_y_m"]), 3), round(float(r["size_z_m"]), 3)])
    if len(e) > 6:
        item["hidden"] = True
    if i + 1 < len(props.R) and len(props.R[i + 1]) > 6:
        item["pair"] = props.R[i + 1][1]
    data.append(item)
html = open("viewer_template.html").read()
html = html.replace("__DATA__", json.dumps(data)).replace("__SHEETS__", json.dumps(props.SHEETS))
open("out/viewer/index.html", "w").write(html)
print("viewer items", len(data))

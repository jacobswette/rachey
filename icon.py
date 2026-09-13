from PIL import Image, ImageDraw

PINE  = (23, 50, 42)
CLAY  = (223, 180, 140)
RUST  = (184, 90, 46)
CREAM = (241, 233, 214)
PINE2 = (51, 86, 74)

def make(size, pad_ratio=0.0):
    S = size * 8  # supersample
    img = Image.new('RGB', (S, S), PINE)
    d = ImageDraw.Draw(img)
    u = S / 40.0
    def P(pts, fill): d.polygon([(x*u, y*u) for x, y in pts], fill=fill)
    P([(20,5),(26,13),(14,13)], CLAY)          # north
    P([(35,20),(27,26),(27,14)], RUST)         # east
    P([(20,35),(14,27),(26,27)], CLAY)         # south
    P([(5,20),(13,14),(13,26)], RUST)          # west
    d.rectangle([14*u, 14*u, 26*u, 26*u], fill=CREAM)
    P([(20,16.4),(22.7,23.6),(17.3,23.6)], PINE2)   # pine
    d.rectangle([19.35*u, 23.3*u, 20.65*u, 25.2*u], fill=PINE2)
    return img.resize((size, size), Image.LANCZOS)

for s in (180, 192, 512):
    make(s).save(f'icon-{s}.png')
make(180).save('apple-touch-icon.png')
print('icons written')

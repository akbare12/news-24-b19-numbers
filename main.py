import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1024, 1024
OUT = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', 'out'), 'entry.png')
CREAM, INK, RED, NAVY, GREY, LGREY = (247, 242, 231), (17, 17, 17), (176, 30, 36), (28, 47, 94), (90, 90, 90), (232, 226, 212)
CHIP = {'CONFIRMED': (27, 120, 60), 'OFFICIAL': (28, 47, 94), 'REPORTED': (90, 90, 90), 'CLAIM': (200, 90, 20)}
def F(s, b=False, serif=False):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf' if serif else ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    try: return ImageFont.truetype(p, s)
    except Exception: return ImageFont.load_default()
def wrap(t, f, w, d):
    out, cur = [], ''
    for wd in t.split():
        s = (cur + ' ' + wd).strip()
        if d.textlength(s, font=f) <= w: cur = s
        else:
            if cur: out.append(cur)
            cur = wd
    if cur: out.append(cur)
    return out
def txt(d, x, y, lines, f, fill=INK, lh=None):
    lh = lh or int(f.size * 1.25)
    for i, l in enumerate(lines): d.text((x, y + i * lh), l, font=f, fill=fill)
    return y + len(lines) * lh
def chip(d, x, y, label):
    f = F(7, True); w = int(d.textlength(label, font=f)) + 8
    d.rounded_rectangle([x, y, x + w, y + 11], 2, fill=CHIP[label]); d.text((x + 4, y + 2), label, font=f, fill=(255, 255, 255)); return x + w + 4
def scene(d, n, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 42, 74) if n in (1, 4) else (210, 226, 235) if n in (3, 5, 13) else (245, 222, 180) if n == 2 else (200, 220, 205) if n in (6, 11) else (235, 200, 200) if n == 8 else (225, 225, 225))
    if n == 1:
        d.rectangle([x + w * .42, y + h * .08, x + w * .58, y + h], fill=(20, 28, 52)); d.rectangle([x + w * .30, y + h * .45, x + w * .42, y + h], fill=(40, 52, 84)); d.rectangle([x + w * .58, y + h * .55, x + w * .72, y + h], fill=(40, 52, 84))
        for i in range(9): d.rectangle([x + w * .44 + (i % 3) * w * .05, y + h * .14 + (i // 3) * h * .22, x + w * .47 + (i % 3) * w * .05, y + h * .19 + (i // 3) * h * .22], fill=(255, 210, 90))
        d.ellipse([x + w * .70, y + h * .10, x + w * .78, y + h * .22], fill=(255, 120, 60)); d.ellipse([x + w * .66, y + h * .18, x + w * .80, y + h * .38], fill=(120, 120, 120)); d.polygon([(x + w * .18, y + h * .30), (x + w * .24, y + h * .28), (x + w * .22, y + h * .34)], fill=(60, 60, 60))
    elif n == 2:
        d.rectangle([x + w * .15, y + h * .30, x + w * .85, y + h], fill=(176, 30, 36)); d.rectangle([x + w * .38, y + h * .55, x + w * .62, y + h], fill=(60, 20, 20)); d.rectangle([x + w * .10, y + h * .18, x + w * .90, y + h * .32], fill=(120, 20, 26))
        for i in range(5): d.rectangle([x + w * .18 + i * w * .14, y + h * .38, x + w * .26 + i * w * .14, y + h * .50], fill=(255, 220, 130))
        d.rectangle([x + w * .62, y + h * .10, x + w * .88, y + h * .28], fill=(255, 255, 255)); d.line([x + w * .65, y + h * .16, x + w * .85, y + h * .16], fill=INK, width=2); d.line([x + w * .65, y + h * .21, x + w * .82, y + h * .21], fill=INK, width=2)
    elif n == 3:
        d.rectangle([x, y + h * .55, x + w, y + h], fill=(90, 110, 140)); d.polygon([(x + w * .10, y + h * .60), (x + w * .50, y + h * .12), (x + w * .90, y + h * .60)], fill=(200, 205, 215))
        for i in range(4): d.rectangle([x + w * .20 + i * w * .15, y + h * .42, x + w * .28 + i * w * .15, y + h * .58], fill=(60, 70, 90))
        d.rectangle([x + w * .44, y + h * .30, x + w * .56, y + h * .44], fill=(176, 30, 36)); d.text((x + w * .47, y + h * .33), 'H', font=F(10, True), fill=(255, 255, 255)); d.ellipse([x + w * .68, y + h * .05, x + w * .86, y + h * .18], fill=(255, 210, 90))
    elif n == 4:
        for i in range(7): d.ellipse([x + w * .08 + i * w * .12, y + h * .15 + (i % 3) * h * .18, x + w * .14 + i * w * .12, y + h * .25 + (i % 3) * h * .18], fill=(255, 180, 80))
        d.rectangle([x + w * .15, y + h * .60, x + w * .30, y + h], fill=(70, 70, 80)); d.rectangle([x + w * .60, y + h * .70, x + w * .80, y + h], fill=(70, 70, 80)); d.polygon([(x + w * .45, y + h * .55), (x + w * .55, y + h * .52), (x + w * .52, y + h * .62)], fill=(40, 40, 40))
    elif n == 5:
        d.polygon([(x + w * .42, y + h * .15), (x + w * .58, y + h * .15), (x + w * .52, y + h * .45), (x + w * .48, y + h * .45)], fill=(255, 210, 90)); d.ellipse([x + w * .40, y + h * .08, x + w * .60, y + h * .22], fill=(255, 210, 90)); d.rectangle([x + w * .30, y + h * .55, x + w * .70, y + h * .75], fill=(120, 30, 30)); d.rectangle([x + w * .15, y + h * .78, x + w * .32, y + h * .92], fill=(0, 120, 60)); d.rectangle([x + w * .68, y + h * .78, x + w * .85, y + h * .92], fill=(220, 60, 60))
    elif n == 6:
        d.rectangle([x, y + h * .55, x + w, y + h], fill=(40, 90, 130)); d.rectangle([x + w * .15, y + h * .30, x + w * .75, y + h * .58], fill=(200, 60, 40)); d.rectangle([x + w * .20, y + h * .20, x + w * .35, y + h * .32], fill=(180, 180, 180)); d.rectangle([x + w * .78, y + h * .45, x + w * .92, y + h * .60], fill=(90, 90, 90))
    elif n == 7:
        d.line([x + w * .08, y + h * .75, x + w * .35, y + h * .55, x + w * .55, y + h * .60, x + w * .92, y + h * .15], fill=(27, 120, 60), width=3); d.line([x + w * .08, y + h * .30, x + w * .92, y + h * .30], fill=RED, width=2); d.rectangle([x + w * .10, y + h * .70, x + w * .25, y + h * .85], fill=NAVY); d.rectangle([x + w * .60, y + h * .65, x + w * .75, y + h * .85], fill=NAVY)
    elif n == 8:
        d.rectangle([x + w * .10, y + h * .55, x + w * .90, y + h * .95], fill=(50, 55, 70)); d.rectangle([x + w * .20, y + h * .30, x + w * .35, y + h * .55], fill=(50, 55, 70)); d.rectangle([x + w * .65, y + h * .30, x + w * .80, y + h * .55], fill=(50, 55, 70))
        for i in range(3): d.rectangle([x + w * .15 + i * w * .28, y + h * .62, x + w * .28 + i * w * .28, y + h * .72], fill=(255, 60, 60))
        d.rectangle([x + w * .42, y + h * .08, x + w * .58, y + h * .26], fill=(200, 30, 30)); d.text((x + w * .47, y + h * .12), '!', font=F(10, True), fill=(255, 255, 255))
    elif n == 9:
        d.polygon([(x + w * .05, y + h * .85), (x + w * .35, y + h * .25), (x + w * .65, y + h * .85)], fill=(110, 130, 110)); d.polygon([(x + w * .40, y + h * .85), (x + w * .70, y + h * .35), (x + w * .95, y + h * .85)], fill=(90, 110, 95)); d.ellipse([x + w * .30, y + h * .15, x + w * .55, y + h * .30], fill=(60, 60, 60)); d.rectangle([x + w * .52, y + h * .20, x + w * .70, y + h * .26], fill=(60, 60, 60)); d.ellipse([x + w * .15, y + h * .75, x + w * .35, y + h * .90], fill=(255, 140, 60))
    elif n == 10:
        d.rectangle([x + w * .10, y + h * .30, x + w * .90, y + h * .90], fill=(220, 200, 160)); d.rectangle([x + w * .15, y + h * .18, x + w * .85, y + h * .32], fill=(176, 30, 36)); d.text((x + w * .38, y + h * .21), 'MART', font=F(9, True), fill=(255, 255, 255))
        for i in range(3): d.rectangle([x + w * .20 + i * w * .22, y + h * .50, x + w * .32 + i * w * .22, y + h * .88], fill=(90, 110, 160))
    elif n == 11:
        d.rectangle([x, y + h * .65, x + w, y + h], fill=(210, 190, 140)); d.polygon([(x + w * .10, y + h * .55), (x + w * .30, y + h * .30), (x + w * .50, y + h * .55)], fill=(160, 120, 80)); d.rectangle([x + w * .60, y + h * .35, x + w * .90, y + h * .65], fill=(90, 90, 90)); d.line([x + w * .60, y + h * .35, x + w * .90, y + h * .65], fill=(255, 255, 255), width=2)
    elif n == 12:
        d.rectangle([x, y + h * .60, x + w, y + h], fill=(200, 180, 130)); d.rectangle([x + w * .10, y + h * .45, x + w * .45, y + h * .62], fill=(120, 60, 40)); d.rectangle([x + w * .55, y + h * .40, x + w * .90, y + h * .60], fill=(150, 70, 50)); d.ellipse([x + w * .70, y + h * .10, x + w * .90, y + h * .30], fill=(255, 200, 80))
    else:
        d.rectangle([x, y + h * .70, x + w, y + h], fill=(70, 80, 100)); d.polygon([(x + w * .45, y + h * .10), (x + w * .55, y + h * .10), (x + w * .58, y + h * .70), (x + w * .42, y + h * .70)], fill=(220, 220, 220)); d.polygon([(x + w * .38, y + h * .30), (x + w * .62, y + h * .30), (x + w * .58, y + h * .45), (x + w * .42, y + h * .45)], fill=(255, 120, 40)); d.ellipse([x + w * .75, y + h * .08, x + w * .95, y + h * .28], fill=(200, 220, 240))

HEROES = [(1, '1 RIYADH \u00b7 MIDDLE EAST', 'CONFIRMED', "Houthi drone hits Riyadh's tallest tower again, 11 hurt", 'A Houthi drone struck the PIF tower, the tallest in Riyadh, for the second time in a week. At least 11 were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians. (Saudi officials)', '14:27 UTC'), (2, '2 SHANGHAI \u00b7 ASIA', 'OFFICIAL', 'China probes Shanghai party chief Chen Jining', 'Chen Jining, 62, the Shanghai party chief, is under investigation for "serious violations". He is the fourth Politburo member to fall in a probe this year. (CCDI)', 'CCDI'), (3, '3 NEW YORK \u00b7 US / TECH', 'CONFIRMED', 'Huawei guilty on 10 of 12 counts', 'A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering; sentencing is set for Sep 2027.', '20:41 UTC')]
CARDS = [(4, '4 ZAPORIZHZHIA \u00b7 EUROPE', 'REPORTED', 'Russian attacks kill 9 across Ukraine in a day', 'Nine killed and 81 wounded as Russia launched 96 drones; 73 were shot down. (Kyiv)', '11:37 UTC'), (5, '5 DAKAR \u00b7 AFRICA / SPORT', 'OFFICIAL', 'CAS hands Senegal back the AFCON title', 'CAS restored the Africa Cup to Senegal after Morocco forfeited 3-0, making it 1-0. (CAS)', 'CAS'), (6, '6 HORMUZ \u00b7 MIDDLE EAST', 'REPORTED', 'IRGC attacks container ship in Hormuz', 'A container ship was attacked in Hormuz; navigation disabled north of Khasab. (UKMTO)', '18:58 UTC'), (7, '7 NEW YORK \u00b7 MARKETS', 'CONFIRMED', 'Dow closes above 50,000 for the first time', 'The Dow closed at 50,018, first above 50,000. The Taiex surged 8.99% to a record.', 'Close'), (8, '8 REDMOND \u00b7 TECH', 'REPORTED', "Microsoft declares 'Code Red' after historic outage", 'After a 24-hour outage, Microsoft set a one-hour global recovery target. (Reuters)', 'Reuters'), (9, '9 ESKISEHIR \u00b7 EUROPE', 'REPORTED', 'Turkish military helicopter crash kills 5', 'An AS-532 helicopter crashed near Eskisehir, killing all five people on board.', '19:52 UTC'), (10, '10 CARTAGENA \u00b7 AMERICAS', 'REPORTED', 'Supermarket hostages: 25 held in Cartagena', 'Twenty-five held hostage in a Cartagena supermarket; five elderly women were freed.', '17:35 UTC'), (11, '11 ADEN \u00b7 MIDDLE EAST', 'REPORTED', 'Houthis advance within 60 km of Aden', 'Houthi forces advanced to within 60 km of Aden, the closest push in years. (Wires)', '16:51 UTC'), (12, '12 LAHJ \u00b7 MIDDLE EAST', 'REPORTED', 'Saudi strikes kill 25, wound 6 in Yemen', 'Saudi strikes on a bus and truck at Wadi Maabaq in Lahj killed 25 and wounded 6.', '10:42 UTC'), (13, '13 JIUQUAN \u00b7 SPACE', 'OFFICIAL', 'China names first foreign astronaut for Tiangong', 'Crew named: Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali of Pakistan. (CMSA)', 'CMSA')]
ALSO = [(14, 'Ankara', 'Haftar visits Turkey for the first time.'), (15, 'London', 'UK sanctions Houthis and 4 officials.'), (16, 'Villavicencio', 'Car bomb injures 23 people.'), (17, 'Gaza', 'Israel kills Hamas internal security chief.'), (18, 'Baghdad', 'Iraq orders federal control of Kurdish oilfields.'), (19, 'Gaza', 'Meningitis epidemic alert: 272 cases in October.'), (20, 'DR Congo', 'Missing Cessna 208; rebels claim shootdown.'), (21, 'Hanoi', 'Hot-pot explosion kills at least 6.'), (22, 'Gulf of Finland', 'Ukraine hits Russian ship Sparta II.'), (23, 'Kuala Lumpur', 'Malaysia to return migrants to Myanmar.'), (24, 'Ulleungdo', 'S. Korea shelter order as Russian jets enter ADIZ.'), (25, 'Dhaka', 'Hasina plans return on 16 Dec.'), (26, 'The Hague', '14 nations endorse ICJ Myanmar ruling.'), (27, 'Jakarta', 'Indonesia nominates 2 VP candidates.'), (28, 'Beijing', 'China sentences official Ma to death for spying.'), (29, 'Brussels', 'NATO vows defence against space threat.'), (30, 'Mexico City', 'US drone aided capture; Mexico tries El Chapo.'), (31, 'San Salvador', 'Bukele names 3 soldiers killed in Haiti.'), (32, 'Ottawa', 'Pentagon: only 41.9% of air fleet ready.'), (33, 'Washington', 'US adds Megaspeed to trade blacklist.'), (34, 'Kyiv', 'Zelensky urges Ukraine-Russia-US-Europe talks soon.'), (35, 'Ras Al Khaimah', 'UAE bus-truck crash kills 13.'), (36, 'London', 'England record 5,258 heat deaths in summer 2026.'), (37, 'Kourou', 'Ariane 6 lofts 36 Amazon satellites.'), (38, 'Cikande', 'Factory-fire toll rises to 26.')]
NUMBERS = [('11', 'hurt in Riyadh'), ('9', 'killed in Ukraine'), ('50,018', 'Dow close'), ('+8.99%', 'Taiex record'), ('25', 'killed in Yemen'), ('26', 'Cikande toll'), ('10/12', 'Huawei guilty'), ('96', 'drones launched')]
UTC = [('02:15', 'NATO vows space defence'), ('08:16', 'Hanoi blast'), ('10:42', 'Saudi strikes Yemen'), ('14:27', 'Riyadh tower hit'), ('16:51', 'Houthis 60 km from Aden'), ('18:58', 'Hormuz ship attack'), ('20:41', 'Huawei guilty')]
REGIONS = [('Europe', 9, (28, 47, 94)), ('Middle East', 8, (176, 30, 36)), ('Asia', 8, (200, 90, 20)), ('Africa', 2, (27, 120, 60)), ('Americas', 7, (120, 60, 120)), ('World/Space', 4, (90, 90, 90))]
PINS = [(1, 24.7, 46.7, 'Riyadh'), (2, 31.2, 121.5, 'Shanghai'), (3, 40.7, -74.0, 'New York'), (4, 47.8, 35.2, 'Zaporizhzhia'), (5, 14.7, -17.4, 'Dakar'), (6, 26.5, 56.3, 'Hormuz'), (7, 40.7, -74.0, 'New York'), (8, 47.7, -122.1, 'Redmond'), (9, 39.8, 30.5, 'Eskisehir'), (10, 10.4, -75.5, 'Cartagena'), (11, 12.8, 45.0, 'Aden'), (12, 13.0, 44.9, 'Lahj'), (13, 39.7, 98.5, 'Jiuquan')]
CONT = [[(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66), (-80, 73), (-65, 60), (-55, 52), (-60, 47), (-70, 42), (-75, 35), (-80, 32), (-81, 26), (-90, 21), (-97, 16), (-105, 20), (-117, 33), (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)], [(-58, 64), (-45, 60), (-40, 65), (-30, 68), (-20, 70), (-30, 76), (-50, 76), (-58, 72)], [(-80, 9), (-72, 12), (-60, 8), (-52, 5), (-50, 0), (-40, -5), (-35, -8), (-40, -20), (-48, -28), (-58, -35), (-65, -41), (-70, -50), (-73, -53), (-73, -44), (-72, -30), (-70, -18), (-77, -12), (-80, -5), (-81, 0)], [(-17, 15), (-10, 5), (-8, -2), (9, -1), (13, -5), (12, -12), (14, -22), (17, -29), (20, -35), (28, -33), (35, -25), (40, -15), (42, -10), (48, 11), (51, 12), (43, 5), (38, 0), (35, 5), (32, 10), (30, 15), (25, 20), (20, 25), (15, 30), (10, 33), (0, 35), (-5, 35), (-10, 30), (-15, 25)], [(-10, 37), (-9, 43), (-2, 48), (-4, 50), (0, 52), (5, 53), (8, 57), (10, 59), (18, 56), (21, 55), (24, 59), (30, 60), (30, 65), (25, 70), (20, 70), (15, 68), (12, 65), (8, 62), (5, 60), (5, 58), (0, 55), (-2, 50), (-5, 48), (-9, 44)], [(30, 65), (40, 68), (50, 69), (60, 69), (70, 72), (80, 73), (90, 75), (100, 76), (110, 74), (120, 73), (130, 71), (140, 72), (150, 70), (160, 69), (170, 66), (178, 65), (170, 60), (162, 56), (158, 52), (150, 60), (142, 55), (140, 45), (135, 43), (130, 42), (127, 40), (122, 38), (120, 32), (122, 28), (115, 23), (110, 20), (108, 12), (105, 8), (100, 7), (98, 10), (95, 15), (92, 21), (88, 22), (85, 20), (80, 15), (77, 8), (75, 12), (72, 20), (68, 22), (66, 25), (60, 25), (57, 26), (54, 27), (52, 28), (50, 29), (48, 30), (45, 30), (42, 32), (40, 36), (36, 36), (33, 36), (30, 36), (30, 40)], [(113, -22), (114, -30), (115, -33), (120, -34), (129, -32), (132, -32), (135, -35), (140, -38), (145, -38), (150, -37), (153, -32), (153, -27), (150, -23), (146, -19), (142, -15), (142, -11), (137, -12), (135, -15), (132, -12), (130, -13), (126, -14), (122, -17), (118, -20)]]

def main():
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 5], fill=RED)
    d.text((10, 8), 'THE WORLD ON ONE DAY', font=F(10, True), fill=RED); d.text((W - 10 - d.textlength('38 STORIES \u00b7 6 REGIONS \u00b7 TUESDAY 24 NOVEMBER 2026', font=F(10, True)), 8), '38 STORIES \u00b7 6 REGIONS \u00b7 TUESDAY 24 NOVEMBER 2026', font=F(10, True), fill=INK)
    d.text((10, 24), 'Tuesday 24 November 2026', font=F(28, True, True), fill=INK)
    d.text((10, 56), 'A Houthi drone hits Riyadh\u2019s tallest tower \u00b7 Shanghai\u2019s party chief is probed \u00b7 Huawei guilty on 10 of 12 counts.', font=F(11, False, True), fill=RED)
    x = 10
    for name, n, c in REGIONS:
        lab = f'{name} {n}'; wdt = int(d.textlength(lab, font=F(9, True))) + 12; d.rectangle([x, 72, x + wdt, 88], fill=c); d.text((x + 6, 75), lab, font=F(9, True), fill=(255, 255, 255)); x += wdt + 4
    d.text((10, 94), 'THE DAY IN UTC', font=F(9, True), fill=RED)
    uw = (W - 150) / 7
    for i, (t, ev) in enumerate(UTC):
        xx = 130 + i * uw; d.text((xx, 94), t, font=F(9, True), fill=RED); txt(d, xx, 106, wrap(ev, F(8), uw - 6, d), F(8), lh=10)
    d.text((10, 128), 'THE DAY IN NUMBERS', font=F(9, True), fill=RED)
    nw = (W - 20) / 8
    for i, (v, lab) in enumerate(NUMBERS):
        xx = 10 + i * nw; d.text((xx, 140), v, font=F(17, True, True), fill=RED); d.text((xx, 160), lab, font=F(8), fill=GREY)
    hw, hg, hy = (W - 20 - 12) // 3, 180, 176
    for i, (n, kick, ch, head, deck, src) in enumerate(HEROES):
        hx = 10 + i * (hw + 6); scene(d, n, hx, hy, hw, 84); d.rectangle([hx, hy + 84, hx + hw, hy + hg], outline=INK, width=1); d.line([hx, hy + 84, hx + hw, hy + 84], fill=INK, width=1)
        d.text((hx + 4, hy + 88), kick, font=F(8, True), fill=RED); cx = chip(d, hx + 4, hy + 102, ch)
        txt(d, hx + 4, hy + 116, wrap(head, F(12, True, True), hw - 8, d)[:2], F(12, True, True), lh=14); txt(d, hx + 4, hy + 116 + 28, wrap(deck, F(8), hw - 8, d)[:3], F(8), lh=10)
    cw, chh, cy = (W - 20 - 24) // 5, 116, 362
    for r in range(2):
        for c in range(5):
            n, kick, ch, head, deck, src = CARDS[r * 5 + c]; cx0 = 10 + c * (cw + 6); cy0 = cy + r * (chh + 6); scene(d, n, cx0, cy0, cw, 32); d.rectangle([cx0, cy0, cx0 + cw, cy0 + chh], outline=INK, width=1)
            d.text((cx0 + 3, cy0 + 35), kick, font=F(7, True), fill=RED); chip(d, cx0 + 3, cy0 + 46, ch)
            txt(d, cx0 + 3, cy0 + 59, wrap(head, F(9, True), cw - 6, d)[:2], F(9, True), lh=11); txt(d, cx0 + 3, cy0 + 81, wrap(deck, F(8), cw - 6, d)[:2], F(8), lh=10)
    my, mh = 608, 168; mx, mw = 10, 470
    d.text((mx, my - 16), 'THE WORLD \u00b7 WHERE IT HAPPENED', font=F(9, True), fill=RED)
    d.rectangle([mx, my, mx + mw, my + mh], fill=(225, 232, 238), outline=INK, width=1)
    def px(lon, lat): return mx + (lon + 180) / 360 * mw
    def py(lat): return my + (75 - lat) / 130 * mh
    for poly in CONT: d.polygon([(px(lon, lat), py(lat)) for lon, lat in poly], fill=(150, 180, 140), outline=(90, 120, 95))
    off = {7: (16, -12), 12: (18, 10), 6: (0, -12)}
    pts = {}
    for n, lat, lon, city in PINS:
        X, Y = px(lon, lat), py(lat); pts[n] = (X, Y)
        ox, oy = off.get(n, (0, 0)); X2, Y2 = X + ox, Y + oy
        if (ox, oy) != (0, 0): d.line([X, Y, X2, Y2], fill=RED, width=1)
        d.ellipse([X2 - 8, Y2 - 8, X2 + 8, Y2 + 8], fill=RED, outline=(255, 255, 255), width=1); d.text((X2 - 3 if n < 10 else X2 - 6, Y2 - 5), str(n), font=F(7, True), fill=(255, 255, 255))
    ly = my + mh + 6
    for i, (n, lat, lon, city) in enumerate(PINS):
        lx = mx + (i % 2) * 240; lyy = ly + (i // 2) * 11; d.ellipse([lx, lyy + 1, lx + 8, lyy + 9], fill=RED); d.text((lx + 1 if n < 10 else lx - 1, lyy + 1), str(n), font=F(6, True), fill=(255, 255, 255)); d.text((lx + 12, lyy), f'{n} {city}', font=F(8), fill=INK)
    ax, aw = 496, W - 496 - 10; ay = 592
    d.text((ax, ay), 'ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES', font=F(9, True), fill=RED)
    for i, (n, city, head) in enumerate(ALSO):
        col, row = i // 13, i % 13; xx = ax + col * (aw // 2); yy = ay + 16 + row * 11
        d.text((xx, yy), f'{n} {city}: {head}', font=F(8), fill=INK)
    dy = 872
    d.rectangle([10, dy, W - 10, dy + 96], fill=(255, 235, 235), outline=RED, width=1)
    dc = "DATE CHECK \u2014 Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov); Huang returns as Nvidia CEO (Mon 23 Nov); EU sanctions package 22 (Mon 23 Nov); COP31 ends with no deal (Sun 22 Nov); Merkury sinks (Sat 22 Nov); El Chapo Isidro arrested (Fri 20 Nov); Cikande fire starts (Sat 21 Nov); Trump hush-money appeal (Mon 23 Nov); ATP final (Sun 22 Nov); Las Vegas GP (Sat 21 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC); MPR session picks VP (11 Dec); Huawei sentencing (Sep 2027); Hasina returns (16 Dec)."
    txt(d, 16, dy + 6, wrap(dc, F(9), W - 32, d), F(9), lh=12)
    fy = dy + 102
    d.text((10, fy), 'Sources: AP \u00b7 Reuters \u00b7 UKMTO \u00b7 CAS \u00b7 CCDI \u00b7 CMSA \u00b7 dailysummaryof.com (24 Nov 2026, 64 sources).', font=F(8), fill=GREY)
    d.text((10, fy + 12), 'CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side\u2019s claim. Scenes are drawn illustrations, not photographs.', font=F(8), fill=GREY)
    os.makedirs(os.path.dirname(OUT) or '.', exist_ok=True); im.save(OUT)
if __name__ == '__main__': main()

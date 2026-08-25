# CLAUDE.md — Aspen Wright Family Itinerary

This file is auto-loaded by Claude Code. It contains everything needed to continue
editing the trip itinerary document. Read it fully before making changes.

---

## WHAT THIS PROJECT IS

A self-contained HTML file (`itinerary.html`) that renders a luxury trip
itinerary for the Wright family's Aspen ski trip (Dec 27, 2026 – Jan 3, 2027).

**As of v21 this is now a screen-first INTERACTIVE web document** (the
"Alpenglow Nocturne" cinematic dark theme), not a print-to-PDF doc. It has a
sticky clickable top nav with scroll-spy, tabbed day panels, an interactive
Leaflet map, photo lightbox, scroll-reveal animations, and ~16 base64-embedded
photos. File is ~10 MB because of the embedded photos — that is expected.

- **`itinerary.html`** — current interactive version (v21). Open in a browser; it
  is meant to be viewed on screen, NOT printed to PDF.
- **`itinerary_v1.html`** — the previous print-to-PDF version (old v20), preserved
  as the "base"/print artifact. Untouched. Use it if a clean PDF is ever needed.
- **`bar_harbor_for_ruby.html`** — the design reference the user supplied; the
  interactive patterns (day-tab `showDay`, Leaflet pins, photo plates) came from it.

---

## HOW TO WORK ON THIS FILE (v21 interactive)

- **Edit `itinerary.html` directly.** One standalone file: CSS in `<style>`, content
  in `<body>`, JS at the bottom, photos embedded as base64 `data:` URIs. The only
  external deps are Google Fonts, Leaflet (CDN), and CARTO dark map tiles — so the
  **map needs internet** to show tiles (pins/markers still render offline).
- **To preview:** open `itinerary.html` in a browser. No PDF workflow anymore.
- **Make targeted edits** with find/replace on unique strings: section ids
  (`#travel #lodging #ski #itinerary #valley #dining #booking`), day panel ids
  (`d0`–`d7`), `.daytab` labels, restaurant names, booking numbers `[1]`–`[10]`.
- **NEVER inline content through a Python f-string or shell heredoc** — `$` chars get
  stripped and corrupt the pricing. Edit the HTML directly, or use placeholder tokens
  + `.replace()` (that's how the images were injected).

### Image pipeline (how the photos got there / how to swap them)
- Source images live in `assets_src/` (originals) and `assets_opt/` (resized to
  1600px, JPEG q62). `assets_src/manifest.json` records each image's source +
  license + attribution (Wikimedia Commons & Flickr, CC / public-domain).
- Helper scripts: `fetch_images.py` (Commons API), `fetch_openverse.py` /
  `fetch_final.py` (Flickr via Openverse), `inject_images.py` (base64-embeds every
  `assets_opt/<slug>.jpg` into the matching `{{IMG_<slug>}}` token — though tokens are
  already replaced in the live file).
- **To swap a photo:** drop a new file at `assets_opt/<slug>.jpg`, then either
  re-run the token build from a clean copy, or just base64-encode the new image
  (`base64 -i new.jpg`) and replace that one image's `data:image/jpeg;base64,...`
  string in `itinerary.html`. Slugs: `hero, lodging, day0_arrival, day1_snowmass,
  day2_ajax, day3_bells, day3_cookhouse, day4_nye, day5_springs, day6_family,
  day7_depart, rest_steak, rest_sushi, rest_italian, rest_alpine, rest_apres`.
- **Real user photos now in (from `photos/`):** lodging (`photo1.avif`), Day 3 French
  Alpine plate (`frenchalpine.webp`), Day 4 Matsuhisa plate (`matsuhisa.jpg`), and day
  BANNERS — Day 0 arrival (`arrival.jpg`, winter drive), Day 3 (`snowmobile.jpg`), Day 4
  (`nye.webp`, fireworks+torchlight over Aspen), Day 5 (`hot springs.jpg`, daytime).
  Day 1/2/6/7 banners + the restaurant-card stock shots are still generic CC stand-ins.

---

## DESIGN SYSTEM — v22 "White Christmas / NYE" (current)

Light, festive theme. Tokens are CSS `:root` variables at the top of the file.
(Built by `retheme_white.py`, which swaps the whole `<style>` block while preserving
the embedded hero image, and switches the Leaflet tiles dark→light.)

- **Background:** soft snow-white radial — `#ffffff → #f4f8f6 → #e9f0ec` (fixed)
- **Surfaces:** frosted white glass cards `rgba(255,255,255,.72)` with gold hairline
  borders + soft shadows
- **Text:** deep evergreen-ink `#1b2a22` (headings/titles via `--snow`/`--evergreen`),
  soft `#46544d`, sage muted `#7E8B83`
- **Accents:** evergreen `#1F4D38` (brand/titles), gold `#B0863A` / bright `#C49A4A`,
  cranberry `#9B2D2A` (italic notes/warnings), champagne `#E8D9B0` (NYE sparkle / day
  ribbons / pin letters). The `--alpenglow` gradient is now a **gold sparkle**
  (`#C49A4A → #E8D9B0 → #B0863A`) on the progress bar, active nav underline, and
  active day tab.
- **Festive cues:** gold **snowflake (❄)** in hero + section ornaments; hero is a
  frosted snow-glass plaque over a snowy photo; day banners use a deep-evergreen
  gradient over the photo; light Leaflet map tiles with evergreen+gold pins.
- **Fonts:** Cormorant Garamond (serif display) + Jost (sans body) — DNA from v1.
- **Layout:** screen-first, `max-width:1080px` `.wrap`, full-bleed photo banners,
  vertical gold timelines per day.

The v21 dark "Alpenglow Nocturne" theme is the same structure with a dark palette —
`retheme_white.py` shows the exact before/after if you ever want to revert or fork.

### Old print design (v1–v20, now in `itinerary_v1.html`)
Parchment `#F5F0E8`, forest green `#2C4A3E`, gold `#B08040`, single flowing
`.content`, print `@page` Letter. Kept only in the v1 file. The "NO red/warm cover
gradient" rule applied to that cover and is moot now (warmth lives in accents).
- **Layout:** ONE single flowing `<div class="content">` — content flows naturally,
  the browser/print engine handles page breaks. The user explicitly REJECTED splitting
  the doc into separate page cards (tried in v17, reverted). Keep it flowing.
- **Text weights:** lowest tier (`.time-note`, `.sub-value`, `.rest-grid-value`) is
  `font-weight: 400` — do not drop to 300 (too light, user flagged readability).

### Key CSS classes
- `.section-head` — large serif section title with gold underline (Travel, Lodging, etc.)
- `.sub-head` — small uppercase letterspaced label
- `.day-banner` — tan bar with gold left border, holds day number + theme
- `.day-intro` — italic gray paragraph introducing each day
- `.time-row` — 2-col grid: time/label on left (~0.95in), content right
- `.sub-item` — nested 2-col grid for detail rows inside a time block
- `.detail-table` — striped tan tables (rooms, drive times, lift tickets, lessons)
- `.rest-card` — restaurant marquee cards in the Restaurants section
- `.casual-table` — the casual restaurants table
- `.booking-item` — numbered booking reference entries
- `.badge` — confirmed (green) / urgent (rust) / tbd (gray) status pills
- `.time-note` — blue italic inline notes

---

## THE TRIP

- **Dates:** Dec 27, 2026 – Jan 3, 2027 (7 nights)
- **Party of 6:** Griffin (planner/host), Ruby (Griffin's girlfriend), Stella (Griffin's
  sister), Ben (Stella's boyfriend), Marcy (mom), Jim (dad)
- **Lodging:** 42 Nighthawk Drive, Red Mountain, Aspen CO 81611 — CONFIRMED, non-refundable

### Room assignments
- Primary suite (upstairs): **Jim + Marcy** — en suite, gas fireplace, loft adjoining
- Downstairs King: **Griffin + Ruby** — en suite
- Downstairs Queen: **Ben + Stella** — shared bath between them
- Pull-out / flex: lower living room, closeable, overflow

### Flights (5 booked seats; Ruby books + pays her own)
- Out: **AA 2357** · Sun Dec 27 · 8:29 AM DFW → 9:40 AM DEN · nonstop
- Return: **AA 1832** · Sun Jan 3 · 4:55 PM DEN → 8:00 PM DFW · nonstop
- Ruby travel TBD — assumed arriving morning of Dec 29 in time to ski Ajax

### Vehicle
- Chevrolet Suburban (or similar) · Turo · DEN pickup Dec 27 → return Jan 3 · ~$1,200 all-in

---

## DAY-BY-DAY (current structure)

- **Day 0 (Sun Dec 27) — Arrival:** Fly DFW→DEN, pick up Suburban, drive to Aspen
  (grocery stop City Market Glenwood Springs), check in 4 PM, **pick up Griffin's
  rentals at FMS Downtown 5:30 PM** (520 E Durant, open til 7 PM). **Welcome dinner = WILD FIG,
  7:30 PM — LOCKED IN** (315 E Hyman, Mediterranean, ~$50/pp). **Books TWO MONTHS out → reserve
  Tue Oct 27, 2026** — the earliest deadline on the whole list. Backup: Meat & Cheese (319 E
  Hopkins) is just as good and takes **no reservations** — walk in. Or cook in.
- **Day 1 (Mon Dec 28) — Buttermilk Lessons + Snowmass:** Marcy + Stella → Buttermilk
  beginner lesson #1. Griffin + Ben → Snowmass. Ruby not yet arrived. End of day: drop
  Griffin's skis at Snowmass corral requesting Ajax transfer; Ben + Ruby use paid FMS
  personal-equipment transfer. Dinner = **Casual** (White House Tavern / Meat & Cheese).
- **Day 2 (Tue Dec 29) — Ajax + Lessons #2:** Ruby arrives AM. Marcy + Stella → Buttermilk
  lesson #2. Griffin + Ruby + Ben → Ajax (pick up skis FMS Ajax 601 E Dean). Bonnie's
  lunch, optional Ajax Tavern après. End: drop at Ajax corral, request Highlands transfer.
  Dinner = **CASA TUA, 7:00 PM — LOCKED IN** (403 S Galena, Northern Italian, ~$200-250/pp,
  phone only (970) 920-7277, not on OpenTable). **Books exactly 30 days out → call Sun Nov 29,
  2026.** Caveat: the Aspen room is closed Oct 15–Dec 9, so the line may not answer on Nov 29 —
  keep calling daily until it does.
- **Day 3 (Wed Dec 30) — Snowmobile Day:** T-Lazy-7 Klondike Lunch snowmobile tour,
  **BOOKED (July 2026) exactly as planned: 9:30 AM departure, 3 doubles = $1,575
  ($262.50/pp, 3 drivers + 3 riders)**. ~2.5-3 hr, lunch + HELMETS ONLY; bring own warm
  clothing/boots/gloves. Back ~1:30.
  PM = downtown Aspen (galleries, Art Museum, shops; gondola is the bluebird alt). Dinner
  ~7:30 = **French Alpine Bistro** (411 E Hopkins, fondue/raclette) **or cook in** (fondue
  night). **Books exactly 30 days out → reserve on OpenTable Mon Nov 30, 2026.** Pine Creek Cookhouse is now the OPTIONAL splurge alternative, not the anchor.
  Changes/questions: (970) 925-4614.
  **GEAR (verified on official tlazy7.com): ranch provides HELMETS ONLY** — everyone
  (incl. Jim/non-skiers) brings their own warm ski-level clothing, snow/après boots, and
  gloves. Snowsuits sometimes available — call to confirm. (Aggregator sites wrongly say
  suits/boots provided; the official site says helmets only.) This means Jim DOES need
  outerwear for Day 3.
- **Day 4 (Thu Dec 31) — Highlands + NYE:** Pick up skis FMS Highlands. Ski Aspen
  Highlands. **Day 4 lunch = Merry-Go-Round** (casual mid-mtn Highlands, walk-in, ~$30/pp,
  (970) 429-3054); Cloud Nine party-lunch DROPPED (kept as optional aside). End: drop skis Highlands corral, request
  Snowmass transfer. **NYE dinner = MATSUHISA omakase, 8:00 PM** (~$280/pp, books exactly 30
  days out ~Dec 1 on OpenTable; cook-in is the fallback). 10:30 PM
  gondola plaza torchlight + fireworks (also visible from house deck). Midnight return:
  Suburban DD or Uber XL (no free taxi Thursday).
- **Day 5 (Fri Jan 1) — Hot Springs:** Iron Mountain Hot Springs, Glenwood Springs,
  12 PM timed entry ~$50/pp. Cook-in dinner.
- **Day 6 (Sat Jan 2) — Family Ski + Closing Dinner:** Pick up skis FMS Snowmass. All 6
  → Snowmass family ski day (optional). Return Griffin's rentals FMS Snowmass; Ben + Ruby
  collect own skis. **Closing dinner =
  STEAKHOUSE 316, 7:30 PM — LOCKED IN** (316 E Hopkins, ~$180/pp, OpenTable / (970) 920-1893).
  **Books exactly 30 days out → reserve Thu Dec 3, 2026.**
  High Mountain Taxi free Sat nights.
- **Day 7 (Sun Jan 3) — Departure:** Checkout 10 AM, depart 10:30, lunch Frisco/Vail,
  DEN 2:30, AA 1832 4:55 PM.

---

## SKI PLAN

| Person | Skiing | Tickets |
|--------|--------|---------|
| Jim | NOT skiing | Optional sightseeing gondola ~$50 |
| Marcy | Lessons Dec 28+29 | Lift included w/ lessons; 1-day passes after |
| Stella | Lesson Dec 28 ONLY (1 day) | Lift included w/ lesson; 4-day Flex Pass ~$679 |
| Griffin | Dec 28(opt),29,31,Jan2 | 4-day Flex Pass ~$679 |
| Ben | Dec 28,29,31,Jan2 | 4-day Flex Pass ~$679 · BRINGS OWN SKIS |
| Ruby | Dec 29,31,Jan2 (+1 banked) | 4-day Flex Pass ~$679 · BRINGS OWN SKIS |

- **No "3-day pass" exists** — Aspen sells 4-day Flex Passes. Everyone skiing 3-4 days
  gets the 4-day Flex Pass (~$679, no blackout dates, unused days bank as credit).
- Book 30+ days ahead · aspensnowmass.com · (877) 282-7736

### Ski rentals — Four Mountain Sports (FMS)
- **Griffin, Stella, and Marcy need rentals** (Ben + Ruby bring their own skis).
  Marcy + Stella's lesson-day rentals are INCLUDED with the Buttermilk lessons; they
  rent separately only for the ski days AFTER their lessons:
  Griffin ~4 days · **Stella 3 days (Dec 29/31/Jan 2)** · **Marcy 2 days (Dec 31/Jan 2)**.
  Pricing: Standard package ~$45–55/day (~$40–47 booked 24h ahead) → est. Stella ~$150,
  Marcy ~$100. Book at shop.aspensnowmass.com. Lives in the Ski Plan "Rentals & Transfer" card.
- All three use FMS mountain-to-mountain transfer: Griffin's is FREE (rental),
  Ben + Ruby pay a small per-transfer fee for personal equipment. Same corral drop.
  **Nobody loads skis in the car** between mountains.
- Transfer sequence: Snowmass(D1) → Ajax(D2) → Highlands(D4) → Snowmass(D6) → return
- Pick up rentals after 2 PM the day before at no charge. Boots/helmets stay with skier.
- Book: aspensnowmass.com/visit/rentals · 15% discount 24+ hrs ahead

### Lessons — Buttermilk
- Adult Beginner Group · Marcy: Dec 28 + 29 (both days) · Stella: Dec 28 ONLY (1 day) · 9:30 AM–3:30 PM
- Request multi-day cohort (same instructor both days). Lift + rentals included.
- ~$330/day · 3 lesson-days (Marcy 2 + Stella 1) = ~$990

### Ski clothing / outerwear rental (NEW — researched)
Four Mountain Sports is equipment-focused (sells apparel, not full outerwear rental). For
jackets/pants/layers use a dedicated clothing rental: **Suit Yourself** (Aspen specialist,
(970) 920-0295), **Kit Lender** (ships full kits to the house, kitlender.com), **Aspen
Collection** (premium, Gondola Plaza), **Miller Sports** (skis + apparel by the gondola).
Lives in the Ski Plan section under "Ski Clothing & Outerwear."
- Book late Sept 2026 · aspensnowmass.com/lessons · (877) 308-7859

---

## RESTAURANTS (own section in doc, before Booking Reference)

**Nothing is booked yet, but every night out is decided.** Day 0 = Wild Fig (Dec 27, 7:30 PM),
Day 2 = Casa Tua (Dec 29, 7 PM), Day 3 = French Alpine Bistro (Dec 30, 7:30 PM), NYE = Matsuhisa
(Dec 31, 8 PM), Day 6 = Steakhouse 316 (Jan 2, 7:30 PM).

**BOOKING WINDOWS — the whole point:** Wild Fig books **two months out (→ Oct 27, 2026)**; the
other four book **exactly 30 days out** → Casa Tua Nov 29 · French Alpine Nov 30 · Matsuhisa
~Dec 1 · Steakhouse 316 Dec 3. Pine Creek is the optional Day 3 splurge alternative.
**Meat & Cheese takes no reservations** — walk-in only, the backup for any night.

### Marquee cards in doc
- **Pine Creek Cookhouse** (Day 3 anchor) — see pricing below
- **Steakhouse 316** — 316 E Hopkins · ~$180/pp · OpenTable / (970) 920-1893 ·
  **DAY 6 CLOSING DINNER (locked in), Sat Jan 2 7:30 PM · books exactly 30 days out ≈ Dec 3**
- **Wild Fig** — 315 E Hyman · ~$50/pp · Mediterranean ·
  **DAY 0 WELCOME DINNER (locked in), Sun Dec 27 7:30 PM · books TWO MONTHS out ≈ Oct 27**
- **Matsuhisa** — 303 E Main · ~$280/pp omakase · OpenTable / (970) 544-6628 · **NYE dinner (the pick), 8:00 PM, books ~30 days out (≈ Dec 1)**
- **Bosq** — 312 S Mill · ~$275/pp 9-course · Tock opens 60 days prior 9 AM MST
  (= Nov 1, 2026 for Dec 31) · NYE option
- **Casa Tua** — 403 S Galena · ~$200-250/pp · phone only (970) 920-7277 · closed Oct 15-Dec 9 ·
  **DAY 2 DINNER (the pick), Tue Dec 29 7:00 PM · books exactly 30 days out ≈ Nov 29**
- **Cloud Nine Alpine Bistro** — mid-mountain Highlands · ~$150/pp · phone (970) 923-8715 ·
  Day 4 lunch · OPENS NOV 26, 2026 for the 26/27 season (it's currently closed only because
  the 25/26 season has ended — it WILL be open for the trip). Call Sept 2026. EXTREME difficulty.

### Casual options table
Ajax Tavern, White House Tavern, **Meat & Cheese (NO reservations — walk-in only, and good)**,
French Alpine Bistro, Wild Fig (now the Day 0 anchor),
Slope Side Tavern, Bonnie's (on-mtn Ajax), Base Camp (on-mtn Snowmass), The Cabin/Lynn Britt (Snowmass)

### Pine Creek Cookhouse — CONFIRMED PRICING (from official site screenshot)
Peak season Dec 21 – Jan 5:
- **Adult Sleigh: $235/pp** · Adult Ski/Snowshoe-in: $195/pp
- Beverages + 20% service charge + 6.9% sales tax NOT included
- True cost: **~$298/pp before drinks, ~$350-400/pp with wine, ~$2,100-2,400 for 6**
- **ALL guests arrive King Cabin Arrival Center at 6 PM** to check in (NOT Ashcroft trailhead)
- Ski area not open before 6 PM. 100% non-refundable for holiday/peak. Credit card required.
- pinecreekcookhouse.com · (970) 925-1044

---

## BOOKING REFERENCE (in doc — items [1]-[9] only; restaurants have their own section now)

- [1] Lodging — CONFIRMED
- [2] Flights — booking
- [3] Ruby travel — TBD
- [4] Suburban Turo — BOOK SOON
- [5] Lift tickets — 30+ days ahead
- [6] Ski rentals FMS — 24+ hrs ahead
- [7] Buttermilk lessons — Sept 2026
- [8] Iron Mountain Hot Springs — 1-2 wks ahead
- [10] Day 3 dinner French Alpine — to book, exactly 30 days out (Nov 30)
- [11] Day 2 dinner Casa Tua — to book, exactly 30 days out (Nov 29), phone only
- [12] Day 0 dinner Wild Fig — to book, TWO months out (Oct 27) — earliest deadline
- [13] Day 6 dinner Steakhouse 316 — to book, exactly 30 days out (Dec 3)
- [14] NYE dinner Matsuhisa — to book, exactly 30 days out (~Dec 1)
- [9] T-Lazy-7 snowmobile — BOOKED (Klondike Lunch · Dec 30 · 9:30 AM · 3 doubles · $1,575; now in the Locked In group)

---

## GETTING AROUND
- Chevrolet Suburban (or similar) primary
- Downtowner: free on-demand Aspen 10 AM–11 PM · (970) 705-4438
- High Mountain Taxi: free Fri/Sat from Rubey Park 12:30/1:00/1:30/2:00 AM · (970) 925-TAXI
- NYE midnight (Thu): no free taxi — Suburban DD or Uber XL ($40-80 surge)

---

## OPEN ITEMS / POSSIBLE NEXT ADDITIONS (user has not committed to these)
Claude previously suggested, user has not acted on:
1. NYE dinner = Matsuhisa (decided, 8:00 PM) — books 30 days out ~Dec 1 on OpenTable
2. Packing list (was removed earlier; could re-add as compact half-page)
3. Consolidated budget summary table
4. Contact / confirmation sheet (flight confirms, Turo host, reservation numbers)
5. Weather / what-to-wear note (Aspen Dec highs 20-35°F on mountain, layering)
6. Confirmed-vs-unconfirmed status tracker

Highest priority if asked: NYE dinner decision + contact sheet.

---

## VERSION HISTORY
- v7: best design — base for everything since
- v10: restaurants moved to end, booking ref cleaned of restaurant entries
- v11: lowest-tier text weight 300→400
- v12: rental logistics into day-by-day; Griffin skiing Day 1; Day 6 dinner→TBD
- v13: Ben brings own skis
- v14: Ben uses FMS transfer
- v15: Ruby uses FMS transfer
- v16: Pine Creek pricing corrected from screenshot
- v17: page-split experiment — REVERTED (user wants single flowing content)
- v18: restored to v16
- v19: Cloud Nine confirmed open (opens Nov 26, 2026)
- v20: Ruby ticket → 4-day Flex Pass (now preserved as `itinerary_v1.html`)
- v21: **MAJOR PIVOT** — full redesign to the screen-first interactive "Alpenglow
  Nocturne" cinematic dark theme. Clickable sticky top nav + scroll-spy, tabbed day
  panels (d0–d7) with vertical timelines, interactive Leaflet map of the valley,
  ~16 base64 photos sourced from Wikimedia Commons + Flickr (CC), photo lightbox,
  scroll-reveal, progress bar. Dropped the print/PDF workflow. v20 kept as the print
  base in `itinerary_v1.html`. Also fixed the Stella "3-day pass" booking-ref
  inconsistency (now 4-day Flex Pass, consistent with the ski plan).
  Photos are generic placeholders pending the user's real images (esp. the house).
- v22: retheme to the light **"White Christmas / NYE"** palette (snow white +
  evergreen + gold + cranberry, gold-sparkle accents, snowflake ornaments, light map
  tiles) via `retheme_white.py`. Swapped Lodging to the **real 42 Nighthawk great-room
  photo** (`photos/photo1.avif`).
- v23: **tabbed navigation** (`sectionize.py`). Long single-scroll → discrete panels;
  the fixed top bar switches sections (Travel · Lodging · Ski · Itinerary ·
  Restaurants · Booking · Map). Each `<section>` is a `.panel` (only the active one is
  `display:block`); clicking a nav item shows that panel and scrolls to its top under
  the bar (fixes the heading-hidden-under-nav bug via offset scroll). Days stay a
  second-tier sub-tab row inside the Itinerary panel. Darkened `--gold` to `#956E29`
  for legible labels; renamed Dining→Restaurants. Map uses `invalidateSize()` when its
  tab opens. Nav best practice: kept primary items to 7 and grouped the 8 days under
  Itinerary rather than flattening everything into one huge tab bar.
- v24: warmed the palette toward a subtle **beige/faded-parchment** feel (body bg +
  `--glass` cards + hero-scrim fade). Pure-white version backed up as
  `itinerary_white_backup.html` in case we revert. **Fixed the map:** it was
  initializing while its panel was `display:none` (0 size) so tiles never laid out —
  now lazy-inits on first Map-tab open with `invalidateSize()`+`fitBounds`. Also
  switched tiles from CARTO (unreachable here, HTTP 000) to **OpenStreetMap** with a
  `.leaflet-tile-pane` sepia filter so the map matches the parchment theme.
- v25/v26: warmed the nav/day-tab/floating-button bars off pure white to parchment;
  added subtle **edge snowfall** (`#snow` canvas, radial mask so it only shows at the
  edges, `prefers-reduced-motion` guarded). Added **Bar-Harbor-style framed photo
  plates** (`.photo-plate` — cream frame, corner brackets, sepia image, italic caption)
  placed *inside the highlight timeline item of each day* (the "coolest thing"), and
  **`.open-spot`** dashed placeholders at the undecided dinners (NYE, Day 6). Inline
  day-image slugs: `day0b day1b day2b day3b day4_highlands day5b rest_apres` (more in
  `assets_src/`). NOTE: headless screenshots of this ~16 MB file mis-paint fixed/hero
  elements — verify the hero/gate in a real browser or a truncated copy, not a tall
  headless capture.
- v27: (1) **Opening gate** (`#gate`, modeled on Bar Harbor's letter) — full-screen
  parchment card with a short description + "Enter the Itinerary" button; `body.gated`
  locks scroll until `#gateBtn` dismisses it. (2) **Booking** split into two shaded
  groups — green "Locked In" (`.bookcard.done`: [1][2]) and "Still To Book" ordered by
  urgency (`.now` red = [10][9][4], `.todo` amber = [7][5][6][8], `.pending` gray =
  [3]), each with a `.bstatus` pill. (3) Swapped hot-springs ([day5_springs] → Glenwood
  pool at night) and family-ski ([day6_family] → powder day) banner photos for cooler
  ones. (4) Day banners taller (min-height 380) and **fade into the page** via a bottom
  `mask-image`. (5) Photo-plate `figcaption` moved **inside** `.pp-frame`. (6) Day-tab
  numbers → **Roman numerals** (I–VII; Arrival stays 0). (7) Snow now mixes **❄ glyphs**
  (~40%) with dots and ~25% more density (`innerWidth/11`).
- v28: nav collapses to a labeled, pulsing **"☰ Menu"** button below 1100px (was 880)
  with `flex-wrap:nowrap` so links never wrap under the brand; **default tab is now
  Itinerary** (active class moved to `#itinerary`, JS default `'itinerary'`). Clicking a
  **day tab** now scrolls so the sticky day-nav sits at the top and the day's banner is
  just beneath it (`showDay` scrolls to the active `.daybanner` offset by daynav height).
  Day banners made smaller (min-height 310) with a softer multi-stop fade that melts into
  the page (title lifted via `padding-bottom:116px` to stay above the fade). **Snow** now
  covers the full screen (removed the edge mask), flakes given a soft slate shadow halo so
  white ❄ glyphs are visible on the light parchment.

### v29 — Budget tab + Booking Timeline
- New **Budget** tab/panel (`#budget`, in nav after Booking): two estimate tables
  (Activities & Logistics; Food & Drink) + subtotal/per-person card. Excludes lodging +
  flights (user's known costs). Estimate ~$13.5–17k excl. lodging/flights (~$2,250–2,850/pp).
- **Booking Timeline** table at the top of the Booking tab — chronological "When / Book /
  How", from now → Nov 1 (Bosq NYE Tock, the one hard deadline) → on-trip rentals.
- Nav is now 8 items (collapses to the Menu button below 1100px).

### v30 — Dark (navy) mode toggle
- Moon/sun button (`#themeToggle`) at the top-right of the nav (in `.nav-right`) toggles
  `body.dark`, persisted to `localStorage['aspenTheme']`; an inline script after `<body>`
  applies it pre-paint to avoid a flash. Map `invalidateSize()` fires on toggle.
- `body.dark { ... }` block (end of `<style>`) overrides the `:root` tokens with the deep
  navy/blue "Alpenglow Nocturne" palette + re-skins the hardcoded light surfaces (nav,
  hero scrim/plaque, gate, daynav/tabs, footer, photo-plate frame). Map tiles are inverted
  via CSS filter for a dark map. Light (white Christmas) remains the default.

### v31 — Signature visual pass + two new tabs + fixes
New reference/utility tabs, a "signature" visual layer, a shared motion system, and a batch
of dark-mode + data fixes. Nav is now **11 items** (Travel · Lodging · Ski · Itinerary ·
Restaurants · Booking · Budget · Contacts · Packing · Photos · Map — collapses to ☰ Menu
below 1100px; getting full on wide screens, a "More ▾" group is a future cleanup).
- **New tabs:** **Contacts** (`#contacts`) — tap-to-call `tel:` cards (emergency, travel,
  activities, dining, getting-around) with fill-in confirmation blanks; **Packing**
  (`#packing`) — forecast stat cells, the red snowmobile "helmets only / Jim needs outerwear"
  alert, 8 checklist columns; **Photos** (`#gallery`) — masonry grid built **in JS by reusing
  the image data-URIs already on the page** (`[data-full]` + inline `background-image`),
  deduped, lazy-loaded, reusing the existing lightbox (NO base64 duplicated → file stays ~19MB).
- **Booking dashboard** (`#statboard`) at top of Booking — counts `.bookcard.done/.now/.todo/
  .pending` live, animates a progress bar when the tab opens (MutationObserver).
- **Countdown:** gate ticker (D/H/M/S tiles) + a compact segmented nav pill (`#navCount`,
  centered via topnav `space-between`). States flip to "In Aspen · Day N" / "Until next time"
  (START `2026-12-27`, END `2027-01-03`). NOTE: the old hero "X days until Aspen" line was
  REMOVED as redundant (nav pill covers it); the `Mountains 4` hero stat was also removed.
- **Motion system:** `:root` tokens `--ease-out/-in-out/-spring` + `--dur-1/2/3` (all <300ms)
  + `--dur-amb` (18s). Route micro-interactions through these.
- **Signature visuals:** `#alpenglow` (fixed `z-index:-1` via `body{isolation:isolate}`) —
  drifting + hue-shifting gradient that tints through the glass panels; cool **aurora** in dark.
  `.hero-glow` (screen-blended alpenglow on the peaks). `.ridgelines` — 3 layered SVG mountain
  silhouettes at the hero base, parallaxed by the hero scroll handler (`data-speed` 0.34/0.2/
  0.08), theme-aware fills + snowcap stroke. `#grain` (fixed SVG-turbulence, `mix-blend
  overlay`/`soft-light`) + `.frostvig` (edge vignette) for printed texture.
- **Polish:** crafted **SVG weather icons** replace the emoji in `.wx-chip` (sun/snow/cloud,
  `currentColor`); **count-up** hero stats (`[data-count]`, fires on `aspen:enter` event from
  the gate); **tab crossfades** (`panelfade`/`fade` on `--dur-3`, day panels animate now);
  **two-depth parallax snow** (each flake has `z` → size/speed/sway/alpha/blur, drawn far→near).
- **Fixes:** dark-mode washouts — `.gate-btn` (was `var(--evergreen)` bg, which flips light in
  dark → gold-sparkle button now), day tabs, and `.chip` pills (had hardcoded white bg → dark
  override). **Cloud Nine fully removed** (restaurant card, Day 4 note, Budget, Contacts).
  **Home map pin** moved to the real coords `[39.205983, -106.822458]`.
- All new motion is `prefers-reduced-motion` guarded and dark-mode aware.

### v32 — Map redesign, immersive Lodging, NYE/eggs, nav consolidation
- **Map fully redesigned** (`#valley`): swapped OSM/sepia for **Esri World Imagery (satellite)** +
  a labels overlay (tile-pane filters overridden to show imagery true; dark mode just dims).
  Category-colored pins (mountains gold / activities blue / dining cranberry / home evergreen) via
  `CATCOL` in `pin()`, plus a **fly-to place rail** (`#mapRail`, built in JS from `places[]`): tap a
  chip → `flyTo` that spot + opens its popup. **Default view is the road-snapped Denver→Aspen drive**
  (`showDrive()` fetches OSRM geometry through DEN → City Market Glenwood → 42 Nighthawk, draws a gold
  line + 3 stop markers; falls back to `DRIVE_FALLBACK` polyline if the fetch fails; lazy + cached).
  "Whole valley" chip resets. Legend moved to top-right; caption sits below the map. The earlier
  ski-transfer "triangle" route was tried and REMOVED (looked half-baked).
- **Immersive Lodging** (`#lodging`): real house photos (from `photos/`, optimized via `sips` to
  ~1200px) embedded as an **elevated bento gallery** (`.bento` CSS grid-template-areas) below the
  location hero — great room (big tile), view, kitchen, deck, hot tub + night view, and a bedroom
  row tagged with the couple assignments (`.who` pill). Hover zoom + caption; click opens the
  lightbox. Tiles use `data-bt` (not `data-full`) so the image isn't duplicated — a `[data-bt]`
  handler opens the lightbox from the tile's own `<img src>`. (Keep base64 single-copy; file ~21MB.)
- **Photos gallery tab REMOVED** entirely (panel + nav + label + build script) — house photos live in
  the Lodging bento now. Panels are back to 10.
- **Nav consolidated** to **6 visible** (Travel · Lodging · Ski · Itinerary · Restaurants · Booking)
  plus a **"More ▾" dropdown** (`#navmore`: Budget · Contacts · Packing · Map). Hover/click reveals;
  shows the active underline when a child tab is open (MutationObserver `sync()`); flattens inline
  on mobile (<1100px). The submenu `<a>`s live inside `#navlinks` so the existing showTab/scroll-spy
  picks them up automatically.
- **Booking:** added an **"In progress"** state (blue `.bookcard.inprog` / `.bstatus.inprog` +
  dashboard tile + `sbProg` count). Suburban [4] → Locked In (Booked); T-Lazy-7 [9] → In progress
  (email sent, awaiting reply). Dashboard funnel is now Locked / In progress / Book now / To book / Waiting.
- **Toys:** **NYE fireworks** burst over the Day 4 banner (one-time, canvas, fires when `#d4` becomes
  active); **easter eggs** — click the hero snowflake (`#snowEgg`) or enter the Konami code → snow
  surge via `window.snowBurst()` (+ toast); **snow cursor trail** (desktop fine-pointer only, gold ❄
  drifting off the cursor, throttled + reduced-motion guarded).
- Removed the redundant hero "days until Aspen" line and the "Mountains 4" hero stat earlier in this arc.
- All `prefers-reduced-motion` guarded, dark-mode aware. Still pending/deferred: per-person checkable
  packing list, "Today" auto-focus mode.

---

## DEPLOYMENT / LIVE LINK

**Live page: https://griffinw1.github.io/Aspen-Trip/** (GitHub Pages).

This working folder (`/Users/griffinwright/code/Aspen Trip 2/`, file `itinerary.html`) is **NOT a
git repo**. The deploy is a **separate folder + repo**: `/Users/griffinwright/code/Aspen-Trip-deploy/`
→ remote `github.com/griffinw1/Aspen-Trip`. The deployed file there is named **`index.html`**.

**To publish updates:**
```
cp "itinerary.html" "../Aspen-Trip-deploy/index.html"
cd "../Aspen-Trip-deploy" && git add -A && git commit -m "..." && git push
```
Pushing to `origin/main` updates the live Pages site. **Edits in the working copy are NOT live
until copied to `index.html` and pushed** — always sync before claiming the live link is updated.

### v33 — Casa Tua locked for Day 2 + 30-day booking windows
- **Day 2 (Tue Dec 29) dinner is now Casa Tua**, 7:00 PM, party of 6 (was a generic "Nice Night"
  with Casa Tua / French Alpine / Wild Fig as options). Marked `.tl star` in the Day 2 timeline.
- **30-day reservation windows surfaced everywhere:** Casa Tua → **Sun Nov 29, 2026** (phone only,
  (970) 920-7277, not on OpenTable); French Alpine Bistro → **Mon Nov 30, 2026** (OpenTable);
  Matsuhisa NYE → ~Dec 1 (already there). Booking Timeline table now leads with those three
  chronological rows; the old "~Dec 9 Casa Tua (if you want it)" and "a few wks ahead French
  Alpine" rows are gone (ski-clothing kits split into their own row).
- **New booking card [11] Casa Tua** in "Still To Book" (`.todo`), placed above [10] French Alpine;
  [10] gained an explicit Book-date row. Added CSS `.bookcard .brow dd.warn` (rose italic) for the
  closed-Oct-15–Dec-9 caveat.
- Restaurants lead rewritten (nights chosen, none reserved, all three are 30-day windows); Casa Tua
  card retitled to the Day 2 pick; Contacts row retagged Day 2.
- **Budget:** "Casual dinners Days 1 & 2 ~$600" split into "Day 2 dinner · Casa Tua 6 × ~$225 =
  ~$1,350" + "Casual dinner Day 1 ~$300". Subtotal ~$12,800–16,300 → **~$13,850–17,350**;
  per-person ~$2,150–2,700 → **~$2,300–2,900**.
- **Map:** added a cranberry Casa Tua dining pin at [39.1888, -106.8203] (403 S Galena).

### v34 — All five dinners locked (nights chosen, booking windows dated)
Every night out now has a named restaurant, a time, and a **dated booking alarm**. Nothing is
actually reserved yet — the dates are when the window opens.

| Night | Restaurant | Window | Book on |
|---|---|---|---|
| Day 0 · Sun Dec 27 | **Wild Fig** (315 E Hyman, ~$50/pp) | **2 months out** | **Tue Oct 27, 2026** |
| Day 2 · Tue Dec 29 | **Casa Tua** (403 S Galena, ~$225/pp, phone only) | 30 days out | Sun Nov 29, 2026 |
| Day 3 · Wed Dec 30 | **French Alpine Bistro** (411 E Hopkins, ~$60/pp) | 30 days out | Mon Nov 30, 2026 |
| Day 4 · Thu Dec 31 | **Matsuhisa** (303 E Main, ~$280/pp omakase) | 30 days out | ~Tue Dec 1, 2026 |
| Day 6 · Sat Jan 2 | **Steakhouse 316** (316 E Hopkins, ~$180/pp) | 30 days out | Thu Dec 3, 2026 |

- **Day 0** welcome dinner changed from "Cook In" → Wild Fig, 7:30 PM (`.tl star`), with
  **Meat & Cheese named as the walk-in backup — it takes no reservations**, and cook-in still an out.
- **Day 6** "Nice Night Out · TBD" + its `.open-spot` placeholder → **Steakhouse 316, locked**.
  That was the last `.open-spot` in the file; there are now none.
- **Wild Fig marquee card** added as the first restcard — it has no photo, so its `.body` uses
  `style="grid-column:1/-1"` to span the 2-col `.restcard` grid. (Reuse that trick for photoless cards.)
- **Booking cards** now [1]–[14]: added [12] Wild Fig, [13] Steakhouse 316, [14] Matsuhisa (the NYE
  dinner had no card before). Still-To-Book order is the dinner cluster [12][11][10][13][14] then
  [7][5][6][8][3]. Statboard counts are live off the CSS classes, so no JS change needed.
- **Booking Timeline** table is fully chronological: Done · Done · Sept (lessons) · **Oct 27 Wild
  Fig** · Nov 29 Casa Tua · Nov 30 French Alpine · ~Dec 1 Matsuhisa · **Dec 3 Steakhouse** ·
  ~30 days lift tickets · clothing kits · hot springs · rentals. Dashboard `.sb-foot` rewritten.
- **Budget:** added "Day 0 dinner · Wild Fig 6 × ~$50 = ~$300". Subtotal **~$14,150–17,650**,
  per person **~$2,350–2,950**.
- **Map:** four new cranberry dining pins — Wild Fig [39.1892,-106.8195], Casa Tua
  [39.1888,-106.8203], Matsuhisa [39.1917,-106.8215], Steakhouse 316 [39.1905,-106.8202].
- **Contacts:** Wild Fig + Meat & Cheese ("walk-in, no reservations") rows added; Casa Tua and
  Steakhouse rows retagged with their day + date.
- Casual table: Meat & Cheese row now says **no reservations — walk-in only**; Wild Fig row
  points at Day 0.

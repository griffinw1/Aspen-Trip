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
- **`lodging` is now the REAL house photo** (the vaulted great room, from
  `photos/photo1.avif`). The restaurant + day-banner shots are still generic
  CC stand-ins the user may replace later.

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
- Cadillac Escalade ESV · Turo · DEN pickup Dec 27 → return Jan 3 · ~$1,200 all-in

---

## DAY-BY-DAY (current structure)

- **Day 0 (Sun Dec 27) — Arrival:** Fly DFW→DEN, pick up Escalade, drive to Aspen
  (grocery stop City Market Glenwood Springs), check in 4 PM, **pick up Griffin's
  rentals at FMS Downtown 5:30 PM** (520 E Durant, open til 7 PM), welcome dinner (cook in).
- **Day 1 (Mon Dec 28) — Buttermilk Lessons + Snowmass:** Marcy + Stella → Buttermilk
  beginner lesson #1. Griffin + Ben → Snowmass. Ruby not yet arrived. End of day: drop
  Griffin's skis at Snowmass corral requesting Ajax transfer; Ben + Ruby use paid FMS
  personal-equipment transfer. Dinner = **Casual** (White House Tavern / Meat & Cheese).
- **Day 2 (Tue Dec 29) — Ajax + Lessons #2:** Ruby arrives AM. Marcy + Stella → Buttermilk
  lesson #2. Griffin + Ruby + Ben → Ajax (pick up skis FMS Ajax 601 E Dean). Bonnie's
  lunch, optional Ajax Tavern après. End: drop at Ajax corral, request Highlands transfer.
  Dinner = **Nice Night** (Casa Tua rec).
- **Day 3 (Wed Dec 30) — Snowmobile Day:** T-Lazy-7 Klondike Lunch snowmobile tour 9 AM
  (4 hr, 3 doubles ~$1,575; lunch included; ranch provides suits/boots/helmets). Back ~1:30.
  PM = downtown Aspen (galleries, Art Museum, shops; gondola is the bluebird alt). Dinner
  ~7:30 = **French Alpine Bistro** (411 E Hopkins, fondue/raclette) **or cook in** (fondue
  night). Pine Creek Cookhouse is now the OPTIONAL splurge alternative, not the anchor.
  Snowmobile breakdown (in doc, Day 3 timeline + Booking [9]): **3 doubles = $1,575
  ($262.50/pp, current plan); 6 singles = $2,250 ($375/pp, +$675; all 6 must be 18+
  licensed)**. Klondike Lunch runs Tue–Sat 9:30 AM & 12:30 PM, ~2.5–3 hr, lunch +
  suits/boots/helmets included; scheduled tours may share the trail — ask for a PRIVATE
  tour for just our group. Book (970) 925-4614.
- **Day 4 (Thu Dec 31) — Highlands + NYE:** Pick up skis FMS Highlands. Ski Aspen
  Highlands. Cloud Nine lunch (call Sept 2026). End: drop skis Highlands corral, request
  Snowmass transfer. NYE dinner **TBD** (Matsuhisa / Bosq / Casa Tua / cook-in). 10:30 PM
  gondola plaza torchlight + fireworks (also visible from house deck). Midnight return:
  Escalade DD or Uber XL (no free taxi Thursday).
- **Day 5 (Fri Jan 1) — Hot Springs:** Iron Mountain Hot Springs, Glenwood Springs,
  12 PM timed entry ~$50/pp. Cook-in dinner.
- **Day 6 (Sat Jan 2) — Family Ski + Closing Dinner:** Pick up skis FMS Snowmass. All 6
  → Snowmass family ski day (optional). Return Griffin's rentals FMS Snowmass; Ben + Ruby
  collect own skis. Dinner = **Nice Night · TBD** (Steakhouse 316 rec, NOT locked).
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

**Nothing is locked/booked yet.** Pine Creek is the Day 3 anchor (pending reservation).
Steakhouse 316 is recommended for Day 6 but not booked. NYE dinner undecided.

### Marquee cards in doc
- **Pine Creek Cookhouse** (Day 3 anchor) — see pricing below
- **Steakhouse 316** — 316 E Hopkins · ~$180/pp · OpenTable / (970) 920-1893 · Day 6 rec
- **Matsuhisa** — 303 E Main · ~$280/pp omakase · OpenTable / (970) 544-6628 · NYE option
- **Bosq** — 312 S Mill · ~$275/pp 9-course · Tock opens 60 days prior 9 AM MST
  (= Nov 1, 2026 for Dec 31) · NYE option
- **Casa Tua** — 403 S Galena · ~$200-250/pp · phone only (970) 920-7277 · closed Oct 15-Dec 9
- **Cloud Nine Alpine Bistro** — mid-mountain Highlands · ~$150/pp · phone (970) 923-8715 ·
  Day 4 lunch · OPENS NOV 26, 2026 for the 26/27 season (it's currently closed only because
  the 25/26 season has ended — it WILL be open for the trip). Call Sept 2026. EXTREME difficulty.

### Casual options table
Ajax Tavern, White House Tavern, Meat & Cheese, French Alpine Bistro, Wild Fig,
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
- [4] Escalade Turo — BOOK SOON
- [5] Lift tickets — 30+ days ahead
- [6] Ski rentals FMS — 24+ hrs ahead
- [7] Buttermilk lessons — Sept 2026
- [8] Iron Mountain Hot Springs — 1-2 wks ahead
- [9] T-Lazy-7 snowmobile — BOOK NOW (90+ days, fills fast, 3129 Maroon Creek Rd, (970) 925-7040)

---

## GETTING AROUND
- Escalade ESV primary
- Downtowner: free on-demand Aspen 10 AM–11 PM · (970) 705-4438
- High Mountain Taxi: free Fri/Sat from Rubey Park 12:30/1:00/1:30/2:00 AM · (970) 925-TAXI
- NYE midnight (Thu): no free taxi — Escalade DD or Uber XL ($40-80 surge)

---

## OPEN ITEMS / POSSIBLE NEXT ADDITIONS (user has not committed to these)
Claude previously suggested, user has not acted on:
1. NYE dinner decision callout (Bosq Tock deadline Nov 1, 2026 9 AM MST is the hard date)
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

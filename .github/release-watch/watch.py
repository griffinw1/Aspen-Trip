"""Release-time watcher for the 5 Aspen dinners (runs on GitHub Actions, no computer needed).

Every ~60 s it checks, for the dates 29/30/31 days out (Mountain Time):
  SevenRooms (Wild Fig, Casa Tua, Steakhouse 316): slot types for party of 2 and party of 6
  OpenTable (French Alpine, Matsuhisa): "too far in advance" vs open (headless Chrome)
and appends a line to log.txt whenever a venue/date changes state. Runs until RUN_MINUTES are up.
"""
import json, os, time, urllib.request, datetime as dt
from zoneinfo import ZoneInfo

MT = ZoneInfo("America/Denver")
LOG = os.environ.get("WATCH_LOG", "log.txt")
RUN_MIN = float(os.environ.get("RUN_MINUTES", "348"))
END_DATE = os.environ.get("END_DATE", "2026-11-22")
SR = {"Wild Fig": "thewildfig", "Casa Tua": "casatuaaspen", "Steakhouse 316": "steakhouse316"}
OT = {"French Alpine Bistro": 228100, "Matsuhisa": 6946}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

def now(): return dt.datetime.now(MT)
def stamp(): return now().strftime("%a %b %d %H:%M:%S MT")
def log(line):
    with open(LOG, "a") as f: f.write(line + "\n")
    print(line, flush=True)

def sr_state(venue, date, party):
    url = ("https://www.sevenrooms.com/api-yoa/availability/ng/widget/range?venue=%s&party_size=%d&halo_size_interval=100"
           "&start_date=%s&num_days=1&channel=SEVENROOMS_WIDGET&exclude_pdr=true") % (venue, party, date)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        j = json.load(urllib.request.urlopen(req, timeout=25))
        times = [t for s in j["data"]["availability"].get(date, []) for t in s.get("times", [])]
        types = sorted({t.get("type") for t in times})
        book = sum(1 for t in times if t.get("type") == "book")
        return ("book%d" % book) if book else ("+".join(types) or "none")
    except Exception as e:
        return "error:" + type(e).__name__

_pw = _browser = None
def ot_state(rid, date):
    global _pw, _browser
    try:
        if _browser is None:
            from playwright.sync_api import sync_playwright
            _pw = sync_playwright().start()
            _browser = _pw.chromium.launch(channel="chromium", args=["--disable-blink-features=AutomationControlled", "--disable-http2"])
        ctx = _browser.new_context(user_agent=UA, locale="en-US", timezone_id="America/Denver", viewport={"width": 1280, "height": 900})
        ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
        p = ctx.new_page()
        resp = p.goto("https://www.opentable.com/restref/client/?rid=%d&restref=%d&datetime=%sT19:00&covers=6" % (rid, rid, date), timeout=45000, wait_until="domcontentloaded")
        if resp is not None and resp.status >= 400:
            ctx.close(); return "http%d" % resp.status
        p.wait_for_timeout(5000)
        txt = p.inner_text("body")
        ctx.close()
        if "that far in advance" in txt: return "too-far"
        if "Find a table" in txt or "Notify me" in txt: return "open"
        if "Access Denied" in txt or "blocked" in txt.lower(): return "blocked"
        return "unknown"
    except Exception as e:
        return "error:" + type(e).__name__ + ":" + str(e).splitlines()[0][:90]

def main():
    if now().date().isoformat() > END_DATE:
        print("watch window over"); return
    t_end = time.time() + RUN_MIN * 60
    last = {}
    log("== run start %s" % stamp())
    i = 0
    while time.time() < t_end:
        d0 = now().date()
        dates = [(d0 + dt.timedelta(days=k)).isoformat() for k in (29, 30, 31)]
        for name, v in SR.items():
            for d in dates:
                for party in (2, 6):
                    k = (name, d, party); st = sr_state(v, d, party)
                    if last.get(k) != st:
                        log("%s | %-20s | %s | party %d | %s -> %s" % (stamp(), name, d, party, last.get(k, "start"), st))
                        last[k] = st
        h = now().hour
        if i % 2 == 0 or h in (23, 0):     # OpenTable every 2 min, every minute around midnight
            for name, rid in OT.items():
                for d in dates:
                    k = (name, d, 6); st = ot_state(rid, d)
                    if last.get(k) != st:
                        log("%s | %-20s | %s | party 6 | %s -> %s" % (stamp(), name, d, last.get(k, "start"), st))
                        last[k] = st
        i += 1
        time.sleep(max(5, 60 - (time.time() % 60)))
    log("== run end %s" % stamp())

if __name__ == "__main__":
    main()

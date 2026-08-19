import json, os
from build import HEAD, topbar, nav, footer, page, write, OUT

with open(os.path.join(OUT, "menu-data.json")) as f:
    MENU = json.load(f)

# ---------------------------------------------------------------
# MENU PAGE
# ---------------------------------------------------------------
def dish_card(item):
    tags = item.get("t", [])
    tag_html = ""
    if tags:
        spans = "".join(f'<span class="tag{" new" if t=="New" else ""}">{t}</span>' for t in tags)
        tag_html = f'<div class="dish-tags">{spans}</div>'
    desc = f'<p class="dish-desc">{item["d"]}</p>' if item.get("d") else ""
    return f"""<div class="dish">
      <div class="dish-top">
        <span class="dish-name">{item['n']}</span>
        <span class="dish-leader"></span>
        <span class="dish-price">{item['p']}</span>
      </div>
      {desc}{tag_html}
    </div>"""

def line_row(item):
    return f'<div class="line-row"><span>{item["n"]}</span><span>{item["p"]}</span></div>'

def group_html(group, dense):
    head = f'<div class="sub-head">{group["head"]}</div>' if group.get("head") else ""
    note = f'<p style="font-size:13px;color:var(--ink-soft);margin:-4px 0 12px;">{group["note"]}</p>' if group.get("note") else ""
    if dense:
        body = f'<div class="line-list">{"".join(line_row(i) for i in group["items"])}</div>'
    else:
        body = f'<div class="card-grid">{"".join(dish_card(i) for i in group["items"])}</div>'
    return head + note + body

tab_buttons = []
panels = []
for i, cat in enumerate(MENU):
    active = " active" if i == 0 else ""
    tab_buttons.append(
        f'<button class="tab-btn{active}" data-idx="{i}"><span class="n">{i+1:02d}</span>{cat["name"]}</button>'
    )
    served = f'<p>{cat["served"]}</p>' if cat.get("served") else ""
    dense = cat["key"] in ("drinks", "wine", "beer", "spirits")
    groups_html = "".join(group_html(g, dense) for g in cat["groups"])
    panels.append(f"""<div class="panel{active}" data-idx="{i}">
      <div class="panel-intro"><h3>{cat['name']}</h3>{served}</div>
      {groups_html}
    </div>""")

menu_body = f"""
<div class="page-header">
  <div class="wrap">
    <div class="eyebrow">The full spread</div>
    <h1>Our Menu</h1>
    <p>Twelve sections, one tab bar &mdash; breakfast through to shooters. Tap a course to jump straight to it.</p>
  </div>
</div>

<section class="menu-section">
  <div class="tab-bar-outer">
    <div class="wrap"><div class="tab-bar" id="tabBar">{''.join(tab_buttons)}</div></div>
  </div>
  <div class="wrap" id="panels">
    {''.join(panels)}
    <p class="note">Prices correct as of the March 2026 printed menu. Kitchen may substitute seasonal items (e.g. avocado) without notice.</p>
  </div>
</section>

<script>
document.querySelectorAll('.tab-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const idx = btn.dataset.idx;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.idx === idx));
    document.querySelectorAll('.panel').forEach(p => p.classList.toggle('active', p.dataset.idx === idx));
    document.getElementById('panels').scrollIntoView({{behavior:'smooth', block:'start'}});
  }});
}});
</script>
"""

write("menu.html", page(
    "Menu — FORE at Kimiad",
    "The full FORE at Kimiad menu: breakfast, burgers, wood-fired pizza, mains, baskets, drinks and more.",
    "menu.html", menu_body
))

# ---------------------------------------------------------------
# INDEX / HOME PAGE
# ---------------------------------------------------------------
home_body = """
<header class="hero">
  <div class="hero-flag"></div>
  <div class="hero-flag two"></div>
  <div class="wrap">
    <div>
      <div class="eyebrow">Kimiad Golf Course &middot; Moreleta Park, Pretoria</div>
      <h1>Great food makes <em>good company.</em></h1>
      <p>Wood-fired pizza, proper burgers and a well-stocked bar, right on the fairway. Play a few rounds, then pull up a chair for the both of us.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="menu.html">Browse the menu</a>
        <a class="btn btn-ghost" href="contact.html">Find us</a>
      </div>
    </div>
    <div class="hero-card">
      <h3>Open today</h3>
      <ul>
        <li>Mon &ndash; Sat <b>09:30 &ndash; 20:30</b></li>
        <li>Sunday <b>09:30 &ndash; 18:00</b></li>
        <li>Kitchen <b>Kid-friendly, all day</b></li>
        <li>Bar <b>Fore Lager on tap</b></li>
      </ul>
    </div>
  </div>
</header>

<section class="strip">
  <div class="wrap">
    <div class="strip-item">
      <div class="strip-ico">&#127968;</div>
      <div><h4>Wood-fired, 28cm</h4><p>Double-zero flour, kneaded daily, fired the way the Italians make it &mdash; thin, crisp, blistered.</p></div>
    </div>
    <div class="strip-item">
      <div class="strip-ico">&#9917;</div>
      <div><h4>On the fairway</h4><p>Views over the Kimiad course from every table, indoors or out.</p></div>
    </div>
    <div class="strip-item">
      <div class="strip-ico">&#128118;</div>
      <div><h4>Kid-friendly, always</h4><p>A dedicated kids menu and space to run around while you finish your beer.</p></div>
    </div>
  </div>
</section>

<section class="menu-section" style="padding-bottom:70px;">
  <div class="wrap">
    <div class="menu-head">
      <div class="eyebrow">Crowd favourites</div>
      <h2>A taste of the menu</h2>
      <p>The full menu runs to twelve sections &mdash; here's what people order most.</p>
    </div>
    <div class="card-grid" style="margin-top:34px;">
      <div class="dish"><div class="dish-top"><span class="dish-name">Bag Rat a.k.a. 'The Caddie'</span><span class="dish-leader"></span><span class="dish-price">R122</span></div><p class="dish-desc">Pure beef burger, Fore sauce, guacamole, bacon & a slice of cheddar cheese.</p></div>
      <div class="dish"><div class="dish-top"><span class="dish-name">Pot Bunker</span><span class="dish-leader"></span><span class="dish-price">R110</span></div><p class="dish-desc">Wood-fired pizza with bacon and feta cheese.</p></div>
      <div class="dish"><div class="dish-top"><span class="dish-name">Trinchado</span><span class="dish-leader"></span><span class="dish-price">R82</span></div><p class="dish-desc">Beef strips cooked in a creamy peri-peri sauce, served with focaccia bread.</p></div>
      <div class="dish"><div class="dish-top"><span class="dish-name">Fore Platter</span><span class="dish-leader"></span><span class="dish-price">R446</span></div><p class="dish-desc">Our biggest sharing platter &mdash; ribs, wings, short rib, crumbed chicken and all the trimmings.</p></div>
    </div>
    <div style="text-align:center;margin-top:34px;">
      <a class="btn btn-rust" href="menu.html">See the full menu</a>
    </div>
  </div>
</section>

<section class="specials" id="specials">
  <div class="wrap" style="justify-content:center;">
    <div class="specials-head">
      <h2>Current specials</h2>
      <p>Also posted on our Facebook and Instagram.</p>
      <a class="btn btn-ghost" href="specials.html">See all specials</a>
    </div>

    <img src="images/current-specials.jpg" alt="FORE @ Kimiad current specials board" style="max-width:420px;width:100%;border-radius:var(--radius);border:1px solid rgba(255,255,255,.25);">
  </div>
</section>

<section class="func-section" style="padding-bottom:0;">
  <div class="wrap">
    <div class="func-banner" style="margin-top:0;">
      <div>
        <h3>Planning an event?</h3>
        <p>Marquee tent, braai buffet, lamb on the spit or a customised set menu &mdash; we host birthdays, functions and golf-day prize-givings.</p>
      </div>
      <a class="btn btn-primary" href="functions.html">See functions &amp; pricing</a>
    </div>
  </div>
</section>

<section class="info" id="contact">
  <div class="wrap">
    <div>
      <h2>Find us on the course</h2>
      <p class="lead">FORE at Kimiad sits inside Kimiad Golf Course, a short drive from Moreleta Park and Faerie Glen. Plenty of parking and outdoor seating.</p>
      <div class="info-card">
        <table class="hours">
          <tr><td>Monday &ndash; Saturday</td><td>09:30 &ndash; 20:30</td></tr>
          <tr><td>Sunday</td><td>09:30 &ndash; 18:00</td></tr>
        </table>
        <div class="contact-row"><div class="contact-ico">&#9742;</div><a href="tel:0878221857">087 822 1857</a></div>
        <div class="contact-row"><div class="contact-ico">&#9993;</div><a href="mailto:info@foreatkimiad.co.za">info@foreatkimiad.co.za</a></div>
        <div class="contact-row"><div class="contact-ico">&#128205;</div><span>711 Wekker Road, Moreleta Park, Pretoria</span></div>
      </div>
    </div>
    <div class="map-block" id="order">
      <div style="font-family:'Fraunces',serif;font-size:18px;color:var(--green);">Order for delivery or collection</div>
      <p style="margin:0;max-width:280px;">Live map embed goes here once you supply your Google Maps place link.</p>
      <div style="display:flex;gap:10px;">
        <a href="https://www.mrdfood.com/" class="btn btn-mrd">Mr D Food</a>
        <a href="https://www.ubereats.com/za" class="btn btn-green">Uber Eats</a>
      </div>
    </div>
  </div>
</section>
"""

write("index.html", page(
    "FORE at Kimiad — Golf course pub & grill, Moreleta Park",
    "Wood-fired pizza, burgers and a full bar at FORE at Kimiad, inside Kimiad Golf Course, Moreleta Park, Pretoria.",
    "index.html", home_body
))

# ---------------------------------------------------------------
# SPECIALS PAGE
# ---------------------------------------------------------------
specials_body = """
<div class="page-header">
  <div class="wrap">
    <div class="eyebrow">Updated regularly</div>
    <h1>Current Specials</h1>
    <p>Also posted to Facebook and Instagram &mdash; follow along so you never miss one. Valid until 27 August 2026, while stocks last.</p>
  </div>
</div>

<section class="menu-section" style="padding-top:56px;padding-bottom:50px;">
  <div class="wrap" style="display:grid;grid-template-columns:0.85fr 1.15fr;gap:40px;align-items:start;">
    <img src="images/current-specials.jpg" alt="FORE at Kimiad current specials board" style="border-radius:var(--radius);border:1px solid var(--border);width:100%;">

    <div>
      <div class="sub-head" style="margin-top:0;">Every day</div>
      <div class="dish">
        <div class="dish-top">
          <span class="dish-name">Kids cheese pizza + a kids shake</span>
          <span class="dish-leader"></span>
          <span class="dish-price">R56</span>
        </div>
      </div>

      <div class="sub-head">Mondays</div>
      <div class="dish">
        <div class="dish-top">
          <span class="dish-name">Bacon &amp; cheese pizza</span>
          <span class="dish-leader"></span>
          <span class="dish-price">R72</span>
        </div>
      </div>

      <div class="sub-head">Tuesdays</div>
      <div class="dish">
        <div class="dish-top">
          <span class="dish-name">Steak, egg &amp; chips</span>
          <span class="dish-leader"></span>
          <span class="dish-price">R91</span>
        </div>
      </div>

      <div class="sub-head">Wednesdays</div>
      <div class="dish">
        <div class="dish-top">
          <span class="dish-name">The Big Bird</span>
          <span class="dish-leader"></span>
          <span class="dish-price">R89</span>
        </div>
        <p class="dish-desc">Jumbo-sized bun, panko-crumbed chicken breast, cheddar, feta, bacon, avo, sauce and garnish, served with chips.</p>
      </div>

      <div class="sub-head">Mon &ndash; Thurs, 12:00 &ndash; 16:00</div>
      <div class="card-grid">
        <div class="dish">
          <div class="dish-top">
            <span class="dish-name">Toasted sandwich</span>
            <span class="dish-leader"></span>
            <span class="dish-price">R38</span>
          </div>
          <p class="dish-desc">Cheese &amp; tomato, ham cheese &amp; tomato, or chicken mayo.</p>
        </div>
        <div class="dish">
          <div class="dish-top">
            <span class="dish-name">Margherita pizza</span>
            <span class="dish-leader"></span>
            <span class="dish-price">R65</span>
          </div>
        </div>
        <div class="dish">
          <div class="dish-top">
            <span class="dish-name">Half chicken schnitzel</span>
            <span class="dish-leader"></span>
            <span class="dish-price">R68</span>
          </div>
          <p class="dish-desc">Served with sides.</p>
        </div>
      </div>

      <p class="note">T&rsquo;s &amp; C&rsquo;s apply &middot; valid until 27 August 2026 &middot; while stocks last &middot; no substitutions &middot; no takeaways.</p>
    </div>
  </div>
</section>

<section class="specials">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;">
    <div>
      <h2 style="color:#fff;font-size:24px;">Come say hello</h2>
      <p style="color:#CFE3D5;margin-top:8px;max-width:420px;font-size:14px;line-height:1.6;">No booking needed for specials &mdash; walk-ins are always welcome, on the course or off it.</p>
    </div>
    <a class="btn btn-primary" href="contact.html">Visit us &mdash; walk-ins accepted</a>
  </div>
</section>
"""
write("specials.html", page(
    "Specials — FORE at Kimiad",
    "Weekly food and drink specials at FORE at Kimiad, Moreleta Park.",
    "specials.html", specials_body
))

# ---------------------------------------------------------------
# FUNCTIONS PAGE
# ---------------------------------------------------------------
functions_body = """
<div class="page-header">
  <div class="wrap">
    <div class="eyebrow">Book Now</div>
    <h1>Events &amp; Functions</h1>
    <p>Birthdays, golf-day prize-givings, engagements or a Saturday get-together &mdash; we set up a marquee on the lawn and take care of the food.</p>
  </div>
</div>

<section class="func-section">
  <div class="wrap">
    <div class="func-banner" style="margin-top:0;">
      <div>
        <h3>Marquee tent &mdash; R1,300</h3>
        <p>Payable upfront to secure your date. Includes the marquee tent, tables, chairs, and white tablecloths. Want to decorate further? You're welcome to &mdash; that part's on your own budget.</p>
      </div>
      <a class="btn btn-primary" href="contact.html">Enquire &amp; book</a>
    </div>

    <div class="menu-head" style="margin-top:56px;text-align:left;max-width:none;">
      <div class="eyebrow">Food options</div>
      <h2>Choose how your guests eat</h2>
    </div>

    <div class="func-grid">
      <div class="func-card">
        <span class="pill">Per person</span>
        <h4>Braai Buffet</h4>
        <div class="price">R260 per person</div>
        <p>Steak, boerewors, and a piece of chicken. Plus pap &amp; sauce, fresh roll &amp; butter, potato salad, and a Greek salad.</p>
      </div>
      <div class="func-card">
        <span class="pill">Per person</span>
        <h4>Lamb on the Spit</h4>
        <div class="price">R270 per person</div>
        <p>&plusmn;350g of succulent spit-roast lamb, roast veggies, garlic roll, potato salad, and a Greek salad.</p>
      </div>
      <div class="func-card">
        <span class="pill">Snack style</span>
        <h4>Pizzas</h4>
        <div class="price">From the menu</div>
        <p>Choice of any pizza from our wood-fired menu. Popular as a snack option &mdash; we prepare a mix and everyone dishes a few slices.</p>
      </div>
      <div class="func-card">
        <span class="pill">Custom</span>
        <h4>Set Menu</h4>
        <div class="price">Designed for you</div>
        <p>Pick 2 burgers, 2&ndash;3 mains, and 2&ndash;3 pizzas from our menu, and we'll build a smaller, customised menu for your event.</p>
      </div>
      <div class="func-card">
        <span class="pill">On request</span>
        <h4>Platters</h4>
        <div class="price">Custom quote</div>
        <p>A few platters, customised to what you need, so everyone can dish for themselves.</p>
      </div>
    </div>

    <div class="func-banner">
      <div>
        <h3>Ready to lock in your date?</h3>
        <p>Call or email our manager with your date, guest count, and preferred food option. Marquee bookings are confirmed on receipt of payment.</p>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn btn-primary" href="tel:0878221857">Call 087 822 1857</a>
        <a class="btn btn-ghost" href="mailto:info@foreatkimiad.co.za">Email us</a>
      </div>
    </div>
  </div>
</section>
"""
write("functions.html", page(
    "Functions & Events — FORE at Kimiad",
    "Marquee tent hire, braai buffets, lamb on the spit and custom set menus for events at FORE at Kimiad.",
    "functions.html", functions_body
))

# ---------------------------------------------------------------
# GALLERY PAGE
# ---------------------------------------------------------------
gallery_labels = [
    "Marquee tent set up on the lawn", "Braai buffet spread", "Wood-fired pizza fresh from the oven",
    "The bar, stocked and ready", "Function tables & seating", "Charcuterie & snack platter",
    "Sunday family lunch on the deck", "Kimiad fairway view from the deck", "Weekend crowd on the patio",
]
tiles = "".join(f'<div class="gallery-tile">{label}<br><span style="opacity:.6;">— replace with your photo —</span></div>' for label in gallery_labels)

gallery_body = f"""
<div class="page-header">
  <div class="wrap">
    <div class="eyebrow">See it for yourself</div>
    <h1>Gallery</h1>
    <p>A look at the venue, the food, and past functions. Swap these placeholders for your own photos from Facebook and Instagram.</p>
  </div>
</div>

<section class="menu-section" style="padding-bottom:80px;">
  <div class="wrap">
    <div class="gallery-grid">{tiles}</div>
    <p class="note" style="margin-top:30px;">This page is set up with a 3-column responsive grid &mdash; drop in real JPGs at the same aspect ratio (square) and each tile will fill automatically. Happy to wire this up to your Instagram feed instead, so it updates itself.</p>
  </div>
</section>
"""
write("gallery.html", page(
    "Gallery — FORE at Kimiad",
    "Photos of the venue, food and functions at FORE at Kimiad, Moreleta Park.",
    "gallery.html", gallery_body
))

# ---------------------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------------------
contact_body = """
<div class="page-header">
  <div class="wrap">
    <div class="eyebrow">We'd love to have you</div>
    <h1>Contact &amp; Location</h1>
    <p>Book a table, ask about functions, or just find out today's hours.</p>
  </div>
</div>

<section class="info">
  <div class="wrap">
    <div>
      <div class="info-card">
        <h3 style="margin-bottom:16px;">Send us a message</h3>
        <form class="contact-form" onsubmit="event.preventDefault(); alert('This is a design demo — hook this form up to your email or a form service like Formspree to go live.');">
          <div>
            <label for="name">Name</label>
            <input id="name" type="text" placeholder="Your name" required>
          </div>
          <div>
            <label for="phone">Phone or email</label>
            <input id="phone" type="text" placeholder="087 000 0000 or you@email.com" required>
          </div>
          <div>
            <label for="reason">What's this about?</label>
            <select id="reason">
              <option>Booking a table</option>
              <option>Function / event enquiry</option>
              <option>Weekly specials by WhatsApp</option>
              <option>General question</option>
            </select>
          </div>
          <div>
            <label for="message">Message</label>
            <textarea id="message" placeholder="Tell us the date, group size, or your question"></textarea>
          </div>
          <button class="btn btn-rust" type="submit" style="align-self:flex-start;">Send message</button>
        </form>
      </div>
    </div>
    <div>
      <div class="info-card" style="margin-bottom:20px;">
        <table class="hours">
          <tr><td>Monday &ndash; Saturday</td><td>09:30 &ndash; 20:30</td></tr>
          <tr><td>Sunday</td><td>09:30 &ndash; 18:00</td></tr>
        </table>
        <div class="contact-row"><div class="contact-ico">&#9742;</div><a href="tel:0878221857">087 822 1857</a></div>
        <div class="contact-row"><div class="contact-ico">&#9993;</div><a href="mailto:info@foreatkimiad.co.za">info@foreatkimiad.co.za</a></div>
        <div class="contact-row"><div class="contact-ico">&#128205;</div><span>711 Wekker Road, Moreleta Park, Pretoria</span></div>
      </div>
      <div class="map-block" id="order">
        <div style="font-family:'Fraunces',serif;font-size:18px;color:var(--green);">Order for delivery or collection</div>
        <p style="margin:0;max-width:280px;">Live map embed goes here once you supply your Google Maps place link.</p>
        <div style="display:flex;gap:10px;">
          <a href="https://www.mrdfood.com/" class="btn btn-mrd">Mr D Food</a>
          <a href="https://www.ubereats.com/za" class="btn btn-green">Uber Eats</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write("contact.html", page(
    "Contact — FORE at Kimiad",
    "Get in touch with FORE at Kimiad, Moreleta Park — hours, phone, email, and directions.",
    "contact.html", contact_body
))

print("All pages written.")

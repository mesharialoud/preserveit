#!/usr/bin/env python3
"""Static site generator for preserveit.com (EN + AR). Run: python3 build.py <outdir>"""
import sys, os, json, datetime, urllib.parse

OUT = sys.argv[1] if len(sys.argv) > 1 else "../site"
BASE = "https://www.preserveit.com"
WHATSAPP = "96500000000"          # <-- replace with the real Kuwait WhatsApp number (country code, no +)
EMAIL = "hello@preserveit.com"
INSTAGRAM = "https://www.instagram.com/preserveit.kw"   # <-- replace when the handle is registered
TODAY = datetime.date.today().isoformat()

PAGES = {  # key: (filename, priority, changefreq)
    "home": ("index.html", "1.0", "weekly"),
    "safety": ("freeze-dried-breast-milk-safety.html", "0.8", "monthly"),
    "benefits": ("benefits.html", "0.8", "monthly"),
}

def url(lang, key):
    f = PAGES[key][0]
    path = "" if f == "index.html" else f
    return f"{BASE}/{'ar/' if lang=='ar' else ''}{path}"

def wa(lang):
    msg = "Hi Preserve It, I'd like to book a breast-milk freeze-drying pickup." if lang=="en" else "مرحبًا بريزيرف إت، أرغب في حجز استلام لتجفيف حليب الأم بالتجميد."
    return f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"

I = {  # inline icons
 "logo": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="15" fill="#366688"/><path d="M3 21 29 15v3L4 24z" fill="#89D0B1"/><path d="M16 6c4 5 7 8.6 7 12.4A7 7 0 0 1 9 18.4C9 14.6 12 11 16 6z" fill="#5AA6E5"/><path d="M17 22.6l8-1.6" stroke="#F4BBD1" stroke-width="2"/><circle cx="13.4" cy="18.6" r="1.9" fill="#fff" opacity=".6"/></svg>',
 "moon": '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
 "sun": '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "snow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2v20M4.9 7l14.2 10M4.9 17L19.1 7M9 4l3 2 3-2M9 20l3-2 3 2"/></svg>',
 "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.8 19.2L16 11l3.5-3.5a2.1 2.1 0 0 0-3-3L13 8 4.8 6.2 3 8l6.5 3.5L6 15H3l-1 1 4 2 2 4 1-1v-3l3.5-3.5L16 21z"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2L3 14h9l-1 8 10-12h-9z"/></svg>',
 "bowl": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 11h18a9 9 0 0 1-18 0zM8 7c0-1.5 1-2 1-3.5M12 7c0-1.5 1-2 1-3.5M16 7c0-1.5 1-2 1-3.5"/></svg>',
 "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8l-9-5-9 5 9 5 9-5zM3 8v8l9 5 9-5V8M12 13v8"/></svg>',
 "nose": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 3c4.97 0 9 4.03 9 9s-4.03 9-9 9-9-4.03-9-9 4.03-9 9-9zM8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
}

# ---------------------------------------------------------------- copy
T = {
"en": {
 "dir":"ltr","name":"Preserve It","sub":"Kuwait",
 "nav":[("home#how","How it works"),("home#offers","Offerings"),("safety","Safety"),("benefits","Benefits")],
 "other":"العربية","theme":"Toggle dark mode","menu":"Menu","skip":"Skip to content",
 "book":"Book a pickup","wa":"WhatsApp us",
 "foot_tag":"Kuwait's breast-milk freeze-drying studio. Your milk, returned to you as a shelf-stable powder — one mother, one batch.",
 "foot_h":["Explore","Learn","Contact"],
 "foot_learn":[("safety","Is it safe?"),("benefits","Long-term benefits"),("home#faq","FAQ")],
 "disc":"Preserve It returns each mother's own milk to her only. We do not sell, share or donate human milk. Information on this site is general and is not medical advice; speak to your paediatrician before using freeze-dried milk, especially for premature, newborn (under 3 months) or medically fragile babies.",
 "rights":"All rights reserved.",
 "hint":"Drag to rotate",
},
"ar": {
 "dir":"rtl","name":"بريزيرف إت","sub":"الكويت",
 "nav":[("home#how","كيف نعمل"),("home#offers","الباقات"),("safety","السلامة"),("benefits","الفوائد")],
 "other":"English","theme":"تبديل الوضع الداكن","menu":"القائمة","skip":"انتقل إلى المحتوى",
 "book":"احجزي الاستلام","wa":"تواصلي عبر واتساب",
 "foot_tag":"أول استوديو في الكويت لتجفيف حليب الأم بالتجميد. نعيد إليكِ حليبكِ مسحوقًا يُحفظ دون تبريد — أمٌّ واحدة، دفعةٌ واحدة.",
 "foot_h":["استكشفي","تعرّفي","تواصلي"],
 "foot_learn":[("safety","هل هو آمن؟"),("benefits","الفوائد على المدى الطويل"),("home#faq","الأسئلة الشائعة")],
 "disc":"تُعيد بريزيرف إت حليب كل أم إليها وحدها، ولا نبيع حليب الأم أو نتبادله أو نتبرع به. المعلومات الواردة في هذا الموقع عامة ولا تُعد استشارة طبية؛ يُرجى استشارة طبيب الأطفال قبل استخدام الحليب المجفف بالتجميد، خصوصًا للمواليد الخُدّج أو من هم دون ثلاثة أشهر أو ذوي الحالات الصحية الخاصة.",
 "rights":"جميع الحقوق محفوظة.",
 "hint":"اسحبي لتدوير المجسّم",
}}

HOME = {
"en": {
 "title":"Preserve It — Breast Milk Freeze-Drying in Kuwait",
 "desc":"Turn your frozen breast milk into a shelf-stable powder. Cold-chain pickup across Kuwait, one mother per batch, no additives, sealed and traceable pouches.",
 "eyebrow":"Breast-milk freeze-drying · Kuwait",
 "h1":"Your milk, <em>kept</em> for the months ahead.",
 "lead":"We gently freeze-dry the breast milk you've worked so hard to pump into a light, shelf-stable powder — no freezer, no ice packs, no additives. Just add water.",
 "chips":["One mother · one batch","Cold-chain pickup","No additives","Traceable pouches"],
 "cta2":"See offerings",
 "stats":[("~87%","of milk weight is water — removed"),("24–40 h","gentle low-temperature cycle"),("1 : 1","one mother per batch, always"),("0","preservatives or additives")],
 "how_k":"How it works","how_h":"From your freezer to your pantry in four steps",
 "how_p":"We collect your frozen milk, process it under a tracked protocol, and return it sealed and labelled — usually within 10–14 days.",
 "steps":[("Book","Choose an offering and book on WhatsApp. We send storage and packing tips for your frozen bags."),
          ("Cold-chain pickup","Our driver collects your milk frozen, in a temperature-logged cooler, anywhere in Kuwait. Drop-off is welcome too."),
          ("Gentle freeze-drying","Your milk is freeze-dried on dedicated, liner-lined trays under vacuum at low temperature — never mixed with anyone else's."),
          ("Sealed & returned","Powder is sealed in light- and oxygen-barrier pouches with your mother ID, batch number and a QR trace code.")],
 "off_k":"Offerings","off_h":"Three ways to preserve your milk",
 "off_p":"Every offering includes inspection, freeze-drying, moisture check, barrier packaging and a batch record. Prices are per ounce (30 ml) of liquid milk received.",
 "offers":[
  {"tag":"For everyday use","name":"The Stash","desc":"Multi-use pouches you scoop from to make any bottle size.","price":"0.300","unit":"KWD / oz",
   "ticks":["Large resealable pouches (~ 30 oz each)","Measuring scoop & mixing guide","Your own milk on your own dedicated trays","Drop-off or pickup (pickup fee applies)"],"cta":"Book The Stash"},
  {"tag":"Most chosen","name":"Single Serve","desc":"Pre-portioned sachets — one sachet, one bottle. Ideal for travel, nursery and work.","price":"0.400","unit":"KWD / oz","featured":True,
   "ticks":["Sachets portioned to 2, 4 or 6 oz","Keeps your bag notes and dates","Free cold-chain pickup in Kuwait","Travel-friendly pouch box"],"cta":"Book Single Serve"},
  {"tag":"Private & priority","name":"Private Batch","desc":"A whole machine cycle reserved for your milk alone, with priority turnaround.","price":"0.550","unit":"KWD / oz",
   "ticks":["The entire chamber runs only your milk","Express 5–7 day turnaround","Optional macronutrient analysis","Mix of pouches and sachets"],"cta":"Book Private Batch"},
 ],
 "off_fine":"Launch pricing. Minimum 40 oz per order. Final quote confirmed after we inspect your bags.",
 "why_k":"Why freeze-dry","why_h":"Made for real life in Kuwait",
 "why":[("snow","Free up the freezer","Months of milk in a pantry shelf — and no worry about power cuts in summer."),
        ("plane","Travel light","No ice, no cooler, no thawing. Pouches go in your hand luggage."),
        ("bowl","Mix into first foods","Sprinkle into purées and cereals from around six months, as your doctor advises."),
        ("nose","High-lipase milk","Many families report freeze-drying improves the soapy taste of high-lipase milk.")],
 "why_link":"All long-term benefits",
 "trust_k":"One mother · one batch","trust_h":"Your milk never meets anyone else's",
 "trust_p":"In Kuwait, where milk kinship matters, traceability isn't a feature — it's the foundation. Every bag is tracked from your door back to your door.",
 "chain":[("Your mother ID","Issued at booking and printed on every label."),("Sealed pickup cooler","Temperature-logged, tagged with your ID."),
          ("Inspection & weigh-in","Each bag is checked, counted and photographed for your record."),("Dedicated trays","Lined, labelled trays used for your milk only; machines sanitised between batches."),
          ("Moisture check & sealing","Barrier pouch, oxygen absorber, heat seal."),("QR batch record","Scan any pouch to see its batch history.")],
 "safety_k":"Safety first","safety_h":"Honest answers about safety",
 "safety_p":"Freeze-drying removes water; it does not sterilise. That's why we're strict about how milk is stored, handled and prepared. Read our full guide before you book.",
 "safety_link":"Read: Is freeze-dried breast milk safe?",
 "faq_k":"FAQ","faq_h":"Questions mothers ask us",
 "faq":[("How long does it take?","Each machine cycle runs roughly 24–40 hours. Including inspection, packing and delivery, most orders are returned within 10–14 days; Private Batch within 5–7 days."),
        ("How long does the powder last?","Sealed pouches are shelf-stable. We print a conservative best-before date of 18 months from processing. Once opened, use within 4 weeks and keep the pouch tightly closed."),
        ("Is anything added to my milk?","No. Nothing is added — no preservatives, fillers or additives. Only water is removed."),
        ("Can my milk be mixed with another mother's?","Never. Your milk stays on your own labelled trays and in your own pouches, and it is returned only to you. Private Batch reserves the whole machine for you."),
        ("How do I prepare a bottle?","Use the ratio on your label with boiled water cooled to a safe temperature, shake gently, and feed within 2 hours. Your paediatrician's guidance comes first."),
        ("How old can my frozen milk be?","Best results come from milk frozen within the last 6 months and kept at −18 °C or colder. Milk up to 12 months old is accepted."),
        ("Is it suitable for premature or newborn babies?","Freeze-dried milk is not sterile. For premature babies, babies under 3 months or medically fragile babies, please speak to your doctor first.")],
 "band_h":"Ready to free up your freezer?","band_p":"Message us on WhatsApp — we'll answer your questions and schedule your pickup.",
},
"ar": {
 "title":"بريزيرف إت — تجفيف حليب الأم بالتجميد في الكويت",
 "desc":"حوّلي حليبكِ المجمّد إلى مسحوق يُحفظ دون تبريد. استلام مبرّد في جميع مناطق الكويت، دفعة مستقلة لكل أم، بلا أي إضافات، وأكياس محكمة قابلة للتتبّع.",
 "eyebrow":"تجفيف حليب الأم بالتجميد · الكويت",
 "h1":"حليبكِ… <em>محفوظ</em> للأشهر القادمة.",
 "lead":"نجفّف حليبكِ الذي تعبتِ في جمعه بالتجميد وبلطف، ليصبح مسحوقًا خفيفًا يُحفظ دون فريزر أو ثلج أو أي إضافات. أضيفي الماء فقط.",
 "chips":["أمٌّ واحدة · دفعةٌ واحدة","استلام بسلسلة تبريد","بلا إضافات","أكياس قابلة للتتبّع"],
 "cta2":"اطّلعي على الباقات",
 "stats":[("~87%","من وزن الحليب ماء — نزيله"),("24–40 ساعة","دورة لطيفة بحرارة منخفضة"),("1 : 1","أمٌّ واحدة لكل دفعة دائمًا"),("0","مواد حافظة أو إضافات")],
 "how_k":"كيف نعمل","how_h":"من الفريزر إلى رفّ المطبخ في أربع خطوات",
 "how_p":"نستلم حليبكِ مجمّدًا، ونعالجه وفق بروتوكول موثّق، ثم نعيده إليكِ محكم الإغلاق ومُعنونًا — عادةً خلال 10 إلى 14 يومًا.",
 "steps":[("الحجز","اختاري الباقة واحجزي عبر واتساب، ونرسل لكِ إرشادات حفظ وتجهيز أكياس الحليب المجمّد."),
          ("استلام مبرّد","يستلم مندوبنا حليبكِ مجمّدًا في حافظة مسجّلة الحرارة من أي منطقة في الكويت، ويمكنكِ أيضًا تسليمه بنفسك."),
          ("تجفيف لطيف بالتجميد","يُجفَّف حليبكِ على صوانٍ مخصّصة ومبطّنة تحت التفريغ وبحرارة منخفضة، ولا يُخلط أبدًا بحليب أي أم أخرى."),
          ("إغلاق وتسليم","يُعبّأ المسحوق في أكياس عازلة للضوء والأكسجين، وعليها رقمكِ ورقم الدفعة ورمز QR للتتبّع.")],
 "off_k":"الباقات","off_h":"ثلاث طرق لحفظ حليبكِ",
 "off_p":"تشمل كل باقة الفحص والتجفيف بالتجميد وقياس الرطوبة والتغليف العازل وسجلّ الدفعة. الأسعار لكل أونصة (30 مل) من الحليب السائل المستلَم.",
 "offers":[
  {"tag":"للاستخدام اليومي","name":"المخزون","desc":"أكياس كبيرة متعددة الاستخدام تأخذين منها بالمغرفة لتحضير أي كمية.","price":"0.300","unit":"د.ك / أونصة",
   "ticks":["أكياس كبيرة قابلة لإعادة الغلق (~ 30 أونصة)","مغرفة قياس ودليل تحضير","حليبكِ وحده على صوانيكِ المخصّصة","تسليم ذاتي أو استلام (برسوم)"],"cta":"احجزي المخزون"},
  {"tag":"الأكثر طلبًا","name":"الجرعة الواحدة","desc":"أظرف مقسّمة مسبقًا — ظرف واحد لرضعة واحدة. مثالية للسفر والحضانة والعمل.","price":"0.400","unit":"د.ك / أونصة","featured":True,
   "ticks":["أظرف بحجم 2 أو 4 أو 6 أونصات","نحافظ على تواريخ وملاحظات أكياسكِ","استلام مبرّد مجاني داخل الكويت","علبة سفر أنيقة"],"cta":"احجزي الجرعة الواحدة"},
  {"tag":"خاصة وبأولوية","name":"الدفعة الخاصة","desc":"دورة كاملة في الجهاز مخصّصة لحليبكِ وحده، مع أولوية في التسليم.","price":"0.550","unit":"د.ك / أونصة",
   "ticks":["الجهاز بالكامل لحليبكِ فقط","تسليم سريع خلال 5–7 أيام","تحليل اختياري للمغذيات الكبرى","مزيج من الأكياس والأظرف"],"cta":"احجزي الدفعة الخاصة"},
 ],
 "off_fine":"أسعار الإطلاق. الحد الأدنى 40 أونصة للطلب. يُؤكَّد السعر النهائي بعد فحص الأكياس.",
 "why_k":"لماذا التجفيف بالتجميد","why_h":"مصمَّم لحياة الأم في الكويت",
 "why":[("snow","فريزر أوسع","مخزون أشهر على رفّ واحد — دون قلق من انقطاع الكهرباء في الصيف."),
        ("plane","سفر أخف","لا ثلج ولا حافظة ولا إذابة. الأكياس ترافقكِ في حقيبة اليد."),
        ("bowl","مع أول طعام صلب","يُرشّ على الهريس والحبوب من عمر ستة أشهر تقريبًا، وفق توجيه الطبيب."),
        ("nose","حليب عالي الليباز","تذكر عائلات كثيرة أن التجفيف يحسّن الطعم الصابوني للحليب عالي الليباز.")],
 "why_link":"جميع الفوائد على المدى الطويل",
 "trust_k":"أمٌّ واحدة · دفعةٌ واحدة","trust_h":"حليبكِ لا يلتقي بحليب أحدٍ غيركِ",
 "trust_p":"في الكويت، حيث للرضاعة أحكامها، التتبّع ليس ميزة إضافية بل هو الأساس. نتتبّع كل كيس من باب بيتكِ وحتى عودته إليه.",
 "chain":[("رقم الأم","يُصدر عند الحجز ويُطبع على كل ملصق."),("حافظة استلام مختومة","مسجّلة الحرارة وتحمل رقمكِ."),
          ("فحص ووزن","يُفحص كل كيس ويُعدّ ويُصوَّر لسجلّكِ."),("صوانٍ مخصّصة","صوانٍ مبطّنة ومُعنونة لحليبكِ وحده، وتعقيم الأجهزة بين الدفعات."),
          ("قياس الرطوبة والإغلاق","كيس عازل، وماصّ أكسجين، وإغلاق حراري."),("سجلّ الدفعة برمز QR","امسحي أي كيس لمعرفة تاريخ دفعته.")],
 "safety_k":"السلامة أولًا","safety_h":"إجابات صادقة عن السلامة",
 "safety_p":"التجفيف بالتجميد يزيل الماء لكنه لا يعقّم؛ لذلك نلتزم بصرامة في طريقة حفظ الحليب ونقله وتحضيره. اقرئي دليلنا الكامل قبل الحجز.",
 "safety_link":"اقرئي: هل حليب الأم المجفف بالتجميد آمن؟",
 "faq_k":"الأسئلة الشائعة","faq_h":"أسئلة تطرحها الأمهات",
 "faq":[("كم تستغرق العملية؟","تستغرق دورة الجهاز الواحدة نحو 24 إلى 40 ساعة. وبإضافة الفحص والتعبئة والتوصيل، تُعاد معظم الطلبات خلال 10 إلى 14 يومًا، والدفعة الخاصة خلال 5 إلى 7 أيام."),
        ("كم يدوم المسحوق؟","الأكياس المغلقة تُحفظ في درجة حرارة الغرفة. نطبع تاريخ «يُفضَّل استخدامه قبل» بعد 18 شهرًا من المعالجة بشكل متحفّظ. بعد الفتح، استخدميه خلال 4 أسابيع مع إحكام الإغلاق."),
        ("هل يُضاف أي شيء إلى حليبي؟","لا. لا نضيف أي مواد حافظة أو مالئة أو إضافات؛ نزيل الماء فقط."),
        ("هل يمكن أن يُخلط حليبي بحليب أم أخرى؟","أبدًا. يبقى حليبكِ على صوانيكِ المُعنونة وفي أكياسكِ الخاصة، ولا يُعاد إلا إليكِ. وفي الدفعة الخاصة يُخصَّص الجهاز بالكامل لكِ."),
        ("كيف أحضّر الرضعة؟","استخدمي النسبة المدوّنة على الملصق مع ماء مغليّ مبرّد إلى حرارة آمنة، ثم رجّي بلطف وأطعمي الطفل خلال ساعتين. وتوجيهات طبيب الأطفال لها الأولوية."),
        ("ما أقصى عمر للحليب المجمّد؟","أفضل النتائج للحليب المجمّد خلال آخر 6 أشهر والمحفوظ عند −18 °م أو أبرد. نقبل الحليب حتى عمر 12 شهرًا."),
        ("هل يناسب الخُدّج وحديثي الولادة؟","الحليب المجفف بالتجميد غير معقّم. للأطفال الخُدّج أو من هم دون ثلاثة أشهر أو ذوي الحالات الصحية الخاصة، يُرجى استشارة الطبيب أولًا.")],
 "band_h":"مستعدة لتفريغ الفريزر؟","band_p":"راسلينا عبر واتساب — نجيب عن أسئلتكِ ونحدّد موعد الاستلام.",
}}

SAFETY = {
"en": {
 "title":"Is Freeze-Dried Breast Milk Safe? An Honest Guide | Preserve It",
 "desc":"What freeze-drying does to breast milk, what it doesn't do, who should check with a doctor first, and how to store and prepare it safely.",
 "kicker":"Safety guide","h1":"Is freeze-dried breast milk safe?",
 "meta":["Updated "+TODAY,"8 min read","Reviewed against CDC storage guidance"],
 "toc":"On this page",
 "sections":[
  ("what","What freeze-drying actually is",
   "<p>Freeze-drying (also called <strong>lyophilisation</strong>) is a three-stage process used for decades in food and pharmaceuticals:</p>"
   "<ol><li><strong>Freezing</strong> — the milk is frozen solid at very low temperature.</li>"
   "<li><strong>Vacuum</strong> — the chamber pressure is lowered dramatically.</li>"
   "<li><strong>Sublimation</strong> — gentle heat turns the ice straight into vapour, without the milk ever becoming liquid again. A final dry phase removes remaining bound moisture.</li></ol>"
   "<p>Because no high heat is used, freeze-drying is considered gentler than heat-drying. Breast milk is roughly 87% water, so what remains is a light, fine powder.</p>"),
  ("keeps","What it preserves — and what research says",
   "<p>Published reviews report that freeze-drying largely retains the fat, protein and calorie content of human milk. Researchers also note that evidence is still limited, particularly for premature babies, and more clinical studies are needed.</p>"
   "<p>Freeze-drying pauses enzyme activity by removing water. That's why many families with <strong>high-lipase milk</strong> (milk that tastes soapy after freezing) find the powder more acceptable to their baby.</p>"
   "<div class='callout'><b>Our honest position</b><p>Fresh breast milk remains the gold standard. Freeze-drying is a storage method — a way to keep milk you've already frozen — not an upgrade to your milk.</p></div>"),
  ("not","What freeze-drying does <em>not</em> do",
   "<ul><li><strong>It does not sterilise.</strong> Like any powdered feed, freeze-dried milk is not sterile; bacteria present before processing are not reliably removed.</li>"
   "<li><strong>It is not formally regulated yet.</strong> In the US the FDA does not regulate breast-milk freeze-drying services specifically, and neither the CDC nor the AAP has an official position on it.</li>"
   "<li><strong>It cannot fix poorly stored milk.</strong> The final product is only as good as the milk that goes in.</li></ul>"
   "<div class='callout warn'><b>Check with your doctor first if your baby is:</b><p>premature, under 3 months old, or has a weakened immune system or other medical condition. These babies are more vulnerable to contamination in any prepared feed.</p></div>"),
  ("protocol","How we protect your milk",
   "<div class='tbl-wrap'><table class='tbl'><thead><tr><th>Stage</th><th>Our standard</th></tr></thead><tbody>"
   "<tr><td>Before pickup</td><td>Milk kept frozen at −18 °C or colder; we accept milk up to 12 months old (within 6 months is best).</td></tr>"
   "<tr><td>Transport</td><td>Sealed, temperature-logged cooler tagged with your mother ID. Bags that arrive thawed are not processed.</td></tr>"
   "<tr><td>Intake</td><td>Every bag inspected, weighed and photographed; damaged or unlabelled bags are set aside and discussed with you.</td></tr>"
   "<tr><td>Processing</td><td>Food-grade lined trays dedicated to one mother; trays and chambers cleaned and sanitised between batches. Staff follow food-handler hygiene rules.</td></tr>"
   "<tr><td>Quality check</td><td>Powder must be fully dry before packing; any batch that fails the dryness check is re-run.</td></tr>"
   "<tr><td>Packaging</td><td>Light- and oxygen-barrier pouches with food-grade oxygen absorbers, heat-sealed and labelled with batch ID and QR trace.</td></tr>"
   "</tbody></table></div>"),
  ("prepare","How to prepare it safely at home",
   "<ol><li>Wash your hands and use clean, sterilised bottles.</li>"
   "<li>Use the water-to-powder ratio printed on your label. Use boiled water cooled to a safe temperature, as your paediatrician recommends.</li>"
   "<li>Add powder to water, swirl gently until dissolved. Never microwave a prepared bottle.</li>"
   "<li>Feed within 2 hours. If you refrigerate a prepared bottle, use it within 24 hours. Discard leftovers after a feed. Never refreeze.</li></ol>"
   "<p>Getting the ratio right matters: too little water concentrates the milk, too much dilutes it. Always measure — don't estimate.</p>"),
  ("store","Storing your powder",
   "<p>Keep sealed pouches in a cool, dry, dark cupboard — not in a hot car or near the stove. Kuwait summers matter here: avoid storing pouches anywhere that gets hot. Once opened, squeeze out the air, close the zip tightly and use within 4 weeks.</p>"
   "<p>Industry services commonly advertise shelf lives of up to three years. Independent long-term data is still limited, so we print a conservative <strong>best-before of 18 months</strong>.</p>"),
  ("refs","Sources",
   "<ol class='refs'>"
   "<li><a href='https://www.cdc.gov/breastfeeding/breast-milk-preparation-and-storage/handling-breastmilk.html' rel='noopener'>CDC — Proper storage and preparation of breast milk</a></li>"
   "<li><a href='https://link.springer.com/article/10.1038/s41372-023-01861-8' rel='noopener'>Journal of Perinatology (2023) — Scoping review: freeze-drying and human milk</a></li>"
   "<li><a href='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12526076/' rel='noopener'>Nutrients (2025) — Freeze-dried donor milk fortification in preterm infants</a></li>"
   "<li><a href='https://aeroflowbreastpumps.com/care-guides/post/freeze-dry-breast-milk' rel='noopener'>Aeroflow Breastpumps — Freeze-dried breast milk care guide</a></li>"
   "<li><a href='https://www.romper.com/parenting/freeze-dried-breast-milk' rel='noopener'>Romper — Paediatricians on freeze-dried breast milk</a></li>"
   "</ol>"),
 ],
 "end_h":"Still have questions?","end_p":"Ask us anything on WhatsApp before you book — or bring your paediatrician's questions to us.",
},
"ar": {
 "title":"هل حليب الأم المجفف بالتجميد آمن؟ دليل صادق | بريزيرف إت",
 "desc":"ماذا يفعل التجفيف بالتجميد بحليب الأم وما لا يفعله، ومن يجب أن يستشير الطبيب أولًا، وكيف يُحفظ ويُحضَّر بأمان.",
 "kicker":"دليل السلامة","h1":"هل حليب الأم المجفف بالتجميد آمن؟",
 "meta":["آخر تحديث "+TODAY,"قراءة 8 دقائق","وفق إرشادات CDC لحفظ الحليب"],
 "toc":"في هذه الصفحة",
 "sections":[
  ("what","ما هو التجفيف بالتجميد فعلًا",
   "<p>التجفيف بالتجميد (ويُسمّى <strong>الليوفيلة</strong>) عملية من ثلاث مراحل تُستخدم منذ عقود في صناعة الغذاء والدواء:</p>"
   "<ol><li><strong>التجميد</strong> — يُجمَّد الحليب تمامًا بدرجة حرارة منخفضة جدًا.</li>"
   "<li><strong>التفريغ</strong> — يُخفَّض الضغط داخل الحجرة بشكل كبير.</li>"
   "<li><strong>التسامي</strong> — حرارة لطيفة تحوّل الجليد إلى بخار مباشرة دون أن يعود الحليب سائلًا، ثم مرحلة تجفيف نهائية تزيل ما تبقّى من رطوبة.</li></ol>"
   "<p>ولأنه لا يعتمد على حرارة عالية، يُعدّ التجفيف بالتجميد ألطف من التجفيف الحراري. ويتكوّن حليب الأم من نحو 87% ماء، فيتبقّى مسحوق ناعم وخفيف.</p>"),
  ("keeps","ما الذي يحافظ عليه — وماذا تقول الأبحاث",
   "<p>تشير المراجعات العلمية المنشورة إلى أن التجفيف بالتجميد يحافظ إلى حدّ كبير على الدهون والبروتين والسعرات في حليب الأم، مع تأكيد الباحثين أن الأدلة ما زالت محدودة، خصوصًا للأطفال الخُدّج، وأن هناك حاجة لمزيد من الدراسات السريرية.</p>"
   "<p>يوقف التجفيف نشاط الإنزيمات مؤقتًا بإزالة الماء؛ ولهذا تجد عائلات كثيرة لديها <strong>حليب عالي الليباز</strong> (الذي يصبح طعمه صابونيًا بعد التجميد) أن المسحوق أكثر قبولًا لدى أطفالها.</p>"
   "<div class='callout'><b>موقفنا بصراحة</b><p>يبقى حليب الأم الطازج هو الخيار الأمثل. التجفيف بالتجميد وسيلة لحفظ حليب سبق تجميده، وليس تحسينًا للحليب نفسه.</p></div>"),
  ("not","ما الذي <em>لا</em> يفعله التجفيف بالتجميد",
   "<ul><li><strong>لا يعقّم الحليب.</strong> مثل أي غذاء مجفف يُعاد تحضيره، الحليب المجفف بالتجميد غير معقّم، ولا يُضمن التخلّص من البكتيريا الموجودة قبل المعالجة.</li>"
   "<li><strong>لا يخضع بعد لتنظيم خاص.</strong> في الولايات المتحدة لا تنظّم إدارة الغذاء والدواء (FDA) خدمات تجفيف حليب الأم تحديدًا، وليس لمراكز CDC ولا للأكاديمية الأمريكية لطب الأطفال (AAP) موقف رسمي منها.</li>"
   "<li><strong>لا يُصلح حليبًا حُفظ بطريقة خاطئة.</strong> جودة المنتج النهائي من جودة الحليب الذي يدخل الجهاز.</li></ul>"
   "<div class='callout warn'><b>استشيري الطبيب أولًا إذا كان طفلكِ:</b><p>من الخُدّج، أو دون ثلاثة أشهر، أو لديه ضعف في المناعة أو حالة صحية خاصة؛ فهؤلاء أكثر عرضة لأي تلوّث في الرضعات المُحضَّرة.</p></div>"),
  ("protocol","كيف نحمي حليبكِ",
   "<div class='tbl-wrap'><table class='tbl'><thead><tr><th>المرحلة</th><th>معيارنا</th></tr></thead><tbody>"
   "<tr><td>قبل الاستلام</td><td>حفظ الحليب مجمّدًا عند −18 °م أو أبرد؛ نقبل الحليب حتى عمر 12 شهرًا (والأفضل خلال 6 أشهر).</td></tr>"
   "<tr><td>النقل</td><td>حافظة مختومة مسجّلة الحرارة تحمل رقم الأم. الأكياس التي تصل ذائبة لا تتم معالجتها.</td></tr>"
   "<tr><td>الاستلام في المختبر</td><td>فحص كل كيس ووزنه وتصويره؛ والأكياس التالفة أو غير المُعنونة تُعزل ونتواصل معكِ بشأنها.</td></tr>"
   "<tr><td>المعالجة</td><td>صوانٍ مبطّنة بمواد غذائية مخصّصة لأم واحدة، وتنظيف وتعقيم الصواني والحجرات بين الدفعات، والتزام الفريق بقواعد النظافة لمتداولي الأغذية.</td></tr>"
   "<tr><td>فحص الجودة</td><td>يجب أن يجف المسحوق تمامًا قبل التعبئة، وتُعاد أي دفعة لا تجتاز فحص الجفاف.</td></tr>"
   "<tr><td>التغليف</td><td>أكياس عازلة للضوء والأكسجين مع ماصّات أكسجين غذائية، مغلقة حراريًا ومُعنونة برقم الدفعة ورمز QR.</td></tr>"
   "</tbody></table></div>"),
  ("prepare","كيف تحضّرينه بأمان في المنزل",
   "<ol><li>اغسلي يديكِ واستخدمي رضّاعات نظيفة ومعقّمة.</li>"
   "<li>استخدمي نسبة الماء إلى المسحوق المطبوعة على الملصق، مع ماء مغليّ ومبرّد إلى حرارة آمنة كما يوصي طبيب الأطفال.</li>"
   "<li>أضيفي المسحوق إلى الماء وحرّكي بلطف حتى يذوب، ولا تسخّني الرضعة في الميكروويف.</li>"
   "<li>أطعمي الطفل خلال ساعتين. وإذا وضعتِ الرضعة في الثلاجة فاستخدميها خلال 24 ساعة. تخلّصي من المتبقي بعد الرضعة ولا تعيدي تجميده.</li></ol>"
   "<p>دقة النسبة مهمة: قلة الماء تركّز الحليب وكثرته تخففه. قيسي دائمًا ولا تعتمدي على التقدير.</p>"),
  ("store","حفظ المسحوق",
   "<p>احفظي الأكياس المغلقة في خزانة باردة وجافة ومظلمة، بعيدًا عن السيارة الحارة أو الموقد — وصيف الكويت يستدعي الانتباه لذلك. بعد الفتح، أخرجي الهواء وأحكمي الإغلاق واستخدميه خلال 4 أسابيع.</p>"
   "<p>تعلن خدمات عديدة في هذا المجال عن صلاحية تصل إلى ثلاث سنوات، لكن البيانات المستقلة طويلة المدى ما زالت محدودة؛ لذلك نطبع تاريخًا متحفّظًا: <strong>يُفضَّل استخدامه خلال 18 شهرًا</strong>.</p>"),
  ("refs","المصادر",
   "<ol class='refs'>"
   "<li><a href='https://www.cdc.gov/breastfeeding/breast-milk-preparation-and-storage/handling-breastmilk.html' rel='noopener'>CDC — الحفظ والتحضير السليم لحليب الأم (بالإنجليزية)</a></li>"
   "<li><a href='https://link.springer.com/article/10.1038/s41372-023-01861-8' rel='noopener'>Journal of Perinatology (2023) — مراجعة حول تجفيف حليب الأم بالتجميد</a></li>"
   "<li><a href='https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12526076/' rel='noopener'>Nutrients (2025) — حليب متبرَّع به مجفف بالتجميد لتدعيم تغذية الخُدّج</a></li>"
   "<li><a href='https://aeroflowbreastpumps.com/care-guides/post/freeze-dry-breast-milk' rel='noopener'>Aeroflow — دليل الحليب المجفف بالتجميد</a></li>"
   "<li><a href='https://www.romper.com/parenting/freeze-dried-breast-milk' rel='noopener'>Romper — آراء أطباء الأطفال</a></li>"
   "</ol>"),
 ],
 "end_h":"هل لديكِ أسئلة أخرى؟","end_p":"اسألينا عن أي شيء عبر واتساب قبل الحجز — أو أحضري لنا أسئلة طبيب طفلكِ.",
}}

BEN = {
"en": {
 "title":"Long-Term Benefits of Freeze-Dried Breast Milk | Preserve It",
 "desc":"How freeze-dried breast milk helps over the months and years ahead: freezer-free storage, travel, returning to work, weaning and first foods.",
 "kicker":"Benefits","h1":"What it's for — and how it pays off over time",
 "lead":"Pumping is hours of work. Freeze-drying protects that work so it can keep feeding your baby long after your freezer would have run out of room — or power.",
 "who_h":"Who it's for","who":[
   ("box","The mother with a full freezer","Turn a freezer stash into a single shelf and stop rotating bags."),
   ("bolt","The mother going back to work","Send pre-portioned sachets to nursery or the nanny — no thawing schedule."),
   ("plane","The travelling family","Summer abroad or Umrah: carry weeks of milk in hand luggage, no ice packs."),
   ("nose","The mother of a high-lipase baby","Powder that many babies accept better than thawed high-lipase milk.")],
 "tl_h":"Your milk across the first two years","tl":[
   ("0–6 m","Build a calm reserve","Freeze extra milk as normal. Send it for freeze-drying before it gets too old in the freezer."),
   ("6–12 m","Mix into first foods","With your doctor's go-ahead, stir powder into purées and cereals — familiar taste, extra nourishment."),
   ("Back to work","Bottles without the stress","Sachets mean exact portions at nursery or with a caregiver."),
   ("12–24 m","Keep going after weaning","A reserve of your own milk is available for the months after you've stopped pumping.")],
 "long_h":"The long-run value","long":[
   ("Nothing wasted","Milk that would have expired in the freezer — or been lost in a power cut — stays usable."),
   ("Peace of mind","No freezer-failure worry in Kuwait's summer heat."),
   ("Space back","Months of milk in a shoebox-sized space."),
   ("Your milk, your baby","Returned only to you, tracked by batch, never shared.")],
 "honest":"<b>The honest part</b><p>Freeze-drying doesn't make milk better, and it isn't sterile. It's a storage method. For premature or newborn babies, or any medical concern, talk to your paediatrician first.</p>",
},
"ar": {
 "title":"فوائد حليب الأم المجفف بالتجميد على المدى الطويل | بريزيرف إت",
 "desc":"كيف يساعدكِ حليب الأم المجفف بالتجميد خلال الأشهر والسنوات القادمة: حفظ دون فريزر، والسفر، والعودة إلى العمل، والفطام، والطعام الصلب الأول.",
 "kicker":"الفوائد","h1":"لماذا تحتاجينه — وكيف يفيدكِ مع الوقت",
 "lead":"شفط الحليب ساعات من الجهد. التجفيف بالتجميد يحمي هذا الجهد ليواصل تغذية طفلكِ طويلًا بعد أن يمتلئ الفريزر أو تنقطع الكهرباء.",
 "who_h":"لمن هو","who":[
   ("box","الأم ذات الفريزر الممتلئ","حوّلي مخزون الفريزر إلى رفّ واحد وتوقّفي عن ترتيب الأكياس باستمرار."),
   ("bolt","الأم العائدة إلى العمل","أرسلي أظرفًا مقسّمة إلى الحضانة أو المربية — دون جدول إذابة."),
   ("plane","العائلة المسافرة","صيف في الخارج أو عمرة: احملي أسابيع من الحليب في حقيبة اليد دون ثلج."),
   ("nose","أم الطفل الذي يرفض الحليب عالي الليباز","مسحوق يتقبّله كثير من الأطفال أفضل من الحليب المذاب عالي الليباز.")],
 "tl_h":"حليبكِ خلال أول عامين","tl":[
   ("0–6 أشهر","ابني مخزونًا مطمئنًا","جمّدي الحليب الزائد كالمعتاد، وأرسليه للتجفيف قبل أن يطول بقاؤه في الفريزر."),
   ("6–12 شهرًا","مع أول طعام صلب","بعد موافقة الطبيب، أضيفي المسحوق إلى الهريس والحبوب — طعم مألوف وتغذية إضافية."),
   ("العودة للعمل","رضعات بلا توتر","الأظرف تعني كميات دقيقة في الحضانة أو مع المربية."),
   ("12–24 شهرًا","استمرّي بعد الفطام","يبقى لديكِ مخزون من حليبكِ للأشهر التي تلي التوقف عن الشفط.")],
 "long_h":"القيمة على المدى الطويل","long":[
   ("لا هدر","الحليب الذي كان سينتهي في الفريزر أو يضيع مع انقطاع الكهرباء يبقى صالحًا."),
   ("راحة بال","لا قلق من تعطّل الفريزر في حرّ صيف الكويت."),
   ("مساحة أكبر","حليب أشهر في مساحة علبة حذاء."),
   ("حليبكِ لطفلكِ","يُعاد إليكِ وحدكِ، ويُتتبَّع برقم الدفعة، ولا يُشارك أبدًا.")],
 "honest":"<b>بصراحة</b><p>التجفيف بالتجميد لا يجعل الحليب أفضل، وهو غير معقّم؛ إنه وسيلة حفظ. للأطفال الخُدّج أو حديثي الولادة أو عند أي استفسار طبي، استشيري طبيب الأطفال أولًا.</p>",
}}

# ---------------------------------------------------------------- templates
def href(lang, cur_lang, target):
    """target like 'home#how' or 'safety'."""
    key, _, frag = target.partition("#")
    f = PAGES[key][0]
    return f + (("#" + frag) if frag else "")

def head(lang, key, title, desc, extra_ld=None):
    pre = "../" if lang == "ar" else ""
    other = "en" if lang == "ar" else "ar"
    ld = [{
        "@context":"https://schema.org","@type":"LocalBusiness","name":"Preserve It","alternateName":"بريزيرف إت",
        "url":BASE+"/","email":EMAIL,"areaServed":"KW","address":{"@type":"PostalAddress","addressCountry":"KW"},
        "description":HOME["en"]["desc"],"sameAs":[INSTAGRAM]}]
    if extra_ld: ld.append(extra_ld)
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{T[lang]['dir']}" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url(lang,key)}">
<link rel="alternate" hreflang="en" href="{url('en',key)}">
<link rel="alternate" hreflang="ar" href="{url('ar',key)}">
<link rel="alternate" hreflang="x-default" href="{url('en',key)}">
<meta name="theme-color" content="#FFFFFF">
<meta property="og:type" content="{'article' if key=='safety' else 'website'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang,key)}">
<meta property="og:locale" content="{'ar_KW' if lang=='ar' else 'en_US'}">
<meta property="og:site_name" content="Preserve It">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/style.css">
<script src="{pre}assets/app.js"></script>
<script type="application/ld+json">{json.dumps(ld if len(ld)>1 else ld[0], ensure_ascii=False)}</script>
</head>
<body>
"""

def header(lang, key):
    t = T[lang]
    other = "en" if lang == "ar" else "ar"
    pre_other = "../" if lang == "ar" else "ar/"
    other_href = pre_other + PAGES[key][0]
    nav = "".join(f'<a href="{href(lang,lang,n)}"{" aria-current=\"page\"" if n==key else ""}>{l}</a>' for n,l in t["nav"])
    drawer = "".join(f'<a href="{href(lang,lang,n)}">{l}</a>' for n,l in t["nav"])
    return f"""<a class="skip" href="#main">{t['skip']}</a>
<header class="hdr"><div class="wrap">
 <a class="brand" href="index.html">{I['logo']}<span>{t['name']}<small>{t['sub']}</small></span></a>
 <nav class="nav" aria-label="Primary">{nav}</nav>
 <div class="tools">
  <a class="icon-btn" href="{other_href}" hreflang="{other}" lang="{other}">{t['other']}</a>
  <button class="icon-btn" id="themeBtn" type="button" aria-label="{t['theme']}">{I['moon']}{I['sun']}</button>
  <button class="icon-btn menu-btn" id="menuBtn" type="button" aria-label="{t['menu']}" aria-expanded="false" aria-controls="drawer">{I['menu']}</button>
 </div>
</div>
<div class="drawer" id="drawer">{drawer}<a href="{wa(lang)}" rel="noopener">{t['book']} →</a></div>
</header>
<main id="main">
"""

def footer(lang):
    t = T[lang]
    explore = "".join(f'<li><a href="{href(lang,lang,n)}">{l}</a></li>' for n,l in t["nav"])
    learn = "".join(f'<li><a href="{href(lang,lang,n)}">{l}</a></li>' for n,l in t["foot_learn"])
    return f"""</main>
<footer class="ftr"><div class="wrap">
 <div class="ftr-grid">
  <div><a class="brand" href="index.html">{I['logo']}<span>{t['name']}</span></a><p>{t['foot_tag']}</p></div>
  <div><h4>{t['foot_h'][0]}</h4><ul>{explore}</ul></div>
  <div><h4>{t['foot_h'][1]}</h4><ul>{learn}</ul></div>
  <div><h4>{t['foot_h'][2]}</h4><ul><li><a href="{wa(lang)}" rel="noopener">WhatsApp</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{INSTAGRAM}" rel="noopener">Instagram</a></li></ul></div>
 </div>
 <p class="disclaimer">{t['disc']}<br><br>© <span id="yr">{datetime.date.today().year}</span> Preserve It · preserveit.com · {t['rights']}</p>
</div></footer>
<div class="mbar"><a class="btn btn-primary" href="{wa(lang)}" rel="noopener">{I['wa']}{t['book']}</a></div>
</body></html>
"""

FALLBACK_SVG = """<svg class="fallback" viewBox="0 0 400 400" aria-hidden="true"><defs><linearGradient id="pg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EEEEEE"/></linearGradient></defs>
<path d="M120 70h160l10 250q-90 20-180 0z" fill="url(#pg)" stroke="#DDE2E7"/><rect x="118" y="70" width="164" height="22" fill="#E6E9EC"/><path d="M114 250h172l4 70q-90 20-180 0z" fill="#366688"/>
<path d="M200 120c14 17 24 30 24 43a24 24 0 0 1-48 0c0-13 10-26 24-43z" fill="#5AA6E5"/><text x="200" y="215" text-anchor="middle" font-family="Fraunces,Georgia,serif" font-size="26" fill="#1B3347">Preserve It</text></svg>"""

PANELS = """<svg class="panels" viewBox="0 0 400 400" preserveAspectRatio="none" aria-hidden="true">
<rect width="400" height="400" fill="#EEEEEE"/>
<polygon points="0,0 400,0 400,112 0,178" fill="#366688"/>
<polygon points="0,198 176,168 176,264 0,252" fill="#89D0B1"/>
<polygon points="196,165 400,131 400,290 196,267" fill="#F4BBD1"/>
<polygon points="0,272 400,310 400,372 0,330" fill="#5AA6E5"/>
</svg>"""

def page_home(lang):
    h, t = HOME[lang], T[lang]
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in h["faq"]]}
    out = head(lang,"home",h["title"],h["desc"],faq_ld) + header(lang,"home")
    chips = "".join(f"<li>{c}</li>" for c in h["chips"])
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a,b in h["stats"])
    out += f"""<section class="hero"><div class="wrap hero-grid">
 <div class="reveal in">
  <span class="eyebrow">{h['eyebrow']}</span>
  <h1>{h['h1']}</h1>
  <p class="lead">{h['lead']}</p>
  <div class="cta-row"><a class="btn btn-primary" href="{wa(lang)}" rel="noopener">{I['wa']}{t['book']}</a><a class="btn btn-ghost" href="#offers">{h['cta2']}</a></div>
  <ul class="chips">{chips}</ul>
 </div>
 <div class="stage" id="stage" role="img" aria-label="3D model of a Preserve It pouch">{PANELS}{FALLBACK_SVG}<span class="hint">{t['hint']}</span></div>
</div><div class="wrap"><div class="stats reveal">{stats}</div></div></section>
"""
    steps = "".join(f'<li class="step reveal"><h3>{a}</h3><p>{b}</p></li>' for a,b in h["steps"])
    out += f"""<section id="how" class="alt"><div class="wrap">
 <div class="sec-head reveal"><span class="kicker">{h['how_k']}</span><h2>{h['how_h']}</h2><p>{h['how_p']}</p></div>
 <ol class="steps">{steps}</ol></div></section>
"""
    offers = ""
    for o in h["offers"]:
        ticks = "".join(f"<li>{x}</li>" for x in o["ticks"])
        feat = " featured" if o.get("featured") else ""
        badge = f'<span class="badge">{o["tag"]}</span>' if o.get("featured") else f'<span class="tag">{o["tag"]}</span>'
        offers += f"""<article class="offer{feat} reveal">{badge}<h3>{o['name']}</h3><p class="desc">{o['desc']}</p>
 <div class="price"><span>{'from' if lang=='en' else 'من'}</span><b>{o['price']}</b><span>{o['unit']}</span></div>
 <ul class="ticks">{ticks}</ul><a class="btn {'btn-primary' if feat else 'btn-ghost'}" href="{wa(lang)}" rel="noopener">{o['cta']}</a></article>"""
    out += f"""<section id="offers"><div class="wrap">
 <div class="sec-head reveal"><span class="kicker">{h['off_k']}</span><h2>{h['off_h']}</h2><p>{h['off_p']}</p></div>
 <div class="offers">{offers}</div><p class="fine">{h['off_fine']}</p></div></section>
"""
    why = "".join(f'<div class="card reveal"><div class="ico">{I[i]}</div><h3>{a}</h3><p>{b}</p></div>' for i,a,b in h["why"])
    out += f"""<section class="alt"><div class="wrap">
 <div class="sec-head reveal"><span class="kicker">{h['why_k']}</span><h2>{h['why_h']}</h2></div>
 <div class="cards">{why}</div>
 <a class="link-arrow" href="{PAGES['benefits'][0]}">{h['why_link']} {I['arrow']}</a></div></section>
"""
    chain = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in h["chain"])
    out += f"""<section class="alt" style="padding-top:0"><div class="wrap split">
 <div class="sec-head reveal"><span class="kicker">{h['trust_k']}</span><h2>{h['trust_h']}</h2><p>{h['trust_p']}</p></div>
 <ol class="chain reveal">{chain}</ol></div></section>
<section><div class="wrap split">
 <div class="sec-head reveal"><span class="kicker">{h['safety_k']}</span><h2>{h['safety_h']}</h2><p>{h['safety_p']}</p>
 <a class="link-arrow" href="{PAGES['safety'][0]}">{h['safety_link']} {I['arrow']}</a></div>
 <div class="card reveal"><div class="ico">{I['shield']}</div>{SAFETY[lang]['sections'][2][2]}</div></div></section>
"""
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in h["faq"])
    out += f"""<section id="faq" class="alt"><div class="wrap">
 <div class="sec-head reveal"><span class="kicker">{h['faq_k']}</span><h2>{h['faq_h']}</h2></div>
 <div class="faq reveal">{faq}</div></div></section>
<section><div class="wrap"><div class="band reveal"><h2>{h['band_h']}</h2><p>{h['band_p']}</p>
 <a class="btn btn-primary" href="{wa(lang)}" rel="noopener">{I['wa']}{t['wa']}</a></div></div></section>
"""
    pre = "../" if lang == "ar" else ""
    out += f'<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script><script src="{pre}assets/pouch3d.js" defer></script>\n'
    return out + footer(lang)

def page_safety(lang):
    s, t = SAFETY[lang], T[lang]
    art_ld = {"@context":"https://schema.org","@type":"Article","headline":s["h1"],"description":s["desc"],"inLanguage":lang,
              "datePublished":TODAY,"dateModified":TODAY,"author":{"@type":"Organization","name":"Preserve It"},
              "publisher":{"@type":"Organization","name":"Preserve It"},"mainEntityOfPage":url(lang,"safety")}
    out = head(lang,"safety",s["title"],s["desc"],art_ld) + header(lang,"safety")
    toc = "".join(f'<li><a href="#{i}">{h}</a></li>' for i,h,_ in s["sections"])
    body = "".join(f'<h2 id="{i}">{h}</h2>{c}' for i,h,c in s["sections"])
    meta = "".join(f"<span>{m}</span>" for m in s["meta"])
    out += f"""<div class="wrap">
<header class="article-hero"><span class="kicker">{s['kicker']}</span><h1>{s['h1']}</h1><div class="meta">{meta}</div></header>
<div class="article-layout">
 <nav class="toc" aria-label="{s['toc']}"><b>{s['toc']}</b><ol>{toc}</ol></nav>
 <article class="prose">{body}
  <div class="band" style="margin-top:40px"><h2>{s['end_h']}</h2><p>{s['end_p']}</p><a class="btn btn-primary" href="{wa(lang)}" rel="noopener">{I['wa']}{t['wa']}</a></div>
 </article>
</div></div>
"""
    return out + footer(lang)

def page_benefits(lang):
    b, t = BEN[lang], T[lang]
    out = head(lang,"benefits",b["title"],b["desc"]) + header(lang,"benefits")
    who = "".join(f'<div class="card reveal"><div class="ico">{I[i]}</div><h3>{x}</h3><p>{y}</p></div>' for i,x,y in b["who"])
    tl = "".join(f'<div class="tl reveal"><span class="when">{w}</span><div><h3>{x}</h3><p>{y}</p></div></div>' for w,x,y in b["tl"])
    lg = "".join(f'<div class="card reveal"><h3>{x}</h3><p>{y}</p></div>' for x,y in b["long"])
    out += f"""<section class="article-hero"><div class="wrap"><span class="kicker">{b['kicker']}</span><h1>{b['h1']}</h1><p class="lead">{b['lead']}</p>
 <div class="cta-row"><a class="btn btn-primary" href="{wa(lang)}" rel="noopener">{I['wa']}{t['book']}</a><a class="btn btn-ghost" href="index.html#offers">{HOME[lang]['cta2']}</a></div></div></section>
<section style="padding-top:20px"><div class="wrap"><div class="sec-head"><h2>{b['who_h']}</h2></div><div class="cards">{who}</div></div></section>
<section class="alt"><div class="wrap"><div class="sec-head"><h2>{b['tl_h']}</h2></div><div class="timeline">{tl}</div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>{b['long_h']}</h2></div><div class="cards">{lg}</div>
 <div class="callout warn" style="margin-top:24px">{b['honest']}</div>
 <a class="link-arrow" href="{PAGES['safety'][0]}">{HOME[lang]['safety_link']} {I['arrow']}</a></div></section>
"""
    return out + footer(lang)

def sitemap():
    rows = []
    for key,(f,pr,cf) in PAGES.items():
        for lang in ("en","ar"):
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{url(l,key)}"/>' for l in ("en","ar"))
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url("en",key)}"/>'
            rows.append(f"""  <url>
    <loc>{url(lang,key)}</loc>{alts}
    <lastmod>{TODAY}</lastmod>
    <changefreq>{cf}</changefreq>
    <priority>{pr if lang=='en' else str(round(float(pr)-0.1,1))}</priority>
  </url>""")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")

def write(path, s):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

for lang in ("en","ar"):
    pre = "ar/" if lang == "ar" else ""
    write(pre+"index.html", page_home(lang))
    write(pre+PAGES["safety"][0], page_safety(lang))
    write(pre+PAGES["benefits"][0], page_benefits(lang))
write("sitemap.xml", sitemap())
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
write("CNAME", "www.preserveit.com\n")
write("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="#366688"/><path d="M16 6c4 5 7 8.6 7 12.4A7 7 0 0 1 9 18.4C9 14.6 12 11 16 6z" fill="#5AA6E5"/></svg>')
write("404.html", head("en","home","Page not found | Preserve It","Page not found").replace('href="assets','href="/assets').replace('src="assets','src="/assets')
      + '<main class="wrap" style="padding:80px 20px;text-align:center"><h1>Page not found</h1><p class="lead" style="margin-inline:auto">لم يتم العثور على الصفحة</p>'
      + '<div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="/">Home</a><a class="btn btn-ghost" href="/ar/">الرئيسية</a></div></main></body></html>')
print("built", OUT)

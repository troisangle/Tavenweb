APP = "https://apps.apple.com/app/id6761032737"

HUB = {
    "title": "Productivity Guides & Task App Comparisons — Taven",
    "desc": "Practical guides on prioritizing tasks, beating to-do list overwhelm and choosing the right task manager for iPhone and iPad, plus honest comparisons of Taven, Todoist and TickTick.",
    "lede": "Practical guides on prioritizing, beating to-do list overwhelm and picking the right task app — including honest comparisons where other apps are the better fit.",
}

DISCLOSURE = '<div class="note"><strong>Disclosure:</strong> this page is published by the makers of Taven. We\'ve tried to be fair — every app here is genuinely good at something, and we say plainly where Taven isn\'t the best fit. App features and pricing change often; check each app\'s App Store page for current details.</div>'

def card(name, tag, best_for, platforms, price, strengths, tradeoffs, extra=""):
    return f'''    <div class="card frost">
      <h3>{name} <span class="tag">{tag}</span></h3>
      {extra}<dl>
        <dt>Best for</dt><dd>{best_for}</dd>
        <dt>Platforms</dt><dd>{platforms}</dd>
        <dt>Price</dt><dd>{price}</dd>
        <dt>Strengths</dt><dd>{strengths}</dd>
        <dt>Trade-offs</dt><dd>{tradeoffs}</dd>
      </dl>
    </div>'''

TAVEN_CARD = lambda tag: card(
    f'<a href="/">Taven</a>', tag,
    "People who don't want to manage a system — they want to open the app and be told what to do next.",
    "iPhone and iPad",
    "Free. No subscription, no in-app account.",
    "On-device AI picks your top task and explains why (“Due today and your top priority”). Smart recurrence for daily, weekly, monthly and yearly tasks, habit streaks, completion analytics, optional iCloud sync. No account, no tracking, no third-party SDKs.",
    "Apple devices only. No team collaboration or shared projects. Fewer integrations and power-user views than long-established apps.")

# ─────────────────────────────────────────────────────────────
PAGES = []

# 1. Best task manager apps for iPhone
PAGES.append(dict(
    kind="list", path="guides/best-task-manager-apps-iphone.html",
    label="App roundup", short="Best task manager apps for iPhone",
    blurb="Seven iPhone to-do apps compared honestly — who each one is for, what it costs and where it falls short.",
    title="Best Task Manager Apps for iPhone (2026): 7 To-Do Apps Compared — Taven",
    desc="An honest comparison of the best task manager and to-do list apps for iPhone and iPad in 2026: Taven, Things 3, Todoist, TickTick, Apple Reminders, Microsoft To Do and OmniFocus.",
    h1="The best task manager apps for <span>iPhone</span>",
    h1_plain="The best task manager apps for iPhone (2026)",
    lede="There's no single best to-do app — there's a best app for how you work. Here are seven strong iPhone options, who each is for, and where each one falls short.",
    answer="If you want an app that <strong>tells you what to do next</strong> with no setup, account or subscription, try <strong>Taven</strong>. If you want a polished, Apple-only planner you buy once, choose <strong>Things 3</strong>. If you need cross-platform sync and shared projects, choose <strong>Todoist</strong>. If you want a calendar, Pomodoro timer and habits in one app, choose <strong>TickTick</strong>. If you just need simple free lists, <strong>Apple Reminders</strong> is already on your phone.",
    itemlist=["Taven", "Things 3", "Todoist", "TickTick", "Apple Reminders", "Microsoft To Do", "OmniFocus"],
    body=f'''    {DISCLOSURE}

    <h2>How we chose</h2>
    <p>We looked at what actually matters day to day on an iPhone: how fast you can capture a task, how well the app helps you decide what to work on, whether it works across your devices, what it costs over a year, and what it does with your data. Every app below is actively maintained and genuinely good — the right pick depends on what you need.</p>

    <h2>Quick comparison</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th>App</th><th>Best for</th><th>Platforms</th><th>Pricing model</th><th>Account needed</th></tr></thead>
      <tbody>
        <tr><td>Taven</td><td>Being told what to do next</td><td>iPhone, iPad</td><td>Free</td><td>No</td></tr>
        <tr><td>Things 3</td><td>Polished personal planning</td><td>iPhone, iPad, Mac, Apple Watch</td><td>One-time purchase per platform</td><td>Only for sync</td></tr>
        <tr><td>Todoist</td><td>Cross-platform &amp; shared projects</td><td>iOS, Android, Mac, Windows, web</td><td>Free plan + subscription</td><td>Yes</td></tr>
        <tr><td>TickTick</td><td>All-in-one: tasks, calendar, habits, Pomodoro</td><td>iOS, Android, Mac, Windows, web</td><td>Free plan + subscription</td><td>Yes</td></tr>
        <tr><td>Apple Reminders</td><td>Simple lists, Siri, sharing with family</td><td>Apple devices, iCloud web</td><td>Free</td><td>Apple ID</td></tr>
        <tr><td>Microsoft To Do</td><td>Microsoft 365 / Outlook users</td><td>iOS, Android, Windows, Mac, web</td><td>Free</td><td>Microsoft account</td></tr>
        <tr><td>OmniFocus</td><td>GTD power users</td><td>iPhone, iPad, Mac, Apple Watch, web</td><td>Subscription or license</td><td>Only for sync</td></tr>
      </tbody>
    </table></div>

    <h2>The apps</h2>
{TAVEN_CARD("Best for deciding what to do next")}
{card("Things 3", "Best design", "Individuals who want a beautiful, calm planner and are fully in the Apple ecosystem.", "iPhone, iPad, Mac, Apple Watch", "One-time purchase, sold separately for iPhone, iPad and Mac.", "Exceptional design, Today/Upcoming/Anytime/Someday structure, projects with headings, fast quick-entry, free Things Cloud sync.", "No collaboration, no Android or Windows, and it organizes tasks beautifully but leaves deciding what to do next to you.")}
{card("Todoist", "Best cross-platform", "People who work across iPhone, Android, Windows and the web, or share projects with others.", "iOS, Android, Mac, Windows, web, browser extensions", "Free plan with limits; paid Pro and Business plans.", "Best-in-class natural-language quick add (“pay rent every 1st”), labels and filters, shared projects, comments, hundreds of integrations, AI features.", "Requires an account and stores your tasks on its servers. The free plan is limited. Powerful filters take time to set up.")}
{card("TickTick", "Best all-in-one", "People who want tasks, a calendar, a habit tracker and a focus timer in one app.", "iOS, Android, Mac, Windows, web", "Free plan; paid Premium subscription.", "Built-in Pomodoro focus timer, habit tracker, calendar views, an Eisenhower matrix view, natural-language entry.", "Requires an account. Many of its best features (like full calendar views) are Premium. Lots of features means a busier interface.")}
{card("Apple Reminders", "Best free built-in", "Simple personal and household lists, especially shared with family.", "iPhone, iPad, Mac, Apple Watch, iCloud.com", "Free.", "Already installed, great Siri integration, shared lists, grocery list sorting, smart lists, tags.", "Doesn't help you prioritize, and analytics and habit tracking are basic.")}
{card("Microsoft To Do", "Best for Microsoft users", "People who live in Outlook and Microsoft 365.", "iOS, Android, Windows, Mac, web", "Free.", "“My Day” daily planning list, syncs with Outlook tasks, shared lists.", "Requires a Microsoft account. Fewer advanced features than Todoist or TickTick.")}
{card("OmniFocus", "Best for GTD power users", "People who follow Getting Things Done and want maximum control.", "iPhone, iPad, Mac, Apple Watch, web", "Subscription or license.", "Perspectives (custom views), defer dates, review mode, deep automation.", "Steep learning curve and the highest price on this list. Overkill for most people.")}

    <h2>Which one should you pick?</h2>
    <ul>
      <li><strong>You have too many tasks and don't know where to start:</strong> Taven. It's built around one question — what should I do next? See also our guide on <a href="/guides/what-task-to-do-next.html">how to decide what task to do next</a>.</li>
      <li><strong>You use Android or Windows too:</strong> Todoist or TickTick.</li>
      <li><strong>You share task lists with a team or partner:</strong> Todoist, or Apple Reminders for simple shared lists.</li>
      <li><strong>You want to buy once, not subscribe, and love design:</strong> Things 3.</li>
      <li><strong>You want a focus timer and habit tracker built in:</strong> TickTick (Taven also tracks habits and streaks, but has no Pomodoro timer).</li>
      <li><strong>Privacy matters most:</strong> Taven (no account, on-device AI) or Things 3.</li>
    </ul>''',
    faqs=[
        ("What is the best free task manager app for iPhone?", "If you want prioritization and habit tracking, Taven is free with no subscription or account. If you only need simple lists, Apple Reminders is free and built in. Todoist and TickTick both have free plans, with more features behind a subscription."),
        ("What is the best to-do app for iPhone and iPad?", "Taven, Things 3, Todoist, TickTick and OmniFocus all work on both iPhone and iPad. Taven syncs between them through your private iCloud account."),
        ("Which iPhone task manager doesn't require an account?", "Taven doesn't require any account and processes everything on your device. Things 3 also works without an account unless you turn on Things Cloud sync."),
        ("Which to-do app tells you what to do next?", "Taven is built specifically for this: its on-device AI weighs importance, due dates and recurrence, then highlights your top task with a short reason."),
    ],
    related=["guides/best-ai-to-do-list-apps.html", "compare/taven-vs-todoist.html", "compare/taven-vs-ticktick.html", "guides/what-task-to-do-next.html"],
))

# 2. Best AI to-do list apps
PAGES.append(dict(
    kind="list", path="guides/best-ai-to-do-list-apps.html",
    label="App roundup", short="Best AI to-do list apps",
    blurb="What AI actually does in task apps today — prioritizing, scheduling, breaking down tasks — and which app fits.",
    title="Best AI To-Do List Apps (2026): What AI Actually Does in Task Managers — Taven",
    desc="A clear guide to AI-powered to-do list and task manager apps in 2026: Taven, Motion, Reclaim.ai, Todoist, Goblin Tools and Sunsama — what each one's AI really does, and who it's for.",
    h1="The best <span>AI</span> to-do list apps",
    h1_plain="The best AI to-do list apps (2026)",
    lede="“AI-powered” means very different things in different task apps. Some pick your next task, some schedule your calendar, some break big tasks into steps. Here's what each one actually does.",
    answer="Pick by the job you want the AI to do. To <strong>tell you which task to do next</strong> — privately, on your iPhone, for free — use <strong>Taven</strong>. To <strong>auto-schedule tasks into your calendar</strong>, use <strong>Motion</strong> or <strong>Reclaim.ai</strong>. To <strong>break a big task into small steps</strong>, use <strong>Goblin Tools</strong>. If you want a full-featured task manager with AI help added on, use <strong>Todoist</strong>.",
    itemlist=["Taven", "Motion", "Reclaim.ai", "Todoist", "Goblin Tools", "Sunsama"],
    body=f'''    {DISCLOSURE}

    <h2>The four kinds of “AI” in task apps</h2>
    <ol>
      <li><strong>Prioritization</strong> — the app looks at your tasks and tells you which one matters most right now. This targets decision fatigue: the minutes (or hours) lost staring at a list.</li>
      <li><strong>Auto-scheduling</strong> — the app places tasks into free slots on your calendar and reshuffles them when things change.</li>
      <li><strong>Task breakdown</strong> — you type “clean the garage” and get a list of concrete sub-steps.</li>
      <li><strong>Assistants</strong> — generative AI that drafts tasks, rewrites them or suggests projects inside a traditional task manager.</li>
    </ol>
    <p>One more thing to check: <strong>where the AI runs</strong>. Cloud AI sends your task text to a server. On-device AI runs on your phone, so your tasks never leave it.</p>

    <h2>Quick comparison</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th>App</th><th>What its AI does</th><th>Where AI runs</th><th>Platforms</th><th>Pricing model</th></tr></thead>
      <tbody>
        <tr><td>Taven</td><td>Picks your next task and explains why</td><td>On your device</td><td>iPhone, iPad</td><td>Free</td></tr>
        <tr><td>Motion</td><td>Auto-schedules tasks and projects into your calendar</td><td>Cloud</td><td>Web, desktop, mobile</td><td>Subscription</td></tr>
        <tr><td>Reclaim.ai</td><td>Schedules tasks, habits and focus time around meetings</td><td>Cloud</td><td>Web (Google/Outlook calendar)</td><td>Free plan + subscription</td></tr>
        <tr><td>Todoist</td><td>AI assistant inside a full task manager</td><td>Cloud</td><td>iOS, Android, desktop, web</td><td>Free plan + subscription</td></tr>
        <tr><td>Goblin Tools</td><td>Breaks tasks into steps, estimates time</td><td>Cloud</td><td>Web, iOS, Android</td><td>Free web; low-cost apps</td></tr>
        <tr><td>Sunsama</td><td>Guided daily planning (with some AI help)</td><td>Cloud</td><td>Web, desktop, mobile</td><td>Subscription</td></tr>
      </tbody>
    </table></div>

    <h2>The apps</h2>
{TAVEN_CARD("Best AI for “what next?”")}
{card("Motion", "Best AI calendar", "Busy professionals and teams whose days are mostly meetings.", "Web, Mac, Windows, iOS, Android", "Subscription; one of the pricier options here.", "Fully automatic scheduling: give it tasks with deadlines and durations and it builds your day, then rebuilds it when things slip. Project management for teams.", "Expensive for individuals, needs your calendar connected, and works best when you estimate every task's duration.")}
{card("Reclaim.ai", "Best for protecting time", "People on Google Calendar or Outlook who want focus time, habits and tasks defended from meetings.", "Web app connected to Google Calendar or Outlook", "Free plan; paid tiers.", "Smart time-blocking for habits and tasks, buffer time, scheduling links.", "Lives in your calendar rather than as a standalone to-do list. Less useful if your day isn't calendar-driven.")}
{card("Todoist", "Best traditional app + AI", "People who want a mature, cross-platform task manager with AI assistance layered in.", "iOS, Android, Mac, Windows, web", "Free plan; AI features and more on paid plans.", "Everything Todoist is known for — natural-language entry, filters, shared projects, integrations — plus AI help to break down and phrase tasks.", "The AI assists you but doesn't decide for you; prioritization still means setting priority flags and building filters. Requires an account.")}
{card("Goblin Tools", "Best for breaking tasks down", "Anyone who gets stuck starting big, vague tasks — popular with neurodivergent users.", "Web (free), iOS, Android", "Free on the web; small one-time price for the apps.", "“Magic To-Do” turns one task into steps, with an adjustable “spiciness” level for how much detail you get. Also has time estimation and tone tools.", "A helper tool rather than a full task manager — no recurrence, reminders or long-term organization.")}
{card("Sunsama", "Best guided planning ritual", "Knowledge workers who want a calm, guided daily and weekly planning routine.", "Web, Mac, Windows, iOS, Android", "Subscription.", "Pulls tasks from email, Slack, Asana, Trello and others into one daily plan; timeboxing; end-of-day shutdown ritual.", "It's mostly a planning method rather than AI. Subscription only, and the daily ritual takes a few minutes every morning.")}

    <h2>Which AI to-do app should you pick?</h2>
    <ul>
      <li><strong>You open your list and freeze:</strong> Taven. It picks one task and tells you why. More on this in <a href="/guides/to-do-list-overwhelm.html">how to stop feeling overwhelmed by your to-do list</a>.</li>
      <li><strong>Your calendar is packed with meetings:</strong> Motion or Reclaim.ai.</li>
      <li><strong>Tasks feel too big to start:</strong> Goblin Tools.</li>
      <li><strong>You want a full-featured, cross-platform app with some AI:</strong> Todoist.</li>
      <li><strong>You don't want your tasks sent to an AI server:</strong> Taven — its intelligence runs entirely on your iPhone or iPad.</li>
    </ul>''',
    faqs=[
        ("Is there an AI app that tells you what to do next?", "Yes. Taven, for iPhone and iPad, is built around this: its on-device AI weighs importance, due dates and recurrence, then surfaces your single most important task with a short explanation such as “Due today and your top priority.”"),
        ("Which AI to-do list app is private?", "Taven runs its AI entirely on your device, needs no account and collects no data. Most other AI task apps (Motion, Reclaim, Todoist's AI features) process your tasks in the cloud."),
        ("Is there a free AI task manager?", "Taven is free with no subscription. Goblin Tools is free on the web. Reclaim.ai and Todoist offer free plans with limits."),
        ("What's the difference between AI prioritization and AI scheduling?", "Prioritization decides <em>which</em> task matters most right now (Taven). Scheduling decides <em>when</em> each task happens by placing it on your calendar (Motion, Reclaim.ai)."),
    ],
    related=["guides/best-task-manager-apps-iphone.html", "guides/what-task-to-do-next.html", "compare/taven-vs-todoist.html", "guides/to-do-list-overwhelm.html"],
))

# 3. Overwhelm
PAGES.append(dict(
    kind="guide", path="guides/to-do-list-overwhelm.html",
    label="Guide", short="How to stop feeling overwhelmed by your to-do list",
    blurb="Why long lists freeze you, and a seven-step reset to get unstuck today.",
    title="How to Stop Feeling Overwhelmed by Your To-Do List (7 Steps) — Taven",
    desc="Why a long to-do list causes overwhelm and procrastination, and a practical seven-step reset: brain dump, cut, pick one task, shrink it, and build a list that stays manageable.",
    h1="How to stop feeling overwhelmed by your <span>to-do list</span>",
    h1_plain="How to stop feeling overwhelmed by your to-do list",
    lede="A long list isn't the problem. The problem is that every time you look at it, you have to decide all over again what matters. Here's how to get out of that loop.",
    answer="Get everything out of your head, cut or postpone what doesn't matter this week, then <strong>pick one task and only look at that one</strong>. Make it small enough to start in two minutes. Overwhelm comes from deciding between many tasks, not from doing them — so reduce the deciding.",
    body='''    <h2>Why your to-do list feels overwhelming</h2>
    <p>Looking at 40 open tasks forces your brain to compare all of them at once: which is most urgent, which is most important, which is quick, which you've been avoiding. That's <strong>decision fatigue</strong>, and it's exhausting before you've done anything. The common result is picking the easiest task (answering email) or doing nothing at all.</p>
    <p>Unfinished tasks also nag at you. Psychologists call this the Zeigarnik effect: incomplete tasks stay active in memory. Research by Masicampo and Baumeister found that simply making a <em>specific plan</em> for an unfinished goal reduced those intrusive thoughts — you don't have to finish everything to feel calmer, you just have to know what happens next.</p>

    <h2>The 7-step reset</h2>
    <h3>1. Brain dump everything</h3>
    <p>Spend ten minutes writing down every task, errand and worry. Don't organize yet. Getting it out of your head and into one trusted place is the first relief.</p>
    <h3>2. Cut ruthlessly</h3>
    <p>For each item ask: will anything bad happen if this never gets done? Delete it, delegate it, or move it to a “someday” list. Most lists shrink by a third.</p>
    <h3>3. Put dates only on things with real deadlines</h3>
    <p>Fake deadlines (“I'll do it Tuesday”) turn into a wall of overdue red that adds guilt without adding information. Date the bill, the appointment and the client deadline — not everything.</p>
    <h3>4. Make recurring things automatic</h3>
    <p>Rent, workouts, weekly reviews and watering plants shouldn't take up decision space. Set them to repeat once and stop thinking about them.</p>
    <h3>5. Pick one task — and hide the rest</h3>
    <p>Choose the single most important task for right now (the next guide covers <a href="/guides/what-task-to-do-next.html">how to decide what task to do next</a>). Then look only at that task. A list of one isn't overwhelming.</p>
    <h3>6. Shrink it until starting is easy</h3>
    <p>“Write report” is a project. “Open the doc and write the three section headings” is a task. If you can't start within two minutes, break it down further.</p>
    <h3>7. Keep a daily limit</h3>
    <p>Plan three to five meaningful tasks a day, not twenty. Finishing your list builds momentum; failing an impossible one builds dread.</p>

    <h2>How Taven helps with overwhelm</h2>
    <p>We built <a href="/">Taven</a> for exactly this problem. Instead of showing you a long list and leaving the decision to you, Taven's on-device AI weighs importance, due dates and recurrence and puts <strong>one suggested task</strong> at the top — with a reason, like “Due today and your top priority.” Smart recurrence takes routine tasks off your mind, and a “Today's Intensity” gauge shows when you've planned too much. It's free on iPhone and iPad, with no account.</p>
    <p>You don't need an app to use the method above — paper works. But if you keep freezing at the same list, letting software make the first decision is a good way to break the loop.</p>''',
    faqs=[
        ("Why do I feel paralyzed by my to-do list?", "Usually it's decision fatigue: a long list forces you to compare every task every time you look at it. Reducing the list and committing to one next task removes most of that load."),
        ("How many tasks should be on a daily to-do list?", "Most people do best with three to five meaningful tasks a day, plus small routine items. The 1-3-5 method (one big, three medium, five small) is a good template."),
        ("Is there an app that helps with to-do list overwhelm?", "Taven for iPhone and iPad is designed for it: it suggests one task to do next and explains why, so you don't have to sort a long list yourself. Goblin Tools is also helpful for breaking big tasks into small steps."),
    ],
    related=["guides/what-task-to-do-next.html", "guides/best-ai-to-do-list-apps.html", "guides/best-task-manager-apps-iphone.html"],
))

# 4. What task next
PAGES.append(dict(
    kind="guide", path="guides/what-task-to-do-next.html",
    label="Guide", short="How to decide what task to do next",
    blurb="Five proven prioritization methods, a simple scoring rule, and when to let an app decide for you.",
    title="How to Decide What Task to Do Next: 5 Prioritization Methods — Taven",
    desc="Five proven ways to decide what task to do next — Eisenhower matrix, eat the frog, 1-3-5, MIT and ABCDE — plus a simple deadline-and-importance rule and when to let an app choose for you.",
    h1="How to decide what task to <span>do next</span>",
    h1_plain="How to decide what task to do next",
    lede="Choosing is often harder than doing. Here are five proven prioritization methods, a simple rule you can use in ten seconds, and how to hand the decision to an app.",
    answer="Do the task with the <strong>nearest real deadline</strong> that also <strong>matters</strong>. If nothing is due, do the most important task you've been avoiding, first thing. If you're stuck between two, pick the one that unblocks other work. Or let an app like <strong>Taven</strong> weigh deadlines, importance and recurrence and pick for you.",
    body='''    <h2>The 10-second rule</h2>
    <p>When you just need an answer, go down this list and stop at the first “yes”:</p>
    <ol>
      <li>Is something <strong>due today</strong> (or overdue) with real consequences? Do that.</li>
      <li>Is something <strong>blocking other people</strong> or other tasks? Do that.</li>
      <li>Is there an <strong>important task you've been avoiding</strong>? Do that — now, before energy runs out.</li>
      <li>Otherwise, do the task that moves your <strong>most important goal</strong> forward.</li>
    </ol>

    <h2>Five proven prioritization methods</h2>
    <h3>1. The Eisenhower matrix</h3>
    <p>Sort tasks by two questions: is it <strong>urgent</strong>, and is it <strong>important</strong>? Urgent and important: do now. Important but not urgent: schedule. Urgent but not important: delegate or batch. Neither: drop. Its power is the second box — the important work that never feels urgent until it's a crisis.</p>
    <h3>2. Eat the frog</h3>
    <p>From Brian Tracy: do your biggest, most dreaded task first thing in the morning. Everything after feels easier, and procrastination doesn't get a chance to build.</p>
    <h3>3. The 1-3-5 rule</h3>
    <p>Each day, plan <strong>one</strong> big task, <strong>three</strong> medium tasks and <strong>five</strong> small ones. It forces realistic days and makes the priority obvious: the one big task.</p>
    <h3>4. Most Important Task (MIT)</h3>
    <p>Each evening, pick one to three tasks that would make tomorrow a success no matter what else happens. Do them before checking email or messages.</p>
    <h3>5. ABCDE method</h3>
    <p>Label every task: A = must do (serious consequences), B = should do, C = nice to do, D = delegate, E = eliminate. Never start a B while an A is open.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Doing quick tasks to feel productive.</strong> Clearing ten trivial items feels good but leaves the important one untouched.</li>
      <li><strong>Re-prioritizing all day.</strong> Decide once, then commit until the task is done or something truly urgent appears.</li>
      <li><strong>Treating every task as high priority.</strong> If everything is a priority, nothing is.</li>
      <li><strong>Ignoring recurring commitments.</strong> Habits and routine tasks quietly compete with projects; account for them.</li>
    </ul>

    <h2>Let an app decide for you</h2>
    <p>All of these methods share one cost: you have to apply them, every day, to every task. That's the reason we built <a href="/">Taven</a>. Its on-device AI does the weighing for you — importance, due dates and recurrence — and puts one <strong>AI Suggested</strong> task at the top of your day with a plain-English reason, like “Due today and your top priority.” You open the app, see what to do next, and do it.</p>
    <p>Taven is free on iPhone and iPad, needs no account, and runs its intelligence entirely on your device. If you prefer to sort tasks yourself, apps like TickTick include an Eisenhower matrix view, and Todoist supports priority levels and custom filters — see our <a href="/guides/best-task-manager-apps-iphone.html">iPhone task app comparison</a>.</p>''',
    faqs=[
        ("How do I decide which task to do first?", "Start with anything due today that has real consequences, then anything blocking others, then the important task you've been avoiding. If none apply, work on whatever moves your most important goal forward."),
        ("What is the best prioritization method?", "The Eisenhower matrix is the most widely used and is good for sorting a long list. Eat the frog and the Most Important Task method are better for daily focus. Many people combine them."),
        ("Is there an app that decides what I should do next?", "Taven for iPhone and iPad uses on-device AI to rank your tasks by importance, due date and recurrence, then highlights the single task you should do next and explains why."),
    ],
    related=["guides/to-do-list-overwhelm.html", "guides/best-ai-to-do-list-apps.html", "guides/best-task-manager-apps-iphone.html"],
))

COMPARE_DISCLOSURE = '<div class="note"><strong>Disclosure:</strong> Taven is our app, so we\'re biased — but we\'ve kept every fact on this page accurate and noted where {other} is the better fit. Features and pricing change often; check the App Store for current details.</div>'

def benefit(title, text):
    return f'''    <h3>{title}</h3>
    <p>{text}</p>'''

def day(app, steps):
    lis = "".join(f"<li>{s}</li>" for s in steps)
    return f'''      <div class="card frost"><h3>{app}</h3><ol>{lis}</ol></div>'''

# 5. Taven vs Todoist
PAGES.append(dict(
    kind="compare", path="compare/taven-vs-todoist.html",
    label="Comparison", short="Taven vs. Todoist",
    blurb="Why people switch from Todoist to Taven: automatic prioritization, real privacy and no subscription.",
    title="Taven vs. Todoist (2026): The Free, Private Todoist Alternative for iPhone — Taven",
    desc="Taven vs. Todoist compared: Taven tells you what to do next with on-device AI, needs no account and is free with no subscription. See where each app wins and why people switch.",
    h1="Taven vs. <span>Todoist</span>",
    h1_plain="Taven vs. Todoist",
    lede="Todoist helps you organize everything. Taven helps you actually get the right thing done — by telling you what to do next. Here's how they compare, and why people on iPhone and iPad are switching.",
    answer="<strong>Taven</strong> is the better choice if you're on iPhone or iPad and want an app that <strong>decides what you should do next</strong> instead of making you build a priority system. It's <strong>free with no subscription</strong>, needs <strong>no account</strong>, and its AI runs <strong>privately on your device</strong>. Todoist is the better fit only if you need Android, Windows or web access, or share projects with a team.",
    body=f'''    {COMPARE_DISCLOSURE.format(other="Todoist")}

    <h2>Why choose Taven over Todoist</h2>
{benefit("1. It tells you what to do next — automatically", "Todoist gives you priority flags (P1–P4), labels and filter queries, and then leaves the decision to you. Taven does the deciding: its on-device AI weighs each task's importance, due date and recurrence, then puts one <strong>AI Suggested</strong> task at the top of your day with a plain-English reason, like “Due today and your top priority.” You open the app and start, instead of scanning a list.")}
{benefit("2. Free — really free", "Taven costs nothing, with no subscription and no feature paywall. Todoist's free plan is limited, and its full feature set — including its AI features — requires a paid plan billed every year.")}
{benefit("3. Your tasks stay yours", "Taven has no accounts, no servers holding your tasks and no third-party SDKs, and it collects zero data. Its AI runs entirely on your iPhone or iPad. Todoist requires an account and stores your tasks in its cloud, where its AI features also run.")}
{benefit("4. Habits built into your tasks", "Every recurring task in Taven — daily, weekly, monthly or yearly — automatically becomes a habit with its own streak and history. Skip a day without losing track. Todoist offers Karma points and daily goals, but not per-task streaks.")}
{benefit("5. Analytics that show when you do your best work", "Completion rings, weekly charts, monthly heatmaps, your completion rate, your best day and a “Today's Intensity” gauge that warns you when you've planned too much.")}
{benefit("6. Nothing to set up or maintain", "Todoist rewards people who build and maintain a system. Taven is designed so you don't have to: add tasks, mark what matters, and let it handle the ordering. Less time organizing means more time doing.")}

    <h2>A typical morning in each app</h2>
    <div class="verdict">
{day("Todoist", ["Open the Today view", "Scan every task due today and overdue", "Check priority flags and labels", "Weigh deadlines against each other", "Pick something — often the easiest one"])}
{day("Taven", ["Open the app", "See your AI Suggested task and why it's first", "Start it"])}
    </div>

    <h2>Side by side</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th></th><th>Taven</th><th>Todoist</th></tr></thead>
      <tbody>
        <tr><td>Decides what to do next</td><td><strong>Yes — AI suggestion with a reason</strong></td><td>No — manual priorities and filters</td></tr>
        <tr><td>Price</td><td><strong>Free, no subscription</strong></td><td>Limited free plan; paid plans for full features</td></tr>
        <tr><td>Account required</td><td><strong>No</strong></td><td>Yes</td></tr>
        <tr><td>Where your tasks live</td><td><strong>On your device</strong> (optional private iCloud sync)</td><td>Todoist's servers</td></tr>
        <tr><td>AI</td><td><strong>On-device and private</strong></td><td>Cloud-based</td></tr>
        <tr><td>Data collected</td><td><strong>None</strong></td><td>Account and usage data</td></tr>
        <tr><td>Habit streaks</td><td><strong>Per task, built in</strong></td><td>Karma points and goals</td></tr>
        <tr><td>Analytics</td><td>Completion rings, weekly charts, monthly heatmaps, daily intensity</td><td>Productivity view and Karma trends</td></tr>
        <tr><td>Recurring tasks</td><td>Daily, weekly, monthly, yearly, optional end dates</td><td>Very flexible, set with natural language</td></tr>
        <tr><td>Platforms</td><td>iPhone, iPad</td><td>iOS, Android, Mac, Windows, web</td></tr>
        <tr><td>Team collaboration</td><td>No</td><td>Shared projects, comments, assignees</td></tr>
        <tr><td>Integrations</td><td>Apple ecosystem</td><td>Large integration library</td></tr>
      </tbody>
    </table></div>

    <h2>When Todoist might be the better fit</h2>
    <p>To be fair, Todoist is a mature, well-made app. Stick with it if:</p>
    <ul>
      <li>You need your tasks on <strong>Android, Windows or the web</strong> — Taven is iPhone and iPad only.</li>
      <li>You <strong>share projects with a team</strong> and need assignees and comments.</li>
      <li>You depend on <strong>integrations</strong> with tools like Slack, email or your calendar.</li>
    </ul>
    <p>If you mostly use Todoist for your own tasks on an iPhone or iPad, none of those apply — and Taven will likely save you both time and money.</p>

    <h2>Switching from Todoist to Taven</h2>
    <ol>
      <li><a href="{APP}">Download Taven</a> — it's free and there's no account to create.</li>
      <li>Add what's due in the next week first. You don't need to move your whole backlog on day one.</li>
      <li>Recreate your recurring tasks; each one becomes a habit with a streak automatically.</li>
      <li>Turn on iCloud sync if you use both iPhone and iPad.</li>
      <li>Tomorrow morning, open Taven and do the task it suggests.</li>
    </ol>

    <h2>The verdict</h2>
    <div class="verdict">
      <div class="card frost"><h3>Choose Taven if…</h3><ul>
        <li>You're on iPhone or iPad</li>
        <li>You want to be told what to do next, not build a system</li>
        <li>You want your tasks private, with no account</li>
        <li>You'd rather not pay a subscription</li>
        <li>You want habits and streaks built into your tasks</li>
      </ul></div>
      <div class="card frost"><h3>Stick with Todoist if…</h3><ul>
        <li>You need Android, Windows or web access</li>
        <li>You manage shared projects with a team</li>
        <li>You rely on third-party integrations</li>
      </ul></div>
    </div>''',
    faqs=[
        ("Is Taven a good Todoist alternative?", "Yes — especially if you're on iPhone or iPad and use Todoist for personal tasks. Taven is free with no subscription, needs no account, keeps your data on your device, and automatically suggests what to do next. If you need Android, Windows or team collaboration, Todoist remains the better fit."),
        ("Why switch from Todoist to Taven?", "The main reasons are automatic prioritization (Taven picks your next task and explains why), privacy (no account, on-device AI, zero data collected), price (free, no subscription) and built-in habit streaks for every recurring task."),
        ("Is Taven free?", "Yes. Taven is free to download with no subscription and no account."),
        ("Does Taven work on Android or Windows?", "No. Taven is available for iPhone and iPad, and syncs between them through your private iCloud account."),
    ],
    related=["compare/taven-vs-ticktick.html", "guides/best-task-manager-apps-iphone.html", "guides/what-task-to-do-next.html"],
))

# 6. Taven vs TickTick
PAGES.append(dict(
    kind="compare", path="compare/taven-vs-ticktick.html",
    label="Comparison", short="Taven vs. TickTick",
    blurb="Why people switch from TickTick to Taven: one clear answer instead of more views, real privacy and no Premium.",
    title="Taven vs. TickTick (2026): The Simpler, Private TickTick Alternative for iPhone — Taven",
    desc="Taven vs. TickTick compared: Taven tells you what to do next with on-device AI, builds habit streaks into your tasks, needs no account and is free with no Premium tier. See where each app wins.",
    h1="Taven vs. <span>TickTick</span>",
    h1_plain="Taven vs. TickTick",
    lede="TickTick gives you more ways to look at your tasks. Taven gives you one answer: what to do next. Here's how they compare, and why people who feel buried in features switch to Taven.",
    answer="<strong>Taven</strong> is the better choice if you're on iPhone or iPad and want a calm app that <strong>tells you what to do next</strong> instead of adding more views to manage. It's <strong>free with no Premium tier</strong>, needs <strong>no account</strong>, builds <strong>habit streaks into every recurring task</strong>, and runs its AI <strong>privately on your device</strong>. TickTick is the better fit if you need a built-in Pomodoro timer, calendar views, or Android, Windows or web access.",
    body=f'''    {COMPARE_DISCLOSURE.format(other="TickTick")}

    <h2>Why choose Taven over TickTick</h2>
{benefit("1. One answer instead of more views", "TickTick offers lists, a calendar, an Eisenhower matrix, a habit tracker and a focus timer — powerful, but every view is another place to look and another decision to make. Taven's on-device AI weighs importance, due dates and recurrence and puts one <strong>AI Suggested</strong> task at the top, with the reason why. Less looking, more doing.")}
{benefit("2. Free, with no Premium paywall", "Taven is free with no subscription. Many of TickTick's standout features, including its full calendar views, require a Premium subscription.")}
{benefit("3. Private by design", "Taven has no accounts, no servers holding your tasks and no third-party SDKs, and it collects zero data. Its AI runs on your device. TickTick requires an account and syncs your tasks through its cloud.")}
{benefit("4. Habits that live inside your tasks", "TickTick keeps habits in a separate tracker you maintain alongside your task list. In Taven, a recurring task <em>is</em> the habit: it gets its own streak and history automatically, and you can skip a day without losing track.")}
{benefit("5. A calmer app", "Fewer features is a feature. Taven has less to configure, fewer places for tasks to hide and nothing pulling your attention away from the one thing you should be doing.")}
{benefit("6. Analytics that keep you honest", "Completion rings, weekly charts, monthly heatmaps, your best day and a “Today's Intensity” gauge that shows when you've planned more than you can finish.")}

    <h2>A typical morning in each app</h2>
    <div class="verdict">
{day("TickTick", ["Open the app", "Choose a view: list, calendar or matrix", "Check your habits in the habit tracker", "Sort out what's urgent versus important", "Pick a task and start a focus timer"])}
{day("Taven", ["Open the app", "See your AI Suggested task and why it's first", "Start it — your habits are already in your task list"])}
    </div>

    <h2>Side by side</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th></th><th>Taven</th><th>TickTick</th></tr></thead>
      <tbody>
        <tr><td>Decides what to do next</td><td><strong>Yes — AI suggestion with a reason</strong></td><td>No — manual priorities and matrix view</td></tr>
        <tr><td>Price</td><td><strong>Free, no subscription</strong></td><td>Free plan; Premium subscription for full features</td></tr>
        <tr><td>Account required</td><td><strong>No</strong></td><td>Yes</td></tr>
        <tr><td>Where your tasks live</td><td><strong>On your device</strong> (optional private iCloud sync)</td><td>TickTick's servers</td></tr>
        <tr><td>Data collected</td><td><strong>None</strong></td><td>Account and usage data</td></tr>
        <tr><td>Habits</td><td><strong>Built into every recurring task</strong></td><td>Separate habit tracker</td></tr>
        <tr><td>Analytics</td><td>Completion rings, weekly charts, monthly heatmaps, daily intensity</td><td>Completion and focus statistics</td></tr>
        <tr><td>Focus timer</td><td>No</td><td>Built-in Pomodoro</td></tr>
        <tr><td>Calendar views</td><td>No</td><td>Yes (fuller views on Premium)</td></tr>
        <tr><td>Platforms</td><td>iPhone, iPad</td><td>iOS, Android, Mac, Windows, web</td></tr>
        <tr><td>Shared lists</td><td>No</td><td>Yes</td></tr>
      </tbody>
    </table></div>

    <h2>When TickTick might be the better fit</h2>
    <p>TickTick is a capable all-in-one app. It may suit you better if:</p>
    <ul>
      <li>You want a <strong>Pomodoro focus timer</strong> or <strong>calendar view</strong> inside your task app.</li>
      <li>You need <strong>Android, Windows or web</strong> access — Taven is iPhone and iPad only.</li>
      <li>You <strong>share lists</strong> with other people.</li>
    </ul>
    <p>If what you actually want is to stop deliberating and start working, Taven's focus on one clear next step is the advantage.</p>

    <h2>Switching from TickTick to Taven</h2>
    <ol>
      <li><a href="{APP}">Download Taven</a> — it's free and there's no account to create.</li>
      <li>Add what's due in the next week first. You don't need to move your whole backlog on day one.</li>
      <li>Turn each TickTick habit into a recurring task in Taven — it gets a streak automatically.</li>
      <li>Turn on iCloud sync if you use both iPhone and iPad.</li>
      <li>Tomorrow morning, open Taven and do the task it suggests.</li>
    </ol>

    <h2>The verdict</h2>
    <div class="verdict">
      <div class="card frost"><h3>Choose Taven if…</h3><ul>
        <li>You're on iPhone or iPad</li>
        <li>Too many views and features make you procrastinate</li>
        <li>You want to be told what to do next</li>
        <li>You want privacy and no subscription</li>
        <li>You want habits tracked right inside your tasks</li>
      </ul></div>
      <div class="card frost"><h3>Stick with TickTick if…</h3><ul>
        <li>You rely on a built-in Pomodoro timer or calendar</li>
        <li>You need Android, Windows or web access</li>
        <li>You share lists with others</li>
      </ul></div>
    </div>''',
    faqs=[
        ("Is Taven a good TickTick alternative?", "Yes — especially if you're on iPhone or iPad and feel TickTick has more features than you use. Taven is free with no Premium tier, needs no account, keeps your data on your device, builds habit streaks into recurring tasks, and tells you what to do next."),
        ("Why switch from TickTick to Taven?", "People switch for a simpler app that makes the prioritization decision for them, for privacy (no account, on-device AI, zero data collected), and to avoid paying for Premium."),
        ("Does Taven have a habit tracker?", "Yes. Every recurring task in Taven (daily, weekly, monthly or yearly) becomes a habit with its own streak and history, and you can skip a day without losing track."),
        ("Does Taven have a Pomodoro timer?", "No. Taven focuses on choosing the right task to work on. If a built-in focus timer is essential to you, TickTick includes one."),
    ],
    related=["compare/taven-vs-todoist.html", "guides/best-task-manager-apps-iphone.html", "guides/to-do-list-overwhelm.html"],
))

# ─────────────────────────────────────────────────────────────
# FAQ page (/faq.html): list of (group heading, [(question, answer_html), ...])
FAQ = [
    ("About Taven", [
        ("What is Taven?", "Taven is a free task manager and AI to-do list app for iPhone and iPad. It doesn't just organize your tasks — it tells you what to do next, using on-device intelligence to surface your most important task."),
        ("How does Taven decide what I should do next?", "Taven weighs each task's importance, due date and recurrence, then puts one AI Suggested task at the top of your day with a short reason, such as “Due today and your top priority.” You don't need to set up filters or priority systems."),
        ("Does Taven track habits?", "Yes. Every recurring task — daily, weekly, monthly or yearly — becomes a habit with its own streak and history, and you can skip a day without losing track."),
        ("How is Taven different from Todoist or TickTick?", 'Todoist and TickTick are powerful, cross-platform organizers with collaboration and lots of views. Taven is simpler, private and free, and decides what you should do next for you. See <a href="/compare/taven-vs-todoist.html">Taven vs. Todoist</a> and <a href="/compare/taven-vs-ticktick.html">Taven vs. TickTick</a>.'),
    ]),
    ("Pricing & devices", [
        ("Is Taven free?", "Yes. Taven is free to download with no subscription."),
        ("Which devices does Taven work on?", "Taven is available for iPhone and iPad. It isn't available on Android, Windows or the web."),
        ("Can I use Taven on more than one device?", "Yes. Taven can optionally sync between your iPhone and iPad through your own private iCloud account."),
    ]),
    ("Privacy & accounts", [
        ("Do I need to create an account?", "No. Taven works without any account."),
        ("Is my data private?", 'Yes. Your tasks stay on your device, Taven\'s AI runs on-device, and Taven collects zero data and includes no third-party SDKs. <a href="/privacy.html">Read the privacy policy</a>.'),
    ]),
    ("Choosing an app", [
        ("Where can I compare Taven with other apps?", 'Read our <a href="/guides/best-task-manager-apps-iphone.html">iPhone task manager comparison</a>, the <a href="/guides/best-ai-to-do-list-apps.html">best AI to-do list apps</a>, or browse <a href="/guides/">all guides</a>.'),
    ]),
]

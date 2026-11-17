APP = "https://apps.apple.com/app/id6761032737"

# Voice notes for anyone editing these pages:
# Write like a thoughtful friend explaining something over coffee. Plain words,
# contractions, short paragraphs, the occasional aside. Be honest about trade-offs.
# No em or en dashes, no "game-changer", no bolded label at the start of every bullet.

HUB = {
    "title": "Productivity Guides and Task App Comparisons | Taven",
    "desc": "Plain-spoken guides on figuring out what to do next, getting unstuck from a huge to-do list, and picking a task app for iPhone and iPad, plus honest comparisons of Taven, Todoist and TickTick.",
    "lede": "Plain-spoken guides on figuring out what to do next, getting unstuck from a huge to-do list, and picking a task app that actually suits you. Including the times when that app isn't ours.",
}

DISCLOSURE = '<div class="note"><strong>Quick disclosure:</strong> we make Taven, so take our enthusiasm with a grain of salt. That said, every app on this page is good at something, and we\'ve tried to say plainly where Taven isn\'t the right pick. Prices and features change a lot, so double check the App Store before you commit to anything.</div>'

def card(name, tag, best_for, platforms, price, strengths, tradeoffs, extra=""):
    return f'''    <div class="card frost">
      <h3>{name} <span class="tag">{tag}</span></h3>
      {extra}<dl>
        <dt>Best for</dt><dd>{best_for}</dd>
        <dt>Platforms</dt><dd>{platforms}</dd>
        <dt>Price</dt><dd>{price}</dd>
        <dt>What's good</dt><dd>{strengths}</dd>
        <dt>The catch</dt><dd>{tradeoffs}</dd>
      </dl>
    </div>'''

TAVEN_CARD = lambda tag: card(
    f'<a href="/">Taven</a>', tag,
    "People who don't want to run a productivity system. You open it, it tells you what to do next, you do it.",
    "iPhone and iPad",
    "Free. No subscription and no account.",
    "The AI picks your top task and tells you why (something like “Due today and your top priority”), and it does this on your phone rather than on a server. It also has a clean, minimal design, a calendar, recurring tasks that double as habits with streaks, and some genuinely nice completion stats. Sync between devices goes through your own iCloud if you want it.",
    "It's Apple only. There's no team collaboration or shared projects, and you won't find the deep integrations or power user views that older apps have built up over the years.")

# ─────────────────────────────────────────────────────────────
PAGES = []

# 1. Best task manager apps for iPhone
PAGES.append(dict(
    kind="list", path="guides/best-task-manager-apps-iphone.html",
    label="App roundup", short="Best task manager apps for iPhone",
    blurb="Seven good iPhone to-do apps, who each one is really for, and where each one falls down.",
    title="Best Task Manager Apps for iPhone (2026): 7 To-Do Apps Compared | Taven",
    desc="An honest look at the best task manager and to-do list apps for iPhone and iPad in 2026: Taven, Things 3, Todoist, TickTick, Apple Reminders, Microsoft To Do and OmniFocus. Who each one suits, and the catch with each.",
    h1="The best task manager apps for <span>iPhone</span>",
    h1_plain="The best task manager apps for iPhone (2026)",
    lede="There isn't one best to-do app. There's the one that fits how your brain works, and most people go through three or four before they find it. Here are seven worth trying.",
    answer="If you'd like an app that simply <strong>tells you what to do next</strong>, with no setup, account or subscription, try <strong>Taven</strong>. If you love beautiful design and would rather pay once than subscribe, get <strong>Things 3</strong>. If you're on Android or Windows too, or you share projects with people, go with <strong>Todoist</strong>. If you want a timer, calendar and habit tracker all in one place, look at <strong>TickTick</strong>. And if you just need a list, <strong>Apple Reminders</strong> is already on your phone.",
    itemlist=["Taven", "Things 3", "Todoist", "TickTick", "Apple Reminders", "Microsoft To Do", "OmniFocus"],
    body=f'''    {DISCLOSURE}

    <h2>How we picked these</h2>
    <p>We tried to judge these the way you'd actually use them. How quickly can you get a task in? Does the app help you decide what to work on, or does it just hold your list? Does it work on all your devices? What will it cost you over a year? And what happens to your data?</p>
    <p>Every app here is actively maintained and good at something. The trick is matching the app to the way you work, rather than the other way round.</p>

    <h2>The quick version</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th>App</th><th>Best for</th><th>Platforms</th><th>How you pay</th><th>Account?</th></tr></thead>
      <tbody>
        <tr><td>Taven</td><td>Being told what to do next</td><td>iPhone, iPad</td><td>Free</td><td>No</td></tr>
        <tr><td>Things 3</td><td>Lovely, calm personal planning</td><td>iPhone, iPad, Mac, Apple Watch</td><td>One-time purchase per device type</td><td>Only for sync</td></tr>
        <tr><td>Todoist</td><td>Working across platforms and with other people</td><td>iOS, Android, Mac, Windows, web</td><td>Free plan plus subscription</td><td>Yes</td></tr>
        <tr><td>TickTick</td><td>Tasks, calendar, habits and a timer in one app</td><td>iOS, Android, Mac, Windows, web</td><td>Free plan plus subscription</td><td>Yes</td></tr>
        <tr><td>Apple Reminders</td><td>Simple lists, Siri and family sharing</td><td>Apple devices, iCloud web</td><td>Free</td><td>Apple ID</td></tr>
        <tr><td>Microsoft To Do</td><td>People who live in Outlook</td><td>iOS, Android, Windows, Mac, web</td><td>Free</td><td>Microsoft account</td></tr>
        <tr><td>OmniFocus</td><td>Serious Getting Things Done fans</td><td>iPhone, iPad, Mac, Apple Watch, web</td><td>Subscription or license</td><td>Only for sync</td></tr>
      </tbody>
    </table></div>

    <h2>The apps</h2>
{TAVEN_CARD("Best for knowing what's next")}
{card("Things 3", "Best design", "Individuals who are all in on Apple and want something calm and gorgeous.", "iPhone, iPad, Mac, Apple Watch", "You pay once, but separately for iPhone, iPad and Mac.", "It's probably the best looking task app ever made. The Today, Upcoming, Anytime and Someday structure is clever, quick entry is fast, and syncing through Things Cloud is free.", "No collaboration, nothing for Android or Windows, and while it organizes your tasks beautifully, deciding what to actually do is still your job.")}
{card("Todoist", "Best cross-platform", "People who bounce between iPhone, Android, Windows and a browser, or who share projects with others.", "iOS, Android, Mac, Windows, web, browser extensions", "There's a free plan with limits, plus paid Pro and Business plans.", "Its natural language entry is the best around. Type “pay rent every 1st” and it just works. Add labels, filters, shared projects, comments, a huge pile of integrations and some AI features, and you can build almost anything.", "You need an account, and your tasks live on Todoist's servers. The free plan is fairly limited, and the really powerful filters take a while to set up.")}
{card("TickTick", "Best all-in-one", "People who'd like their tasks, calendar, habit tracker and focus timer all in the same app.", "iOS, Android, Mac, Windows, web", "Free plan, with a paid Premium subscription.", "There's a built-in Pomodoro timer, a habit tracker, calendar views, an Eisenhower matrix view and natural language entry. It's a lot of app for the money.", "You need an account, and plenty of the best bits (like the full calendar views) are Premium only. All those features also make for a busier screen.")}
{card("Apple Reminders", "Best free built-in", "Simple personal and household lists, especially ones you share with family.", "iPhone, iPad, Mac, Apple Watch, iCloud.com", "Free.", "It's already installed, Siri handles it well, and shared lists, smart lists, tags and the grocery list sorting are all genuinely useful.", "It holds your list but won't help you prioritize it, and the stats and habit tracking are pretty basic.")}
{card("Microsoft To Do", "Best for Microsoft people", "Anyone whose working life runs through Outlook and Microsoft 365.", "iOS, Android, Windows, Mac, web", "Free.", "The “My Day” list is a nice daily planning habit, and it syncs with your Outlook tasks. Shared lists work well too.", "You'll need a Microsoft account, and it has fewer advanced features than Todoist or TickTick.")}
{card("OmniFocus", "Best for GTD power users", "People who follow Getting Things Done and want total control over how they see their work.", "iPhone, iPad, Mac, Apple Watch, web", "Subscription or license.", "Custom perspectives, defer dates, a proper weekly review mode and deep automation.", "The learning curve is steep and it's the priciest app here. For most people, it's a lot more than they need.")}

    <h2>So which one should you get?</h2>
    <p>If you've got too many tasks and you never know where to start, that's exactly the problem Taven was built for. It's organized around one question: what should I do next? (We wrote a whole guide on <a href="/guides/what-task-to-do-next.html">how to decide what task to do next</a> if you'd like to do it by hand.)</p>
    <p>If you also use Android or Windows, you'll want Todoist or TickTick. If you share lists with a team or a partner, Todoist is the strongest choice, though Apple Reminders is fine for simple shared lists. If you hate subscriptions and care a lot about design, Things 3 is lovely.</p>
    <p>If a focus timer matters to you, TickTick has one built in. Taven has a calendar and habit streaks, but no Pomodoro timer. And if privacy is your top priority, Taven (no account, AI on your device) and Things 3 are the two to look at.</p>''',
    faqs=[
        ("What's the best free task manager app for iPhone?", "If you want help prioritizing plus habit tracking, Taven is free with no subscription or account. If you just need simple lists, Apple Reminders is free and already on your phone. Todoist and TickTick both have free plans too, with more behind a subscription."),
        ("What's the best to-do app for both iPhone and iPad?", "Taven, Things 3, Todoist, TickTick and OmniFocus all work on both. Taven syncs between them through your own private iCloud account."),
        ("Which iPhone task manager doesn't need an account?", "Taven doesn't need one at all, and it does all its processing on your device. Things 3 also works without an account unless you turn on Things Cloud sync."),
        ("Which to-do app tells you what to do next?", "That's Taven's whole thing. It looks at importance, due dates and how often a task repeats, then highlights the one task you should do next and tells you why."),
    ],
    related=["guides/best-ai-to-do-list-apps.html", "compare/taven-vs-todoist.html", "compare/taven-vs-ticktick.html", "guides/what-task-to-do-next.html"],
))

# 2. Best AI to-do list apps
PAGES.append(dict(
    kind="list", path="guides/best-ai-to-do-list-apps.html",
    label="App roundup", short="Best AI to-do list apps",
    blurb="What “AI” actually does inside task apps right now, and which app to pick depending on what you need help with.",
    title="Best AI To-Do List Apps (2026): What the AI Actually Does | Taven",
    desc="A plain-English guide to AI to-do list and task manager apps in 2026: Taven, Motion, Reclaim.ai, Todoist, Goblin Tools and Sunsama. What each one's AI really does, and who it's for.",
    h1="The best <span>AI</span> to-do list apps",
    h1_plain="The best AI to-do list apps (2026)",
    lede="Every task app seems to say “AI powered” now, and it means wildly different things. Some pick your next task. Some rearrange your calendar. Some break big jobs into small steps. Here's what each one actually does.",
    answer="Start with the job you want the AI to do. If you want it to <strong>tell you which task to do next</strong>, privately on your iPhone and for free, use <strong>Taven</strong>. If you want it to <strong>schedule your tasks into your calendar</strong>, try <strong>Motion</strong> or <strong>Reclaim.ai</strong>. If big tasks paralyze you and you want them <strong>broken into small steps</strong>, use <strong>Goblin Tools</strong>. And if you want a full traditional task manager with some AI help sprinkled on top, <strong>Todoist</strong> is the safe choice.",
    itemlist=["Taven", "Motion", "Reclaim.ai", "Todoist", "Goblin Tools", "Sunsama"],
    body=f'''    {DISCLOSURE}

    <h2>What “AI” usually means in a task app</h2>
    <p>Once you look past the marketing, the AI in to-do apps tends to do one of four things.</p>
    <p>The first is prioritization. The app looks at everything on your list and tells you which task matters most right now. This goes after decision fatigue, which is that miserable stretch of time you spend staring at a list trying to work out where to start.</p>
    <p>The second is scheduling. The app finds free slots in your calendar, drops your tasks into them, and shuffles things around when your day changes.</p>
    <p>The third is breaking tasks down. You type “clean the garage” and get back a list of actual, doable steps.</p>
    <p>The fourth is the general assistant, where a chatbot style AI inside a normal task manager helps you write, rewrite or organize tasks.</p>
    <p>It's also worth asking where the AI runs. Cloud AI sends your task text off to a server somewhere. On-device AI runs on your phone, so your tasks never leave it. If your to-do list includes anything personal (and whose doesn't?), that difference matters.</p>

    <h2>The quick version</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th>App</th><th>What its AI does</th><th>Where the AI runs</th><th>Platforms</th><th>How you pay</th></tr></thead>
      <tbody>
        <tr><td>Taven</td><td>Picks your next task and explains why</td><td>On your device</td><td>iPhone, iPad</td><td>Free</td></tr>
        <tr><td>Motion</td><td>Schedules tasks and projects into your calendar</td><td>Cloud</td><td>Web, desktop, mobile</td><td>Subscription</td></tr>
        <tr><td>Reclaim.ai</td><td>Fits tasks, habits and focus time around your meetings</td><td>Cloud</td><td>Web (Google or Outlook calendar)</td><td>Free plan plus subscription</td></tr>
        <tr><td>Todoist</td><td>An AI assistant inside a full task manager</td><td>Cloud</td><td>iOS, Android, desktop, web</td><td>Free plan plus subscription</td></tr>
        <tr><td>Goblin Tools</td><td>Breaks tasks into steps and estimates time</td><td>Cloud</td><td>Web, iOS, Android</td><td>Free on the web, cheap apps</td></tr>
        <tr><td>Sunsama</td><td>Guided daily planning, with a bit of AI help</td><td>Cloud</td><td>Web, desktop, mobile</td><td>Subscription</td></tr>
      </tbody>
    </table></div>

    <h2>The apps</h2>
{TAVEN_CARD("Best for “what now?”")}
{card("Motion", "Best AI calendar", "Busy professionals and teams whose days are mostly meetings.", "Web, Mac, Windows, iOS, Android", "Subscription, and one of the pricier options here.", "It schedules everything for you. Give it tasks with deadlines and time estimates and it builds your day, then rebuilds it when something slips. There's project management for teams too.", "It's expensive if you're just one person, it needs your calendar connected, and it only works well if you estimate how long every task will take.")}
{card("Reclaim.ai", "Best for protecting your time", "People on Google Calendar or Outlook who want focus time and habits defended from meetings.", "Web app that connects to Google Calendar or Outlook", "Free plan, plus paid tiers.", "Smart time blocking for habits and tasks, buffers between meetings, and scheduling links.", "It lives in your calendar rather than being a to-do list in its own right, so it's much less useful if your day isn't calendar driven.")}
{card("Todoist", "Best classic app with AI added", "People who want a mature, cross-platform task manager with a little AI help on the side.", "iOS, Android, Mac, Windows, web", "Free plan, with AI features and more on paid plans.", "You get everything Todoist is known for (natural language entry, filters, shared projects, integrations) plus AI help breaking down and wording tasks.", "The AI helps you, but it doesn't decide for you. Prioritizing still means setting flags and building filters yourself, and you'll need an account.")}
{card("Goblin Tools", "Best for breaking tasks down", "Anyone who gets stuck starting big, vague tasks. It's especially popular with neurodivergent folks.", "Web (free), iOS, Android", "Free on the web, with a small one-time price for the apps.", "Its “Magic To-Do” turns one task into a list of steps, and a “spiciness” dial controls how much detail you get. There are handy time estimation and tone checking tools as well.", "It's a helper rather than a full task manager. There are no reminders, no recurring tasks and no long term organization.")}
{card("Sunsama", "Best planning ritual", "Knowledge workers who'd like a calm, guided routine for planning each day and week.", "Web, Mac, Windows, iOS, Android", "Subscription.", "It pulls tasks in from email, Slack, Asana, Trello and friends into one daily plan, with timeboxing and an end of day shutdown ritual.", "It's really a planning method more than AI. It's subscription only, and the morning ritual does take a few minutes every day.")}

    <h2>So which one should you pick?</h2>
    <p>If you open your list and just freeze, try Taven. It picks one task and tells you why, and we've written more about that feeling in <a href="/guides/to-do-list-overwhelm.html">how to stop feeling overwhelmed by your to-do list</a>.</p>
    <p>If your calendar is wall to wall meetings, Motion or Reclaim.ai will probably help you more. If your problem is that tasks feel too big to even start, Goblin Tools is great, and it's free. If you want a full featured app that works everywhere with some AI on top, Todoist is the dependable option.</p>
    <p>And if you'd rather your tasks weren't sent to an AI server at all, Taven is the one that keeps everything on your iPhone or iPad.</p>''',
    faqs=[
        ("Is there an AI app that tells you what to do next?", "Yes. Taven, for iPhone and iPad, is built around exactly this. Its on-device AI looks at importance, due dates and how often tasks repeat, then shows you your single most important task with a short reason like “Due today and your top priority.”"),
        ("Which AI to-do list app is the most private?", "Taven runs its AI entirely on your device, doesn't need an account and doesn't collect any data. Most other AI task apps, including Motion, Reclaim and Todoist's AI features, process your tasks in the cloud."),
        ("Is there a free AI task manager?", "Taven is free with no subscription. Goblin Tools is free on the web. Reclaim.ai and Todoist both have free plans with some limits."),
        ("What's the difference between AI prioritizing and AI scheduling?", "Prioritizing decides <em>which</em> task matters most right now, which is what Taven does. Scheduling decides <em>when</em> each task happens by putting it on your calendar, which is what Motion and Reclaim.ai do."),
    ],
    related=["guides/best-task-manager-apps-iphone.html", "guides/what-task-to-do-next.html", "compare/taven-vs-todoist.html", "guides/to-do-list-overwhelm.html"],
))

# 3. Overwhelm
PAGES.append(dict(
    kind="guide", path="guides/to-do-list-overwhelm.html",
    label="Guide", short="How to stop feeling overwhelmed by your to-do list",
    blurb="Why a long list freezes you up, and a seven-step reset to get moving again today.",
    title="How to Stop Feeling Overwhelmed by Your To-Do List (7 Steps) | Taven",
    desc="Why a long to-do list leads to overwhelm and procrastination, and a practical seven-step reset: get it all out of your head, cut hard, pick one task, make it tiny, and keep your list manageable.",
    h1="How to stop feeling overwhelmed by your <span>to-do list</span>",
    h1_plain="How to stop feeling overwhelmed by your to-do list",
    lede="Here's the slightly annoying truth. The length of your list usually isn't the real problem. The problem is that every time you look at it, you have to decide all over again what matters. So let's fix that.",
    answer="Get everything out of your head and onto one list. Cut or postpone anything that doesn't matter this week. Then <strong>pick one task and look only at that one</strong>, and make it small enough that you could start it in two minutes. Overwhelm mostly comes from choosing between lots of tasks, not from doing them, so the goal is to do less choosing.",
    body='''    <h2>Why your list feels so heavy</h2>
    <p>When you look at forty open tasks, your brain tries to compare all of them at once. Which is most urgent? Which is most important? Which one's quick? Which one have you been quietly avoiding for three weeks? That's decision fatigue, and it wears you out before you've actually done anything. What usually happens next is that you pick the easiest thing (hello, inbox) or you go and make a coffee and don't come back.</p>
    <p>Unfinished tasks also have a way of nagging at you. Psychologists call it the Zeigarnik effect: incomplete tasks tend to stay active in your memory. The encouraging part comes from some research by Masicampo and Baumeister, who found that simply making a specific plan for an unfinished goal reduced those intrusive thoughts. In other words, you don't have to finish everything to feel calmer. You just need to know what happens next.</p>

    <h2>A seven-step reset</h2>
    <h3>1. Get everything out of your head</h3>
    <p>Set a timer for ten minutes and write down every task, errand and low level worry you can think of. Don't organize anything yet. Just getting it all into one place you trust is a surprising relief.</p>
    <h3>2. Cut hard</h3>
    <p>Go through the list and ask, for each item, whether anything bad would actually happen if it never got done. If not, delete it, hand it to someone else, or move it to a “someday” list. Most lists lose about a third of their weight here.</p>
    <h3>3. Only put dates on things with real deadlines</h3>
    <p>Pretend deadlines (“I'll do it Tuesday”) slowly turn into a wall of red overdue tasks that make you feel guilty without telling you anything useful. Date the bill, the appointment and the client deadline. Leave the rest undated.</p>
    <h3>4. Put the repeating stuff on autopilot</h3>
    <p>Rent, workouts, the weekly review, watering the plants. None of this should be taking up space in your head. Set it to repeat once and stop thinking about it.</p>
    <h3>5. Pick one task and hide the rest</h3>
    <p>Choose the one task that matters most right now. (If you're not sure how, our guide on <a href="/guides/what-task-to-do-next.html">deciding what task to do next</a> walks through it.) Then look only at that task. Nobody has ever been overwhelmed by a list with one thing on it.</p>
    <h3>6. Shrink it until it's easy to start</h3>
    <p>“Write report” is a project, not a task. “Open the doc and type out the three section headings” is a task. If you can't picture yourself starting it in the next two minutes, break it down a bit more.</p>
    <h3>7. Keep each day small</h3>
    <p>Plan three to five meaningful things for the day, not twenty. Finishing a short list gives you momentum. Failing an impossible one just gives you dread for tomorrow.</p>

    <h2>Where Taven fits in</h2>
    <p>This is honestly the exact problem we built <a href="/">Taven</a> to solve. Instead of showing you a long list and leaving the choice to you, Taven's on-device AI looks at importance, due dates and how often things repeat, and puts <strong>one suggested task</strong> at the top along with the reason, something like “Due today and your top priority.” Repeating tasks run themselves, and a little “Today's Intensity” gauge lets you know when you've planned more than you can realistically do. It's free on iPhone and iPad, and there's no account to make.</p>
    <p>To be clear, you don't need an app for any of the steps above. Paper works fine. But if you keep freezing in front of the same list day after day, letting something else make that first decision can be a really easy way to break the loop.</p>''',
    faqs=[
        ("Why do I freeze up when I look at my to-do list?", "Most of the time it's decision fatigue. A long list makes you compare every task against every other task each time you look at it. Shrinking the list and committing to one next task takes most of that weight away."),
        ("How many tasks should I put on my daily list?", "Most people do best with three to five meaningful tasks a day, plus a few small routine ones. The 1-3-5 method (one big thing, three medium, five small) is a nice template if you want one."),
        ("Is there an app that helps with to-do list overwhelm?", "Taven for iPhone and iPad was made for it. It suggests the one task to do next and tells you why, so you don't have to sort through the whole list yourself. Goblin Tools is also great for breaking big tasks into small steps."),
    ],
    related=["guides/what-task-to-do-next.html", "guides/best-ai-to-do-list-apps.html", "guides/best-task-manager-apps-iphone.html"],
))

# 4. What task next
PAGES.append(dict(
    kind="guide", path="guides/what-task-to-do-next.html",
    label="Guide", short="How to decide what task to do next",
    blurb="Five tried and tested ways to prioritize, a quick rule you can use in ten seconds, and when to let an app decide.",
    title="How to Decide What Task to Do Next: 5 Simple Methods | Taven",
    desc="Five proven ways to decide what task to do next (the Eisenhower matrix, eat the frog, 1-3-5, MIT and ABCDE), plus a quick deadline and importance rule, and when it makes sense to let an app choose for you.",
    h1="How to decide what task to <span>do next</span>",
    h1_plain="How to decide what task to do next",
    lede="Choosing what to work on is often harder than the work itself. Here are five methods people have relied on for years, a rule you can use in about ten seconds, and what to do if you'd rather not decide at all.",
    answer="Do the task with the <strong>nearest real deadline</strong> that also <strong>actually matters</strong>. If nothing's due, do the important task you've been avoiding, and do it first. If you're stuck between two, pick the one that unblocks other work. Or let an app like <strong>Taven</strong> look at your deadlines, priorities and repeating tasks and pick for you.",
    body='''    <h2>The ten-second rule</h2>
    <p>When you just need an answer right now, run down this list and stop at the first yes.</p>
    <ol>
      <li>Is anything due today (or already overdue) where missing it would actually cause problems? Do that.</li>
      <li>Is anything holding up other people, or blocking your other tasks? Do that.</li>
      <li>Is there an important task you've been dodging? Do that, now, while you still have the energy.</li>
      <li>If none of the above, do whatever moves your most important goal forward.</li>
    </ol>

    <h2>Five methods worth knowing</h2>
    <h3>1. The Eisenhower matrix</h3>
    <p>Sort your tasks using two questions: is it urgent, and is it important? Urgent and important things get done now. Important but not urgent things get scheduled. Urgent but unimportant things get handed off or batched together. Anything that's neither gets dropped. The real value is that second group, the important work that never feels urgent until suddenly it's an emergency.</p>
    <h3>2. Eat the frog</h3>
    <p>This one was popularized by Brian Tracy. Do your biggest, most dreaded task first thing in the morning. Everything after that feels easier by comparison, and procrastination never gets a chance to build up.</p>
    <h3>3. The 1-3-5 rule</h3>
    <p>Each day, plan one big task, three medium ones and five small ones. It forces you into realistic days, and it makes your priority obvious. It's the big one.</p>
    <h3>4. Your Most Important Task</h3>
    <p>The night before, pick one to three tasks that would make tomorrow a good day no matter what else happens. Then do them before you open your email or your messages.</p>
    <h3>5. The ABCDE method</h3>
    <p>Give every task a letter. A means you must do it (there are real consequences). B means you should. C means it'd be nice. D means delegate it, and E means get rid of it. The only rule is that you never start a B while an A is still open.</p>

    <h2>A few traps to watch out for</h2>
    <p>The most common one is doing the quick little tasks so you feel productive. Clearing ten tiny things feels great, but the important thing is still sitting there afterwards.</p>
    <p>Another is re-prioritizing all day long. Decide once, then stick with it until the task is finished or something genuinely urgent shows up. It's also easy to treat everything as high priority, which is the same as having no priorities at all. And don't forget your recurring commitments. Habits and routine tasks quietly compete with your projects for the same hours, so count them.</p>

    <h2>Or let an app decide</h2>
    <p>Every one of these methods has the same hidden cost. You have to actually apply it, every day, to every task. That's the reason we made <a href="/">Taven</a>. Its on-device AI does the weighing for you (importance, due dates and repeating tasks) and puts one <strong>AI Suggested</strong> task at the top of your day with a reason in plain English, like “Due today and your top priority.” You open the app, see what's next, and get on with it.</p>
    <p>Taven is free on iPhone and iPad, there's no account, and all the thinking happens on your device. If you'd rather sort things yourself, TickTick has an Eisenhower matrix view and Todoist lets you set priority levels and build custom filters. Our <a href="/guides/best-task-manager-apps-iphone.html">iPhone task app comparison</a> goes through the options.</p>''',
    faqs=[
        ("How do I decide which task to do first?", "Start with anything due today that has real consequences, then anything that's holding other people up, then the important task you've been avoiding. If none of those apply, work on whatever moves your biggest goal forward."),
        ("What's the best way to prioritize?", "The Eisenhower matrix is the most popular, and it's great for sorting a long list. Eat the frog and the Most Important Task method are better for staying focused day to day. Plenty of people mix and match."),
        ("Is there an app that decides what I should do next?", "Yes. Taven for iPhone and iPad uses on-device AI to rank your tasks by importance, due date and how often they repeat, then highlights the one task you should do next and tells you why."),
    ],
    related=["guides/to-do-list-overwhelm.html", "guides/best-ai-to-do-list-apps.html", "guides/best-task-manager-apps-iphone.html"],
))

COMPARE_DISCLOSURE = '<div class="note"><strong>Quick disclosure:</strong> Taven is our app, so yes, we\'re biased. We\'ve still kept every fact on this page accurate, and we\'ve pointed out where {other} is the better choice. Features and prices change often, so check the App Store for the latest.</div>'

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
    blurb="Why people move from Todoist to Taven: it prioritizes for you, it's genuinely private, and there's no subscription.",
    title="Taven vs. Todoist (2026): A Free, Private Todoist Alternative for iPhone | Taven",
    desc="Taven vs. Todoist: Taven tells you what to do next using on-device AI, doesn't need an account, and is free with no subscription. Here's where each app wins and why people switch.",
    h1="Taven vs. <span>Todoist</span>",
    h1_plain="Taven vs. Todoist",
    lede="Todoist is brilliant at helping you organize everything. Taven is about helping you get the right thing done, by telling you what to do next. Here's how they stack up, and why a lot of iPhone and iPad users are making the switch.",
    answer="If you're on iPhone or iPad and you'd like an app that <strong>decides what you should do next</strong> instead of asking you to build a priority system, <strong>Taven</strong> is the better pick. It's <strong>free with no subscription</strong>, there's <strong>no account</strong>, and the AI runs <strong>privately on your device</strong>. Todoist only really pulls ahead if you need Android, Windows or the web, or you share projects with a team.",
    body=f'''    {COMPARE_DISCLOSURE.format(other="Todoist")}

    <h2>Why you might choose Taven over Todoist</h2>
{benefit("1. It tells you what to do next", "Todoist gives you priority flags (P1 to P4), labels and filter queries, and then it's up to you to decide. Taven makes the call for you. Its on-device AI looks at how important each task is, when it's due and whether it repeats, then puts one <strong>AI Suggested</strong> task at the top of your day with a reason in plain English, like “Due today and your top priority.” You open the app and get going, rather than scrolling through a list.")}
{benefit("2. It's actually free", "Taven costs nothing. There's no subscription and nothing hidden behind a paywall. Todoist's free plan is fairly limited, and you'll need a paid plan for the full feature set, AI features included.")}
{benefit("3. Your tasks stay yours", "Taven has no accounts, no servers storing your tasks and no third-party SDKs, and it collects no data at all. The AI runs entirely on your iPhone or iPad. Todoist needs an account and keeps your tasks in its cloud, which is also where its AI runs.")}
{benefit("4. Habits are built right into your tasks", "Every recurring task in Taven, whether it's daily, weekly, monthly or yearly, automatically becomes a habit with its own streak and history. You can skip a day without losing track. Todoist has Karma points and daily goals, but not a streak for each task.")}
{benefit("5. Stats that show when you do your best work", "You get completion rings, weekly charts, monthly heatmaps, your completion rate, your best day, and a “Today's Intensity” gauge that warns you when you've piled on too much.")}
{benefit("6. There's nothing to set up", "Todoist really rewards people who enjoy building and maintaining a system. Taven is designed for people who don't. Add your tasks, mark what matters, and let it sort out the order. Less time organizing, more time actually doing things.")}

    <h2>A typical morning in each app</h2>
    <div class="verdict">
{day("Todoist", ["Open the Today view", "Look through everything due today and overdue", "Check your priority flags and labels", "Weigh the deadlines against each other", "Pick something, which is often the easiest thing"])}
{day("Taven", ["Open the app", "See your AI Suggested task and why it's first", "Start it"])}
    </div>

    <h2>Side by side</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th></th><th>Taven</th><th>Todoist</th></tr></thead>
      <tbody>
        <tr><td>Decides what to do next</td><td><strong>Yes, an AI suggestion with a reason</strong></td><td>No, you set priorities and filters yourself</td></tr>
        <tr><td>Price</td><td><strong>Free, no subscription</strong></td><td>Limited free plan, paid plans for the full features</td></tr>
        <tr><td>Account needed</td><td><strong>No</strong></td><td>Yes</td></tr>
        <tr><td>Where your tasks live</td><td><strong>On your device</strong> (optional private iCloud sync)</td><td>On Todoist's servers</td></tr>
        <tr><td>AI</td><td><strong>On your device, private</strong></td><td>In the cloud</td></tr>
        <tr><td>Data collected</td><td><strong>None</strong></td><td>Account and usage data</td></tr>
        <tr><td>Habit streaks</td><td><strong>One for every recurring task</strong></td><td>Karma points and goals</td></tr>
        <tr><td>Stats</td><td>Completion rings, weekly charts, monthly heatmaps, daily intensity</td><td>Productivity view and Karma trends</td></tr>
        <tr><td>Recurring tasks</td><td>Daily, weekly, monthly, yearly, with optional end dates</td><td>Very flexible, set up with natural language</td></tr>
        <tr><td>Platforms</td><td>iPhone, iPad</td><td>iOS, Android, Mac, Windows, web</td></tr>
        <tr><td>Team collaboration</td><td>No</td><td>Shared projects, comments, assignees</td></tr>
        <tr><td>Integrations</td><td>Apple ecosystem</td><td>A big integration library</td></tr>
      </tbody>
    </table></div>

    <h2>When Todoist might suit you better</h2>
    <p>In fairness, Todoist is a mature, really well made app, and there are good reasons to stay with it. If you need your tasks on Android, Windows or the web, Todoist has you covered and Taven doesn't (it's iPhone and iPad only). If you share projects with a team and need assignees and comments, Todoist is built for that. And if your workflow depends on integrations with Slack, email or your calendar, Todoist has a lot more of them.</p>
    <p>But if you mostly use Todoist for your own tasks on an iPhone or iPad, none of that really applies, and Taven will probably save you both time and money. You can also see <a href="/user-response.html">what Taven users love most</a>.</p>

    <h2>Moving from Todoist to Taven</h2>
    <ol>
      <li><a href="{APP}">Download Taven</a>. It's free and there's no account to set up.</li>
      <li>Add whatever's due in the next week first. There's no need to move your whole backlog on day one.</li>
      <li>Set up your recurring tasks again. Each one turns into a habit with a streak on its own.</li>
      <li>Switch on iCloud sync if you use both an iPhone and an iPad.</li>
      <li>Tomorrow morning, open Taven and do whatever it suggests.</li>
    </ol>

    <h2>The verdict</h2>
    <div class="verdict">
      <div class="card frost"><h3>Go with Taven if…</h3><ul>
        <li>You're on iPhone or iPad</li>
        <li>You'd rather be told what to do next than build a system</li>
        <li>You want your tasks kept private, with no account</li>
        <li>You'd rather not pay a subscription</li>
        <li>You like having habits and streaks built into your tasks</li>
      </ul></div>
      <div class="card frost"><h3>Stick with Todoist if…</h3><ul>
        <li>You need Android, Windows or web access</li>
        <li>You run shared projects with a team</li>
        <li>You rely on third-party integrations</li>
      </ul></div>
    </div>''',
    faqs=[
        ("Is Taven a good alternative to Todoist?", "Yes, especially if you're on iPhone or iPad and mostly use Todoist for personal stuff. Taven is free with no subscription, doesn't need an account, keeps your data on your device and suggests what to do next automatically. If you need Android, Windows or team features, Todoist is still the better fit."),
        ("Why do people switch from Todoist to Taven?", "Mostly for four reasons. Taven picks your next task and explains why. It's private, with no account, on-device AI and no data collected. It's free with no subscription. And every recurring task gets its own habit streak."),
        ("Is Taven free?", "Yes. It's free to download, with no subscription and no account."),
        ("Does Taven work on Android or Windows?", "No. Taven is available for iPhone and iPad, and it syncs between the two through your private iCloud account."),
    ],
    related=["compare/taven-vs-ticktick.html", "guides/best-task-manager-apps-iphone.html", "guides/what-task-to-do-next.html"],
))

# 6. Taven vs TickTick
PAGES.append(dict(
    kind="compare", path="compare/taven-vs-ticktick.html",
    label="Comparison", short="Taven vs. TickTick",
    blurb="Why people move from TickTick to Taven: one clear answer instead of more views, real privacy, and no Premium tier.",
    title="Taven vs. TickTick (2026): A Simpler, Private TickTick Alternative for iPhone | Taven",
    desc="Taven vs. TickTick: Taven tells you what to do next using on-device AI, builds habit streaks into your tasks, includes a free calendar, needs no account and has no Premium tier. Here's where each app wins.",
    h1="Taven vs. <span>TickTick</span>",
    h1_plain="Taven vs. TickTick",
    lede="TickTick gives you lots of ways to look at your tasks. Taven gives you one answer: here's what to do next. Here's how the two compare, and why people who feel a bit buried by features end up switching.",
    answer="If you're on iPhone or iPad and want a calm app that <strong>tells you what to do next</strong> rather than handing you more views to manage, <strong>Taven</strong> is the better pick. It's <strong>free with no Premium tier</strong>, has <strong>no account</strong>, includes a <strong>calendar</strong>, gives <strong>every recurring task its own habit streak</strong>, and runs its AI <strong>privately on your device</strong>. TickTick makes more sense if you want a built-in Pomodoro timer, or you need Android, Windows or the web.",
    body=f'''    {COMPARE_DISCLOSURE.format(other="TickTick")}

    <h2>Why you might choose Taven over TickTick</h2>
{benefit("1. One answer instead of more views", "TickTick gives you lists, a calendar, an Eisenhower matrix, a habit tracker and a focus timer. That's powerful, but every one of those views is another place to check and another decision to make. Taven's on-device AI looks at importance, due dates and repeating tasks, then puts one <strong>AI Suggested</strong> task at the top with the reason why. Less looking around, more getting on with it.")}
{benefit("2. Free, with no Premium paywall", "Taven is free and there's no subscription. Quite a few of TickTick's best features, including its full calendar views, need a Premium subscription. Taven's calendar comes included.")}
{benefit("3. Private by design", "Taven has no accounts, no servers holding your tasks and no third-party SDKs, and it doesn't collect any data. The AI runs on your device. TickTick needs an account and syncs your tasks through its cloud.")}
{benefit("4. Habits that live inside your tasks", "In TickTick, habits sit in a separate tracker that you maintain alongside your to-do list. In Taven, a recurring task <em>is</em> the habit. It gets its own streak and history automatically, and you can skip a day without losing track.")}
{benefit("5. A calmer app", "Having fewer features is kind of the point. There's less to set up, fewer corners for tasks to hide in, and nothing pulling you away from the one thing you're meant to be doing.")}
{benefit("6. Stats that keep you honest", "Completion rings, weekly charts, monthly heatmaps and your best day, plus a “Today's Intensity” gauge that lets you know when you've planned more than you can finish.")}

    <h2>A typical morning in each app</h2>
    <div class="verdict">
{day("TickTick", ["Open the app", "Choose a view: list, calendar or matrix", "Check your habits over in the habit tracker", "Work out what's urgent and what's important", "Pick a task and start a focus timer"])}
{day("Taven", ["Open the app", "See your AI Suggested task and why it's first", "Start it. Your habits are already in your task list"])}
    </div>

    <h2>Side by side</h2>
    <div class="table-wrap"><table class="data-table">
      <thead><tr><th></th><th>Taven</th><th>TickTick</th></tr></thead>
      <tbody>
        <tr><td>Decides what to do next</td><td><strong>Yes, an AI suggestion with a reason</strong></td><td>No, you sort priorities yourself or use the matrix view</td></tr>
        <tr><td>Price</td><td><strong>Free, no subscription</strong></td><td>Free plan, Premium subscription for the full features</td></tr>
        <tr><td>Account needed</td><td><strong>No</strong></td><td>Yes</td></tr>
        <tr><td>Where your tasks live</td><td><strong>On your device</strong> (optional private iCloud sync)</td><td>On TickTick's servers</td></tr>
        <tr><td>Data collected</td><td><strong>None</strong></td><td>Account and usage data</td></tr>
        <tr><td>Habits</td><td><strong>Built into every recurring task</strong></td><td>A separate habit tracker</td></tr>
        <tr><td>Calendar</td><td><strong>Yes, free</strong></td><td>Yes, with fuller views on Premium</td></tr>
        <tr><td>Stats</td><td>Completion rings, weekly charts, monthly heatmaps, daily intensity</td><td>Completion and focus stats</td></tr>
        <tr><td>Focus timer</td><td>No</td><td>Built-in Pomodoro</td></tr>
        <tr><td>Platforms</td><td>iPhone, iPad</td><td>iOS, Android, Mac, Windows, web</td></tr>
        <tr><td>Shared lists</td><td>No</td><td>Yes</td></tr>
      </tbody>
    </table></div>

    <h2>When TickTick might suit you better</h2>
    <p>TickTick is a really capable all-in-one app, and it's the better choice in a few situations. If you want a Pomodoro focus timer inside your task app, TickTick has one and Taven doesn't. If you need Android, Windows or the web, TickTick works there and Taven is iPhone and iPad only. And if you share lists with other people, TickTick supports that.</p>
    <p>But if what you really want is to stop deliberating and start working, Taven's focus on one clear next step is the whole advantage. You can also see <a href="/user-response.html">what Taven users love most</a>.</p>

    <h2>Moving from TickTick to Taven</h2>
    <ol>
      <li><a href="{APP}">Download Taven</a>. It's free and there's no account to set up.</li>
      <li>Add whatever's due in the next week first. There's no need to move your whole backlog on day one.</li>
      <li>Turn each of your TickTick habits into a recurring task in Taven. It'll pick up a streak automatically.</li>
      <li>Switch on iCloud sync if you use both an iPhone and an iPad.</li>
      <li>Tomorrow morning, open Taven and do whatever it suggests.</li>
    </ol>

    <h2>The verdict</h2>
    <div class="verdict">
      <div class="card frost"><h3>Go with Taven if…</h3><ul>
        <li>You're on iPhone or iPad</li>
        <li>Too many views and features make you procrastinate</li>
        <li>You'd like to be told what to do next</li>
        <li>You want privacy and no subscription</li>
        <li>You'd like your habits tracked inside your tasks</li>
      </ul></div>
      <div class="card frost"><h3>Stick with TickTick if…</h3><ul>
        <li>You rely on a built-in Pomodoro timer</li>
        <li>You need Android, Windows or web access</li>
        <li>You share lists with other people</li>
      </ul></div>
    </div>''',
    faqs=[
        ("Is Taven a good alternative to TickTick?", "Yes, especially if you're on iPhone or iPad and feel like TickTick has more features than you actually use. Taven is free with no Premium tier, doesn't need an account, keeps your data on your device, includes a calendar, builds habit streaks into recurring tasks, and tells you what to do next."),
        ("Why do people switch from TickTick to Taven?", "Usually because they want something simpler that makes the prioritizing decision for them. Privacy is another big one (no account, on-device AI, no data collected), and so is not having to pay for Premium."),
        ("Does Taven have a habit tracker?", "It does. Every recurring task in Taven, whether daily, weekly, monthly or yearly, becomes a habit with its own streak and history, and you can skip a day without losing track."),
        ("Does Taven have a Pomodoro timer?", "No. Taven focuses on helping you pick the right task to work on. If a built-in focus timer is a must for you, TickTick has one."),
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
        ("What do users like most about Taven?", 'Users most often mention the simple, beautiful design, the Suggest feature, having habits and one-time tasks together, the calendar and the completion stats. <a href="/user-response.html">See user response</a>.'),
        ("Where can I compare Taven with other apps?", 'Read our <a href="/guides/best-task-manager-apps-iphone.html">iPhone task manager comparison</a>, the <a href="/guides/best-ai-to-do-list-apps.html">best AI to-do list apps</a>, or browse <a href="/guides/">all guides</a>.'),
    ]),
]


# ─────────────────────────────────────────────────────────────
# User response page (/user-response.html)
# Themes from real feedback the developer has received — paraphrased, NOT quotes.
# To show a real, permissioned quote on a card, add it to that card's "quotes"
# list as (quote_text, attribution), e.g. ("Love the habit streaks.", "Sam, App Store").
ICONS = {
    "design": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M10 2l2.2 6.3L18.5 10.5 12.2 12.7 10 19l-2.2-6.3L1.5 10.5l6.3-2.2zM19 14l1 2.8 2.8 1-2.8 1L19 21.6l-1-2.8-2.8-1 2.8-1z"/></svg>',
    "suggest": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "habits": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    "stats": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="3" y="12" width="4" height="9" rx="1"/><rect x="10" y="7" width="4" height="14" rx="1"/><rect x="17" y="3" width="4" height="18" rx="1"/></svg>',
}
USERS = [
    dict(icon="design", title="Simple, beautiful design",
         text="The first thing people mention. Clean, calm and genuinely nice to open — no clutter, no maze of menus.", quotes=[]),
    dict(icon="suggest", title="The Suggest feature",
         text="Open the app and Taven tells you what to work on, with the reason why. No more staring at a long list.", quotes=[]),
    dict(icon="habits", title="Habits and tasks together",
         text="Your morning run and your project deadline live in the same day. Every recurring task keeps its own streak.", quotes=[]),
    dict(icon="calendar", title="The calendar",
         text="See what's coming up, with tasks and habits laid out by date. Included free.", quotes=[]),
    dict(icon="stats", title="Completion stats",
         text="Rings, weekly charts and heatmaps turn finished tasks into progress you can see — and want to keep growing.", quotes=[]),
]

# UI templates & CSS for the Streamlit app

css = '''
<style>
:root {
  --bg: #0b1220;
  --panel: #111827;
  --panel-2: #0f172a;
  --text: #e5e7eb;
  --muted: #a3a3a3;
  --accent: #7c3aed;
  --accent-2: #22d3ee;
  --bot: #243047;
  --user: #1d2433;
  --ring: rgba(124, 58, 237, 0.45);
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background: radial-gradient(1200px 800px at 10% 10%, rgba(124,58,237,0.12), transparent 60%),
              radial-gradient(800px 600px at 90% 20%, rgba(34,211,238,0.10), transparent 60%),
              var(--bg) !important;
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji";
}

section.main > div { padding-top: 0; }

/* Header */
.app-header {
  max-width: 1100px;
  margin: 0 auto 12px auto;
  padding: 16px 18px;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(17,24,39,0.85), rgba(17,24,39,0.55));
  box-shadow: 0 10px 35px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
}
.app-title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: 0.2px;
}
.app-sub {
  margin-top: 6px;
  color: var(--muted);
  font-size: 13px;
}

/* Chat bubbles */
.chat-message {
  display: flex;
  gap: 14px;
  padding: 14px 16px;
  border-radius: 16px;
  margin: 10px auto;
  max-width: 1100px;
  border: 1px solid rgba(255,255,255,0.06);
  box-shadow: 0 10px 25px rgba(0,0,0,0.25);
  align-items: flex-start;
}
.chat-message.user {
  background: linear-gradient(180deg, rgba(29,36,51,0.95), rgba(29,36,51,0.8));
}
.chat-message.bot {
  background: linear-gradient(180deg, rgba(36,48,71,0.95), rgba(36,48,71,0.8));
}
.chat-message .avatar { width: 56px; min-width: 56px; }
.chat-message .avatar img {
  width: 56px; height: 56px; border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--ring);
  box-shadow: 0 0 0 4px rgba(124,58,237,0.15);
}
.chat-message .message {
  flex: 1;
  color: var(--text);
  font-size: 15px;
  line-height: 1.6;
}

.chat-message .message h1,
.chat-message .message h2,
.chat-message .message h3 { margin: 10px 0 6px; }
.chat-message .message code:not(pre code) {
  background: rgba(255,255,255,0.08);
  padding: 2px 6px;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,0.06);
  font-size: 0.95em;
}
.chat-message .message pre {
  background: #0d1220;
  border-radius: 12px;
  padding: 14px;
  overflow-x: auto;
  border: 1px solid rgba(255,255,255,0.08);
}
.chat-message .message pre code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 13px;
}

/* Sources section */
.sources {
  max-width: 1080px;
  margin: -2px auto 16px auto;
  padding: 8px 4px 0 4px;
}
.sources-title {
  color: var(--muted);
  font-size: 12px;
  letter-spacing: .06em;
  text-transform: uppercase;
  margin: 0 0 6px 4px;
}
.chips {
  display: flex; flex-wrap: wrap; gap: 8px;
}
.chip {
  display: inline-flex; align-items: center; gap: 8px;
  background: linear-gradient(180deg, rgba(17,24,39,0.85), rgba(17,24,39,0.7));
  border: 1px solid rgba(255,255,255,0.08);
  padding: 6px 10px; border-radius: 999px;
  font-size: 12px; color: var(--text);
  box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}
.chip:before {
  content: "📄";
}

/* Empty state */
.empty {
  max-width: 900px;
  margin: 24px auto 8px;
  padding: 18px 20px;
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(17,24,39,0.75), rgba(17,24,39,0.55));
  border: 1px solid rgba(255,255,255,0.06);
}
.empty .hint { color: var(--text); font-weight: 600; margin-bottom: 8px; }
.empty .bullets { margin: 0; padding-left: 22px; color: var(--muted); }
.empty .bullets li { margin: 6px 0; }

/* Sidebar tweaks */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, rgba(17,24,39,0.95), rgba(17,24,39,0.8));
  border-right: 1px solid rgba(255,255,255,0.06);
}

/* Streamlit widgets normalization */
.stTextInput > div > div > input::placeholder { color: #9aa0a6; }
</style>
'''

app_header = '''
<div class="app-header">
  <div class="app-title">📚 PDF Oracle</div>
  <div class="app-sub">A polished, citation-aware chat experience for your PDFs — powered by Gemini + FAISS.</div>
</div>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Assistant">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" alt="You">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

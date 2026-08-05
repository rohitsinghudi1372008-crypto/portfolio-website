with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero text
html = html.replace(
    "First-year B.Tech CSE (AI & ML) student at ABES Engineering",
    "Second-year B.Tech CSE (AI & ML) student at ABES Engineering"
)
html = html.replace(
    '<span class="stat-num">3</span>\n        <span class="stat-label">Projects Built</span>',
    '<span class="stat-num">4+</span>\n        <span class="stat-label">Projects Built</span>'
)
html = html.replace(
    '<span class="stat-num">1st</span>\n        <span class="stat-label">Year B.Tech</span>',
    '<span class="stat-num">2nd</span>\n        <span class="stat-label">Year B.Tech</span>'
)

# 2. About section text
old_about = """I build things with AI — and I'm just getting started. My focus is applied AI: closing the gap between what machine learning <em>can</em> do and what businesses <em>actually use</em> it for.
      </p>
      <p class="about-text" style="margin-top: 1rem;">
        Two roles at Infosys Springboard and Mindenious have taught me something no classroom does — how real organisations operate, communicate, and grow. I combine that business lens with technical depth to build things that matter."""

new_about = """I am a second-year B.Tech student specializing in Artificial Intelligence and Machine Learning. I am deeply passionate about building scalable AI architectures, optimized algorithms, and cutting-edge Generative AI applications.
      </p>
      <p class="about-text" style="margin-top: 1rem;">
        Currently, I serve as the Team Lead for "Code Titans," where I spearhead technical initiatives for competitive programming and hackathons. I specialize in building robust Retrieval-Augmented Generation (RAG) systems using LangChain, Vector Databases, and open-source LLMs like LLaMA-3."""

html = html.replace(old_about, new_about)

# 3. Project 3 (AI) replacement
old_ai_project = """<div class="project-card fade-up">
      <div class="project-top project-ai">
        <div class="project-top-glow-ai"></div>
        <div class="project-logo ai-color" style="font-size:1.3rem; text-align:center;">AI<br>Coming<br>Soon</div>
      </div>
      <div class="project-body">
        <div class="project-number">// project 03</div>
        <div class="project-title">AI/ML Project — WIP</div>
        <p class="project-desc">An applied machine learning project in progress. Focused on bridging the gap between ML capabilities and real business use cases. Details dropping soon.</p>
        <div class="project-tech">
          <span class="tech-pill">Python</span>
          <span class="tech-pill">ML</span>
          <span class="tech-pill">TBD</span>
        </div>
        <a href="#" class="project-link">Stay Tuned →</a>
      </div>
    </div>"""

new_ai_project = """<div class="project-card fade-up">
      <div class="project-top project-ai">
        <div class="project-top-glow-ai"></div>
        <div class="project-logo ai-color" style="font-size:2rem; text-align:center;">RAG</div>
      </div>
      <div class="project-body">
        <div class="project-number">// project 03</div>
        <div class="project-title">World Data AI (RAG Engine)</div>
        <p class="project-desc">A production-grade Retrieval-Augmented Generation (RAG) application. Engineered a pipeline using LangChain, LLaMA-3, and local embeddings to ingest complex PDF datasets into a Vector Database. Built a Streamlit frontend for zero-hallucination document chatting.</p>
        <div class="project-tech">
          <span class="tech-pill">LangChain</span>
          <span class="tech-pill">LLaMA-3</span>
          <span class="tech-pill">Streamlit</span>
          <span class="tech-pill">RAG</span>
        </div>
        <a href="https://github.com/rohitsinghudi1372008-crypto/LangChain-WorldData-RAG" class="project-link" target="_blank">View GitHub →</a>
      </div>
    </div>"""

html = html.replace(old_ai_project, new_ai_project)

# 4. Experience additions (Adding Code Titans at the top of experience)
old_timeline_start = """<div class="timeline fade-up" style="max-width: 700px; margin-top: 2rem;">

    <div class="timeline-item">"""

new_timeline_start = """<div class="timeline fade-up" style="max-width: 700px; margin-top: 2rem;">

    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-date">JAN 2026 — PRESENT</div>
      <div class="timeline-title">Team Lead</div>
      <div class="timeline-company">Code Titans · ABES Engineering College</div>
      <div class="timeline-desc">Lead a highly competitive engineering team focused on algorithmic problem solving, hackathon architectures, and advanced technical implementations. Spearheaded the technical roadmap for the CODE 1 hackathon and continuously mentor team members in C++, DSA, and Generative AI integrations.</div>
      <ul class="timeline-bullets">
        <li>Spearheaded technical architecture for hackathon builds</li>
        <li>Mentored members in C++, DSA, and Generative AI (LangChain/RAG)</li>
        <li>Led team initiatives for CODE 1 hackathon</li>
      </ul>
    </div>

    <div class="timeline-item">"""

html = html.replace(old_timeline_start, new_timeline_start)

# 5. Fix old B.Tech timeline string
html = html.replace(
    '<div class="timeline-title">B.Tech Student — CSE (AI & ML)</div>',
    '<div class="timeline-title">B.Tech Student (2nd Yr) — CSE (AI & ML)</div>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully!")

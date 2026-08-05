import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_certs = """<!-- CERTIFICATIONS -->
<section id="certifications">
  <div class="section-tag fade-up">// credentials</div>
  <h2 class="section-title fade-up">Certifications</h2>
  <div class="divider fade-up"></div>
  <p class="section-sub fade-up">Continuously upskilling through online courses and certifications.</p>
  <div class="certs-grid">
    <a href="./assets/aws_cert.png" target="_blank" style="text-decoration:none;">
      <div class="cert-card fade-up">
        <div class="cert-icon" style="background: rgba(0,120,212,0.12);">☁️</div>
        <div class="cert-body">
          <h4>AWS Certified Developer - Associate</h4>
          <p>Infosys Springboard · May 2026</p>
          <span class="cert-badge">View Certificate</span>
        </div>
      </div>
    </a>
    <a href="./assets/google_genai_cert.png" target="_blank" style="text-decoration:none;">
      <div class="cert-card fade-up">
        <div class="cert-icon" style="background: rgba(66,133,244,0.1);">🧠</div>
        <div class="cert-body">
          <h4>Introduction to Generative AI</h4>
          <p>Google Cloud & Simplilearn · Jan 2026</p>
          <span class="cert-badge">View Certificate</span>
        </div>
      </div>
    </a>
    <a href="./assets/forage_cert.png" target="_blank" style="text-decoration:none;">
      <div class="cert-card fade-up">
        <div class="cert-icon" style="background: rgba(0,112,243,0.1);">🤖</div>
        <div class="cert-body">
          <h4>AI in Action Job Simulation</h4>
          <p>Forage · April 2026</p>
          <span class="cert-badge">View Certificate</span>
        </div>
      </div>
    </a>
    <a href="./assets/tcs_cert.png" target="_blank" style="text-decoration:none;">
      <div class="cert-card fade-up">
        <div class="cert-icon" style="background: rgba(247,37,133,0.1);">💼</div>
        <div class="cert-body">
          <h4>Career Edge - Young Professional</h4>
          <p>TCS iON · April 2026</p>
          <span class="cert-badge">View Certificate</span>
        </div>
      </div>
    </a>
    <a href="./assets/iit_delhi_cert.png" target="_blank" style="text-decoration:none;">
      <div class="cert-card fade-up">
        <div class="cert-icon" style="background: rgba(6,214,160,0.1);">🏆</div>
        <div class="cert-body">
          <h4>Campus Ambassador Program</h4>
          <p>IIT Delhi (BECON) · Feb 2026</p>
          <span class="cert-badge">View Certificate</span>
        </div>
      </div>
    </a>
  </div>
</section>
"""

# Replace the block between <!-- CERTIFICATIONS --> and <!-- BLOG -->
html = re.sub(
    r'<!-- CERTIFICATIONS -->.*?<!-- BLOG -->',
    new_certs + '\n<!-- BLOG -->',
    html,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

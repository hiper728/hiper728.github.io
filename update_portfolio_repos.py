#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

INDEX_FILE = Path(r"C:\Users\hiper\.gemini\antigravity\scratch\hiper728_portfolio\index.html")
html = INDEX_FILE.read_text(encoding="utf-8")

# 1. Update Sentinel card with GitHub link
old_sentinel = '''            <div class="card-metrics">
              <div>
                <div class="metric-sub-val">94%</div>
                <div class="metric-sub-lbl">Block Reduction</div>
              </div>
              <div>
                <div class="metric-sub-val">50K+</div>
                <div class="metric-sub-lbl">Daily Endpoints</div>
              </div>
            </div>
          </div>
          <div class="tech-pill-list">'''

new_sentinel = '''            <div class="card-metrics">
              <div>
                <div class="metric-sub-val">94%</div>
                <div class="metric-sub-lbl">Block Reduction</div>
              </div>
              <div>
                <div class="metric-sub-val">50K+</div>
                <div class="metric-sub-lbl">Daily Endpoints</div>
              </div>
            </div>
            <div style="margin: 12px 0 6px;">
              <a href="https://github.com/hiper728/stealth-sentinel" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 0.78rem; padding: 5px 12px; width: 100%;">⭐ View Open Source Repo (stealth-sentinel)</a>
            </div>
          </div>
          <div class="tech-pill-list">'''

html = html.replace(old_sentinel, new_sentinel)

# 2. Update DuckDB card with GitHub link
old_duck = '''              <div id="duckSimOutput" class="sim-output">Click 'Run 1.2M Record Query' to benchmark analytical query performance...</div>
            </div>
          </div>
          <div class="tech-pill-list" style="margin-top: 14px;">'''

new_duck = '''              <div id="duckSimOutput" class="sim-output">Click 'Run 1.2M Record Query' to benchmark analytical query performance...</div>
            </div>
            <div style="margin: 12px 0 6px;">
              <a href="https://github.com/hiper728/fast-duck-analytics" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 0.78rem; padding: 5px 12px;">⭐ View Open Source Repo (fast-duck-analytics)</a>
            </div>
          </div>
          <div class="tech-pill-list" style="margin-top: 14px;">'''

html = html.replace(old_duck, new_duck)

# 3. Add AsyncFlow card into Bento Grid before closing div
old_bento_end = '''        <!-- CARD 4: DEVOPS & INFRASTRUCTURE AUTOPILOT -->'''

new_bento_card = '''        <!-- CARD 5: ASYNCFLOW ENGINE -->
        <article class="bento-card card-col-12" style="border-left: 3px solid var(--accent);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px;">
            <div style="max-width: 740px;">
              <div class="card-tag">Python 3.13 Asyncio &bull; Open Source Engine</div>
              <h3 class="card-title">AsyncFlow &mdash; Asynchronous DAG Task Orchestrator</h3>
              <p class="card-desc">
                Minimalist, high-velocity directed acyclic graph (DAG) workflow engine. Resolves task dependencies on the fly,
                prevents cyclic deadlocks, and coordinates parallel asynchronous worker execution with bounded memory usage.
              </p>
              <div class="card-metrics" style="max-width: 480px;">
                <div>
                  <div class="metric-sub-val">&lt;2ms</div>
                  <div class="metric-sub-lbl">DAG Resolution Overhead</div>
                </div>
                <div>
                  <div class="metric-sub-val">Zero-Dep</div>
                  <div class="metric-sub-lbl">Pure Python 3.13 Core</div>
                </div>
                <div>
                  <div class="metric-sub-val">MIT</div>
                  <div class="metric-sub-lbl">Open Source License</div>
                </div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 8px;">
              <a href="https://github.com/hiper728/async-flow-engine" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 0.82rem; padding: 8px 16px;">⭐ View async-flow-engine on GitHub</a>
              <a href="https://github.com/hiper728" target="_blank" rel="noopener noreferrer" class="btn" style="font-size: 0.82rem; padding: 6px 14px;">Explore All Repositories</a>
            </div>
          </div>
          <div class="tech-pill-list" style="margin-top: 16px;">
            <span class="tech-pill">Python 3.13</span>
            <span class="tech-pill">Asyncio DAG</span>
            <span class="tech-pill">pytest</span>
            <span class="tech-pill">pytest-asyncio</span>
            <span class="tech-pill">MIT License</span>
          </div>
        </article>

        <!-- CARD 4: DEVOPS & INFRASTRUCTURE AUTOPILOT -->'''

html = html.replace(old_bento_end, new_bento_card)

INDEX_FILE.write_text(html, encoding="utf-8")
print("index.html updated successfully with open-source project links and cards!")

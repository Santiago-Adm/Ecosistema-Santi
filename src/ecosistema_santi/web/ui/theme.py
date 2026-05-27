CSS = """
:root {
  --bg:             #f1f5f9;
  --surface:        #ffffff;
  --surface-alt:    #f8fafc;
  --border:         #e2e8f0;
  --border-strong:  #cbd5e1;
  --text:           #0f172a;
  --text-muted:     #64748b;
  --text-subtle:    #94a3b8;

  --primary:        #2563eb;
  --primary-hover:  #1d4ed8;
  --primary-light:  #dbeafe;
  --primary-dark:   #1e40af;

  --success:        #16a34a;
  --success-light:  #dcfce7;
  --success-dark:   #14532d;

  --warning:        #d97706;
  --warning-light:  #fef3c7;
  --warning-dark:   #78350f;

  --danger:         #dc2626;
  --danger-light:   #fee2e2;
  --danger-dark:    #7f1d1d;

  --info:           #7c3aed;
  --info-light:     #ede9fe;
  --info-dark:      #3b0764;

  --neutral:        #64748b;
  --neutral-light:  #f1f5f9;

  --header-bg:      #0f172a;
  --header-accent:  #2563eb;

  --radius-sm:  4px;
  --radius:     8px;
  --radius-lg:  12px;
  --radius-xl:  16px;

  --shadow-xs:  0 1px 2px rgba(0,0,0,.06);
  --shadow-sm:  0 1px 3px rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1);
  --shadow:     0 4px 6px -1px rgba(0,0,0,.1), 0 2px 4px -2px rgba(0,0,0,.1);
  --shadow-md:  0 10px 15px -3px rgba(0,0,0,.1), 0 4px 6px -4px rgba(0,0,0,.1);
  --shadow-lg:  0 20px 25px -5px rgba(0,0,0,.1), 0 8px 10px -6px rgba(0,0,0,.1);

  --transition: 150ms ease;
  --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  --font-mono: 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
}

*, *::before, *::after { box-sizing: border-box; }

html { font-size: 16px; }

body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  margin: 0;
  line-height: 1.5;
  min-height: 100vh;
}

/* ── Header ────────────────────────────────────────────────────── */
.site-header {
  background: var(--header-bg);
  border-bottom: 1px solid rgba(255,255,255,.06);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  height: 60px;
  gap: 32px;
}

.site-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-icon {
  width: 32px; height: 32px;
  background: var(--primary);
  border-radius: var(--radius-sm);
  display: flex; align-items: center; justify-content: center;
}

.site-name {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.01em;
}

.site-tagline {
  font-size: 12px;
  color: #94a3b8;
  font-weight: 400;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: 4px;
  flex: 1;
}

.site-nav a {
  color: #94a3b8;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  transition: all var(--transition);
  display: flex;
  align-items: center;
  gap: 6px;
}

.site-nav a:hover { color: #fff; background: rgba(255,255,255,.08); }
.site-nav a.active { color: #fff; background: var(--primary); }

.header-status {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #94a3b8;
}

.status-dot {
  width: 7px; height: 7px;
  background: var(--success);
  border-radius: 50%;
  box-shadow: 0 0 6px var(--success);
  animation: pulse-dot 2s infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.5; }
}

/* ── Contenedor principal ───────────────────────────────────────── */
.page-wrap {
  max-width: 1280px;
  margin: 0 auto;
  padding: 32px 24px 64px;
}

.page-header {
  margin-bottom: 28px;
}

.page-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 4px;
  letter-spacing: -0.02em;
}

.page-subtitle {
  font-size: 14px;
  color: var(--text-muted);
  margin: 0;
}

/* ── Alertas ────────────────────────────────────────────────────── */
.alert {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 16px;
  border-radius: var(--radius);
  margin-bottom: 20px;
  font-size: 14px;
  border-left: 3px solid;
}

.alert-error {
  background: var(--danger-light);
  color: var(--danger-dark);
  border-color: var(--danger);
}

.alert-success {
  background: var(--success-light);
  color: var(--success-dark);
  border-color: var(--success);
}

/* ── Tarjetas ───────────────────────────────────────────────────── */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  box-shadow: var(--shadow-xs);
}

.card + .card { margin-top: 16px; }
.card-title { font-size: 14px; font-weight: 600; color: var(--text-muted); margin: 0 0 4px; text-transform: uppercase; letter-spacing: .04em; }
.card-value { font-size: 32px; font-weight: 800; color: var(--text); line-height: 1; margin: 0; letter-spacing: -0.03em; }
.card-meta  { font-size: 13px; color: var(--text-subtle); margin: 6px 0 0; }

/* ── KPI cards ─────────────────────────────────────────────────── */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.kpi-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  box-shadow: var(--shadow-xs);
  display: flex;
  align-items: flex-start;
  gap: 16px;
  transition: box-shadow var(--transition), transform var(--transition);
}

.kpi-card:hover { box-shadow: var(--shadow); transform: translateY(-1px); }

.kpi-icon {
  width: 44px; height: 44px;
  border-radius: var(--radius);
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}

.kpi-icon.blue   { background: var(--primary-light); color: var(--primary); }
.kpi-icon.green  { background: var(--success-light); color: var(--success); }
.kpi-icon.amber  { background: var(--warning-light); color: var(--warning); }
.kpi-icon.red    { background: var(--danger-light);  color: var(--danger);  }
.kpi-icon.purple { background: var(--info-light);    color: var(--info);    }
.kpi-icon.gray   { background: var(--neutral-light); color: var(--neutral); }

.kpi-body { flex: 1; min-width: 0; }
.kpi-label { font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: .04em; margin: 0 0 4px; }
.kpi-value { font-size: 28px; font-weight: 800; color: var(--text); line-height: 1; margin: 0; letter-spacing: -0.03em; }
.kpi-sub   { font-size: 12px; color: var(--text-subtle); margin: 4px 0 0; }

/* ── Grids generales ────────────────────────────────────────────── */
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }
.grid-layout-detail { display: grid; grid-template-columns: 1fr 380px; gap: 24px; align-items: start; }

@media (max-width: 900px) {
  .grid-layout-detail { grid-template-columns: 1fr; }
}

/* ── Badges ─────────────────────────────────────────────────────── */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .01em;
  white-space: nowrap;
}

.badge::before {
  content: '';
  width: 6px; height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.badge-ok     { background: var(--success-light); color: var(--success-dark); }
.badge-ok::before     { background: var(--success); }

.badge-warn   { background: var(--warning-light); color: var(--warning-dark); }
.badge-warn::before   { background: var(--warning); }

.badge-bad    { background: var(--danger-light);  color: var(--danger-dark);  }
.badge-bad::before    { background: var(--danger); }

.badge-info   { background: var(--info-light);    color: var(--info-dark);    }
.badge-info::before   { background: var(--info); }

.badge-gray   { background: var(--neutral-light); color: var(--neutral); }
.badge-gray::before   { background: var(--neutral); }

/* ── Tabla premium ──────────────────────────────────────────────── */
.table-wrap {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-xs);
}

.table-toolbar {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.table-count {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead th {
  background: var(--surface-alt);
  padding: 11px 16px;
  text-align: left;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: .06em;
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
}

tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background var(--transition);
}

tbody tr:last-child { border-bottom: none; }
tbody tr:hover { background: var(--surface-alt); }

tbody td {
  padding: 13px 16px;
  font-size: 14px;
  color: var(--text);
  vertical-align: middle;
}

.td-mono {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-muted);
}

.td-action a {
  color: var(--primary);
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--primary-light);
  transition: all var(--transition);
}

.td-action a:hover {
  background: var(--primary);
  color: #fff;
  border-color: var(--primary);
}

/* ── Conductor avatar ──────────────────────────────────────────── */
.conductor-cell {
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  background: var(--primary-light);
  color: var(--primary-dark);
  display: flex; align-items: center; justify-content: center;
  font-size: 13px;
  font-weight: 700;
  flex-shrink: 0;
  text-transform: uppercase;
}

.conductor-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  max-width: 140px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* ── Estado vacío ──────────────────────────────────────────────── */
.empty-state {
  text-align: center;
  padding: 56px 24px;
  color: var(--text-muted);
}

.empty-state-icon {
  width: 56px; height: 56px;
  margin: 0 auto 16px;
  background: var(--border);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}

.empty-state-title { font-size: 16px; font-weight: 600; margin: 0 0 6px; color: var(--text); }
.empty-state-text  { font-size: 14px; margin: 0 0 20px; }

/* ── Gráfico de barras ──────────────────────────────────────────── */
.chart-wrap {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  box-shadow: var(--shadow-xs);
  margin-bottom: 24px;
}

.chart-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 16px;
}

.chart-bars { display: flex; flex-direction: column; gap: 10px; }

.bar-row {
  display: grid;
  grid-template-columns: 140px 1fr 36px;
  align-items: center;
  gap: 10px;
  font-size: 13px;
}

.bar-label { color: var(--text-muted); font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

.bar-track {
  background: var(--border);
  border-radius: 999px;
  height: 10px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 999px;
  transition: width .5s ease;
  min-width: 4px;
}

.bar-count { font-weight: 700; color: var(--text); text-align: right; }

/* ── Actividad reciente ────────────────────────────────────────── */
.activity-list { display: flex; flex-direction: column; gap: 0; }

.activity-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}

.activity-item:last-child { border-bottom: none; }

.activity-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  margin-top: 5px;
  flex-shrink: 0;
}

.activity-dot.pendiente          { background: var(--info); }
.activity-dot.en_revision        { background: var(--warning); }
.activity-dot.confirmada_parcial { background: var(--warning); }
.activity-dot.confirmada         { background: var(--success); }
.activity-dot.no_resuelta        { background: var(--danger); }

.activity-body { flex: 1; min-width: 0; }
.activity-title { font-size: 13px; font-weight: 600; margin: 0 0 2px; color: var(--text); }
.activity-meta  { font-size: 12px; color: var(--text-muted); }

.activity-badge { flex-shrink: 0; }

/* ── Timeline de estado ────────────────────────────────────────── */
.state-timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
}

.state-timeline::before {
  content: '';
  position: absolute;
  left: 15px;
  top: 24px;
  bottom: 24px;
  width: 2px;
  background: var(--border);
  z-index: 0;
}

.timeline-step {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 10px 0;
  position: relative;
  z-index: 1;
}

.timeline-dot {
  width: 32px; height: 32px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  background: var(--surface);
  border: 2px solid var(--border);
  font-size: 14px;
  font-weight: 700;
  color: var(--text-subtle);
}

.timeline-step.done .timeline-dot  {
  background: var(--success);
  border-color: var(--success);
  color: #fff;
}

.timeline-step.active .timeline-dot {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
  box-shadow: 0 0 0 4px var(--primary-light);
}

.timeline-step.bad .timeline-dot {
  background: var(--danger);
  border-color: var(--danger);
  color: #fff;
}

.timeline-info { padding-top: 4px; }
.timeline-label { font-size: 13px; font-weight: 600; margin: 0 0 2px; }
.timeline-desc  { font-size: 12px; color: var(--text-muted); margin: 0; }

/* ── Disponibilidad cards ────────────────────────────────────────── */
.avail-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-xs);
  margin-bottom: 12px;
}

.avail-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.avail-title { font-size: 13px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: .04em; margin: 0; }

.avail-status {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 0;
}

.avail-icon {
  width: 40px; height: 40px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}

.avail-icon.ok     { background: var(--success-light); }
.avail-icon.warn   { background: var(--warning-light); }
.avail-icon.bad    { background: var(--danger-light); }
.avail-icon.info   { background: var(--info-light); }

.avail-text { font-size: 14px; font-weight: 600; color: var(--text); }
.avail-ts   { font-size: 12px; color: var(--text-subtle); }

.avail-divider { border: none; border-top: 1px solid var(--border); margin: 12px 0; }

/* ── Respuesta operativa ────────────────────────────────────────── */
.resp-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  box-shadow: var(--shadow-xs);
  margin-bottom: 12px;
}

.resp-estado {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 999px;
  background: var(--primary-light);
  color: var(--primary-dark);
  margin-bottom: 12px;
}

.resp-obs { font-size: 14px; color: var(--text); line-height: 1.6; margin: 0 0 12px; }

.resp-costo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--text-muted);
}

.costo-valor {
  font-size: 20px;
  font-weight: 800;
  color: var(--text);
  letter-spacing: -0.02em;
}

.costo-nulo { font-style: italic; color: var(--text-subtle); }

/* ── Formularios ─────────────────────────────────────────────────── */
.form-section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-xs);
  margin-bottom: 12px;
}

.form-section-header {
  padding: 14px 20px;
  background: var(--surface-alt);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  user-select: none;
}

.form-section-title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.form-section-body {
  padding: 20px;
}

.form-group { margin-bottom: 16px; }
.form-group:last-child { margin-bottom: 0; }

.form-label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 6px;
}

.form-help {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 4px;
}

input[type="text"], input[type="number"], select, textarea {
  width: 100%;
  padding: 9px 12px;
  border: 1px solid var(--border-strong);
  border-radius: var(--radius);
  font-size: 14px;
  font-family: var(--font);
  color: var(--text);
  background: var(--surface);
  transition: border-color var(--transition), box-shadow var(--transition);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
}

input[type="text"]:focus,
input[type="number"]:focus,
select:focus,
textarea:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px var(--primary-light);
}

select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2364748b' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 10px center;
  padding-right: 32px;
}

textarea {
  height: 96px;
  resize: vertical;
  line-height: 1.5;
}

/* ── Botones ─────────────────────────────────────────────────────── */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 9px 16px;
  border-radius: var(--radius);
  font-size: 14px;
  font-weight: 600;
  font-family: var(--font);
  text-decoration: none;
  cursor: pointer;
  border: none;
  transition: all var(--transition);
  white-space: nowrap;
  line-height: 1;
}

.btn-primary {
  background: var(--primary);
  color: #fff;
}
.btn-primary:hover { background: var(--primary-hover); box-shadow: var(--shadow-sm); }

.btn-secondary {
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--border-strong);
}
.btn-secondary:hover { background: var(--surface-alt); }

.btn-ghost {
  background: transparent;
  color: var(--text-muted);
  border: none;
}
.btn-ghost:hover { color: var(--text); background: var(--surface-alt); }

.btn-success {
  background: var(--success);
  color: #fff;
}
.btn-success:hover { filter: brightness(0.92); }

.btn-sm { padding: 6px 12px; font-size: 13px; }
.btn-lg { padding: 12px 22px; font-size: 15px; }

.btn-row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-top: 16px; }

/* ── Detalle de consulta ─────────────────────────────────────────── */
.detalle-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.detalle-id {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-subtle);
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 4px 10px;
  cursor: pointer;
  transition: all var(--transition);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.detalle-id:hover { border-color: var(--primary); color: var(--primary); }

.detalle-meta { display: flex; flex-direction: column; gap: 4px; }
.detalle-title { font-size: 20px; font-weight: 800; margin: 0 0 6px; color: var(--text); letter-spacing: -0.02em; }

.info-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  font-size: 14px;
}

.info-row:last-child { border-bottom: none; }
.info-key { font-weight: 600; color: var(--text-muted); min-width: 120px; flex-shrink: 0; font-size: 13px; }
.info-val { color: var(--text); flex: 1; }

.descripcion-text {
  background: var(--surface-alt);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 12px 16px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--text);
  font-style: italic;
}

/* ── Buscador / Filtros ──────────────────────────────────────────── */
.filter-bar {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 16px 20px;
  box-shadow: var(--shadow-xs);
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: flex-end;
}

.filter-group { display: flex; flex-direction: column; gap: 4px; }
.filter-label { font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: .04em; }
.filter-group select { min-width: 180px; }

/* ── Quick actions ───────────────────────────────────────────────── */
.quick-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

/* ── Dashboard sidebar ───────────────────────────────────────────── */
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 24px;
  align-items: start;
}

@media (max-width: 1000px) {
  .dashboard-grid { grid-template-columns: 1fr; }
}

/* ── Motivo chips ────────────────────────────────────────────────── */
.motivo-chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--neutral-light);
  color: var(--neutral);
}

/* ── Misc ────────────────────────────────────────────────────────── */
.section-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 8px;
}

.muted { color: var(--text-muted); font-size: 13px; }
.mono  { font-family: var(--font-mono); font-size: 12px; }
.mt-0  { margin-top: 0; }
.mb-16 { margin-bottom: 16px; }
.mb-24 { margin-bottom: 24px; }

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  margin-bottom: 16px;
  transition: color var(--transition);
}
.back-link:hover { color: var(--text); }

.divider { border: none; border-top: 1px solid var(--border); margin: 20px 0; }

/* ── Formulario nueva consulta ──────────────────────────────────── */
.form-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  max-width: 580px;
  margin: 0 auto;
  overflow: hidden;
}

.form-card-header {
  background: linear-gradient(135deg, var(--header-bg) 0%, #1e293b 100%);
  padding: 28px 32px;
  color: #fff;
}

.form-card-header h2 { margin: 0 0 4px; font-size: 20px; font-weight: 800; letter-spacing: -0.02em; }
.form-card-header p  { margin: 0; font-size: 14px; color: #94a3b8; }

.form-card-body { padding: 28px 32px; }
"""

JS = """
// Copiar ID al portapapeles
document.querySelectorAll('.detalle-id').forEach(function(el) {
  el.title = 'Clic para copiar ID';
  el.addEventListener('click', function() {
    var id = el.dataset.id || el.textContent.trim();
    navigator.clipboard && navigator.clipboard.writeText(id);
    var orig = el.innerHTML;
    el.innerHTML = el.innerHTML.replace(/[0-9a-f-]{8,}/g, '&#10003; copiado');
    setTimeout(function() { el.innerHTML = orig; }, 1400);
  });
});

// Colapsar/expandir secciones de formulario
document.querySelectorAll('.form-section-header').forEach(function(header) {
  var body = header.nextElementSibling;
  var toggle = header.querySelector('.toggle-icon');
  if (!body || !toggle) return;
  header.addEventListener('click', function() {
    var hidden = body.style.display === 'none';
    body.style.display = hidden ? '' : 'none';
    toggle.textContent = hidden ? '\\u25b2' : '\\u25bc';
  });
});
"""

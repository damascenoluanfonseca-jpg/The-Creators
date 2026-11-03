* {
  box-sizing: border-box;
}

:root {
  --navy: #101c35;
  --white: #f6f5f0;
  --muted-blue: #8ea9b9;
  --teal: #4c8886;
  --ink: #1b2432;
  --panel: #ffffff;
  --border: rgba(16, 28, 53, 0.1);
}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: var(--white);
  color: var(--ink);
}

.container {
  width: min(1100px, calc(100% - 2rem));
  margin: 0 auto;
}

.site-header {
  background: rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(8px);
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 72px;
}

.brand {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--navy);
}

.nav ul {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav a {
  text-decoration: none;
  color: var(--navy);
}

.hero {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 2rem;
  padding: 4rem 0 2rem;
  align-items: center;
}

.eyebrow {
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-size: 0.76rem;
  color: var(--teal);
  font-weight: 700;
}

h1 {
  font-size: clamp(2.3rem, 5vw, 4rem);
  color: var(--navy);
  line-height: 1.05;
  margin: 0 0 1rem;
}

.hero-copy p {
  font-size: 1.05rem;
  max-width: 36rem;
}

button {
  border: none;
  background: var(--navy);
  color: var(--white);
  padding: 0.9rem 1.5rem;
  border-radius: 999px;
  cursor: pointer;
  font-size: 0.95rem;
}

.hero-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 12px 30px rgba(16, 28, 53, 0.06);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0 3rem;
}

.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 1rem;
}

.card h3 {
  margin-top: 0;
  color: var(--navy);
}

@media (max-width: 760px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .nav {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0;
  }
}

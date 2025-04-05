const baseNumbers = [1, 7, 8, 14, 15, 17, 19, 31, 38, 39, 42, 52, 57, 58, 60, 64, 65, 72, 75, 76];
const totalNumbers = Array.from({ length: 76 }, (_, i) => i + 1);
const historicalFrequentNumbers = [3, 37, 10, 22, 26, 33, 7, 31, 1, 45];

function generateCombination() {
  const shuffledBase = baseNumbers.sort(() => 0.5 - Math.random()).slice(0, 5);
  const outsideBase = totalNumbers.filter(n => !baseNumbers.includes(n));
  const shuffledOutside = outsideBase.sort(() => 0.5 - Math.random()).slice(0, 5);
  return [...shuffledBase, ...shuffledOutside].sort((a, b) => a - b);
}

function generateHistoricalCombination() {
  const shuffledHistorical = historicalFrequentNumbers.sort(() => 0.5 - Math.random()).slice(0, 5);
  const outsideHistorical = totalNumbers.filter(n => !historicalFrequentNumbers.includes(n));
  const shuffledOutside = outsideHistorical.sort(() => 0.5 - Math.random()).slice(0, 5);
  return [...shuffledHistorical, ...shuffledOutside].sort((a, b) => a - b);
}

function render() {
  const root = document.getElementById('root');
  const combo = generateCombination();
  const historicalCombo = generateHistoricalCombination();
  root.innerHTML = `
    <h1 style="color:#1e40af; font-family:sans-serif; font-size:2rem;">Kino - Nueva versión</h1>
    <div style="display:grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 20px 0;">
      <h2>Combinación balanceada:</h2>
      ${combo.map(num => <div style="padding:10px; background:#f0f0f0; border-radius:10px; text-align:center;">${num.toString().padStart(2,'0')}</div>).join('')}
    </div>
    <div style="display:grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 20px 0;">
      <h2>Combinación basada en históricos:</h2>
      ${historicalCombo.map(num => <div style="padding:10px; background:#f0f0f0; border-radius:10px; text-align:center;">${num.toString().padStart(2,'0')}</div>).join('')}
    </div>
    <button id="generate" style="padding:10px 20px; font-size:1rem;">Generar nuevas combinaciones</button>
  `;
  document.getElementById('generate').onclick = render;
}

render();
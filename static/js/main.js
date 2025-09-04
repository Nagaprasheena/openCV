(function () {
  // Read operations from JSON script tag to avoid IDE lint errors on inline JS templating
  let operations = [];
  try {
    const jsonEl = document.getElementById('ops-data');
    if (jsonEl) {
      operations = JSON.parse(jsonEl.textContent || '[]');
    }
  } catch (e) {
    console.error('Failed to parse operations JSON', e);
  }

  const opSelect = document.getElementById('operation');
  const paramsDiv = document.getElementById('params');

  function renderParams(opName) {
    if (!paramsDiv) return;
    paramsDiv.innerHTML = '';
    const op = operations.find(o => o.name === opName);
    if (!op || !op.params) return;

    op.params.forEach(p => {
      const col = document.createElement('div');
      col.className = 'col-md-6';
      const id = `param_${p.name}`;
      const inputType = p.type === 'float' ? 'number' : 'number';
      const step = p.type === 'float' ? 'any' : '1';
      col.innerHTML = `
        <label class="form-label" for="${id}">${p.label}</label>
        <input class="form-control" id="${id}" name="${p.name}" type="${inputType}" step="${step}" value="${p.default ?? ''}" />
      `;
      paramsDiv.appendChild(col);
    });
  }

  if (opSelect) {
    renderParams(opSelect.value);
    opSelect.addEventListener('change', (e) => renderParams(e.target.value));
  }
})();

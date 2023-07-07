document.getElementById('codeForm').addEventListener('submit', handleSubmit);

function handleSubmit(event) {
  event.preventDefault();

  const code = document.getElementById('code').value;
  const targetLanguage = document.getElementById('targetLanguage').value;
  const service = document.getElementById('service').value;

  if (code.trim() === '' || targetLanguage === '' || service === '') {
    alert('Please fill in all fields');
    return;
  }

  const prompt =
    service === 'conversion'
      ? `Convert the following code from ${targetLanguage} to JavaScript:\n\n${code}`
      : service === 'debugging'
      ? `Debug the following code:\n\n${code}`
      : service === 'quality-check'
      ? `Perform a quality check on the following code:\n\n${code}`
      : '';

  if (prompt === '') {
    alert('Invalid service');
    return;
  }

  callApi(prompt)
    .then((response) => {
      const output = document.getElementById('output');
      output.textContent = response.result;
    })
    .catch((error) => {
      alert('Error processing the request');
      console.error(error);
    });
}

function callApi(prompt) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/request');
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function () {
      if (xhr.status === 200) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject(new Error('Request failed'));
      }
    };

    xhr.onerror = function () {
      reject(new Error('Request failed'));
    };

    const data = JSON.stringify({ prompt });
    xhr.send(data);
  });
}

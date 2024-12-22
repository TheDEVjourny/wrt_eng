const doOnSubmit = document.querySelector('#sa-submit');
const titleData = document.querySelector('#title-input');
const contextDta = document.querySelector('#context');
let outputText = document.querySelector('#gen-ai-text');

// function callAPI(URL, method, data = {}, apiKey = '') {
//     let answer = {}
//     let flag = false;
//     const FormData = FormData(data)
//     // let Formdata = FormData(data)
//     const requestOptions = {
//         method: method,
//         body: FormData,
//         // headers: {
//         //     'Authorization': `Bearer ${apiKey}`,
//         //   },
//     }

//     if (method === 'GET') {
//         fetch(URL)
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error('Network response was not ok');
//                 }
//                 return response.json();
//             })
//             .then(data => {
//                 answer = data;
//             })
//             .catch(error => {
//                 flag = true;
//                 console.error('Error:', error);
//             });
//     } else if (method === 'POST') {
//         fetch(URL, requestOptions)
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error('Network response was not ok');
//                 }
//                 return response.json();
//             })
//             .then(data => {
//                 answer = data;
//             })
//             .catch(error => {
//                 flag = true;
//                 console.error('Error:', error);
//             });
//     }
//     if (flag)
//         return {};
//     return answer;
// }

function getOutput(backendData) {
    // {
    //     context:,
    //     sugession:,
    // }
    outputText.innerHTML = `<p>${backendData.context}</p>`;
    // outputText.innerHTML = `<p>${backendData.sugession}</p>`
}

doOnSubmit.addEventListener('click', function (event) {
    console.log("submit done");
    event.preventDefault();
    apiUrl = 'http://127.0.0.1:8000/app-api/get-gpt-help';
    console.log(titleData.value);
    console.log(contextDta.value);
    data = {
        "title": titleData.value,
        "context": contextDta.value
    }
    backendData = callAPI(apiUrl, 'POST', data)
    console.log(backendData);
    getOutput(backendData)
});


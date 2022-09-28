// const button = search for form id [form id is in HTML]
// Add an event listener to the form ID [event listener will be in JS file]
// Use fetch request to route in server.py [fetch will be in JS that refers to server.py file]
// Fetch request will send request to Server. Server then handles response. Based on response, does its thing [will be in JS file] 
// Server function is going to run it through crud function [function will be server.py that imports CRUD file in server file; refers to CRUD function]
// Take that crud function data and send it back to Javascript [fetch.then part in JS file]
// Javascript takes that response and use it to display on HTML [Javascript will do append thing and ]
// Empty div in HTML will have things appended to it that will show our 'Use this word instead'


const form = document.querySelector('#search-sentence');

form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    console.log("event fired")

    const formInputs = {
        sentence: document.querySelector('#sentence').value
    };

    console.log(formInputs)

    fetch('/sentencequery', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((responseJson) => {
        console.log(responseJson.status)
        console.log(responseJson.search_complete)
        document.querySelector("#user-response").innerHTML = `Your original sentence: <br>${responseJson.status}</br>`
        document.querySelector("#found-terms").innerHTML = `We found the following terms in our non-inclusive database: <mark>${responseJson.search_complete.found_terms_in_sentence}</mark>`
        document.querySelector("#suggested-terms").innerHTML = `We suggest this instead: <br>${responseJson.search_complete.suggest_new_terms}</br>`
    });
});


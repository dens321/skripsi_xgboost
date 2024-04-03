const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);

function handleSubmit(event) {
    event.preventDefault();
    const url = new URL(form.action);
    const formData = new FormData(form);

    const fetchOptions = {
        method: form.method,
        body: formData,
    };

    document.getElementById("loading-container").classList.remove("hidden");
    
    // check if the table already been shown
    let result_container = document.getElementById("post-upload-container");
    if(!result_container.classList.contains("hidden")){
        document.getElementById("loading-container").classList.add("hidden");
        return;
    }

    fetch(url, fetchOptions)
    .then(resp => resp.text())
    .then(data => {
        const resp_obj = JSON.parse(data);
        if (resp_obj.status == "failed"){
            document.getElementById("loading-container").classList.add("hidden");
            let err_container = document.getElementById("error-container");

            err_container.innerHTML = resp_obj.message;
            err_container.classList.remove("hidden");

            document.getElementById("success-container").classList.add("hidden");
        } else if (resp_obj.status == "success"){
            // set global variable
            window.preprocessed_data = JSON.parse(resp_obj.preprocessed_data) || "";

            window.x_train = JSON.parse(resp_obj.x_train) || [];
            window.x_train_shape = resp_obj.x_train_shape;

            window.x_test = JSON.parse(resp_obj.x_test) || [];
            window.x_test_shape = resp_obj.x_test_shape;

            window.y_train = JSON.parse(resp_obj.y_train) || [];
            window.y_train_shape = resp_obj.y_train_shape;

            window.y_test = JSON.parse(resp_obj.y_test) || [];
            window.y_test_shape = resp_obj.y_test_shape;

            window.y_pred = resp_obj.y_pred;

            window.statistics = resp_obj.statistics;

            // display success message
            let success_container = document.getElementById("success-container");
            success_container.innerHTML = "Data successfully uploaded, scroll down to see the results";
            success_container.classList.remove("hidden");
            // hide error container
            document.getElementById("error-container").classList.add("hidden");

            // get post-upload-container 
            let result_container = document.getElementById("post-upload-container");
            
            // remove class "hidden" from post-upload-container element
            result_container.classList.remove("hidden");

            document.getElementById("preprocess").classList.remove("hidden");

            // parse response object
            let data_obj = JSON.parse(resp_obj.data);
            

            // generate table header
            let table = document.getElementById("table-preview");
            table.innerHTML = "";
            let header_row = table.insertRow(0);
            for(let column in data_obj.columns){
                header_row.insertCell(column).outerHTML = "<th>" + data_obj.columns[column] + "</th>";
            }

            for(let data in data_obj.data){
                let row = table.insertRow(parseInt(data)+1);
                for (let entry in data_obj.data[data]){
                    row.insertCell(entry).innerHTML = data_obj.data[data][entry];
                }
            }
            // hide loading screen
            document.getElementById("loading-container").classList.add("hidden"); 
        }
    })
    .catch(err => {
        document.getElementById("loading-container").classList.add("hidden") 
        console.error(err)
    })
}

const reset = document.getElementById("reset");
reset.addEventListener("click", () => {
    // hide error message
    let err_container = document.getElementById('error-container');
    err_container.innerHTML = "";
    err_container.classList.add("hidden");

    // hide success message
    let succ_container = document.getElementById('success-container');
    succ_container.innerHTML = "";
    succ_container.classList.add("hidden");

    // hide table preview section
    document.getElementById('post-upload-container').classList.add('hidden');

    // hide split data section
    document.getElementById('split-section').classList.add("hidden")

    // hide preprocess and split button
    document.getElementById('preprocess').classList.add('hidden');
    document.getElementById('split').classList.add('hidden');
})

const preprocess = document.getElementById("preprocess-button");
preprocess.addEventListener("click", () => {
    if(window.preprocessed_data){
        let table = document.getElementById("table-preview");
        table.innerHTML = "";
        let header_row = table.insertRow(0);
        for(let column in window.preprocessed_data.columns){
            header_row.insertCell(column).outerHTML = "<th>" + window.preprocessed_data.columns[column] + "</th>";
        }

        for(let data in window.preprocessed_data.data){
            let row = table.insertRow(parseInt(data)+1);
            for (let entry in window.preprocessed_data.data[data]){
                row.insertCell(entry).innerHTML = window.preprocessed_data.data[data][entry];
            }
        }

        let split_button = document.getElementById("split");
        split_button.classList.remove("hidden");
    }
})

let split_button = document.getElementById("split-button");
split_button.addEventListener("click", () => {
    let split_section = document.getElementById("split-section");
    split_section.classList.remove("hidden");

    populateTable(window.x_train, 'x-train-table');
    document.getElementById('x-train-title').innerHTML = "X Train <br> Entries : " + window.x_train_shape[0];

    populateTable(window.y_train, 'y-train-table');
    document.getElementById('y-train-title').innerHTML = "Y Train <br> Entries : " + window.y_train_shape[0];

    populateTable(window.y_test, 'y-test-table');
    document.getElementById('y-test-title').innerHTML = "Y Test <br> Entries : " + window.y_test_shape[0];

    populateTable(window.x_test, 'x-test-table');
    document.getElementById('x-test-title').innerHTML = "X Test <br> Entries : " + window.x_test_shape[0];

    document.getElementById('result').classList.remove("hidden");
})

let result_button = document.getElementById('result-button');
result_button.addEventListener('click', () => {
    document.getElementById('result-section').classList.remove('hidden');
    let table = document.getElementById('y-pred-table');
    table.innerHTML = "";
    let header_row = table.insertRow(0);
    let columns = "Predicted Value";
    header_row .insertCell(0).outerHTML = "<th>" + columns+ "</th>";
    for(let data in window.y_pred) {
        let row = table.insertRow(parseInt(data)+1);
        row.insertCell(0).innerHTML = window.y_pred[data]
    }

    populateTable(window.y_test, 'y-true-table')

    document.getElementById('r2-score').innerHTML = window.statistics.r2;
    document.getElementById('mape').innerHTML = window.statistics.mape;
    document.getElementById('mae').innerHTML = window.statistics.mae;
})

function populateTable(df, table_id) {
    let table = document.getElementById(table_id);
    table.innerHTML = "";
    let header_row = table.insertRow(0);
    let columns = df.columns || df.name;
    if (columns.constructor === Array) {
        for (let column in columns){
            header_row.insertCell(column).outerHTML = "<th>" + columns[column] + "</th>";
        }
    }
    else {
        header_row.insertCell(0).outerHTML = "<th>" + columns + "</th>";
    }
    for (let data in df.data) {
        let row = table.insertRow(parseInt(data)+1);
        if (df.data[data].constructor === Array){
            for (let entry in df.data[data]){
                row.insertCell(entry).innerHTML = df.data[data][entry];
            }
        }   
        else {
            row.insertCell(0).innerHTML = df.data[data]
        }
    }
}
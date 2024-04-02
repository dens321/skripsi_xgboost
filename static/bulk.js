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
    console.log(window.x_train);
})
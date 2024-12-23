const car_types = {
    "Toyota": [
        "Harrier",
        "Fortuner",
        "Vellfire",
        "Kijang Innova",
        "Alphard",
        "Land Cruiser Cygnus",
        "Rush",
        "Veloz",
        "Corolla Altis",
        "Calya",
        "Voxy",
        "Raize",
        "Avanza",
        "Vios",
        "Agya",
        "Yaris",
        "Land Cruiser",
        "Kijang Innova Zenix",
        "Camry",
        "Corolla Cross",
        "Innova Venturer",
        "Sienta",
        "Noah",
        "Camry Hybrid",
        "Kijang",
        "Hiace",
        "86",
        "NAV1",
        "Hilux",
        "Land Cruiser Prado",
        "Yaris Cross",
        "GranAce",
        "Mark X",
        "Etios Valco",
        "Estima",
        "Corolla",
        "C-HR",
        "Etios"
    ],
    "KIA": [
        "Sorento",
        "Rio",
        "Sportage",
        "Seltos",
        "Picanto",
        "Carnival",
        "Sonet",
        "Sonet 7"
    ],
    "Audi": [
        "Q3",
        "Q7",
        "A4",
        "A6",
        "A5",
        "Q5"
    ],
    "Mercedes-Benz": [
        "CLS-Class",
        "E-Class",
        "GLS-Class",
        "GL-Class",
        "GLC-Class",
        "A-Class",
        "C-Class",
        "GLA-Class",
        "B-Class",
        "ML-Class",
        "GLE-Class",
        "CLA-Class",
        "SLK-Class",
        "GLB-Class",
        "S-Class",
        "G-Class",
        "SL-Class",
        "V-Class",
        "no group",
        "CLK-Class",
        "AMG GT"
    ],
    "Ford": [
        "Escape",
        "Fiesta",
        "EcoSport",
        "Focus",
        "Mustang",
        "Everest",
        "Ranger"
    ],
    "Lexus": [
        "RX270",
        "RX300",
        "LX600",
        "UX200",
        "RX350",
        "ES300h",
        "LM350",
        "LX570",
        "NX200t",
        "LS460L",
        "NX300",
        "RX200t",
        "RX350h",
        "LM350h",
        "CT200h"
    ],
    "Mazda": [
        "CX-5",
        "6",
        "CX-9",
        "CX-7",
        "2",
        "CX-3",
        "MX-5",
        "3",
        "CX-30",
        "Biante",
        "CX-8",
        "8"
    ],
    "BMW": [
        "X",
        "5 Series",
        "7 Series",
        "8 Series",
        "3 Series",
        "4 Series",
        "M",
        "Z",
        "6 Series",
        "2 Series"
    ],
    "Honda": [
        "Brio",
        "Odyssey",
        "Civic",
        "Jazz",
        "HR-V",
        "Mobilio",
        "Freed",
        "Accord",
        "CR-V",
        "City",
        "BR-V",
        "Elysion",
        "WR-V",
        "CR-Z"
    ],
    "Renault": [
        "Koleos",
        "Kwid"
    ],
    "Nissan": [
        "Murano",
        "March",
        "Teana",
        "Livina",
        "Juke",
        "Kicks",
        "Navara",
        "Serena",
        "X-Trail",
        "Grand Livina",
        "Elgrand",
        "Livina X-Gear",
        "Terra",
        "Magnite",
        "Evalia"
    ],
    "Mitsubishi": [
        "Pajero Sport",
        "Xpander",
        "Mirage",
        "Triton",
        "Outlander Sport",
        "Strada Triton",
        "Colt",
        "Grandis",
        "Outlander",
        "Kuda",
        "Fuso",
        "Canter",
        "Colt L300",
        "Airtrek",
        "Delica"
    ],
    "Daihatsu": [
        "Terios",
        "Ayla",
        "Gran Max",
        "Rocky",
        "Sirion",
        "Luxio",
        "Sigra",
        "Xenia",
        "Taruna",
        "Taft"
    ],
    "Jeep": [
        "Cherokee",
        "Grand Cherokee",
        "Compass",
        "Wrangler",
        "Gladiator"
    ],
    "Volkswagen": [
        "Scirocco",
        "Tiguan",
        "Golf",
        "The Beetle",
        "Polo",
        "Caravelle",
        "New Beetle",
        "Touran"
    ],
    "Suzuki": [
        "SX4 S-Cross",
        "Baleno",
        "Ertiga",
        "XL7",
        "Jimny",
        "Ignis",
        "Carry",
        "Karimun Wagon R",
        "SX4",
        "APV",
        "Swift",
        "Splash",
        "Grand Vitara",
        "Karimun",
        "Escudo",
        "Katana",
        "S-Presso"
    ],
    "Wuling": [
        "Almaz",
        "Cortez",
        "Alvez",
        "Confero",
        "Formo"
    ],
    "Land Rover": [
        "Defender",
        "Range Rover Velar",
        "Range Rover",
        "Discovery 3",
        "Range Rover Sport",
        "Range Rover Evoque",
        "Discovery",
        "Discovery 4"
    ],
    "Peugeot": [
        "3008",
        "5008",
        "RCZ"
    ],
    "MINI": [
        "Countryman",
        "Cooper",
        "Cabrio",
        "Clubman",
        "Paceman"
    ],
    "Porsche": [
        "Macan",
        "Boxster",
        "Panamera",
        "Cayman",
        "911",
        "Cayenne",
        "718"
    ],
    "MG": [
        "HS",
        "5",
        "ZS"
    ],
    "Hyundai": [
        "Stargazer",
        "Santa Fe",
        "Creta",
        "Tucson",
        "H-1",
        "Stargazer X",
        "Staria",
        "Palisade",
        "Grand Avega",
        "Grand i10"
    ],
    "Subaru": [
        "BRZ",
        "Forester"
    ],
    "Chevrolet": [
        "Trax",
        "Orlando",
        "Captiva",
        "Colorado",
        "Trailblazer",
        "Spark",
        "Spin",
        "Optra",
        "Aveo"
    ],
    "smart": [
        "fortwo"
    ],
    "Jaguar": [
        "XF",
        "XJ",
        "F-Pace",
        "S-Type"
    ],
    "DFSK": [
        "Glory i-Auto"
    ],
    "Dodge": [
        "Journey"
    ],
    "Isuzu": [
        "Giga",
        "Elf",
        "Panther",
        "MU-X",
        "Traga"
    ],
    "Hummer": [
        "H2"
    ],
    "Chery": [
        "Omoda 5",
        "Tiggo 8 Pro",
        "Tiggo 7 Pro"
    ],
    "Bentley": [
        "Continental GT"
    ],
    "McLaren": [
        "650S",
        "720S"
    ],
    "Datsun": [
        "GO+",
        "Cross",
        "GO"
    ],
    "Hino": [
        "Ranger",
        "Dutro"
    ],
    "UD TRUCKS": [
        "Kuzer"
    ],
    "Rolls-Royce": [
        "Ghost"
    ]
}

const brand_options = [];

for (let brand in car_types){
    brand_options.push(brand);
}

const form = document.getElementById("myForm");

// reset handler
const reset = document.getElementById("reset");
reset.addEventListener("click", () => {
    document.getElementById('response').innerHTML = "";
})

// submit handler
form.addEventListener("submit", (e) => {
    e.preventDefault();

    let tahun_kendaraan = document.getElementById("tahun_kendaraan");
    let kilometer = document.getElementById("kilometer");
    let warna = document.getElementById("warna");
    let transmisi = document.getElementById("transmisi");
    let kapasitas_kursi = document.getElementById("kapasitas_kursi");
    let cc_mesin = document.getElementById("cc_mesin");
    let tipe_bahan_bakar = document.getElementById("tipe_bahan_bakar");
    let merek = document.getElementById("merek");

    if(tahun_kendaraan.value == "" || kilometer.value == "" || warna.value == "" || transmisi.value == "" || kapasitas_kursi.value == "" || cc_mesin == "" || tipe_bahan_bakar == "" || merek == ""){
        alert("All fields must be filled!");
    } else {
        data = {
            tahun_kendaraan: tahun_kendaraan.value,
            kilometer: kilometer.value,
            warna: warna.value,
            transmisi: transmisi.value,
            kapasitas_kursi: kapasitas_kursi.value,
            cc_mesin: cc_mesin.value,
            tipe_bahan_bakar: tipe_bahan_bakar.value,
            merek: merek.value
        }
        let json_data = JSON.stringify(data)
        fetch('/prediction', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json_data)
        }).then(resp => resp.text())
        .then(data => {
            let data_obj = JSON.parse(data)
            if (data_obj.error){
                document.getElementById("response").innerHTML = data_obj.message;
                return;
            }
            const formatter = new Intl.NumberFormat('en-US', {
                style: 'currency',
                currency: 'IDR',
              });
            const data_number = formatter.format(parseInt(data.replace(/["]/g, "")));
            document.getElementById("response").innerHTML = data_number;
        })
        .catch(error => {
            console.error(error);
        });
    }
});

// add color options from javascript
const color_options = ["Abu-abu", "Biru", "Coklat", "Emas", "Hijau", "Hitam", "Kuning", "Lainnya", "Marun", "Merah", "Orange", "Putih", "Silver", "Ungu"];
let warna = document.getElementById("warna");
for (let options in color_options){
    let opt = document.createElement('option');
    opt.value = color_options[options];
    opt.innerHTML = color_options[options];
    warna.appendChild(opt);
}

// add brand options from javascript
let is_first = true;
let merek = document.getElementById("merek");
for (let options in brand_options){
    let opt = document.createElement('option');
    opt.value = brand_options[options];
    opt.innerHTML = brand_options[options];
    merek.appendChild(opt);
    if(is_first){
        is_first = false;
        let tipe_mobil = document.getElementById('tipe_mobil');
        let type_options = car_types[brand_options[options]];
        for (let options_ in type_options){
            let opt = document.createElement('option');
            opt.value = type_options[options_];
            opt.innerHTML = type_options[options_];
            tipe_mobil.appendChild(opt);
        }
    }
}

merek.addEventListener('change', (e) => {
    // console.log(e.target.value);
    let tipe_mobil = document.getElementById('tipe_mobil');
    tipe_mobil.innerHTML = "";
    let type_options = car_types[e.target.value];
    for (let options in type_options){
        let opt = document.createElement('option');
        opt.value = type_options[options];
        opt.innerHTML = type_options[options];
        tipe_mobil.appendChild(opt);
    }
})
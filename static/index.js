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
    warna.appendChild(opt)
}

// add brand options from javascript
const brand_options = ["Audi", "BMW", "Bentley", "Cadillac", "Chery", "Chevrolet", "DFSK", "Daihatsu", "Datsun", "Dodge", "Elf", "Ferrari", "Ford", "Hino", "Honda", "Hummer", "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Jeep", "KIA", "Lamborghini", "Land Rover", "Lexus", "MAXUS", "MG", "MINI", "Maserati", "Mazda", "McLaren", "Mercedes-Benz", "Mitsubishi", "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Rolls-Royce", "Subaru", "Suzuki", "Tata", "Toyota", "Volkswagen", "Volvo", "Wuling", "smart"];
let merek = document.getElementById("merek");
for (let options in brand_options){
    let opt = document.createElement('option');
    opt.value = brand_options[options];
    opt.innerHTML = brand_options[options];
    merek.appendChild(opt)
}
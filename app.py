from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score
from joblib import load
import pandas as pd
import json

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory='static')

@app.on_event("startup")
def load_model():
    app.model = load("xgb_model_categorical_latest.joblib")

@app.post("/prediction")
async def prediction(request: Request):
    json_request = await request.json()
    json_data = json.loads(json_request) # turn request body to python dictionary

    numerical_fields = ['tahun_kendaraan', 'kilometer', 'kapasitas_kursi', 'cc_mesin']
    for field in numerical_fields:
        if not json_data[field].isnumeric():
            return {'error': True,'message': f"Invalid value for field {field}. Value given: {json_data[field]}"}

    tahun_kendaraan = int(json_data["tahun_kendaraan"])
    kilometer = int(json_data["kilometer"])
    kapasitas_kursi = int(json_data["kapasitas_kursi"])
    cc_mesin = float(json_data["cc_mesin"])

    pred_df = create_dataframe(tahun_kendaraan, kilometer, json_data['warna'], json_data["transmisi"], kapasitas_kursi, cc_mesin, json_data["tipe_bahan_bakar"], json_data["merek"])
    predictions = app.model.predict(pred_df)[0]
    return str(predictions)

@app.post("/bulk/process")
async def bulkProcessData(file: list[UploadFile]):
    # try:
    df1 = pd.read_csv(file[0].file)
    df2 = pd.read_csv(file[1].file)
    df3 = pd.read_csv(file[2].file)
    df4 = pd.read_csv(file[3].file)
    df5 = pd.read_csv(file[4].file)
    df6 = pd.read_csv(file[5].file)
    df7 = pd.read_csv(file[6].file)
    df8 = pd.read_csv(file[7].file)
    df9 = pd.read_csv(file[8].file)
    df10 = pd.read_csv(file[9].file)
    df11 = pd.read_csv(file[10].file)
    main_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11])
    preprocessed_df = preprocess_bulk_data(main_df)
    x_train, x_test, y_train, y_test = split_bulk_data(preprocessed_df)
    y_pred = app.model.predict(x_test)
    y_predictions = []
    for i in range(0, 5):
        y_predictions.append(str(y_pred[i]))

    r2 = r2_score(y_test, y_pred)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    statistics = {
        "r2": r2,
        "mape": mape,
        "mae": mae
    }
    # except Exception as err:
    #     print(err)
    #     return {"status": "failed","message": f"Failed to read CSV with the following error: {err}"}

    return {
        "status": "success", 
        "data": main_df.head().to_json(orient='split'), 
        "preprocessed_data": preprocessed_df.head().to_json(orient='split'), 
        "x_test": x_test.head().to_json(orient='split'), 
        "x_test_shape": x_test.shape,
        "x_train": x_train.head().to_json(orient='split'), 
        "x_train_shape": x_train.shape,
        "y_train": y_train.head().to_json(orient='split'), 
        "y_train_shape": y_train.shape,
        "y_test": y_test.head().to_json(orient='split'),
        "y_test_shape": y_test.shape,
        "y_pred": y_predictions,
        "statistics": statistics
    }

    
@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.get("/bulk", response_class=HTMLResponse)
def bulk(request: Request):
    return templates.TemplateResponse('bulk.html', {"request": request})

def create_dataframe(tahun_kendaraan, kilometer, warna, transmisi, kapasitas_kursi, cc_mesin, tipe_bahan_bakar, merek):
    data = {
        'tahun kendaraan': [tahun_kendaraan],
        'kilometer': [kilometer],
        'Kapasitas_kursi': [kapasitas_kursi],
        'cc_mesin': [cc_mesin],
        'tipe_mobil_2': [0], 
        'tipe_mobil_2 Series': [0], 
        'tipe_mobil_3': [0], 
        'tipe_mobil_3 Series': [0],
        'tipe_mobil_3008': [0], 
        'tipe_mobil_4 Series':[0], 
        'tipe_mobil_5':[0], 
        'tipe_mobil_5 Series': [0], 
        'tipe_mobil_5008': [0], 
        'tipe_mobil_6':[0], 
        'tipe_mobil_6 Series':[0], 
        'tipe_mobil_650S': [0], 
        'tipe_mobil_7 Series': [0], 
        'tipe_mobil_718':[0], 
        'tipe_mobil_720S':[0], 
        'tipe_mobil_8': [0], 
        'tipe_mobil_8 Series':[0], 
        'tipe_mobil_86':[0], 
        'tipe_mobil_911':[0], 
        'tipe_mobil_A-Class':[0], 
        'tipe_mobil_A4':[0], 
        'tipe_mobil_A5':[0], 
        'tipe_mobil_A6':[0], 
        'tipe_mobil_AMG GT':[0], 
        'tipe_mobil_APV':[0], 
        'tipe_mobil_Accord':[0], 
        'tipe_mobil_Agya':[0], 
        'tipe_mobil_Airtrek':[0], 
        'tipe_mobil_Almaz':[0], 
        'tipe_mobil_Alphard':[0], 
        'tipe_mobil_Alvez':[0], 
        'tipe_mobil_Avanza':[0], 
        'tipe_mobil_Aveo':[0], 
        'tipe_mobil_Ayla':[0], 
        'tipe_mobil_B-Class':[0], 
        'tipe_mobil_BR-V':[0], 
        'tipe_mobil_BRZ':[0], 
        'tipe_mobil_Baleno':[0], 
        'tipe_mobil_Biante':[0], 
        'tipe_mobil_Boxster':[0], 
        'tipe_mobil_Brio':[0], 
        'tipe_mobil_C-Class':[0], 
        'tipe_mobil_C-HR':[0], 
        'tipe_mobil_CLA-Class':[0], 
        'tipe_mobil_CLK-Class':[0], 
        'tipe_mobil_CLS-Class':[0], 
        'tipe_mobil_CR-V':[0], 
        'tipe_mobil_CR-Z':[0], 
        'tipe_mobil_CT200h':[0], 
        'tipe_mobil_CX-3':[0], 
        'tipe_mobil_CX-30':[0], 
        'tipe_mobil_CX-5':[0], 
        'tipe_mobil_CX-7':[0], 
        'tipe_mobil_CX-8':[0], 
        'tipe_mobil_CX-9':[0], 
        'tipe_mobil_Cabrio':[0], 
        'tipe_mobil_Calya':[0], 
        'tipe_mobil_Camry':[0], 
        'tipe_mobil_Camry Hybrid': [0], 
        'tipe_mobil_Canter':[0], 
        'tipe_mobil_Captiva':[0], 
        'tipe_mobil_Caravelle':[0], 
        'tipe_mobil_Carnival':[0], 
        'tipe_mobil_Carry':[0], 
        'tipe_mobil_Cayenne':[0], 
        'tipe_mobil_Cayman':[0], 
        'tipe_mobil_Cherokee':[0], 
        'tipe_mobil_City':[0], 
        'tipe_mobil_Civic':[0], 
        'tipe_mobil_Clubman':[0], 
        'tipe_mobil_Colorado':[0], 
        'tipe_mobil_Colt':[0], 
        'tipe_mobil_Colt L300':[0], 
        'tipe_mobil_Compass':[0], 
        'tipe_mobil_Confero':[0], 
        'tipe_mobil_Continental GT':[0], 
        'tipe_mobil_Cooper':[0], 
        'tipe_mobil_Corolla':[0], 
        'tipe_mobil_Corolla Altis':[0], 
        'tipe_mobil_Corolla Cross':[0], 
        'tipe_mobil_Cortez':[0], 'tipe_mobil_Countryman':[0], 
        'tipe_mobil_Creta':[0], 'tipe_mobil_Cross':[0], 
        'tipe_mobil_Defender':[0], 'tipe_mobil_Delica':[0], 
        'tipe_mobil_Discovery':[0], 'tipe_mobil_Discovery 3':[0], 
        'tipe_mobil_Discovery 4':[0], 'tipe_mobil_Dutro':[0], 
        'tipe_mobil_E-Class':[0], 'tipe_mobil_ES300h':[0], 'tipe_mobil_EcoSport':[0], 
        'tipe_mobil_Elf':[0], 'tipe_mobil_Elgrand':[0], 'tipe_mobil_Elysion':[0], 
        'tipe_mobil_Ertiga':[0], 'tipe_mobil_Escape':[0], 'tipe_mobil_Escudo':[0], 'tipe_mobil_Estima':[0],
        'tipe_mobil_Etios':[0], 'tipe_mobil_Etios Valco':[0], 'tipe_mobil_Evalia':[0], 'tipe_mobil_Everest':[0], 'tipe_mobil_F-Pace':[0], 'tipe_mobil_Fiesta':[0],
        'tipe_mobil_Focus':[0], 'tipe_mobil_Forester':[0], 'tipe_mobil_Formo':[0], 'tipe_mobil_Fortuner':[0], 'tipe_mobil_Freed':[0], 
        'tipe_mobil_Fuso':[0], 'tipe_mobil_G-Class':[0], 'tipe_mobil_GL-Class':[0], 'tipe_mobil_GLA-Class':[0], 'tipe_mobil_GLB-Class':[0], 'tipe_mobil_GLC-Class':[0], 'tipe_mobil_GLE-Class':[0], 'tipe_mobil_GLS-Class':[0], 'tipe_mobil_GO':[0], 'tipe_mobil_GO+':[0], 'tipe_mobil_Ghost':[0], 'tipe_mobil_Giga':[0], 'tipe_mobil_Gladiator':[0],
        'tipe_mobil_Glory i-Auto':[0], 'tipe_mobil_Golf':[0], 'tipe_mobil_Gran Max':[0], 'tipe_mobil_GranAce':[0], 'tipe_mobil_Grand Avega':[0], 'tipe_mobil_Grand Cherokee':[0], 'tipe_mobil_Grand Livina':[0], 
        'tipe_mobil_Grand Vitara':[0], 'tipe_mobil_Grand i10':[0], 'tipe_mobil_Grandis':[0], 'tipe_mobil_H-1':[0], 'tipe_mobil_H2':[0], 'tipe_mobil_HR-V':[0], 'tipe_mobil_HS':[0], 'tipe_mobil_Harrier':[0], 'tipe_mobil_Hiace':[0], 
        'tipe_mobil_Hilux':[0], 'tipe_mobil_Ignis':[0], 'tipe_mobil_Innova Venturer':[0], 'tipe_mobil_Jazz':[0], 'tipe_mobil_Jimny':[0], 'tipe_mobil_Journey':[0], 'tipe_mobil_Juke':[0], 'tipe_mobil_Karimun':[0], 'tipe_mobil_Karimun Wagon R':[0], 'tipe_mobil_Katana':[0], 'tipe_mobil_Kicks':[0], 'tipe_mobil_Kijang':[0], 'tipe_mobil_Kijang Innova':[0], 
        'tipe_mobil_Kijang Innova Zenix':[0], 'tipe_mobil_Koleos':[0], 'tipe_mobil_Kuda':[0], 'tipe_mobil_Kuzer':[0], 'tipe_mobil_Kwid':[0], 'tipe_mobil_LM350':[0], 'tipe_mobil_LM350h':[0], 'tipe_mobil_LS460L':[0], 
        'tipe_mobil_LX570':[0], 'tipe_mobil_LX600':[0], 'tipe_mobil_Land Cruiser':[0], 'tipe_mobil_Land Cruiser Cygnus':[0], 'tipe_mobil_Land Cruiser Prado':[0], 'tipe_mobil_Livina':[0], 'tipe_mobil_Livina X-Gear':[0], 'tipe_mobil_Luxio':[0], 'tipe_mobil_M':[0], 'tipe_mobil_ML-Class':[0], 'tipe_mobil_MU-X':[0], 'tipe_mobil_MX-5':[0], 'tipe_mobil_Macan':[0], 
        'tipe_mobil_Magnite':[0], 'tipe_mobil_March':[0], 'tipe_mobil_Mark X':[0], 'tipe_mobil_Mirage':[0], 'tipe_mobil_Mobilio':[0], 'tipe_mobil_Murano':[0], 'tipe_mobil_Mustang':[0], 'tipe_mobil_NAV1':[0], 'tipe_mobil_NX200t':[0], 'tipe_mobil_NX300':[0], 'tipe_mobil_Navara':[0], 'tipe_mobil_New Beetle':[0], 'tipe_mobil_Noah':[0], 'tipe_mobil_Odyssey':[0], 'tipe_mobil_Omoda 5':[0], 'tipe_mobil_Optra':[0], 'tipe_mobil_Orlando':[0], 'tipe_mobil_Outlander':[0], 'tipe_mobil_Outlander Sport':[0],
        'tipe_mobil_Paceman':[0], 'tipe_mobil_Pajero Sport':[0], 'tipe_mobil_Palisade':[0], 'tipe_mobil_Panamera':[0], 'tipe_mobil_Panther':[0], 'tipe_mobil_Picanto':[0], 'tipe_mobil_Polo':[0], 'tipe_mobil_Q3':[0], 'tipe_mobil_Q5':[0], 'tipe_mobil_Q7':[0], 'tipe_mobil_RCZ':[0], 'tipe_mobil_RX200t':[0],
        'tipe_mobil_RX270':[0], 'tipe_mobil_RX300':[0], 'tipe_mobil_RX350':[0], 'tipe_mobil_RX350h':[0], 'tipe_mobil_Raize':[0], 'tipe_mobil_Range Rover':[0], 'tipe_mobil_Range Rover Evoque':[0], 'tipe_mobil_Range Rover Sport':[0], 'tipe_mobil_Range Rover Velar':[0], 'tipe_mobil_Ranger':[0], 'tipe_mobil_Rio':[0], 'tipe_mobil_Rocky':[0], 'tipe_mobil_Rush':[0], 'tipe_mobil_S-Class':[0], 'tipe_mobil_S-Presso':[0], 'tipe_mobil_S-Type':[0], 'tipe_mobil_SL-Class':[0], 'tipe_mobil_SLK-Class':[0], 'tipe_mobil_SX4':[0], 'tipe_mobil_SX4 S-Cross':[0], 'tipe_mobil_Santa Fe':[0], 'tipe_mobil_Scirocco':[0], 'tipe_mobil_Seltos':[0], 'tipe_mobil_Serena':[0], 'tipe_mobil_Sienta':[0], 'tipe_mobil_Sigra':[0], 'tipe_mobil_Sirion':[0], 'tipe_mobil_Sonet':[0], 'tipe_mobil_Sonet 7':[0], 'tipe_mobil_Sorento':[0], 
        'tipe_mobil_Spark':[0], 'tipe_mobil_Spin':[0], 'tipe_mobil_Splash':[0], 'tipe_mobil_Sportage':[0], 'tipe_mobil_Stargazer':[0], 'tipe_mobil_Stargazer X':[0], 'tipe_mobil_Staria':[0], 'tipe_mobil_Strada Triton':[0], 'tipe_mobil_Swift':[0], 'tipe_mobil_Taft':[0], 'tipe_mobil_Taruna':[0], 'tipe_mobil_Teana':[0], 'tipe_mobil_Terios':[0], 'tipe_mobil_Terra':[0], 'tipe_mobil_The Beetle':[0], 'tipe_mobil_Tiggo 7 Pro':[0], 'tipe_mobil_Tiggo 8 Pro':[0], 'tipe_mobil_Tiguan':[0], 'tipe_mobil_Touran':[0], 'tipe_mobil_Traga':[0], 'tipe_mobil_Trailblazer':[0], 'tipe_mobil_Trax':[0], 'tipe_mobil_Triton':[0], 'tipe_mobil_Tucson':[0], 'tipe_mobil_UX200':[0], 'tipe_mobil_V-Class':[0], 'tipe_mobil_Vellfire':[0], 
        'tipe_mobil_Veloz':[0], 'tipe_mobil_Vios':[0], 'tipe_mobil_Voxy':[0], 'tipe_mobil_WR-V':[0], 'tipe_mobil_Wrangler':[0], 'tipe_mobil_X':[0], 'tipe_mobil_X-Trail':[0], 'tipe_mobil_XF':[0], 'tipe_mobil_XJ':[0], 'tipe_mobil_XL7':[0], 'tipe_mobil_Xenia':[0], 'tipe_mobil_Xpander':[0], 'tipe_mobil_Yaris':[0], 'tipe_mobil_Yaris Cross':[0], 'tipe_mobil_Z':[0], 'tipe_mobil_ZS':[0], 'tipe_mobil_fortwo':[0], 'tipe_mobil_no group':[0],
        'Transmisi_Automatic': [0],
        'Transmisi_Manual': [0],
        'warna_Abu-abu': [0],
        'warna_Biru': [0],
        'warna_Coklat': [0],
        'warna_Emas': [0],
        'warna_Hijau': [0],
        'warna_Hitam': [0],
        'warna_Kuning': [0],
        'warna_Lainnya': [0],
        'warna_Marun': [0],
        'warna_Merah': [0],
        'warna_Orange': [0],
        'warna_Putih': [0],
        'warna_Silver': [0],
        'warna_Ungu': [0],
        'Merek_Audi': [0],
        'Merek_BMW': [0],
        'Merek_Bentley': [0],
        'Merek_Chery': [0],
        'Merek_Chevrolet': [0],
        'Merek_DFSK': [0],
        'Merek_Daihatsu': [0],
        'Merek_Datsun': [0],
        'Merek_Dodge': [0],
        'Merek_Ford': [0],
        'Merek_Hino': [0],
        'Merek_Honda': [0],
        'Merek_Hummer': [0],
        'Merek_Hyundai': [0],
        'Merek_Isuzu': [0],
        'Merek_Jaguar': [0],
        'Merek_Jeep': [0],
        'Merek_KIA': [0],
        'Merek_Land Rover': [0],
        'Merek_Lexus': [0],
        'Merek_MG': [0],
        'Merek_MINI': [0],
        'Merek_Mazda': [0],
        'Merek_McLaren': [0],
        'Merek_Mercedes-Benz': [0],
        'Merek_Mitsubishi': [0],
        'Merek_Nissan': [0],
        'Merek_Peugeot': [0],
        'Merek_Porsche': [0],
        'Merek_Renault': [0],
        'Merek_Rolls-Royce': [0],
        'Merek_Subaru': [0],
        'Merek_Suzuki': [0],
        'Merek_Toyota': [0],
        'Merek_UD TRUCKS':[0],
        'Merek_Volkswagen': [0],
        'Merek_Wuling': [0],
        'Merek_smart': [0],
        'tipe_bahan_bakar_Bensin': [0],
        'tipe_bahan_bakar_Solar': [0],
    }

    if transmisi in ["Automatic", "automatic", "matic"]:
        data.update({"Transmisi_Automatic": [1]})
    else:
        data.update({"Transmisi_Manual": [1]})

    if warna in ["Abu-abu", "Biru", "Coklat", "Emas", "Hijau", "Hitam", "Kuning", "Lainnya", "Marun", "Merah", "Orange", "Putih", "Silver", "Ungu"]:
        key = f"warna_{warna}"
        data.update({key: [1]})
    else:
        data.update({"warna_Lainnya": [1]})

    if tipe_bahan_bakar in ["Bensin", "Pertamax", "pertamax", "Pertalite", "pertalite"]:
        data.update({"tipe_bahan_bakar_Bensin": [1]})
    else:
        data.update({"tipe_bahan_bakar_Solar": [1]})

    if merek in ["Audi", "BMW", "Bentley", "Cadillac", "Chery", "Chevrolet", "DFSK", "Daihatsu", "Datsun", "Dodge", "Elf", "Ferrari", "Ford", "Hino", "Honda", "Hummer", "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Jeep", "KIA", "Lamborghini", "Land Rover", "Lexus", "MAXUS", "MG", "MINI", "Maserati", "Mazda", "McLaren", "Mercedes-Benz", "Mitsubishi", "Nissan", "Opel", "Peugeot", "Porsche", "Renault", "Rolls-Royce", "Subaru", "Suzuki", "Tata", "Toyota", "Volkswagen", "Volvo", "Wuling", "smart"]:
        merek_key = f"Merek_{merek}"
        data.update({merek_key: [1]})

    return pd.DataFrame(data)

def preprocess_bulk_data(df):
    df = df.drop(["web-scraper-order", "web-scraper-start-url", "Link", "Link-href", "tanggal"], axis=1)
    fuels = ["Solar", "Petrol - Unleaded", "Pertamax", "Diesel"]
    df = df[df.tipe_bahan_bakar.isin(fuels)]
    df = df.dropna()

    for i in range(len(df)):
        df.iloc[i, 2] = df.iloc[i, 2].split('-')[-1].replace(' km', '').replace('K', '000').replace(" ", '')

        df.iloc[i, 8] = df.iloc[i, 8].replace('Rp', '').replace(".", '').replace(' ', '')

    df["kilometer"] = df["kilometer"].astype(int)

    df["harga_jual"] = df["harga_jual"].astype(int)

    df["tipe_bahan_bakar"] = df["tipe_bahan_bakar"].replace(['Pertamax', 'Petrol - Unleaded'], 'Bensin')
    df["tipe_bahan_bakar"] = df["tipe_bahan_bakar"].replace(['Solar', 'Diesel'], 'Solar')
    # df = df.drop(["nama_mobil"], axis=1)
    dummies = pd.get_dummies(df[["tipe_mobil", "Transmisi", "warna", "Merek", "tipe_bahan_bakar"]], dtype=int)
    df = pd.concat([df, dummies], axis=1)
    df.drop('Merek', axis=1, inplace=True)
    df.drop('tipe_bahan_bakar', axis=1, inplace=True)
    df.drop('Transmisi', axis=1, inplace=True)
    df.drop('warna', axis=1, inplace=True)
    df.drop('tipe_mobil', axis=1, inplace=True)

    return df

def split_bulk_data(df):
    x = df.drop('harga_jual', axis=1)
    y = df['harga_jual']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
    # print(x_test.head())
    return x_train, x_test, y_train, y_test
    pass
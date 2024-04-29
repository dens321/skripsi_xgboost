from fastapi import FastAPI, Form, Request, UploadFile, File
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
    try:
        df1 = pd.read_csv(file[0].file)
        df2 = pd.read_csv(file[1].file)
        df3 = pd.read_csv(file[2].file)
        df4 = pd.read_csv(file[3].file)
        df5 = pd.read_csv(file[4].file)
        main_df = pd.concat([df1, df2, df3, df4, df5])
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
    except Exception as err:
        return {"status": "failed","message": f"Failed to read CSV with the following error: {err}"}

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
        'Merek_Aston Martin': [0],
        'Merek_Audi': [0],
        'Merek_BMW': [0],
        'Merek_Bentley': [0],
        'Merek_Cadillac': [0],
        'Merek_Chery': [0],
        'Merek_Chevrolet': [0],
        'Merek_DFSK': [0],
        'Merek_Daihatsu': [0],
        'Merek_Datsun': [0],
        'Merek_Dodge': [0],
        'Merek_Elf': [0],
        'Merek_Ferrari': [0],
        'Merek_Ford': [0],
        'Merek_Hino': [0],
        'Merek_Honda': [0],
        'Merek_Hummer': [0],
        'Merek_Hyundai': [0],
        'Merek_Infiniti': [0],
        'Merek_Isuzu': [0],
        'Merek_Jaguar': [0],
        'Merek_Jeep': [0],
        'Merek_KIA': [0],
        'Merek_Lamborghini': [0],
        'Merek_Land Rover': [0],
        'Merek_Lexus': [0],
        'Merek_MAXUS': [0],
        'Merek_MG': [0],
        'Merek_MINI': [0],
        'Merek_Maserati': [0],
        'Merek_Mazda': [0],
        'Merek_McLaren': [0],
        'Merek_Mercedes-Benz': [0],
        'Merek_Mitsubishi': [0],
        'Merek_Nissan': [0],
        'Merek_Opel': [0],
        'Merek_Peugeot': [0],
        'Merek_Porsche': [0],
        'Merek_Renault': [0],
        'Merek_Rolls-Royce': [0],
        'Merek_Subaru': [0],
        'Merek_Suzuki': [0],
        'Merek_Tata': [0],
        'Merek_Toyota': [0],
        'Merek_Volkswagen': [0],
        'Merek_Volvo': [0],
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
    df = df.drop(["nama_mobil"], axis=1)
    dummies = pd.get_dummies(df[["Transmisi", "warna", "Merek", "tipe_bahan_bakar"]], dtype=int)
    df = pd.concat([df, dummies], axis=1)
    df.drop('Merek', axis=1, inplace=True)
    df.drop('tipe_bahan_bakar', axis=1, inplace=True)
    df.drop('Transmisi', axis=1, inplace=True)
    df.drop('warna', axis=1, inplace=True)

    return df

def split_bulk_data(df):
    x = df.drop('harga_jual', axis=1)
    y = df['harga_jual']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
    return x_train, x_test, y_train, y_test
    pass
import numpy as np
import pickle
import streamlit as st

# Modelin yüklenmesi
loaded_model = pickle.load(open('bank_marketing_prediction.sav', 'rb'))

def bank_marketing_prediction(input_data):
    # Özellik isimlerini eğitim verileriyle eşleştirin
    column_names = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
                    'contact', 'month', 'day_of_week', 'campaign', 'pdays', 'previous', 
                    'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 
                    'euribor3m', 'nr.employed']  # Alt çizgi yerine nokta kullanın

    input_data = pd.DataFrame([input_data], columns=column_names)
    prediction = loaded_model.predict(input_data)
    return prediction[0]


def main():
    # Başlık
    st.title('Banka Pazarlama Tahmin Web Uygulaması')
    
    # Kullanıcıdan veri alma
    age = st.number_input('Yaş')
    job = st.selectbox('Meslek', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 
                               'retired', 'self-employed', 'services', 'student', 'technician', 
                               'unemployed', 'unknown'])
    marital = st.selectbox('Medeni Durum', ['divorced', 'married', 'single', 'unknown'])
    education = st.selectbox('Eğitim Seviyesi', ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 
                                                 'illiterate', 'professional.course', 'university.degree', 'unknown'])
    default = st.selectbox('Kredi Temerrüdü', ['no', 'yes', 'unknown'])
    housing = st.selectbox('Konut Kredisi', ['no', 'yes', 'unknown'])
    loan = st.selectbox('Bireysel Kredi', ['no', 'yes', 'unknown'])
    contact = st.selectbox('İletişim Türü', ['cellular', 'telephone'])
    month = st.selectbox('Son İletişim Ayı', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 
                                                'aug', 'sep', 'oct', 'nov', 'dec'])
    day_of_week = st.selectbox('Son İletişim Günü', ['mon', 'tue', 'wed', 'thu', 'fri'])
    campaign = st.number_input('Bu Kampanya Sırasındaki İletişim Sayısı')
    pdays = st.number_input('Önceki Kampanyadan Sonra Geçen Gün Sayısı')
    previous = st.number_input('Bu Kampanya Öncesi İletişim Sayısı')
    poutcome = st.selectbox('Önceki Kampanya Sonucu', ['failure', 'nonexistent', 'success'])
    emp_var_rate = st.number_input('İstihdam Değişim Oranı')
    cons_price_idx = st.number_input('Tüketici Fiyat Endeksi')
    cons_conf_idx = st.number_input('Tüketici Güven Endeksi')
    euribor3m = st.number_input('Euribor 3 Aylık Faiz Oranı')
    nr_employed = st.number_input('Çalışan Sayısı')

    # Tahmin için kod
    prediction = ''
    
    # Kullanıcıdan alınan giriş verileri
    if st.button('Banka Pazarlama Tahmini'):
        prediction = bank_marketing_prediction([age, job, marital, education, default, housing, loan,
                                                contact, month, day_of_week, campaign, pdays, previous, 
                                                poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, 
                                                euribor3m, nr_employed])
        
    st.success(prediction)
    
if _name_ == '_main_':
    main()

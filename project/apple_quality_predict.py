import streamlit as st
import numpy as np
import joblib  

# Загрузка модели и scaler
model = joblib.load("apple_quality_model.pkl")  # Замените на имя вашего файла модели

# Заголовок приложения
st.title("Предсказание качества яблока")
st.write("Введите значения свойств яблока, чтобы узнать его качество (good/bad).")

# Поля для ввода значений
size = st.number_input("Размер (Size)", min_value=-7.15, max_value=6.41, value=0.0)
weight = st.number_input("Вес (Weight)", min_value=-7.15, max_value=5.79, value=0.0)
sweetness = st.number_input("Сладость (Sweetness)", min_value=-6.89, max_value=6.37, value=0.0)
crunchiness = st.number_input("Хрусткость (Crunchiness)", min_value=-6.06, max_value=7.62, value=0.0)
juiciness = st.number_input("Сочность (Juiciness)", min_value=-5.96, max_value=7.36, value=0.0)
ripeness = st.number_input("Спелость (Ripeness)", min_value=-5.86, max_value=7.24, value=0.0)
acidity = st.number_input("Кислотность (Acidity)", min_value=-7.01, max_value=7.4, value=0.0)

# Кнопка для предсказания
if st.button("Предсказать качество"):
    # Подготовка данных для модели
    input_data = np.array([[size, weight, sweetness, crunchiness, juiciness, ripeness, acidity]])

    # Предсказание
    prediction = model.predict(input_data)
    predicted_quality = "good" if prediction[0] == 1 else "bad"

    # Результат
    st.write(f"Предсказанное качество яблока: **{predicted_quality}**")

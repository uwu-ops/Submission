import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

all_dataset = pd.read_csv("dashboard/all_dataset.csv")


st.header('Analisis Data E-Commerce Public Dataset')

st.subheader(
    """Score Review per-Kategori Barang"""
)
st.table(
    all_dataset.groupby(by=["product_category_name_english"]).agg(
    {
        "review_score": "mean"
    }).sort_values("review_score")
)
data = all_dataset.groupby(by=["product_category_name_english"]).agg(
    {
        "review_score": "mean"
    }
)
data["review_score"] = ["{:.2f}".format(v) for v in data["review_score"]]
data = data.sort_values("review_score")

fig = plt.figure(figsize=(12, 8))
x = data.index
y = data["review_score"]

plt.bar(x, y)
plt.xlabel("Kategori Barang")
plt.ylabel("Score Review")
plt.xticks(rotation=90)
plt.title("Score Review per-Kategori Barang")
plt.margins(.02)
st.pyplot(fig)

st.subheader(
    """Persebaran Konsumen Berdasarkan State"""
)

data_state = all_dataset.groupby(by="customer_state").customer_id.count()
fig = plt.figure(figsize=(12, 8))
y = sorted(list(data_state))
x = list(data_state.index)

for i in range(len(x)):
  plt.text(i,y[i],y[i], ha = 'center')

plt.bar(x, y)
plt.title("Persebaran konsumen Berdasarkan State")
plt.xlabel("State")
plt.ylabel("Jumlah Customer")
st.pyplot(fig)

st.subheader(
    """Kategori Produk yang Sering Dibeli"""
)

st.table(
     all_dataset.groupby(by=["product_category_name_english"]).agg(
    {
        "payment_sequential" : "sum"
    }).sort_values("payment_sequential")
)

data = all_dataset.groupby(by=["product_category_name_english"]).agg(
    {
        "payment_sequential" : "sum"
    }
)
data = data.sort_values("payment_sequential")

fig = plt.figure(figsize=(12, 8))
x = data.index
y = data["payment_sequential"]

plt.bar(x, y)
plt.xlabel("Kategori Barang")
plt.ylabel("Total Pembelian")
plt.xticks(rotation=90)
plt.title("Kategori Barang yang Sering Dibeli")
plt.margins(.02)
st.pyplot(fig)

st.subheader(
    """Jumlah Order Berdasarkan State"""
)

amount_order__by_state = all_dataset.groupby(by="customer_state").order_id.nunique().sort_values(ascending=False)

fig = plt.figure(figsize=(12, 8))
y = sorted(list(amount_order__by_state))
x = list(amount_order__by_state.index)

for i in range(len(x)):
  plt.text(i,y[i],y[i], ha = 'center')

plt.bar(x, y)
plt.title("Persebaran Order Berdasarkan State")
plt.xlabel("State")
plt.ylabel("Jumlah Order")
st.pyplot(fig)

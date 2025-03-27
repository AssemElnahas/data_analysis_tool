import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# إعداد الواجهة
st.title("📊 أداة تحليل البيانات التفاعلية")
st.write("🔹 قم برفع ملف CSV لتحليل البيانات وعرض الرسوم البيانية بسهولة.")

# تحميل ملف CSV
uploaded_file = st.file_uploader("📂 اختر ملف CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # عرض معلومات أولية عن البيانات
    st.subheader("🔍 نظرة عامة على البيانات")
    st.write(df.head())

    st.subheader("📌 معلومات عن البيانات")
    st.write(f"✅ عدد الصفوف: {df.shape[0]}")
    st.write(f"✅ عدد الأعمدة: {df.shape[1]}")
    st.write(f"✅ القيم الفارغة:\n{df.isnull().sum()}")

    # اختيار العمود لتحليل البيانات
    selected_column = st.selectbox("📊 اختر عمودًا للتحليل:", df.columns)

    if df[selected_column].dtype in ['int64', 'float64']:
        st.subheader(f"📈 إحصائيات عمود {selected_column}")
        st.write(df[selected_column].describe())

        # رسم مخطط بياني
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, bins=30, ax=ax)
        st.pyplot(fig)

    # فلترة البيانات بناءً على المستخدم
    st.subheader("🔎 فلترة البيانات")
    filter_value = st.text_input(f"🔍 أدخل قيمة للبحث في {selected_column}:")

    if filter_value:
        filtered_df = df[df[selected_column].astype(str).str.contains(
            filter_value, case=False, na=False)]
        st.write(filtered_df)

    # تصدير البيانات إلى Excel
    st.subheader("📥 تصدير البيانات")
    if st.button("💾 تحميل البيانات كـ Excel"):
        df.to_excel("Analyzed_Data.xlsx", index=False)
        st.success("✅ تم حفظ البيانات بنجاح!")

else:
    st.warning("⚠️ الرجاء رفع ملف CSV أولًا.")

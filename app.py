
import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="SHIROE LABO カウンセリングシート", layout="centered")

st.title("SHIROE LABO カウンセリングシート")

with st.form(key="counseling_form"):
    st.subheader("■ 基本情報")

    col1, col2 = st.columns(2)
    with col1:
        last_name = st.text_input("姓")
    with col2:
        first_name = st.text_input("名")

    col3, col4 = st.columns(2)
    with col3:
        last_name_kana = st.text_input("セイ（カタカナ）")
    with col4:
        first_name_kana = st.text_input("メイ（カタカナ）")

    gender = st.radio("性別", ["女性", "男性", "その他"])

    st.markdown("### 生年月日")
    col_year, col_month, col_day = st.columns(3)
    with col_year:
        birth_year = st.selectbox("年", list(range(1950, datetime.today().year + 1)), index=30)
    with col_month:
        birth_month = st.selectbox("月", list(range(1, 13)))
    with col_day:
        birth_day = st.selectbox("日", list(range(1, 32)))

    try:
        birth_date = datetime(birth_year, birth_month, birth_day)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        st.markdown(f"**年齢：{age}歳**")
    except:
        st.warning("正しい生年月日を選択してください。")

    zipcode = st.text_input("郵便番号")
    address = st.text_input("住所")
    phone = st.text_input("電話番号（任意）")

    st.subheader("■ 印象・目的について")

    impressions = st.multiselect("なりたい印象（複数選択）", [
        "清潔感がある", "若々しく見える", "自信がありそう", "垢抜けている",
        "健康的な印象", "信頼感", "話しかけやすい", "透明感がある"
    ])

    motive = st.multiselect("ご来店の目的・背景（複数選択）", [
        "仕事・面接に向けて", "恋愛・婚活", "大切な予定のため", "自分磨きの一環として",
        "SNSなどで気になった", "久々に人と会う予定", "なんとなく整えたい"
    ])

    tooth_state = st.radio("現在の歯の状態", [
        "特に気にしていない", "少し黄ばみが気になる", "人と比べて気になる",
        "鏡や写真で気になる", "笑う時に気になる"
    ])

    history = st.multiselect("これまでのホワイトニング経験（複数選択）", [
        "初めて", "歯科ホワイトニング", "セルフホワイトニング（サロン）",
        "ホームホワイトニング（歯科キット）", "市販ホワイトニング（歯磨き粉・シート等）"
    ])

    style = st.radio("理想の通い方", [
        "週1〜2回で集中して通いたい",
        "月2回くらいのペースで通いたい",
        "不定期でも気になったときに通いたい",
        "一度白くしたら、その後は維持として通いたい"
    ])

    concerns = st.text_area("その他、気になること・不安など")

    st.subheader("■ 同意事項")
    with st.expander("▼ ご確認ください（クリックで表示）", expanded=False):
        st.markdown("""
●個人情報の使用について
当店ではお客様の個人情報をお聞きしておりますが、これらの情報は、ご利用者様の確認・照会にのみ使用しております。
法律に基づき開示が義務づけられている等の特別な事情がない限り、お客様ご本人の事前の許可なく第三者に個人情報を提供いたしません。
住所・ご登録内容に変更がありました場合はご連絡ください。

●注意事項
（中略）詳細は実アプリで展開
        """)

    agree = st.checkbox("上記注意事項をすべて確認し、同意しました。")
    date = datetime.today().strftime("%Y-%m-%d")
    st.markdown(f"**同意日：{date}**")

    st.subheader("■ 署名欄")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",
        stroke_width=2,
        stroke_color="#000000",
        background_color="#ffffff",
        height=150,
        width=400,
        drawing_mode="freedraw",
        key="canvas"
    )

    submitted = st.form_submit_button("送信")

    if submitted and agree:
        st.success("回答を受け付けました（※保存処理は後で接続）")
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data, caption="署名画像（プレビュー）")
        else:
            st.warning("署名が見つかりません。もう一度お試しください。")
    elif submitted and not agree:
        st.error("注意事項への同意が必要です。")

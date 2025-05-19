
import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="SHIROE LABO カウンセリングシート", layout="centered")

st.title("SHIROE LABO カウンセリングシート")
karte_no = "No.001（仮）"
st.markdown(f"### あなたのカルテ番号：{karte_no}")

with st.form(key="counseling_form"):
    st.subheader("■ 基本情報")
    name = st.text_input("お名前（フルネーム）")
    furigana = st.text_input("フリガナ")
    gender = st.radio("性別", ["女性", "男性", "その他"])
    birthdate = st.date_input("生年月日")
    zipcode = st.text_input("郵便番号")
    address = st.text_input("住所")

    st.subheader("■ 印象について")
    impressions = st.multiselect("なりたい印象を選んでください", [
        "清潔感がある", "若々しく見える", "自信がありそう", "垢抜けている",
        "健康的な印象", "信頼感", "話しかけやすい", "透明感がある"
    ])
    motive = st.multiselect("目的・背景を教えてください", [
        "仕事や面接に向けて", "恋愛・婚活", "大切な予定のため", "自分に自信を持ちたい",
        "SNSなどで気になった", "久々に人に会う予定", "なんとなく整えたい"
    ])
    tooth_state = st.radio("現在の歯の状態", [
        "特に気にしていない", "少し黄ばみが気になる", "人と比べて気になる",
        "鏡や写真で気になる", "笑う時に気になる"
    ])
    history = st.radio("ホワイトニング経験", [
        "歯科で経験あり", "セルフで経験あり", "市販商品を使用", "初めて"
    ])
    style = st.radio("理想の通い方", [
        "週1〜2回で集中したい", "月2回ほど", "不定期でも整えたい", "維持として通いたい"
    ])
    concerns = st.text_area("その他気になること・不安などあればご記入ください")

    st.subheader("■ 同意事項（抜粋）")
    st.markdown("""
    - 施術効果には個人差があり、白さや斑点などが出ることがあります  
    - 妊娠中・顎関節症・光過敏症などに該当する方はご遠慮ください  
    - 使用中に痛みが出た場合は直ちに中止してください  
    - 使用による損害・損失については一切の責任を負いかねます  
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

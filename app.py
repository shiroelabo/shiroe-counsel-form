
import streamlit as st
import requests
from datetime import datetime
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="SHIROE LABO カウンセリングシート", layout="centered")

# ロゴとタイトル
st.image("logo.png", width=300)
st.markdown("## カウンセリングシート")

def lookup_address(zipcode):
    if len(zipcode) == 7 and zipcode.isdigit():
        response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                result = data["results"][0]
                return f"{result['address1']}{result['address2']}{result['address3']}"
    return ""

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

    zipcode = st.text_input("郵便番号（ハイフンなし）")
    address_default = lookup_address(zipcode)
    address = st.text_input("住所", value=address_default)
    phone = st.text_input("電話番号")

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

●施術後の仕上がりには個人差があり、色斑や斑点、縞模様が出ることがあります。
●医療機関で治療を受けている方やお痛みのある方、下記に当てはまる方はご使用をお控えください。
1、顎関節症の方
2、アレルギー体質の方
3、光過敏症の方
●妊娠中の方は、施術を受けることを予めかかりつけの医師に確認の上、施術を行うことを原則とします。施術中・施術後にいかなる不測の事態が生じても当店は一切の責任を負いかねますので、その旨をご承知頂いた上での施術と致します。
●使用中に痛みや異常を感じた際には直ちに使用を中止してください。中断した場合もご返金には応じかねます。
●マウスオープナーを使用した照射後に、唇及び口の周辺に鬱血や乾燥等により、唇、口周り等が黒く変色する可能性があります。
●使用中は唾液が溜まりやすいので施術中や終了時に起き上がる際には十分に注意ください。
●効果には個人差があります。(お客様の歯の状態により仕上がりが異なります)
●差し歯・入れ歯・詰め物・被せ物に於ける材質の経年劣化による変色には効果がありません。
●神経を抜いたことにより歯が変色している場合や、遺伝により歯にもともと色素沈着がある場合、表面ではなく内部が変色している歯は白さを実感しにくくなります。
●フッ素症の症状が見られる場合は多様な症状が現れる場合があります。
●歯の構造により汚れの落ち方に差異が生じ、白点や白線状のものが歯に浮かび上がることがまれに発生いたします。
●液剤を塗布した歯に光が当たる事で効果を発揮します。照射中は光が歯からずれないようにしてください。
●ご利用中に生じた人的・物的事故及び盗難・紛失につきましては、弊社に故意または重大な過失がある場合や、本サービスを利用する際に使用する製品に欠陥がある場合を除き責任を負いません。
●いかなる場合も、施術後の返金には応じかねます。
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

    if agree:
        submit_btn = st.form_submit_button("送信", type="primary")
    else:
        submit_btn = st.form_submit_button("送信")

    if submit_btn and agree:
        st.success("回答を受け付けました（※保存処理は後で接続）")
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data, caption="署名画像（プレビュー）")
        else:
            st.warning("署名が見つかりません。もう一度お試しください。")
    elif submit_btn and not agree:
        st.error("注意事項への同意が必要です。")

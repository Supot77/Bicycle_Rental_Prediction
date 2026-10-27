"""A visible starting point. Students add the real prediction flow later."""

import json

import streamlit as st

from starter_support import configuration_problems, load_config


st.set_page_config(page_title="Bicycle Rental Prediction", page_icon="🚲")
st.title("Bicycle Rental Demand Prediction")
st.caption("IFJC4002 · โครงเริ่มต้นสำหรับงานกลุ่ม")
st.info("ยังไม่มีโมเดลทำนาย: อยู่ระหว่างเตรียมงานและรอ dataset จากอาจารย์")
st.write("เริ่มจากคู่มือและ notebook 00 จากนั้นทำตามช่วงงาน 01–05 เมื่อได้รับข้อมูลจริง")

try:
    config = load_config()
except (OSError, ValueError, json.JSONDecodeError) as error:
    st.error(f"อ่าน config/project.json ไม่ได้: {error}")
    st.stop()

problems = configuration_problems(config)
if problems:
    st.error("แก้รูปแบบ config ก่อนเริ่มเชื่อมระบบ")
    for problem in problems:
        st.write(f"• {problem}")
    st.stop()

st.subheader("สิ่งที่ต้องทำก่อนเปิดใช้การทำนาย")
for step in (
    "ยืนยันข้อมูล หน่วย และคำถามกับอาจารย์",
    "วิเคราะห์ข้อมูลและกำหนดวิธีแบ่งชุดข้อมูล",
    "ทดลอง baseline และอย่างน้อย 2 อัลกอริทึม",
    "เลือกจากหลักฐาน ประเมิน test และบันทึก pipeline",
    "เพิ่มช่องกรอก ตรวจ input และเทียบผลกับ notebook",
):
    st.write(f"• {step}")

with st.expander("ดูรายการตั้งค่าที่ยังต้องยืนยัน"):
    for problem in configuration_problems(config, require_ready=True):
        st.write(f"• {problem}")
    st.caption("การกรอก config ครบยังไม่หมายถึงมีโมเดลหรือผ่านการทดสอบแล้ว")

st.link_button("อ่านคู่มือใน repository", "https://github.com/Supot77/Bicycle_Rental_Prediction#readme")

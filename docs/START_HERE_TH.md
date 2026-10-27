# เริ่มต้นครั้งแรก

เป้าหมายรอบแรกคือเปิดงานได้ รู้ว่าแต่ละส่วนอยู่ไหน และทำแบบฝึกเล็กหนึ่งชิ้นสำเร็จ ยังไม่ต้องฝึกโมเดลของโครงงาน

## เลือกวิธีเปิด notebook

ใช้เครื่องตัวเองเหมาะกับคนที่ต้องการฝึกและต่อแอปในที่เดียว แต่ต้องติดตั้ง Python/Git ส่วน Google Colab เริ่ม notebook ผ่านเว็บสะดวก แต่ไฟล์ใน runtime เป็นชั่วคราวและต้องนำงานกลับมาเก็บให้ถูกที่ ทั้งสองทางทำงานร่วมกันได้เมื่อใช้ config และไฟล์รุ่นเดียวกัน

## วิธี A: Windows PowerShell

ติดตั้ง Python 3.12 และ Git ก่อน ตรวจด้วย `py -3.12 --version` และ `git --version` ถ้าเครื่องมี Python รุ่นอื่น ไม่ต้องลบของเดิม ให้ติดตั้ง 3.12 แยกและเรียกผ่าน `py -3.12`

```powershell
git clone https://github.com/Supot77/Bicycle_Rental_Prediction.git
cd Bicycle_Rental_Prediction
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/check_setup.py
.\.venv\Scripts\python.exe -m jupyterlab
```

เปิด notebook 00 ในหน้า JupyterLab รันทีละ cell ด้วย Shift+Enter และอ่านคำอธิบายก่อนข้ามไป cell ถัดไป

เปิดแอปด้วย terminal อีกหน้าที่อยู่ในโฟลเดอร์โครงงาน:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

หยุด server ด้วย Ctrl+C คำสั่งใช้ Python ใน `.venv` ตรง ๆ จึงไม่ต้องเปิดใช้สคริปต์ Activate.ps1

## วิธี B: macOS / Linux

ตรวจว่า Python ที่เรียกเป็น 3.12 แล้วใช้:

```bash
git clone https://github.com/Supot77/Bicycle_Rental_Prediction.git
cd Bicycle_Rental_Prediction
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/check_setup.py
.venv/bin/python -m jupyterlab
```

เปิดแอปด้วย `.venv/bin/python -m streamlit run app.py`

## วิธี C: Google Colab

1. เปิด [notebook 00 ใน Colab](https://colab.research.google.com/github/Supot77/Bicycle_Rental_Prediction/blob/main/notebooks/00_orientation.ipynb) แล้วบันทึกสำเนาสำหรับงานตนเอง
2. Notebook 00 ใช้ Python พื้นฐาน ไม่ต้องใช้ dataset หรือ clone ก่อน
3. สำหรับ notebook 01–05 ให้เปิด notebook ที่ต้องการจาก GitHub ผ่าน Colab และเตรียม repository ใน runtime หนึ่งครั้งตามคำสั่งด้านล่าง

```python
from pathlib import Path
import subprocess
import sys

repo = Path('/content/Bicycle_Rental_Prediction')
if not repo.exists():
    subprocess.run(['git', 'clone',
                    'https://github.com/Supot77/Bicycle_Rental_Prediction.git',
                    str(repo)], check=True)
subprocess.run([sys.executable, '-m', 'pip', 'install',
                '-r', str(repo / 'requirements.txt')], check=True)
```

4. เมื่อได้ dataset ให้อัปโหลดไฟล์เข้า `data/raw/` ใน runtime และแก้ config ให้ตรงกัน หาก clone หลังเพื่อนแก้ config แล้ว ให้ตรวจไฟล์อีกครั้ง
5. บันทึกสำเนา notebook และดาวน์โหลดหลักฐานที่จำเป็นก่อนปิด runtime การแก้ใน Colab ไม่ได้อัปเดต GitHub ให้อัตโนมัติ อย่าเขียนทับงานเพื่อนโดยไม่ตรวจความต่าง

ใน Colab ให้ใช้ Python ที่ runtime จัดไว้ บันทึกรุ่นไลบรารีจริง และตรวจความเข้ากันได้เมื่อย้ายโมเดลไป environment แอป หากรุ่นต่างจาก 3.12 ให้ทดสอบโหลดโมเดลใน environment ที่ deploy จริงอีกครั้ง

Colab เป็นเส้นทางทำ notebook ส่วนการเปิดแอปให้ทดสอบในเครื่องหรือ Streamlit Community Cloud ในช่วงงานแอป ไม่ต้องตั้ง tunnel เพิ่มเพื่อเริ่มเรียนรู้

## งานแรกที่ทำได้โดยไม่รอข้อมูล

- อ่าน notebook 00 แล้วลองเปลี่ยนรายการตัวเลขและอธิบายผล
- เลือกงานเตรียมตัวหนึ่งชิ้นจาก WORKBOOK และเพิ่มเจ้าของใน `evidence/task_board.csv`
- ลองแก้คำอธิบายหนึ่งจุดบน branch ของตนแล้วส่งให้เพื่อนตรวจตาม CONTRIBUTING
- เพิ่ม contribution เฉพาะงานที่ได้ทำจริง อย่าใส่ชื่อเพื่อนแทนกัน

## ถ้ารันไม่ผ่าน

| อาการ | สิ่งที่ตรวจ |
| --- | --- |
| หา `py` หรือ `python3.12` ไม่เจอ | ติดตั้ง Python/ตรวจตัวเรียกของระบบก่อนสร้าง venv |
| `ModuleNotFoundError` | ใช้ Python ตัวเดียวกับที่ติดตั้ง requirements; ใน Windows ใช้คำสั่ง `.venv` เต็มตามคู่มือ |
| หา config ไม่เจอใน notebook | เปิดจาก repository หรือใช้ขั้นตอนเตรียม Colab ไม่อัปโหลด notebook เดี่ยวแล้วคาดว่าจะมีไฟล์อื่นครบ |
| ยังไม่ได้กำหนด dataset/target | เป็นสถานะคาดหมายก่อนรับข้อมูล ไม่ต้องสร้างข้อมูลปลอมเพื่อทำให้ผ่าน |
| ภาษาใน CSV อ่านไม่ได้ | ยืนยัน encoding กับไฟล์ต้นฉบับและแก้ config ไม่เปลี่ยนข้อมูลต้นฉบับแบบเดาสุ่ม |
| push ไม่ได้ | ตรวจสิทธิ์ผู้ร่วมงาน หรือใช้ fork + pull request; ไม่ใส่ token ใน notebook |

เมื่อขอความช่วยเหลือ ให้บอกคำสั่ง error และสิ่งที่คาดหวัง โดยไม่แนบข้อมูลที่ห้ามเผยแพร่

เอกสารเครื่องมือ: [Python venv](https://docs.python.org/3/library/venv.html), [Streamlit installation](https://docs.streamlit.io/get-started/installation/command-line)

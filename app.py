import streamlit as st
import re

# --- פונקציית הגנה על פרטיות ---
def anonymize_text(text):
    if not text: return ""
    text = re.sub(r'\d{2,3}-?\d{7}', '[PHONE]', text) # טלפונים
    text = re.sub(r'\b\d{9}\b', '[ID]', text) # תעודות זהות
    return text

# --- הגדרת סיסמה פשוטה ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    
    if st.session_state["password_correct"]:
        return True

    st.subheader("כניסה למערכת התשאול של ד"ר גנמור")
    pwd = st.text_input("נא להזין סיסמה כפי שקיבלתם מהמרפאה:", type="password")
    if st.button("כניסה"):
        if pwd == "Ganmore2026": # כאן אתה קובע את הסיסמה
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("סיסמה שגויה")
    return False

if check_password():
    st.title("תשאול טרום-ביקור - נוירולוגיה קוגניטיבית")
    
    with st.form("main_form"):
        # פרטים טכניים ללא שמות
        job = st.text_input("עיסוק (עבר והווה):")
        edu = st.text_input("שנות לימוד ותארים:")
        
        # אנמנזה
        history = st.text_area("תיאור קצר של סיבת הפנייה (נא להימנע משמות):")
        
        # שאלות ספציפיות מהסגנון שלך
        rbd = st.radio("האם יש תנועות חריגות או צעקות בשינה?", ["לא", "כן", "לא ידוע"])
        hearing = st.radio("מצב שמיעה:", ["תקין", "ירידה - עם מכשיר", "ירידה - ללא מכשיר"])
        
        if st.form_submit_button("הפק סיכום"):
            safe_history = anonymize_text(history)
            st.code(f"עיסוק: {job}\nשנות לימוד: {edu}\nשינה (RBD): {rbd}\nשמיעה: {hearing}\n\nתיאור: {safe_history}")
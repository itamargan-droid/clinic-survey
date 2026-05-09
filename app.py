import streamlit as st

st.set_page_config(page_title="תשאול טרום-ביקור - ד"ר גנמור", layout="centered")

# כותרת הממשק
st.title("מערכת הכנה לביקור נוירולוגי - ד"ר איתמר גנמור")
st.write("אנא מלאו את הפרטים הבאים כדי לסייע לדוקטור להכין את סיכום הביקור בצורה המדויקת ביותר.")

with st.form("patient_form"):
    st.subheader("1. פרטים דמוגרפיים")
    job = st.text_input("עיסוק (בעבר ובהווה):")
    years_of_study = st.text_input("מספר שנות לימוד ופירוט תארים:")
    origin = st.text_input("ארץ לידה ומוצא:")
    dominant_hand = st.selectbox("יד דומיננטית:", ["ימנית", "שמאלית", "אמבידקסטרי"])
    insurance = st.radio("האם קיים ביטוח פרטי עם סעיף תרופות מחוץ לסל?", ["כן", "לא", "לא ידוע"])

    st.subheader("2. רקע רפואי ושינה")
    complaint = st.text_area("מהי התלונה העיקרית ומתי החלה?")
    rbd_symptoms = st.radio("האם יש עדות לצעקות או תנועות חריגות בשינה (RBD)?", ["כן", "לא", "לעתים"])
    hearing = st.radio("האם יש ירידה בשמיעה?", ["לא", "כן - ללא מכשיר", "כן - נעזר במכשיר שמיעה"])
    
    st.subheader("3. תפקוד ובטיחות")
    driving = st.radio("האם המטופל/ת נוהג/ת כיום?", ["כן", "לא", "הפסיק/ה לאחרונה"])
    falls = st.radio("האם היו נפילות בתקופה האחרונה?", ["לא", "כן"])
    urinary = st.radio("האם יש הפרעה בשליטה על סוגרים?", ["לא", "דחיפות", "אי-שליטה מלאה"])

    submitted = st.form_submit_button("הפק סיכום גולמי לרופא")

if submitted:
    st.success("הנתונים עובדו בהצלחה. להלן הטיוטה לסיכום:")
    
    # יצירת הטקסט הערוך להעתקה
    summary_text = f"""
    ### טיוטה לסיכום ביקור (מבוסס תשאול מוקדם):
    
    **פרטים אישיים:**
    עיסוק: {job}
    שנות לימוד: {years_of_study}
    מוצא: {origin}
    דומיננטיות: {dominant_hand}
    ביטוח פרטי: {insurance}
    
    **אנמנזה גולמית:**
    תלונה עיקרית: {complaint}
    הפרעת שינה (RBD): {rbd_symptoms}
    שמיעה: {hearing}
    
    **תפקוד ובטיחות:**
    נהיגה: {driving}
    נפילות: {falls}
    סוגרים: {urinary}
    """
    
    st.text_area("העתק מכאן:", value=summary_text, height=400)
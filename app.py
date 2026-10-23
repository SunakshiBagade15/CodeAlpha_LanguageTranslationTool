import streamlit as st
import requests
import html
from code_editor import code_editor

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Anuvaad Setu",
    page_icon="🌐",
    layout="wide"
)

# ---------------- LANGUAGES ----------------
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Gujarati": "gu",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja"
}

# ---------------- SESSION STATE ----------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "last_request" not in st.session_state:
    st.session_state.last_request = None

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #e5f4ff 0%, transparent 28%),
        radial-gradient(circle at 90% 20%, #eee7ff 0%, transparent 30%),
        linear-gradient(180deg, #f8fcff 0%, #ffffff 55%, #f8f7ff 100%);
}

.block-container {
    max-width: 1200px;
    padding-top: 50px;
}

.logo {
    font-size: 30px;
    font-weight: 800;
    color: #20266f;
}

.tagline {
    color: #7b84a3;
    font-size: 13px;
    margin-left: 42px;
}

.hero {
    text-align: center;
    padding: 35px 10px 30px;
}

.hero h1 {
    color: #20266f;
    font-size: 44px;
    font-weight: 800;
}

.hero p {
    color: #7b84a3;
}

.section-title {
    font-size: 17px;
    font-weight: 600;
    color: #333b67;
    margin-bottom: 10px;
}

div[data-testid="stTextArea"] textarea {
    border-radius: 14px;
    border: 1px solid #dce3f3;
}

div[data-testid="stTextInput"] input {
    border-radius: 14px;
    border: 1px solid #dce3f3;
    padding: 14px;
}

.feature {
    background: white;
    border: 1px solid #e3e8f5;
    border-radius: 18px;
    padding: 25px 15px;
    text-align: center;
    min-height: 140px;
    box-shadow: 0 8px 25px rgba(50,70,130,0.06);
}

.feature-icon {
    font-size: 28px;
}

.feature-title {
    font-weight: 700;
    color: #252d68;
    margin-top: 8px;
}

.feature-text {
    font-size: 12px;
    color: #7b84a3;
    margin-top: 5px;
}

.footer {
    text-align: center;
    color: #7b84a3;
    margin-top: 45px;
    padding-bottom: 20px;
}

.footer strong {
    color: #6957dd;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="logo">🌐 Anuvaad Setu</div>
<div class="tagline">Break language barriers, understand the world</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Translate Anything.</h1>
    <p>Your Language Bridge, Wherever You Go.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- LANGUAGE SELECTION ----------------
def swap_languages():
    st.session_state.source_lang, st.session_state.target_lang = (
        st.session_state.target_lang,
        st.session_state.source_lang
    )
col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    source_language = st.selectbox(
        "From",
        list(language_codes.keys()),
        index=0,
        key="source_lang"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button(
        "🔄",
        help="Swap languages",
        on_click=swap_languages,
        use_container_width=True
    )

with col3:
    target_language = st.selectbox(
        "To",
        list(language_codes.keys()),
        index=2,
        key="target_lang"
    )

# ---------------- INPUT ----------------
st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="small")

with left:
    st.markdown("**Your Text**")

    response = code_editor(
        "",
        lang="text",
        height=220,
        key="translation_input_box",
        options={
            "wrap": True,
            "showLineNumbers": False,
            "showGutter": False,
            "highlightActiveLine": False,
            "fontSize": 15,
            "minLines": 8,
            "maxLines": 12
        },
        response_mode="debounce"
    )

    text = response.get("text", "")

    
    st.caption(f"{len(text)} / 5000 characters")

# ---------------- AUTOMATIC TRANSLATION ----------------
request_key = (
    text,
    source_language,
    target_language
)

if request_key != st.session_state.last_request:
    st.session_state.last_request = request_key

    if not text.strip():
        st.session_state.translated_text = ""

    elif len(text) > 5000:
        st.session_state.translated_text = ""
        st.warning("Please enter fewer than 5000 characters.")

    elif source_language == target_language:
        st.session_state.translated_text = text

    else:
        try:
            with st.spinner("Translating..."):
                response = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={
                        "q": text,
                        "langpair": (
                            f"{language_codes[source_language]}|"
                            f"{language_codes[target_language]}"
                        )
                    },
                    timeout=15
                )

                response.raise_for_status()
                data = response.json()

                if data.get("responseStatus") != 200:
                    raise ValueError(
                        data.get("responseDetails", "Translation failed")
                    )

                translated_text = data["responseData"]["translatedText"]

                st.session_state.translated_text = html.unescape(
                    translated_text
                )

        except Exception as e:
            st.session_state.translated_text = ""
            st.error(f"Translation failed: {e}")

# ---------------- OUTPUT ----------------
with right:
    st.markdown("**Translation**")

    if st.session_state.translated_text:
        st.code(
            st.session_state.translated_text,
            language=None,
            height=220
        )
    else:
        st.code(
            "Your translated text will appear here...",
            language=None,
            height=220
        )
        
# ---------------- FEATURES ----------------
st.markdown("<br><br>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Text Translation</div>
        <div class="feature-text">
            Translate text automatically.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🌐</div>
        <div class="feature-title">Multiple Languages</div>
        <div class="feature-text">
            Connect across languages and cultures.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Automatic Translation</div>
        <div class="feature-text">
            Translate without clicking a button.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Different Languages • <strong>Same Meaning</strong>
</div>
""", unsafe_allow_html=True)
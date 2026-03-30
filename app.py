import streamlit as st
import requests

# ── Page Config ──
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🎯", layout="centered")

# ── Custom CSS ──
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        background: #f0f4f8;
        font-family: 'Inter', sans-serif;
    }

    /* Top banner */
    .top-banner {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }

    .top-banner h1 {
        color: #ffffff;
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .top-banner p {
        color: #a0aec0;
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
    }

    .top-banner .badge {
        display: inline-block;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        color: #fff;
        border-radius: 20px;
        padding: 0.2rem 0.8rem;
        font-size: 0.75rem;
        margin-top: 0.8rem;
        letter-spacing: 1px;
    }

    /* Feature cards */
    .feature-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border-top: 3px solid #4361ee;
        transition: transform 0.2s;
    }

    .feature-card .icon { font-size: 1.6rem; }
    .feature-card .title {
        color: #1a1a2e;
        font-weight: 700;
        font-size: 0.9rem;
        margin-top: 0.4rem;
    }
    .feature-card .desc { color: #718096; font-size: 0.78rem; }

    /* Input section */
    .input-section {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin-top: 1.5rem;
    }

    .section-label {
        color: #1a1a2e;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f0f4f8;
    }

    /* Score card */
    .score-card {
        background: linear-gradient(135deg, #1a1a2e, #0f3460);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        margin: 1.5rem 0;
    }

    .score-label {
        color: #a0aec0;
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .score-number {
        font-size: 4rem;
        font-weight: 800;
        line-height: 1.1;
    }

    .score-tag {
        display: inline-block;
        border-radius: 20px;
        padding: 0.3rem 1rem;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    /* Result cards */
    .result-card {
        background: #ffffff;
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #2d3748;
        font-size: 0.88rem;
        line-height: 1.5;
        border-left: 4px solid #4361ee;
    }

    .result-card-red { border-left-color: #e53e3e; }
    .result-card-green { border-left-color: #38a169; }
    .result-card-yellow { border-left-color: #d69e2e; }

    /* Section headers */
    .results-header {
        color: #1a1a2e;
        font-size: 1rem;
        font-weight: 700;
        margin: 1.2rem 0 0.5rem 0;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4361ee, #3a0ca3);
        color: white;
        font-weight: 700;
        font-size: 1rem;
        border: none;
        border-radius: 10px;
        padding: 0.75rem;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 15px rgba(67,97,238,0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #3a0ca3, #4361ee);
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: #f8fafc !important;
        color: #1a1a2e !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-size: 0.9rem !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #a0aec0;
        font-size: 0.78rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #f8fafc !important;
        border: 2px dashed #4361ee !important;
        border-radius: 10px !important;
    }

    /* Radio */
    .stRadio > label {
        color: #1a1a2e !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Top Banner ──
st.markdown("""
<div class="top-banner">
    <h1>🎯 AI Resume Analyzer</h1>
    <p>Match your resume to any job posting instantly with AI</p>
    <div class="badge">⚡ POWERED BY GPT-3.5</div>
</div>
""", unsafe_allow_html=True)

# ── Feature Cards ──
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">📄</div>
        <div class="title">PDF Resume</div>
        <div class="desc">Upload any PDF resume</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">🔍</div>
        <div class="title">Job Analysis</div>
        <div class="desc">URL or paste description</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="icon">🤖</div>
        <div class="title">AI Insights</div>
        <div class="desc">Match score + suggestions</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="section-label">📋 Analyze Your Resume</div>', unsafe_allow_html=True)

# ── Radio OUTSIDE form so it updates UI instantly ──
input_method = st.radio(
    "How would you like to provide the job description?",
    ["🔗 Paste Job URL", "📋 Paste Job Description Text"],
    horizontal=True
)

with st.form(key="analyze_form"):
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF only)",
        type=["pdf"]
    )
    if uploaded_file:
        st.success(f"✅ {uploaded_file.name} ready for analysis!")

    st.markdown("<br>", unsafe_allow_html=True)

    job_url = ""
    job_text_input = ""

    if input_method == "🔗 Paste Job URL":
        job_url = st.text_input(
            "Job Posting URL",
            placeholder="https://www.indeed.com/viewjob?jk=...",
        )
        st.caption("⚠️ Works best with Indeed, Glassdoor. LinkedIn requires login.")
    else:
        job_text_input = st.text_area(
            "Paste Job Description Here",
            placeholder="Copy and paste the full job description text here...",
            height=200
        )

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🚀 Analyze My Resume")

# ── Results ──
if submitted:
    if not uploaded_file:
        st.warning("⚠️ Please upload your resume PDF!")
    elif not job_url and not job_text_input:
        st.warning("⚠️ Please provide a job URL or paste the job description!")
    else:
        with st.spinner("🤖 AI is analyzing your resume against the job posting..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}

            if input_method == "📋 Paste Job Description Text":
                data = {"job_url": "", "job_text_override": job_text_input}
            else:
                data = {"job_url": job_url, "job_text_override": ""}

            response = requests.post(
                "https://web-production-48a5b.up.railway.app/full-analyze",
                files=files,
                data=data
            )
            result = response.json()

        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        elif "analysis" not in result:
            st.error(f"❌ Unexpected response from backend:")
            st.json(result)  # shows exactly what backend returned
        else:
            analysis = result["analysis"]

            # ── Score Card ──
            color = "#68d391" if score >= 70 else "#f6ad55" if score >= 50 else "#fc8181"
            label = "Strong Match 🎉" if score >= 70 else "Moderate Match 👍" if score >= 50 else "Needs Work 💪"
            bg = "#276749" if score >= 70 else "#7b341e" if score >= 50 else "#742a2a"

            st.markdown(f"""
            <div class="score-card">
                <div class="score-label">Match Score</div>
                <div class="score-number" style="color:{color}">{score}%</div>
                <div class="score-tag" style="background:{bg}; color:{color}">{label}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── Results Grid ──
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="results-header">✅ Your Strengths</div>',
                           unsafe_allow_html=True)
                for s in analysis["strengths"]:
                    st.markdown(f'<div class="result-card result-card-green">✅ {s}</div>',
                               unsafe_allow_html=True)

                st.markdown('<div class="results-header">❌ Missing Skills</div>',
                           unsafe_allow_html=True)
                for s in analysis["missing_skills"]:
                    st.markdown(f'<div class="result-card result-card-red">❌ {s}</div>',
                               unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="results-header">💡 Suggestions</div>',
                           unsafe_allow_html=True)
                for s in analysis["suggestions"]:
                    st.markdown(f'<div class="result-card result-card-yellow">💡 {s}</div>',
                               unsafe_allow_html=True)

            # ── Summary ──
            st.markdown('<div class="results-header">📋 Overall Summary</div>',
                       unsafe_allow_html=True)
            st.markdown(f'<div class="result-card result-card-green" style="font-size:0.92rem; line-height:1.7">{analysis["summary"]}</div>',
                       unsafe_allow_html=True)

            # ── Footer ──
            st.markdown(f"""
            <div class="footer">
                📄 {result['filename']} · {result['resume_pages']} pages · 
                Powered by GPT-3.5 · AI Resume Analyzer
            </div>
            """, unsafe_allow_html=True)
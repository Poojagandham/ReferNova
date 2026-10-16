
import streamlit as st
from datetime import datetime

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="ReferNova | Career Outreach AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =====================================================
# 2. CUSTOM DESIGN
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #0b1020;
    color: #f4f6ff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: #0b1020;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.brand {
    font-size: 2rem;
    font-weight: 800;
    line-height: 1.5;
    letter-spacing: -1px;
    color: #ffffff;
    margin: 0;
}

.brand-accent {
    color: #a78bfa;
}

.tagline {
    color: #c4b5fd;
    text-align: right;
    padding-top: 15px;
    font-size: 0.88rem;
}

.hero-box {
    background: linear-gradient(125deg, #171d3a, #11172d 60%, #241744);
    border: 1px solid #30365b;
    border-radius: 22px;
    padding: 36px;
    margin-top: 18px;
    margin-bottom: 26px;
}

.eyebrow {
    color: #c4b5fd;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-title {
    color: #ffffff;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1.2;
    margin-top: 16px;
    margin-bottom: 16px;
}

.hero-description {
    color: #c1c9e0;
    font-size: 1rem;
    line-height: 1.8;
}

.feature-card {
    background: #121a30;
    border: 1px solid #293653;
    border-radius: 15px;
    padding: 18px;
    min-height: 150px;
}

.feature-icon {
    font-size: 1.5rem;
    margin-bottom: 8px;
}

.feature-title {
    color: #ffffff;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.feature-description {
    color: #aab6d3;
    font-size: 0.84rem;
    line-height: 1.65;
}

.section-heading {
    font-size: 1.45rem;
    font-weight: 800;
    color: #ffffff;
    margin-top: 12px;
    margin-bottom: 5px;
}

.muted {
    color: #aab6d3;
    font-size: 0.9rem;
    line-height: 1.7;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #7c3aed, #6366f1);
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    color: white;
    border: 1px solid #c4b5fd;
    background: #6d28d9;
}

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background: #0c1326;
    color: #f4f6ff;
    border: 1px solid #33415f;
    border-radius: 10px;
}

div[data-testid="stFileUploader"] {
    background: #0c1326;
    border: 1px dashed #6475a0;
    border-radius: 12px;
    padding: 12px;
}

div[data-testid="stExpander"] {
    border: 1px solid #293653;
    border-radius: 12px;
    background: #11182b;
}

label {
    color: #dbe2f5 !important;
}

hr {
    border-color: #293653;
}

@media (max-width: 700px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    .hero-box {
        padding: 22px;
    }

    .brand {
        font-size: 1.6rem;
    }

    .tagline {
        font-size: 0.75rem;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. HEADER
# =====================================================
header_left, header_right = st.columns([3, 1])

with header_left:
    st.markdown(
        '<div class="brand">🚀 Refer<span class="brand-accent">Nova</span></div>',
        unsafe_allow_html=True,
    )

with header_right:
    st.markdown(
        '<div class="tagline">✦ Your career copilot</div>',
        unsafe_allow_html=True,
    )


# =====================================================
# 4. HERO SECTION
# =====================================================
st.markdown("""
<div class="hero-box">
    <div class="eyebrow">AI-POWERED CAREER OUTREACH</div>
    <div class="hero-title">
        Make your next career move<br>with confidence.
    </div>
    <div class="hero-description">
        Turn your resume and a job description into personalized outreach.
        Prepare referral requests, cold emails, and tailored cover letters
        from one simple workspace.
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# 5. FEATURE CARDS
# =====================================================
features = [
    (
        "📄",
        "Resume-aware",
        "Upload your resume PDF to provide context for your application.",
    ),
    (
        "✉️",
        "Cold emails",
        "Prepare a professional introduction for recruiters and hiring teams.",
    ),
    (
        "🤝",
        "Referral requests",
        "Draft a concise LinkedIn referral message.",
    ),
    (
        "📝",
        "Cover letters",
        "Create a role-focused cover letter draft.",
    ),
]

feature_columns = st.columns(4)

for column, feature in zip(feature_columns, features):
    with column:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature[0]}</div>
            <div class="feature-title">{feature[1]}</div>
            <div class="feature-description">{feature[2]}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")


# =====================================================
# 6. FORM INTRODUCTION
# =====================================================
st.markdown(
    '<div class="section-heading">Build your outreach</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="muted">'
    'Add your resume and target role details to prepare your drafts.'
    '</div>',
    unsafe_allow_html=True,
)

st.write("")


# =====================================================
# 7. INPUT FORM
# =====================================================
left, right = st.columns([0.95, 1.05], gap="large")

with left:
    st.subheader("01 · Your resume")

    resume = st.file_uploader(
        "Upload your resume (PDF) *",
        type=["pdf"],
        help="Choose your resume in PDF format.",
    )

    if resume is not None:
        st.success(f"Selected: {resume.name}")
        st.caption(f"File size: {resume.size / 1024:.1f} KB")

    st.divider()
    st.subheader("02 · Target role")

    full_name = st.text_input(
        "Your name *",
        placeholder="e.g. Priya Sharma",
    )

    target_role = st.text_input(
        "Target job title *",
        placeholder="e.g. Python Developer Intern",
    )

    company = st.text_input(
        "Company name *",
        placeholder="e.g. Example Technologies",
    )

    recipient = st.text_input(
        "Recipient name (optional)",
        placeholder="e.g. Hiring Manager",
    )


with right:
    st.subheader("03 · Job description")

    job_description = st.text_area(
        "Paste the complete job description *",
        placeholder=(
            "Paste the job responsibilities, required skills, "
            "qualifications, and other details here..."
        ),
        height=280,
    )

    st.divider()
    st.subheader("04 · Customize your draft")

    output_type = st.selectbox(
        "Choose content type",
        [
            "LinkedIn Referral Request",
            "Cold Email",
            "Cover Letter",
            "Generate All Three",
        ],
    )

    tone = st.selectbox(
        "Writing tone",
        [
            "Professional",
            "Friendly and conversational",
            "Confident and concise",
        ],
    )

    extra_details = st.text_area(
        "Additional details (optional)",
        placeholder=(
            "Add your relevant projects, achievements, "
            "or reasons for applying."
        ),
        height=100,
    )


# =====================================================
# 8. DRAFT GENERATION FUNCTIONS
# =====================================================
def make_referral(name, role, company_name, recipient_name, skills, extra):
    greeting = f"Hi {recipient_name}," if recipient_name else "Hi,"

    return f"""Subject: Referral Request for {role} at {company_name}

{greeting}

I hope you're doing well. My name is {name}, and I'm interested in the {role} opportunity at {company_name}.

My interests align with the role's focus on {skills}. I am eager to contribute to the team and continue growing professionally.

Would you be comfortable sharing some advice about the opportunity or considering a referral if you feel my profile is a good fit?

{extra}

Thank you for your time and consideration.

Best regards,
{name}"""


def make_email(name, role, company_name, recipient_name, skills, extra):
    greeting = (
        f"Dear {recipient_name},"
        if recipient_name
        else "Dear Hiring Team,"
    )

    return f"""Subject: Application Interest — {role} at {company_name}

{greeting}

My name is {name}, and I am writing to express my interest in the {role} opportunity at {company_name}.

I am interested in this role because of its focus on {skills}. I am motivated to apply my knowledge, contribute to practical projects, and continue developing my skills.

{extra}

I would appreciate the opportunity to discuss how my background may align with your team's needs.

Thank you for your time and consideration.

Best regards,
{name}"""


def make_cover_letter(name, role, company_name, recipient_name, skills, extra):
    greeting = (
        f"Dear {recipient_name},"
        if recipient_name
        else "Dear Hiring Team,"
    )

    return f"""Subject: Application for {role} at {company_name}

{greeting}

I am writing to express my interest in the {role} position at {company_name}.

I am enthusiastic about software development and eager to apply my knowledge in a professional environment. This opportunity interests me because it involves {skills}, an area I am keen to develop further.

{extra}

I would welcome the opportunity to discuss my interests and qualifications.

Thank you for considering my application.

Sincerely,
{name}"""


# =====================================================
# 9. GENERATE BUTTON
# =====================================================
st.write("")

button_col, info_col = st.columns([1, 2], vertical_alignment="center")

with button_col:
    generate_clicked = st.button(
        "✨ Generate outreach",
        use_container_width=True,
    )

with info_col:
    st.markdown(
        '<div class="muted">'
        'Complete the required fields before generating your drafts.'
        '</div>',
        unsafe_allow_html=True,
    )


# =====================================================
# 10. VALIDATION AND DRAFT CREATION
# =====================================================
if generate_clicked:
    missing_fields = []

    if resume is None:
        missing_fields.append("Upload your resume PDF.")

    if not full_name.strip():
        missing_fields.append("Enter your name.")

    if not target_role.strip():
        missing_fields.append("Enter the target job title.")

    if not company.strip():
        missing_fields.append("Enter the company name.")

    if not job_description.strip():
        missing_fields.append("Paste the job description.")

    if missing_fields:
        st.error("Please complete these required fields:")

        for field in missing_fields:
            st.write(f"- {field}")

    else:
        skill_list = [
            "Python",
            "SQL",
            "Django",
            "Flask",
            "Streamlit",
            "Java",
            "JavaScript",
            "React",
            "REST APIs",
            "Git",
            "GitHub",
            "Data Structures and Algorithms",
            "Machine Learning",
            "AWS",
            "PostgreSQL",
            "MySQL",
        ]

        jd_lower = job_description.lower()

        detected_skills = [
            skill
            for skill in skill_list
            if skill.lower() in jd_lower
        ]

        skills = (
            ", ".join(detected_skills[:5])
            if detected_skills
            else target_role
        )

        extra = extra_details.strip()

        if not extra:
            extra = (
                "I am motivated to learn, collaborate with the team, "
                "and contribute to practical solutions."
            )

        drafts = {
            "LinkedIn Referral Request": make_referral(
                full_name,
                target_role,
                company,
                recipient,
                skills,
                extra,
            ),
            "Cold Email": make_email(
                full_name,
                target_role,
                company,
                recipient,
                skills,
                extra,
            ),
            "Cover Letter": make_cover_letter(
                full_name,
                target_role,
                company,
                recipient,
                skills,
                extra,
            ),
        }

        if output_type == "Generate All Three":
            selected_drafts = drafts
        else:
            selected_drafts = {
                output_type: drafts[output_type]
            }

        st.session_state["refernova_drafts"] = selected_drafts
        st.session_state["refernova_created_at"] = (
            datetime.now().strftime("%d %b %Y, %I:%M %p")
        )


# =====================================================
# 11. GENERATED OUTPUTS
# =====================================================
if st.session_state.get("refernova_drafts"):
    st.divider()

    st.markdown(
        '<div class="section-heading">Your outreach drafts</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="muted">'
        'Review and edit each draft before sending it.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Current version: drafts use templates and job-description "
        "keyword matching. Resume text extraction and real AI generation "
        "are not connected yet."
    )

    for index, (draft_title, draft_text) in enumerate(
        st.session_state["refernova_drafts"].items()
    ):
        with st.expander(f"✦ {draft_title}", expanded=True):
            edited_draft = st.text_area(
                "Edit your draft",
                value=draft_text,
                height=280,
                key=f"refernova_editor_{index}",
            )

            st.download_button(
                "⬇ Download draft",
                data=edited_draft,
                file_name=f"refernova_draft_{index + 1}.txt",
                mime="text/plain",
                key=f"refernova_download_{index}",
            )

    st.caption(
        "Created: "
        + st.session_state.get("refernova_created_at", "")
    )


# =====================================================
# 12. FOOTER
# =====================================================
st.write("")
st.divider()

footer_left, footer_right = st.columns(2)

with footer_left:
    st.caption("🚀 ReferNova · Your next opportunity starts here.")

with footer_right:
    st.markdown(
        '<div style="text-align:right; color:#9ca9c8; font-size:0.8rem;">'
        'Review all details for accuracy before sending.'
        '</div>',
        unsafe_allow_html=True,
    )

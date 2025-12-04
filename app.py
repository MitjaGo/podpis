import streamlit as st

st.set_page_config(page_title="Email Signature Builder", layout="wide")

st.title("📧 Company Email Signature Generator")
st.write("Fill in your details and copy the final signature into Outlook.")

# ==========================================================
# STEP 1 - PERSONAL DATA
# ==========================================================
st.header("Step 1: Personal Data")

col1, col2 = st.columns(2)

with col1:
    full_name = st.text_input("Full Name")
    job_title = st.text_input("Job Title")
    phone = st.text_input("Phone")
    email = st.text_input("Email")

with col2:
    st.info("👉 All fields required")

if not all([full_name, job_title, phone, email]):
    st.warning("Please complete all personal data fields to continue.")
    st.stop()


# ==========================================================
# STEP 2 - COMPANY DATA
# ==========================================================
st.header("Step 2: Company Data")

company_name = st.text_input("Company Name", "Adria d.o.o.")
company_address = st.text_input("Address", "Ankaranska cesta 25, 6000 Koper")
website = st.text_input("Website", "www.adria-ankaran.si")


# ==========================================================
# STEP 3 - GRAPHICS
# ==========================================================
st.header("Step 3: Graphics")

col1, col2 = st.columns(2)

with col1:
    logo_url = st.text_input(
        "Company Logo URL",
        "https://www.adria-ankaran.si/wp-content/uploads/2020/01/cropped-Logo-Adria-Ankaran.png"
    )

    banner_url = st.text_input(
        "Banner Image URL (Optional)",
        ""
    )

with col2:
    show_logo = st.checkbox("Show Logo", value=True)
    show_banner = st.checkbox("Show Banner", value=False)

# ==========================================================
# STEP 4 - SOCIAL MEDIA
# ==========================================================
st.header("Step 4: Social Media")

col1, col2, col3 = st.columns(3)

with col1:
    facebook = st.text_input("Facebook link")

with col2:
    instagram = st.text_input("Instagram link")

with col3:
    youtube = st.text_input("YouTube link")


# ==========================================================
# STEP 5 - STYLE
# ==========================================================
st.header("Step 5: Style")

col1, col2, col3 = st.columns(3)

with col1:
    primary_color = st.color_picker("Primary Color", "#1f6db5")

with col2:
    text_color = st.color_picker("Text Color", "#000000")

with col3:
    font_size = st.slider("Font Size", 10, 22, 14)


# ==========================================================
# DISCLAIMER
# ==========================================================
st.header("Disclaimer")

disclaimer = st.text_area(
    "Disclaimer text",
    "The content of this email is confidential and intended only for the person to whom it is addressed..."
)


# ==========================================================
# SOCIAL LINKS HTML
# ==========================================================
social_html = ""

if facebook:
    social_html += f'<a href="{facebook}" style="margin-right:15px;">Facebook</a>'

if instagram:
    social_html += f'<a href="{instagram}" style="margin-right:15px;">Instagram</a>'

if youtube:
    social_html += f'<a href="{youtube}" style="margin-right:15px;">YouTube</a>'


# ==========================================================
# FINAL SIGNATURE HTML
# ==========================================================
signature_html = f"""
<table style="font-family: Arial; color:{text_color}; font-size:{font_size}px; line-height:1.5;">
<tr>
<td>

{"<img src='" + logo_url + "' width='180'><br><br>" if show_logo and logo_url else ""}

{"<img src='" + banner_url + "' width='600'><br><br>" if show_banner and banner_url else ""}

<strong style="color:{primary_color}; font-size:{font_size + 6}px;">{full_name}</strong><br>
<span style="color:{primary_color};">{job_title}</span>
<br><br>

<strong>{company_name}</strong><br>
{company_address}<br><br>

📞 {phone}<br>
✉️ <a href="mailto:{email}">{email}</a><br>
🌍 <a href="https://{website}">{website}</a><br><br>

{social_html}

<br><br>
<span style="font-size:{font_size - 2}px; color: gray;">
{disclaimer}
</span>

</td>
</tr>
</table>
"""


# ==========================================================
# PREVIEW
# ==========================================================
st.header("✅ Signature Preview")
st.markdown(signature_html, unsafe_allow_html=True)


# ==========================================================
# COPY / EXPORT
# ==========================================================
st.header("📋 Copy your signature")

st.code(signature_html, language="html")

st.download_button(
    "Download signature as HTML",
    signature_html,
    file_name="email_signature.html",
    mime="text/html"
)


# ==========================================================
# OUTLOOK INSTRUCTIONS
# ==========================================================
st.header("📧 How to add this to Outlook")

st.success("""
1. Select and COPY the signature above (Ctrl + C / Cmd + C)
2. Open Outlook
3. Go to:
   File → Options → Mail → Signatures
4. Click "New"
5. Give it a name
6. Paste (Ctrl + V / Cmd + V) into the signature field
7. Save and select it as default
""")

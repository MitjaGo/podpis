import streamlit as st

st.set_page_config(page_title="Email Signature Builder", layout="wide")

st.title("📧 Company Email Signature Generator")
st.write("Enter your personal details. Company branding is applied automatically.")

# ==========================================================
# STEP 1 - PERSONAL DATA (REQUIRED)
# ==========================================================
st.header("Step 1: Personal Data")

col1, col2 = st.columns(2)

with col1:
    full_name = st.text_input("Full Name (Name and Surname)")
    phone = st.text_input("Phone")

with col2:
    email = st.text_input("Company Email (must be @adria-ankaran.si)")

# ✅ Job title dropdown instead of free typing
st.header("Step 2: Job Title")

job_title = st.selectbox(
    "Select your job title",
    [
        "",
        "Reception",
        "Sales Manager",
        "Marketing Manager",
        "Revenue Manager",
        "Finance",
        "Operations",
        "Human Resources",
        "Maintenance",
        "Hotel Manager",
        "Restaurant Manager",
        "Other"
    ]
)

# ==========================================================
# ✅ VALIDATION
# ==========================================================

if not all([full_name, phone, email, job_title]):
    st.warning("Please complete all fields to continue.")
    st.stop()

# ✅ Name must contain name + surname
if len(full_name.strip().split(" ")) < 2:
    st.error("Please enter both Name and Surname (example: John Smith)")
    st.stop()

# ✅ Email must be company domain
if not email.endswith("@adria-ankaran.si"):
    st.error("Email must end with @adria-ankaran.si")
    st.stop()


# ==========================================================
# HIDDEN - COMPANY DATA (LOCKED)
# ==========================================================

company_name = "Adria d.o.o."
company_address = "Ankaranska cesta 25, 6000 Koper"
website = "www.adria-ankaran.si"


# ==========================================================
# HIDDEN - GRAPHICS (LOCKED)
# ==========================================================

logo_url = "https://scontent.flju1-1.fna.fbcdn.net/v/t39.30808-1/538848259_1373858921407395_3734947029332493437_n.jpg?stp=c221.221.1034.1034a_dst-jpg_s480x480_tt6&_nc_cat=110&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=rQqWdd-dIjEQ7kNvwGGaLrC&_nc_oc=Adm5HbeGQAg7iOscjyRg4I_1-DxOGT_-XpFenV9BrcqAPUvq7LR4yQcvmFpyQ3Ny-0Q&_nc_zt=24&_nc_ht=scontent.flju1-1.fna&_nc_gid=K1yl1X6bMzrQwCCL6mUTUQ&oh=00_Afk80MzUfBMbBeR-pnpyRce_Xn8JyLoI8HJzvZgoDi6KAw&oe=69378E63"

show_logo = True


# ==========================================================
# HIDDEN - SOCIAL MEDIA (LOCKED)
# ==========================================================

facebook = "https://www.facebook.com/adriaankaran"
instagram = "https://www.instagram.com/adria_ankaran"
youtube = "https://www.youtube.com"


# ==========================================================
# HIDDEN - STYLE (LOCKED)
# ==========================================================

primary_color = "#1f6db5"
text_color = "#000000"
font_size = 14   # Between 10–22 but locked here


# ==========================================================
# DISCLAIMER (LOCKED)
# ==========================================================

disclaimer = """
The content of this email is confidential and intended only for the person to whom it is addressed.
If you received this email in error, please inform the sender and delete it.
"""


# ==========================================================
# SOCIAL HTML
# ==========================================================

social_html = f"""
<a href="{facebook}" style="margin-right:15px;">Facebook</a>
<a href="{instagram}" style="margin-right:15px;">Instagram</a>
<a href="{youtube}">YouTube</a>
"""


# ==========================================================
# FINAL SIGNATURE HTML
# ==========================================================

signature_html = f"""
<table style="font-family: Arial; color:{text_color}; font-size:{font_size}px; line-height:1.5;">
<tr>
<td>

{'<img src="' + logo_url + '" width="180"><br><br>' if show_logo else ''}

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

st.header("✅ Live Signature Preview")
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

st.header("📧 Add this signature to Outlook")

st.success("""
1. Select and COPY the signature above (Ctrl + C / Cmd + C)
2. Open Outlook
3. Go to File → Options → Mail → Signatures
4. Click “New” and name it
5. Paste the signature
6. Save and set it as default
✅ Done
""")



import streamlit as st

st.set_page_config(page_title="Email Signature Builder", layout="wide")

st.title("📧 Company Email Signature Generator")
st.write("Fill in your details and copy the final signature into Outlook. Company branding is locked.")

# ==========================================================
# STEP 1 - PERSONAL DATA (REQUIRED)
# ==========================================================
st.header("Step 1: Personal Data")

col1, col2 = st.columns(2)

with col1:
    full_name = st.text_input("Full Name (Name and Surname)")
    job_title = st.text_input("Job Title")
    phone = st.text_input("Phone")
    email = st.text_input("Email")

with col2:
    st.info("👉 All fields are required")

# Validate fields
if not all([full_name, job_title, phone, email]):
    st.warning("Please complete all fields to continue.")
    st.stop()

# Make sure name + surname are entered
if len(full_name.strip().split(" ")) < 2:
    st.error("Please enter both Name and Surname (example: John Smith)")
    st.stop()


# ==========================================================
# STEP 2 - COMPANY DATA (LOCKED)
# ==========================================================
st.header("Step 2: Company Data")

company_name = "Adria d.o.o."
company_address = "Ankaranska cesta 25, 6000 Koper"
website = "www.adria-ankaran.si"

st.text(f"Company Name: {company_name}")
st.text(f"Address: {company_address}")
st.text(f"Website: {website}")

st.info("✅ Company information is locked")


# ==========================================================
# STEP 3 - GRAPHICS (LOCKED)
# ==========================================================
st.header("Step 3: Graphics")

# Default company logo (locked)
logo_url = "https://scontent.flju1-1.fna.fbcdn.net/v/t39.30808-1/538848259_1373858921407395_3734947029332493437_n.jpg?stp=c221.221.1034.1034a_dst-jpg_s480x480_tt6&_nc_cat=110&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=rQqWdd-dIjEQ7kNvwGGaLrC&_nc_oc=Adm5HbeGQAg7iOscjyRg4I_1-DxOGT_-XpFenV9BrcqAPUvq7LR4yQcvmFpyQ3Ny-0Q&_nc_zt=24&_nc_ht=scontent.flju1-1.fna&_nc_gid=K1yl1X6bMzrQwCCL6mUTUQ&oh=00_Afk80MzUfBMbBeR-pnpyRce_Xn8JyLoI8HJzvZgoDi6KAw&oe=69378E63"

show_logo = st.checkbox("Show Company Logo", value=True)

st.image(logo_url, width=180)
st.info("✅ Company logo is locked")


# ==========================================================
# STEP 4 - SOCIAL MEDIA (LOCKED)
# ==========================================================
st.header("Step 4: Social Media")

facebook = "https://www.facebook.com/adriaankaran"
instagram = "https://www.instagram.com/adria_ankaran"
youtube = "https://www.youtube.com"

col1, col2, col3 = st.columns(3)

with col1:
    st.text("Facebook")
    st.caption(facebook)

with col2:
    st.text("Instagram")
    st.caption(instagram)

with col3:
    st.text("YouTube")
    st.caption(youtube)

st.info("✅ Social media links are locked")


# ==========================================================
# STEP 5 - STYLE (LOCKED)
# ==========================================================
st.header("Step 5: Style")

primary_color = "#1f6db5"
text_color = "#000000"
font_size = 14   # Must remain between 10–22 (locked at 14)

col1, col2, col3 = st.columns(3)

with col1:
    st.text("Primary Color")
    st.color_picker("", primary_color, disabled=True)

with col2:
    st.text("Text Color")
    st.color_picker("", text_color, disabled=True)

with col3:
    st.text("Font Size (10 – 22)")
    st.slider("", 10, 22, font_size, disabled=True)

st.info("✅ Style is locked based on company branding")


# ==========================================================
# DISCLAIMER (LOCKED)
# ==========================================================
st.header("Disclaimer")

disclaimer = """
The content of this email is confidential and intended only for the person to whom it is addressed.
If you have received this email by mistake, please notify the sender and delete it immediately.
"""

st.caption(disclaimer)


# ==========================================================
# SOCIAL LINKS HTML
# ==========================================================
social_html = f"""
<a href="{facebook}" style="margin-right:15px;">Facebook</a>
<a href="{instagram}" style="margin-right:15px;">Instagram</a>
<a href="{youtube}" style="margin-right:15px;">YouTube</a>
"""


# ==========================================================
# FINAL SIGNATURE HTML
# ==========================================================
signature_html = f"""
<table style="font-family: Arial; color:{text_color}; font-size:{font_size}px; line-height:1.5;">
<tr>
<td>

{"<img src='" + logo_url + "' width='180'><br><br>" if show_logo else ""}

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
st.header("✅ Live Preview")
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
3. Go to: File → Options → Mail → Signatures
4. Click "New" and give it a name
5. Paste (Ctrl + V / Cmd + V) into the editor
6. Save and set as default signature
✅ Done!
""")


import streamlit as st
import re

st.set_page_config(page_title="Adria Signature Generator", layout="centered")

# ==========================================================
# COMPANY SETTINGS
# ==========================================================
logo_url = "https://scontent.flju1-1.fna.fbcdn.net/v/t39.30808-1/538848259_1373858921407395_3734947029332493437_n.jpg?stp=c221.221.1034.1034a_dst-jpg_s480x480_tt6"

facebook = "https://www.facebook.com/adriaankaran"
instagram = "https://www.instagram.com/adria_ankaran"
youtube = "https://www.youtube.com"
website = "https://www.adria-ankaran.si"

primary_color = "#1f6db5"
text_color = "#000000"
font_size = 14

# ==========================================================
# TITLE
# ==========================================================
st.title("📧 Adria Resort – Email Signature Generator")
st.caption("Fill in your personal data only")

# ==========================================================
# STEP 1 – PERSONAL DATA
# ==========================================================
full_name = st.text_input("Full Name (Name and Surname)")

# Validate full name
if full_name and len(full_name.strip().split(" ")) < 2:
    st.error("Please enter both Name and Surname (example: John Smith)")
    st.stop()

# Auto-generate email if full name is valid
if full_name and len(full_name.strip().split(" ")) >= 2:
    first_name, last_name = full_name.strip().split(" ", 1)
    email = st.text_input("Email", f"{first_name.lower()}.{last_name.lower()}@adria-ankaran.si")
else:
    email = st.text_input("Email")

# Job title dropdown
job_title = st.selectbox(
    "Job Title",
    [
        "Revenue",
        "Sales Manager",
        "Front Office Manager",
        "Marketing Specialist",
        "Hotel Manager",
        "Operations",
    ]
)

phone = st.text_input("Phone", "041708455")
if phone and not re.fullmatch(r"\+?\d+", phone):
    st.error("Phone number can only contain digits and optional leading +")
    st.stop()

if email and not re.match(r"^[\w\.-]+@adria-ankaran\.si$", email):
    st.error("Email must be in the format name@adria-ankaran.si")
    st.stop()

# Optional Banner URL
banner_url = st.text_input(
    "Optional Banner Image URL (minimum width 514px)",
    "https://scontent.flju1-1.fna.fbcdn.net/v/t39.30808-6/490598416_1250886907037931_2980757396709213237_n.jpg?stp=dst-jpg_p960x960_tt6&_nc_cat=107&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=2n69QymOR8wQ7kNvwEKiVsS&_nc_oc=Adk_rW1TmQkjLJ578L9HpykTh30fdeXhLOfbRwBGB-N-VqeC7oC6Aq70KOwXLdGNPvU&_nc_zt=23&_nc_ht=scontent.flju1-1.fna&_nc_gid=K1yl1X6bMzrQwCCL6mUTUQ&oh=00_AflJDO1YHZEDCZeaXyk-ecbMJYOmu0s9cDEdLDE2kmOtKQ&oe=693786F2"
)

# ==========================================================
# GENERATE SIGNATURE
# ==========================================================
if st.button("Generate My Signature"):

    # Optional banner HTML
    banner_html = ""
    if banner_url.strip() != "":
        banner_html = f"""
        <div style="margin-top:10px;">
          <a href="{website}">
            <img src="{banner_url}" width="514" style="border-radius:8px; max-width:100%;">
          </a>
          <p style="font-size:10px; color:#888; margin:2px 0 0 0;">
            Disclaimer: This email and any attachments are confidential. Please do not share without permission.
          </p>
        </div>
        """

    # Main signature HTML
    signature_html = f"""
    <table style="font-family: Arial; font-size:{font_size}px; color:{text_color}; width:100%; max-width:600px; border-collapse:collapse;">
      <tr>
        <td style="padding-right:15px; vertical-align: top;">
          <p style="margin:0; color:{primary_color}; font-size:22px; font-weight:bold;">
            {full_name}
          </p>
          <p style="margin:0; font-size:16px;">
            {job_title}
          </p>
          <hr style="border:1px solid {primary_color}; margin:6px 0 10px 0;">
          <p style="margin:2px 0;">📞 {phone}</p>
          <p style="margin:2px 0;">✉️ {email}</p>
          <p style="margin:6px 0;">
            <a href="{website}" style="color:{primary_color}; text-decoration:none;">
              www.adria-ankaran.si
            </a>
          </p>
          <div style="margin-top:10px;">
            <a href="{facebook}" style="margin-right:8px;">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="22">
            </a>
            <a href="{instagram}" style="margin-right:8px;">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733558.png" width="22">
            </a>
            <a href="{youtube}">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733646.png" width="22">
            </a>
          </div>
        </td>
        <td style="vertical-align: top; text-align: center;">
          <img src="{logo_url}" width="120" style="border-radius:8px;">
        </td>
      </tr>
    </table>
    {banner_html}
    """

    # ==========================================================
    # LIVE PREVIEW (visual)
    # ==========================================================
    st.subheader("✅ Signature Preview")
    st.markdown(signature_html, unsafe_allow_html=True)

    # ==========================================================
    # OUTLOOK COPY BOX (HTML)
    # ==========================================================
    st.subheader("📋 Copy & Paste into Outlook")
    st.text_area("Copy HTML below", value=signature_html, height=350)
    st.success("Select → Copy → Paste into Outlook signature editor")






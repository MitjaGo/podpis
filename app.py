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
if full_name and len(full_name.strip().split(" ")) < 2:
    st.error("Please enter both Name and Surname (example: John Smith)")
    st.stop()

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

email = st.text_input("Email")
if email and not re.match(r"^[\w\.-]+@adria-ankaran\.si$", email):
    st.error("Email must be in the format name@adria-ankaran.si")
    st.stop()

# ==========================================================
# GENERATE SIGNATURE
# ==========================================================
if st.button("Generate My Signature"):

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
    st.text_area("Copy HTML below", value=signature_html, height=300)
    st.success("Select → Copy → Paste into Outlook signature editor")





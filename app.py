import streamlit as st
import re

st.set_page_config(page_title="Adria Signature Generator", layout="centered")

# ==========================================================
# COMPANY SETTINGS
# ==========================================================
logo_url = "https://www.adria-ankaran.si/app/uploads/2025/10/logo-Adria.jpg"

Adria = "ADRIA Turistično podjetje d.o.o."
Adres = "Jadranska cesta 25, SI-6280 Ankaran, Slovenija"

facebook = "https://www.facebook.com/AdriaAnkaranResort/"
instagram = "https://www.instagram.com/adriaankaranresort/"
youtube = "https://www.youtube.com/@adriaankaran1577"
website = "https://www.adria-ankaran.si"

primary_color = "#1f6db5"
text_color = "#000000"
font_size = 14

# ==========================================================
# TITLE
# ==========================================================
st.title("📧 Adria Resort – Email Generator")
st.caption("Dodaj svoje osebne podatke")

# ==========================================================
# STEP 1 – PERSONAL DATA
# ==========================================================
full_name = st.text_input("Ime in Priimek (Primer: Mitja Goja)")

# Validate full name
if full_name and len(full_name.strip().split(" ")) < 2:
    st.error("Dodaj Ime in Priimek (Primer: Mitja Goja)")
    st.stop()

# Auto-generate email if full name is valid
if full_name and len(full_name.strip().split(" ")) >= 2:
    first_name, last_name = full_name.strip().split(" ", 1)
    email = st.text_input("Email se generira sam ko se vnese ime in priimek (V kolikor imate mail drugačen, to popravite ročno)", f"{first_name.lower()}.{last_name.lower()}@adria-ankaran.si")
else:
    email = st.text_input("Email")

# Job title dropdown
job_title = st.selectbox(
    "Izberi naziv",
    [
        "Rezervacije / Reservations",
        "Komercialist prodaje / Sales Manager",
        "Vodja Hotela / Hotel Manager",
        "Managing Director / Direktor",
        "Vodja Kuhinje",
        "Recepcija / Reception",
    ]
)

phone = st.text_input("Telefon (Vnesi številko npr 41 454 444 s predledki)","+386")

# Check if phone is empty
if not phone.strip():
    st.error("Dodaj telefonsko številko s presledki")
    st.stop()

if email and not re.match(r"^[\w\.-]+@adria-ankaran\.si$", email):
    st.error("Email must be in the format name@adria-ankaran.si")
    st.stop()

# Optional Banner URL
banner_url = st.text_input(
    "Neobvezni URL pasice (širina 514px višina 195px)"
)

# ==========================================================
# GENERATE SIGNATURE
# ==========================================================
if st.button("Generiraj e-podpis"):

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
          <p style="margin:2px 0;">T.: {phone}</p>
          <p style="margin:2px 0;">E.: {email}</p>
          <p style="margin:6px 0;">
            <a href="{website}" style="color:{primary_color}; text-decoration:none;">
            www.adria-ankaran.si
            </a>
          </p>
              <p style="margin:0; font-size:16px;">
            {Adria}
            <p style="margin:0; font-size:16px;">
            {Adres}
          <div style="margin-top:10px;">
            <a href="{facebook}" style="margin-right:8px;color:#ffffff;">
              <img src="https://raw.githubusercontent.com/MitjaGo/podpis/main/icons/fb.png
" width="22.5">
            </a>
            <a href="{instagram}" style="margin-right:8px;color:#ffffff;">
              <img src="https://raw.githubusercontent.com/MitjaGo/podpis/main/icons/it.png
" width="22">
            </a>
            <a href="{youtube}">
              <img src="https://raw.githubusercontent.com/MitjaGo/podpis/main/icons/yt.png
" width="22.5">
            </a>
          </div>
        </td>
        <td style="vertical-align: top; text-align: center;">
          <img src="{logo_url}" width="100" style="border-radius:8px;">
        </td>
      </tr>
    </table>

<div style="font-family: Arial; font-size:10px; color:#808080; width:100%; max-width:600px; border-collapse:collapse;">
  * To e-poštno sporočilo vam pošiljam zdaj, saj mi to ustreza. 
  Ne pričakujem, da se boste nanj odzvali izven svojega običajnega delovnega časa.
</div>
    {banner_html}
    """

    # ==========================================================
    # LIVE PREVIEW (visual)
    # ==========================================================
    st.subheader("✅ Označi celoten e-podpis in ga kopiraj v mail podpis")
    st.markdown(signature_html, unsafe_allow_html=True)









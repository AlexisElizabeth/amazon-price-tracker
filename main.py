from bs4 import BeautifulSoup
import requests
import smtplib
import os


MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


if __name__ == "__main__":
    url = "https://www.amazon.com/Instant-Pot-Ultimate-Pressure-Dehydrate/dp/B0B1G5M31V?ref_=ast_sto_dp&th=1&psc=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/107.0.0.0 Safari/537.36", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,sv;q=0.7,"
                                                                                  "it;q=0.6"}
    response = requests.get(url=url, headers=headers)
    website_html = response.text
    soup = BeautifulSoup(website_html, "lxml")

    price = soup.find_all(name="span", class_="a-offscreen")[0].getText()
    price = float(price.split("$")[1])

    if price < 300.00:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon Price Alert!!!!!\n\n"
                    f"The Instant Pot Duo Crisp Ultimate Lid, 13-in-1 Air Fryer and "
                    f"Pressure Cooker Combo is now {price}!  Check out {url} for details!")

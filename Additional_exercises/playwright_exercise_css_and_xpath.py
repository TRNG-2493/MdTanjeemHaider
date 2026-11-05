from pathlib import Path
import pytest
from playwright.sync_api import Page, expect

PRACTICE_PAGE = Path(__file__).parent / "index.html"

@pytest.fixture
def store(page: Page):
    page.goto(PRACTICE_PAGE.as_uri())
    return page

# ------------------------------CSS selectors only---------------------------------

# 5. Sign in button — find by its type attribute; assert its text is "Sign in"
def test_sign_in_button(store: Page):
    loc = store.locator('button[type="submit"]')
    expect(loc).to_have_text("Sign in")

# 6. Logo image — find by its alt attribute; assert its src ends with "logo.png"
def test_logo_image(store: Page):
    loc = store.locator('img[alt="Practice Store logo"]')
    expect(loc).to_have_attribute("src", "logo.png")

# 7. All links inside the navigation bar — assert their texts, in order
def test_nav_links(store: Page):
    loc = store.locator("nav a")
    expect(loc).to_have_text(["Home", "Products", "Contact us"])

# 8. "Contact us" link — find by its href; assert its text is "Contact us"
def test_contact_us_link(store: Page):
    loc = store.locator('a[href="#contact"]')
    expect(loc).to_have_text("Contact us")

# 9. 🚚 icon — find by a partial match on its title (contains "shipping");
#    assert the full title attribute value
def test_shipping_icon(store: Page):
    loc = store.locator('[title*="shipping"]')
    expect(loc).to_have_attribute("title", "Free shipping on orders over $50")

# 10. Checkout button — find by data-testid; assert its text is "Checkout"
def test_checkout_button(store: Page):
    loc = store.locator('[data-testid="checkout-button"]')
    expect(loc).to_have_text("Checkout")

# 11. All product items — assert there are exactly 4 of them
def test_all_product_items(store: Page):
    loc = store.locator(".product")
    expect(loc).to_have_count(4)

# 12. All product prices — assert their texts, in order
def test_all_product_prices(store: Page):
    loc = store.locator(".product .price")
    expect(loc).to_have_text(["$29.99", "$9.99", "$15.99", "$49.99"])

# 13. The disabled "Add to cart" button — assert it is disabled
def test_disabled_add_to_cart_button(store: Page):
    loc = store.locator('button:disabled')
    expect(loc).to_be_disabled()

# 14. All "Add to cart" buttons that are NOT disabled — assert there are 3
def test_enabled_add_to_cart_buttons(store: Page):
    loc = store.locator('.product button:not(:disabled)')
    expect(loc).to_have_count(3)

# 15. Name of the first product — assert its text is "Backpack"
def test_first_product_name(store: Page):
    loc = store.locator(".product h3").first
    expect(loc).to_have_text("Backpack")

# 16. Price of the third product — assert its text is "$15.99"
def test_third_product_price(store: Page):
    loc = store.locator(".product .price").nth(2)
    expect(loc).to_have_text("$15.99")

# 17. Stock status of the last product — assert its text is "In stock"
def test_last_product_stock_status(store: Page):
    loc = store.locator(".product .stock").last
    expect(loc).to_have_text("In stock")

# 18. All h2 headings that are direct children of a section — assert their texts, in order
def test_section_headings(store: Page):
    loc = store.locator("section > h2")
    expect(loc).to_have_text(["Sign in", "Products", "Recent orders"])

# 19. All rows in the orders table body (excluding the header row) — assert there are 4
def test_all_order_rows(store: Page):
    loc = store.locator("table tbody tr")
    expect(loc).to_have_count(4)

# 20. Status cell of the second order row — assert its text is "Pending"
def test_second_order_status(store: Page):
    loc = store.locator("table tbody tr").nth(1)
    loc = loc.locator("td").nth(2)
    expect(loc).to_have_text("Pending")


# ------------------------------Xpath selectors only---------------------------------

# 5. "Forgot password?" link — partial text match ("Forgot"); assert full text
def test_forgot_password_link(store: Page):
    loc = store.locator("//a[contains(text(), 'Forgot')]")
    expect(loc).to_have_text("Forgot password?")

# 6. Sign in BUTTON (not the heading) — locate by role + text; assert type="submit"
def test_sign_in_button(store: Page):
    loc = store.locator("//button[text()='Sign in']")
    expect(loc).to_have_attribute("type", "submit")

# 7. Checkbox inside the <label> that contains "Remember me" — assert its id
def test_remember_me_checkbox(store: Page):
    loc = store.locator("//label[contains(text(), 'Remember me')]/input[@type='checkbox']")
    expect(loc).to_have_id("remember")

# 8. Checkout button — locate by its text; assert data-testid attribute
def test_checkout_button(store: Page):
    loc = store.locator("//button[text()='Checkout']")
    expect(loc).to_have_attribute("data-testid", "checkout-button")

# 9. All <li> product elements — locate by class attribute; assert there are 4
def test_all_product_elements(store: Page):
    loc = store.locator("//li[@class='product']")
    expect(loc).to_have_count(4)

# 10. Product heading whose text is "Jacket" — assert it is visible
def test_jacket_heading(store: Page):
    loc = store.locator("//h3[text()='Jacket']")
    expect(loc).to_be_visible()

# 11. Price of "Bike Light" — start from its heading, move to sibling; assert text
def test_bike_light_price(store: Page):
    loc = store.locator("//h3[text()='Bike Light']/following-sibling::p[@class='price']")
    expect(loc).to_have_text("$9.99")

# 12. Name of the product marked "Out of stock" — go up to parent <li>, then down
#     to the name element; assert text
def test_out_of_stock_product_name(store: Page):
    loc = store.locator("//p[text()='Out of stock']/ancestor::li//h3")
    expect(loc).to_have_text("Bike Light")

# 13. "Add to cart" button inside the "T-Shirt" product — assert it is enabled
def test_add_to_cart_button_tshirt(store: Page):
    loc = store.locator("//h3[text()='T-Shirt']/following-sibling::button[text()='Add to cart']")
    expect(loc).to_be_enabled()

# 14. All buttons with the disabled attribute — assert there is exactly 1
def test_disabled_buttons(store: Page):
    loc = store.locator("//button[@disabled]")
    expect(loc).to_have_count(1)

# 15. Heading of the SECOND product — use ( … )[1] indexing; assert text
def test_second_product_heading(store: Page):
    loc = store.locator("(//li[@class='product']//h3)[2]")
    expect(loc).to_have_text("Bike Light")

# 16. Last price on the page — use last(); assert text
def test_last_price(store: Page):
    loc = store.locator("(//p[@class='price'])[last()]")
    expect(loc).to_have_text("$49.99")

# 17. All stock <p> whose text is exactly "In stock" — assert there are 3
def test_all_in_stock_elements(store: Page):
    loc = store.locator("//p[text()='In stock']")
    expect(loc).to_have_count(3)

# 18. Status of the order placed by "Chen Wei" — assert text
def test_order_status_chen_wei(store: Page):
    loc = store.locator("//td[text()='Chen Wei']/following-sibling::td[1]")
    expect(loc).to_have_text("Shipped")

# 19. Order number of the "Pending" order — preceding-sibling axis; assert text
def test_order_number_pending(store: Page):
    loc = store.locator("//td[text()='Pending']/preceding-sibling::td[2]")
    expect(loc).to_have_text("1002")

# 20. Total of the "Cancelled" order — assert text
def test_total_cancelled_order(store: Page):
    loc = store.locator("//td[text()='Cancelled']/following-sibling::td[1]")
    expect(loc).to_have_text("$15.99")
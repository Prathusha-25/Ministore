import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.hero {
    background: linear-gradient(90deg,#4F46E5,#7C3AED);
    padding:30px;
    border-radius:15px;
    color:white;
    margin-bottom:20px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
    transition:0.3s;
}

.product-card:hover{
    transform:translateY(-5px);
}

.price{
    color:#4F46E5;
    font-size:22px;
    font-weight:bold;
}

.category{
    background:#EDE9FE;
    color:#5B21B6;
    padding:4px 10px;
    border-radius:10px;
    display:inline-block;
    font-size:13px;
}

.sidebar-title{
    font-size:22px;
    font-weight:bold;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SAMPLE PRODUCTS
# --------------------------------------------------

products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium sound quality with noise cancellation.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4499,
        "description": "Fitness tracking and heart-rate monitoring.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3599,
        "description": "Comfortable lightweight sports shoes.",
        "category": "Fashion"
    },
    {
        "name": "Laptop Backpack",
        "price": 1899,
        "description": "Water-resistant backpack with laptop compartment.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Mug",
        "price": 499,
        "description": "Ceramic mug perfect for coffee lovers.",
        "category": "Home"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 2499,
        "description": "Portable speaker with powerful bass.",
        "category": "Electronics"
    }
]

# --------------------------------------------------
# SESSION STATE FOR CART
# --------------------------------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown("## 🛒 MiniStore")

categories = ["All"] + sorted(list(set(p["category"] for p in products)))

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Shopping Cart")

if len(st.session_state.cart) == 0:
    st.sidebar.info("Cart is empty")
else:

    total = 0

    for item in st.session_state.cart:
        st.sidebar.write(f"• {item['name']}")
        total += item["price"]

    st.sidebar.markdown("---")
    st.sidebar.success(f"Total: ₹{total}")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
<h1>🛍️ Welcome to MiniStore</h1>
<p>Your one-stop destination for premium products at amazing prices.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FEATURED SECTION
# --------------------------------------------------

st.subheader("⭐ Featured Products")

# Filter products

if selected_category != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]
else:
    filtered_products = products

# --------------------------------------------------
# PRODUCT GRID
# --------------------------------------------------

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(
            f"""
            <div class="product-card">

            <h3>{product['name']}</h3>

            <div class="category">
            {product['category']}
            </div>

            <br><br>

            <p>{product['description']}</p>

            <div class="price">
            ₹{product['price']}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added!")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.caption("© 2026 MiniStore Demo Website | Built with Streamlit")
import streamlit as st
from data import products

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------------
# Session Cart
# ----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>

.hero{
background:linear-gradient(90deg,#4F46E5,#7C3AED);
padding:30px;
border-radius:15px;
color:white;
}

.product-card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 2px 10px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.price{
color:#4F46E5;
font-size:22px;
font-weight:bold;
}

.support-btn{
position:fixed;
bottom:25px;
right:25px;
background:#4F46E5;
padding:15px;
border-radius:50%;
font-size:30px;
text-align:center;
z-index:999;
text-decoration:none;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

categories = ["All"] + sorted(list(set(x["category"] for x in products)))

selected = st.sidebar.selectbox(
    "Category",
    categories
)

st.sidebar.markdown("## Cart")

if len(st.session_state.cart) == 0:
    st.sidebar.info("Empty")
else:

    total = 0

    for item in st.session_state.cart:
        st.sidebar.write(item["name"])
        total += item["price"]

    st.sidebar.success(f"₹{total}")

# ----------------------------
# Hero
# ----------------------------

st.markdown("""
<div class="hero">
<h1>🛍️ MiniStore</h1>
<p>Your favorite online shopping destination.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.header("Featured Products")

if selected != "All":
    display = [p for p in products if p["category"] == selected]
else:
    display = products

cols = st.columns(3)

for i, product in enumerate(display):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">

        <h3>{product['name']}</h3>

        <b>{product['category']}</b>

        <p>{product['description']}</p>

        <div class="price">
        ₹{product['price']}
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Add to Cart",
            key=i
        ):
            st.session_state.cart.append(product)

# ----------------------------
# Floating Support Button
# ----------------------------

st.markdown("""
<a href="/Support_Chatbot" target="_self">
<div class="support-btn">
💬
</div>
</a>
""", unsafe_allow_html=True)
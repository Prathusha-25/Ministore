import streamlit as st
from data import products

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Chatbot")

# -----------------------
# Chat History
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------
# Rule-Based Bot
# -----------------------

def chatbot_reply(user):

    text = user.lower()

    # ---------------- Product Questions ----------------

    for p in products:

        if p["name"].lower() in text:

            return f"""
**{p['name']}**

Price: ₹{p['price']}

Category: {p['category']}

Description:
{p['description']}
"""

    if "product" in text:
        return "We currently sell Wireless Headphones, Smart Watch, Running Shoes, Laptop Backpack, Coffee Mug and Bluetooth Speaker."

    # ---------------- Delivery ----------------

    if "delivery" in text or "shipping" in text:
        return "Standard delivery takes 3-5 business days. Express delivery takes 1-2 days."

    # ---------------- Refund ----------------

    if "refund" in text:
        return "Refunds are processed within 5-7 business days after approval."

    # ---------------- Returns ----------------

    if "return" in text:
        return "Products can be returned within 30 days if unused and in original packaging."

    # ---------------- Payment ----------------

    if "payment" in text or "pay" in text:
        return "We accept Credit Card, Debit Card, UPI, Net Banking and Cash on Delivery."

    # ---------------- Order Status ----------------

    if "order" in text or "status" in text:
        return "Demo mode: Order tracking is not connected yet. In a real app your live order status would appear here."

    # ---------------- Greetings ----------------

    if "hello" in text or "hi" in text:
        return "Hello 👋 How can I help you today?"

    # ---------------- Default ----------------

    return "Sorry, I couldn't understand that. Ask me about products, delivery, refunds, returns, payments or order status."

# -----------------------
# Chat Input
# -----------------------

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = chatbot_reply(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)
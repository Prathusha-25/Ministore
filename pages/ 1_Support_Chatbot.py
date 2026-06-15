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
        import streamlit as st
from openai import OpenAI
from data import products

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬"
)

st.title("💬 MiniStore Customer Support")

# ----------------------------------------------------
# Initialize OpenAI Client
# ----------------------------------------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ----------------------------------------------------
# Create Product Catalog for System Prompt
# ----------------------------------------------------

catalog = ""

for product in products:
    catalog += f"""
Product: {product['name']}
Category: {product['category']}
Price: ₹{product['price']}
Description: {product['description']}

"""

# ----------------------------------------------------
# System Prompt
# ----------------------------------------------------

SYSTEM_PROMPT = f"""
You are the official customer support assistant for MiniStore.

Your job is to help customers with:

- Product information
- Product recommendations
- Delivery and shipping
- Orders
- Refunds
- Returns
- Payment methods
- General store policies

Store Catalog:

{catalog}

Rules:

1. Only answer questions related to MiniStore.
2. Use the product catalog above when answering product questions.
3. If a user asks about topics unrelated to the store
   (politics, coding, math, science, history, etc.),
   politely respond:

   "I'm here to help with MiniStore products,
   orders, delivery, refunds, returns, and payments.
   Please ask a store-related question."

4. Be professional, friendly, and concise.

5. Never invent products that are not in the catalog.
"""

# ----------------------------------------------------
# Chat History
# ----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------

user_input = st.chat_input("Ask about products, orders, refunds...")

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    # Call OpenAI API

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.3
    )

    assistant_reply = response.choices[0].message.content

    # Save assistant reply

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
import streamlit as st
import one as tc
from one import BinomialTreeOption   # Import your binomial tree option pricing class
from one import TrinomialTreeOption  # Import your trinomial tree option pricing class

st.title('Option Pricing Tool')

# Radio button for selecting the pricing method
method = st.radio("Select Pricing Method", ["Binomial Tree", "Trinomial Tree"])

# Input fields for option parameters
S0 = st.number_input("Initial Stock Price (S0)")
K = st.number_input("Strike Price (K)")
r = st.number_input("Risk-free Interest Rate (r)")
T = st.number_input("Time to Maturity (T)")
N = st.number_input("Number of Steps (N)", step=1)
sigma = st.number_input("Volatility (sigma)")

is_put = st.checkbox("Is Put")
is_am = st.checkbox("Is American")

# Function to calculate and display the option price


def calculate_option_price():
    option_price=None
    
    if method == "Binomial Tree":
        option = tc.BinomialTreeOption(S0, K, r, T, N, sigma, is_put, is_am)
    else:
        option = tc.TrinomialTreeOption(S0, K, r, T, N, sigma, is_put, is_am)

    option_price = option.price()
    st.write(f'Option Price: {option_price:.4f}')

# Button to trigger the calculation
if st.button("Calculate Option Price"):
    calculate_option_price()

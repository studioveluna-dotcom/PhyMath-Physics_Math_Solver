
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

st.set_page_config(page_title="PhyMath", page_icon="⚡")

st.title("PhyMath: Gotta Solve 'Em All! ⚡")
st.write("Catching calculation errors like pokemons so you score 80+")

# Sidebar inputs
st.sidebar.header("Projectile Launcher")
u = st.sidebar.number_input("Initial Velocity u (m/s)", min_value=0.0, value=20.0)
theta = st.sidebar.number_input("Launch Angle θ (degrees)", 0.0, 90.0, 45.0)
g = 9.81

if st.sidebar.button("I Choose You! Solve It"):
    # Calculations
    theta_rad = np.radians(theta)
    t_flight = 2 * u * np.sin(theta_rad) / g
    h_max = (u**2) * (np.sin(theta_rad)**2) / (2 * g)
    range_p = (u**2) * np.sin(2 * theta_rad) / g

    # Fun success messages
    poke_msgs = ["Pikachu used 100% Accuracy!", "Bulbasaur says: Perfect shot!", 
                 "Charizard approves: That’s hot math!", "Physics Master Badge earned!"]
    
    st.balloons()
    st.success(random.choice(poke_msgs))
    
    # Results
    col1, col2, col3 = st.columns(3)
    col1.metric("Time of Flight", f"{t_flight:.2f} s")
    col2.metric("Max Height", f"{h_max:.2f} m") 
    col3.metric("Range", f"{range_p:.2f} m")

    # Show steps toggle
    with st.expander("Show Steps - How I caught this answer"):
        st.latex(r'''Time: t = \frac{2u\sin\theta}{g} = \frac{2 \times %s \times \sin(%s°)}{9.81} = %.2f s''' % (u, theta, t_flight))
        st.latex(r'''Height: H = \frac{u^2\sin^2\theta}{2g} = %.2f m''' % h_max)
        st.latex(r'''Range: R = \frac{u^2\sin2\theta}{g} = %.2f m''' % range_p)

    # Graph
    t = np.linspace(0, t_flight, 100)
    x = u * np.cos(theta_rad) * t
    y = u * np.sin(theta_rad) * t - 0.5 * g * t**2
    
    fig, ax = plt.subplots()
    ax.plot(x, y, color='#FFCB05', linewidth=3)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Your Pokemon's Trajectory")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

st.write("---")
st.caption("Built by [SJK] | Class 12, Sri Guru Hargobind Public School | Next: Adding Calculus Mode")

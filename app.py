
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import math 

st.set_page_config(page_title="PhyMath", page_icon="⚡")

st.title("PhyMath: Gotta Solve 'Em All! ⚡")
st.write("Catching calculation errors like pokemons so you score 80+")
# Helper function 
def check_answer(selected, correct, explanation):
    if selected == correct:
        st.session_state.score += 1
        st.success("Pikachu used Thunderbolt! Correct! ⚡")
        st.balloons()
        st.write(f"**Explanation:** {explanation}")
    else:
        st.error("Team Rocket: 'Looks like you're blasting off agaaaain!' 💥")
        st.write(f"**Correct Answer:** {correct}")
        st.write(f"**Explanation:** {explanation}")
mode = st.selectbox("Choose your Trainer path:", ["Physics Projectile Solver", "Trainer Quiz Mode"])
st.divider()

if mode == "Physics Projectile Solver":
     # Sidebar inputs
     st.sidebar.header("Projectile Launcher")
     u = st.sidebar.number_input("Initial Velocity u (m/s)", min_value=0.0, value=20.0)
     theta = st.sidebar.number_input("Launch Angle θ (degrees)", 0.0, 90.0, 45.0)
     g = 9.81

     if st.sidebar.button("Thunderbooolllltttttt!!!! Calculatiiinnngggg"):
          # Calculatingg
          theta_rad = np.radians(theta)
          t_flight = 2 * u * np.sin(theta_rad) / g
          h_max = (u**2) * (np.sin(theta_rad)**2) / (2 * g)
          range_p = (u**2) * np.sin(2 * theta_rad) / g
          
          # Fun success messages
          poke_msgs = ["Pikachu used 100% Accuracy!", "Bulbasaur says: Perfect shot!", 
               "Charizard approves: That’s hot math!", "Physics Master Badge earned!"]
          
          st.toast('Thunderbolt! Direct hit! ⚡' , 
          icon='⚡')
          st.success("Pikachu used Thunderbolt!!! A perfect HITT")
          st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3gxMHliM2lrajI3NTN4N25sZWVuYjQ1bTFjeXA0a2d1OG84ZjM0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6sPy5yjk6b6aQ/giphy.gif")
          
          # Results
          col1, col2, col3 = st.columns(3)
          col1.metric("Time of Flight", f"{t_flight:.2f} s")
          col2.metric("Max Height", f"{h_max:.2f} m") 
          col3.metric("Range", f"{range_p:.2f} m")
          
          # Showing steps  in toggle
          with st.expander("Show Steps - How I caught this answer"):
               st.latex(r'''Time: t = \frac{2u\sin\theta}{g} = \frac{2 \times %s \times \sin(%s°)}{9.81} = %.2f s''' % (u, theta, t_flight))
               st.latex(r'''Height: H = \frac{u^2\sin^2\theta}{2g} = %.2f m''' % h_max)
               st.latex(r'''Range: R = \frac{u^2\sin2\theta}{g} = %.2f m''' % range_p)
          
          # Graphingg
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

elif mode == "Trainer Quiz Mode":
        st.header("Welcome to Trainer Quiz!!🎮 ")
        st.write("Hey!! Team Rocket is Blastiong off with Physics Question. Answer the RIGHT One to WIN!!")

          #Initialize score in session state
     if 'score' not in st.session_state:
             st.session_state.score = 0
             st.session_state.q_num = 0

         # Question bank - Team Rocket themed
     questions = [
        {
            "q": "Team Rocket asks: If u=20 m/s and θ=30°, what is the time of flight? (g=9.8)",
            "options": ["2.04 s", "4.08 s", "1.02 s", "20.4 s"],
            "ans": "2.04 s",
            "explain": "Time = 2*u*sinθ/g = 2*20*sin30°/9.8 = 40*0.5/9.8 = 2.04s"
        },
        {
            "q": "Meowth challenges: A Pokéball launched at 15 m/s, 45° has what max height?",
            "options": ["5.74 m", "11.47 m", "22.94 m", "1.53 m"],
            "ans": "5.74 m",
            "explain": "H = u²sin²θ/2g = 225*0.5/19.6 = 5.74m"
        },
        {
            "q": "James sneers: Which angle gives MAXIMUM range for same speed?",
            "options": ["30°", "45°", "60°", "90°"],
            "ans": "45°",
            "explain": "Range = u²sin2θ/g. sin2θ is max when 2θ=90°, so θ=45°"
        }
    ]

    # Display current question
    current_q = questions[st.session_state.q_num % len(questions)]
    st.subheader(f"Question {st.session_state.q_num + 1}")
    st.write(current_q["q"])

    # Ash encouraging image/text
    st.info("Ash: 'I choose you, SJK! You can do it!'")

    # Answer buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button(current_q["options"][0]):
            check_answer(current_q["options"][0], current_q["ans"], current_q["explain"])
    with col2:
        if st.button(current_q["options"][1]):
            check_answer(current_q["options"][1], current_q["ans"], current_q["explain"])
    with col1:
        if st.button(current_q["options"][2]):
            check_answer(current_q["options"][2], current_q["ans"], current_q["explain"])
    with col2:
        if st.button(current_q["options"][3]):
            check_answer(current_q["options"][3], current_q["ans"], current_q["explain"])

    # Score display
    st.metric("Your Trainer Score", st.session_state.score)
    st.progress(st.session_state.score / 10)

    if st.button("Next Question →"):
        st.session_state.q_num += 1
        st.rerun()


     
     
st.caption("Built by [SJK] | Class 12, Sri Guru Hargobind Public School | Next: Adding Calculus Mode")

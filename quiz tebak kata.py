 streamlit as st
import random
import
# Daftar kata
words = ["school", "friend", "python", "holiday", "garden"]

def scramble(word):
    """Mengacak huruf-huruf dalam sebuah kata."""
    letters = list(word)
    while True:
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled

# Inisialisasi session state
if "selected_words" not in st.session_state:
    st.session_state.selected_words = random.sample(words, 5)
    st.session_state.scrambled_words = [scramble(word) for word in st.session_state.selected_words]
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = [""] * 5
    st.session_state.finished = False

st.title("🎮 Game Menyusun Kata Bahasa Inggris")
st.write("Tebak kata asli dari huruf yang sudah diacak!")

if not st.session_state.finished:
    idx = st.session_state.current
    scrambled = st.session_state.scrambled_words[idx]
    original = st.session_state.selected_words[idx]

    st.subheader(f"Soal {idx + 1} dari 5")
    st.write(f"Huruf acak: **{scrambled}**")

    answer = st.text_input("Jawabanmu:", key=f"input_{idx}")

    if st.button("Periksa"):
        st.session_state.answers[idx] = answer.strip().lower()
        if st.session_state.answers[idx] == original:
            st.success("Benar!")
            st.session_state.score += 1
        else:
            st.error(f"Salah. Jawaban benar: {original}")

        st.session_state.current += 1

        if st.session_state.current >= 5:
            st.session_state.finished = True
        st.experimental_rerun()

else:
    st.success("Permainan selesai!")
    st.write(f"Skor akhir kamu: **{st.session_state.score} / 5**")

    if st.button("Main Lagi"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

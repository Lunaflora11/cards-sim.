import streamlit as st
import random

st.title("نظام محاكاة سحب البطاقات")

# إعداد الكوتشينة
if 'deck' not in st.session_state:
    suits = ['♥ القلوب', '♠ السباتي', '♦ الديمون', '♣ الشيريا']
    st.session_state.deck = [suit for suit in suits for _ in range(13)]
    st.session_state.drawn = []

total = len(st.session_state.deck)
counts = {s: st.session_state.deck.count(s) for s in ['♥ القلوب', '♠ السباتي', '♦ الديمون', '♣ الشيريا']}

# عرض الاحتمالات
cols = st.columns(4)
for i, (suit, count) in enumerate(counts.items()):
    prob = (count / total * 100) if total > 0 else 0
    cols[i].metric(label=suit, value=f"{prob:.1f}%")
    cols[i].progress(prob / 100)

# زر السحب
if st.button('اسحب بطاقة'):
    if total > 0:
        card = random.choice(st.session_state.deck)
        st.session_state.deck.remove(card)
        st.session_state.drawn.insert(0, card)
        st.rerun()

# النتائج
if st.session_state.drawn:
    st.success(f"البطاقة الحالية: {st.session_state.drawn[0]}")
    st.info(f"العدد المتبقي في الكوتشينة: {total}")
  

import streamlit as st
import pandas as pd
import altair as alt


st.write("""
# DNA Nucleotid Count Web APP

This app counts the nucleotide composition of query DNA!
""")

# Input Textbox

st.header('Enter DNA Sequence')

sequence_input = "DNA Query \nACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC\nCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC\nCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG\nAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC\nCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG\nTTTAATTACAGACCTGAA"

sequence =  st.text_area('Sequence input', sequence_input, height=250)
sequence =  ''.join(sequence.splitlines()[1:])
# The next lines show how is done in the tutorial
# sequence =  sequence.splitlines()
# sequence =  sequence[1:]
# sequence = ''.join(sequence)

st.write("""
        ***
""")

st.header('INPUT (DNA Query)')
sequence

## DNA Nucleotid count
st.header('OUTPUT (DNA Nucleotid count)')

st.subheader('1. Print dictionary')

def DNA_nucleotid_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
        ])
    return d

X = DNA_nucleotid_count(sequence)

X

## Print Text
st.subheader('2. Print text')

st.write(f"There are {X['A']} adenine (A)")
st.write(f"There are {X['T']} thymine (T)")
st.write(f"There are {X['G']} guanine (G)")
st.write(f"There are {X['C']} cytosine (C)")

## Display Dataframe
st.subheader('3. Print Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'Nucleotide'})
st.write(df)

## Display Bar chart using Altair
st.subheader('4. Display bar chart')
p = alt.Chart(df).mark_bar().encode(
        x='Nucleotide',
        y='Count'
        )
p = p.properties(
    width= alt.Step(80) #Increase bar width
        )
st.write(p)

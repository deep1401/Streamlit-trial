import streamlit as st
from graphviz import Digraph
import time

graph=Digraph(comment="Test_graph")

graph.edge("Root", "Node11")
graph.edge("Root", "Node12")
graph.edge("Node11", "Node21")
graph.edge("Node11", "Node22")
graph.edge("Node12", "Node23")
graph.edge("Node12", "Node24")
graph.edge("Root", "Node24")


st.graphviz_chart(graph)

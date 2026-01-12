
import streamlit as st
import os
import glob
import chromadb
from datetime import datetime

# Page Config
st.set_page_config(page_title="MACS Admin Dashboard", layout="wide")
st.title("🧠 MACS Admin Dashboard")

# Constants
DEBATE_DIR = "data/debates"
CHROMA_DIR = "data/chroma"

# Tabs
tab1, tab2, tab3 = st.tabs(["📂 File Storage", "💾 Vector DB (Chroma)", "🔍 Search Playground"])

# --- Tab 1: File Storage ---
with tab1:
    st.header("Local Markdown Files")
    
    # List files
    if not os.path.exists(DEBATE_DIR):
        st.warning(f"Directory not found: {DEBATE_DIR}")
        files = []
    else:
        files = glob.glob(os.path.join(DEBATE_DIR, "*.md"))
        files.sort(key=os.path.getmtime, reverse=True)
    
    if not files:
        st.info("No debate files found.")
    else:
        # File Selection
        selected_file = st.selectbox("Select a file to view:", files, format_func=lambda x: os.path.basename(x))
        
        if selected_file:
            st.divider()
            with open(selected_file, "r") as f:
                content = f.read()
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("Preview (Rendered)")
                st.markdown(content)
            with col2:
                st.subheader("Raw Content")
                st.code(content, language="markdown")

# --- Tab 2: Vector DB ---
with tab2:
    st.header("ChromaDB Inspector")
    
    if not os.path.exists(CHROMA_DIR):
        st.error(f"ChromaDB directory not found: {CHROMA_DIR}")
    else:
        try:
            client = chromadb.PersistentClient(path=CHROMA_DIR)
            collections = client.list_collections()
            
            if not collections:
                st.info("No collections found in ChromaDB.")
            else:
                col_names = [c.name for c in collections]
                selected_col_name = st.selectbox("Select Collection:", col_names)
                
                if selected_col_name:
                    collection = client.get_collection(selected_col_name)
                    count = collection.count()
                    st.metric("Total Documents", count)
                    
                    # Peek
                    st.subheader("Recent Items (Peek)")
                    if count > 0:
                        peek_data = collection.peek(limit=5)
                        
                        # Display as manageable tabs or json
                        for i in range(len(peek_data['ids'])):
                            with st.expander(f"Doc ID: {peek_data['ids'][i]}"):
                                st.write("**Metadata:**")
                                st.json(peek_data['metadatas'][i])
                                st.write("**Document:**")
                                st.text(peek_data['documents'][i])
        except Exception as e:
            st.error(f"Error connecting to ChromaDB: {e}")

# --- Tab 3: Search Playground ---
with tab3:
    st.header("Semantic Search Playground")
    
    query_text = st.text_input("Enter search query:", placeholder="e.g., TDD에 대한 토론")
    
    if query_text:
        try:
            # Re-init client to ensure connection (or reuse)
            client = chromadb.PersistentClient(path=CHROMA_DIR)
            collection = client.get_collection("debates") # Default collection name used in app
            
            results = collection.query(
                query_texts=[query_text],
                n_results=3
            )
            
            st.subheader("Results")
            
            if not results['ids'][0]:
                st.info("No matching results found.")
            else:
                for i in range(len(results['ids'][0])):
                    doc_id = results['ids'][0][i]
                    distance = results['distances'][0][i]
                    meta = results['metadatas'][0][i]
                    doc_content = results['documents'][0][i]
                    
                    st.markdown(f"**{i+1}. Distance: {distance:.4f}**")
                    st.info(f"📄 {doc_content}")
                    st.caption(f"Metadata: {meta}")
                    st.divider()
                    
        except Exception as e:
            st.error(f"Search Error: {e}")

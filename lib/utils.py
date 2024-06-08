import streamlit.components.v1 as components

def change_button_height(widget_label, height):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button);
            for (var i = 0; i < elements.length; ++1) {{
                if (elements[i].innerText == '{widget_label}') {{
                    elements[i]..style.height '{height}px';
            
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)
import gradio as gr
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'auxiliar')))

from functions import askQuestion

with open('styles/styles.css', 'r') as file:
    css = file.read()

with gr.Blocks(title='WorldWealth', css=css, head="<link rel='icon' href='styles/logo.png' type='image/png'>") as demo:

# Esto inserta el favicon
    markdown_content = """
    <div style="text-align:center;">
        <h1 >World Wealth</h1>
        <p style="font-family: Protest Guerrilla; font-size: 20px; margin-top:0px;">2021</p>
    </div>
    """
    gr.Image("styles/logo.png", label="WorldWealth Logo", show_label=False, height=100,container=False)
    gr.Markdown(markdown_content)

    with gr.Tab("WealthANALYTICS"):
        # text_input = gr.Textbox(label="Enter text")
        # text_output = gr.Textbox(label="Flipped text")
        text_button = gr.Button("Flip")
        # text_button.click(flip_text, inputs=text_input, outputs=text_output)

    with gr.Tab("WealthCHATBOT"):

        chat = gr.ChatInterface(
            askQuestion,
            type="messages",
            save_history=True,
        )

        # btn_audio=gr.Button('BotonAUDIO')
        # btn_audio.click(text_to_speech)
    # with gr.Accordion("Open for More!", open=False):
    #     gr.Markdown("Look at me...")
    #     temp_slider = gr.Slider(
    #         0, 1,
    #         value=0.1,
    #         step=0.1,
    #         interactive=True,
    #         label="Slide me",
    #     )

if __name__ == "__main__":
    demo.launch(favicon_path='styles/logo.png')


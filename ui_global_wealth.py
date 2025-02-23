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
      grafana_iframe = """
        <iframe src="http://localhost:3000/d-solo/eedvm7u2s854wa/10-mayores-fortunas?orgId=1&from=1740251347418&to=1740272947418&timezone=browser&panelId=1&__feature.dashboardSceneSolo" width="1400" height="400" frameborder="0"></iframe>        """
      gr.HTML(grafana_iframe)

      grafana_iframe2= """
        <iframe src="http://localhost:3000/d-solo/bedvxj5e3qps0f/sectores-con-mayor-concentracion-de-riqueza?orgId=1&from=1740253439673&to=1740275039673&timezone=browser&panelId=1&__feature.dashboardSceneSolo" width="1400" height="400" frameborder="0"></iframe>        """
      gr.HTML(grafana_iframe2)
      grafana_iframe3= """
            <iframe src="http://localhost:3000/d-solo/fedvwiy0837cwc/new-dashboard?orgId=1&from=1740252763306&to=1740274363306&timezone=browser&panelId=1&__feature.dashboardSceneSolo" width="1400" height="400" frameborder="0"></iframe>
          """
      gr.HTML(grafana_iframe3)

    with gr.Tab("WealthCHATBOT"):

        chat = gr.ChatInterface(
            askQuestion,
            type="messages",
            save_history=True
        )

if __name__ == "__main__":
    demo.launch(favicon_path='styles/logo.png')


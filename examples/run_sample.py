from otter_api_wrapper import OtterAPI
from otter_api_wrapper.utils import save_plotly_figure
import pandas as pd

otter_api = OtterAPI(
    api_token='<your API token>'
)
df, inference_id = otter_api.run_sample_path(
    file_path='examples/data/rhabdomyosarcoma.genes.hugo.results',
    model_name='otter',
    sample_name='rhabdo'
)

otter_api.download_pdf_report(inference_id, 'examples/results/rhabdo_report.pdf')

# returns sunburst_plot and top_path
plot = otter_api.plot_sample(df) 
save_plotly_figure(plot['sunburst_plot'], 'examples/results/rhabdo_sunburst.png')
print(plot['top_path'])

# returns age_plot, diagnosis_plot, and sex_plot
plot = otter_api.get_explore_plots(plot['top_path']['names'][-1])
save_plotly_figure(plot['age_plot'], 'examples/results/rhabdo_age.png')
save_plotly_figure(plot['diagnosis_plot'], 'examples/results/rhabdo_diagnosis.png')
save_plotly_figure(plot['sex_plot'], 'examples/results/rhabdo_sex.png')

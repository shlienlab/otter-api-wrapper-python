from otter_api_wrapper import OtterAPI
from otter_api_wrapper.utils import save_plotly_figure
import pandas as pd

ATLAS_VERSION='v2'

# Run a sample and get the results
otter_api = OtterAPI(
    api_token='ioq9Cwao1cSNPFyMwf52sh5BtBT2FQTG',
    base_api_url='http://localhost:3000/api',
    base_app_url='http://localhost:3000/app',
)

# If wait_for_result is False, returns task_id and inference_id
df, inference_id = otter_api.run_sample_path(
    file_path='data/rhabdomyosarcoma.genes.hugo.results',
    model_name='hierarchical',
    atlas_version=ATLAS_VERSION,
    sample_name='rhabdo',
    # share_with=['<someone_else_email>'],
    wait_for_result=True,
    timeout=300
)

otter_api.download_pdf_report(inference_id, 'results/rhabdo_report.pdf')

# returns sunburst_plot and top_path
plot = otter_api.plot_sample(df, atlas_version=ATLAS_VERSION) 
save_plotly_figure(plot['sunburst_plot'], 'results/rhabdo_sunburst.png')
print(plot['top_path'])

# returns age_plot, diagnosis_plot, and sex_plot
plot = otter_api.get_explore_plots(plot['top_path']['names'][-1], atlas_version=ATLAS_VERSION)
save_plotly_figure(plot['age_plot'], 'results/rhabdo_age.png')
save_plotly_figure(plot['diagnosis_plot'], 'results/rhabdo_diagnosis.png')
save_plotly_figure(plot['sex_plot'], 'results/rhabdo_sex.png')


import sys
from streamlit.web import cli as stcli

# NOTA: Para rodar o projeto web top_100, executar esse arquivo

sys.argv = ["streamlit", "run", "top_100.py"]
sys.exit(stcli.main())

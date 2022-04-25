import pytest
import os
from Resources import config
from datetime import datetime

if __name__ == '__main__':
    test_dt = datetime.now().strftime('%Y-%m-%d %H-%M')
    report = f'{os.path.join(config.html_report_folder, test_dt)}.html'
    # pytest.main(['-v', '-k search', f'--html={report}'])
    pytest.main(['-v', f'--html={report}'])


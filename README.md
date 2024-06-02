## Description
This script extracts data on "Approved Action Plan Report" of all the sub-districts of a district
from "https://egramswaraj.gov.in/webservice/approvedActionPlanExternalReport/"{Village_LGD_Code}"/2022-2023" 

![XLS Preview](https://github.com/aryam-j/ws_action_plan_report/blob/master/sc.png?raw=true)
## Instruction to Run
1. `git clone https://github.com/aryam-j/ws_action_plan_report.git`
2. `cd ws_action_plan_report`
3. `pip install -r requirements.txt`
4. `python report_scrapper.py`

## To run for other panchayat codes
1. Modify `panchayat_codes` in report_scrapper.py

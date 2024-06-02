from dataclasses import dataclass

import pandas as pd
import requests
from bs4 import BeautifulSoup
from typing import Optional

# str -> HTML(BS) -> CustomObject -> dict -> DataFrame -> File

panchayat_codes = [64061, 64059, 64056, 64057, 64055, 64060, 64058]
link = "https://egramswaraj.gov.in/webservice/approvedActionPlanExternalReport/{}/2022-2023"


@dataclass
class PanchayatStat:
    year: str
    state: str
    district_panchayat: str
    block_panchayat: str
    village_panchayat: str

    def to_df(self) -> pd.DataFrame:
        data = {
            'Year': [self.year],
            'State': [self.state],
            'District Panchayat': [self.district_panchayat],
            'Block Panchayat': [self.block_panchayat],
            'Village Panchayat': [self.village_panchayat]
        }
        df = pd.DataFrame(data)
        return df


@dataclass
class PlanSummary:
    total_amount_tied_sc: int
    total_amount_tied_st: int
    total_amount_tied_general: int
    total_amount_tied_total: int

    total_amount_untied_sc: int
    total_amount_untied_st: int
    total_amount_untied_general: int
    total_amount_untied_total: int

    total_planned_tied_sc: int
    total_planned_tied_st: int
    total_planned_tied_general: int
    total_planned_tied_total: int

    total_planned_untied_sc: int
    total_planned_untied_st: int
    total_planned_untied_general: int
    total_planned_untied_total: int

    def to_df(self) -> pd.DataFrame:
        data = {
            'total_amount_tied_sc': [self.total_amount_tied_sc],
            'total_amount_tied_st': [self.total_amount_tied_st],
            'total_amount_tied_general': [self.total_amount_tied_general],
            'total_amount_tied_total': [self.total_amount_tied_total],
            'total_amount_untied_sc': [self.total_amount_untied_sc],
            'total_amount_untied_st': [self.total_amount_untied_st],
            'total_amount_untied_general': [self.total_amount_untied_general],
            'total_amount_untied_total': [self.total_amount_untied_total],
            'total_planned_tied_sc': [self.total_planned_tied_sc],
            'total_planned_tied_st': [self.total_planned_tied_st],
            'total_planned_tied_general': [self.total_planned_tied_general],
            'total_planned_tied_total': [self.total_planned_tied_total],
            'total_planned_untied_sc': [self.total_planned_untied_sc],
            'total_planned_untied_st': [self.total_planned_untied_st],
            'total_planned_untied_general': [self.total_planned_untied_general],
            'total_planned_untied_total': [self.total_planned_untied_total]
        }
        df = pd.DataFrame(data)
        return df


@dataclass
class SectoralView:
    sno: str
    sector: str
    planned_outlay_scheme_tied_sc: str
    planned_outlay_scheme_tied_st: str
    planned_outlay_scheme_tied_general: str
    planned_outlay_scheme_tied_total: str

    planned_outlay_scheme_untied_sc: str
    planned_outlay_scheme_untied_st: str
    planned_outlay_scheme_untied_general: str
    planned_outlay_scheme_untied_total: str

    @classmethod
    def to_df(cls, views: list["SectoralView"]):
        data = [
            {
                'sno': view.sno,
                'sector': view.sector,
                'planned_outlay_scheme_tied_sc': view.planned_outlay_scheme_tied_sc,
                'planned_outlay_scheme_tied_st': view.planned_outlay_scheme_tied_st,
                'planned_outlay_scheme_tied_general': view.planned_outlay_scheme_tied_general,
                'planned_outlay_scheme_tied_total': view.planned_outlay_scheme_tied_total,
                'planned_outlay_scheme_untied_sc': view.planned_outlay_scheme_untied_sc,
                'planned_outlay_scheme_untied_st': view.planned_outlay_scheme_untied_st,
                'planned_outlay_scheme_untied_general': view.planned_outlay_scheme_untied_general,
                'planned_outlay_scheme_untied_total': view.planned_outlay_scheme_untied_total
            }
            for view in views
        ]
        df = pd.DataFrame(data)
        return df


@dataclass
class SchemeView:
    sno: str
    scheme_name: str
    component_name: str

    amount_allocated_tied_sc: str
    amount_allocated_tied_st: str
    amount_allocated_tied_general: str
    amount_allocated_tied_total: str

    amount_allocated_untied_sc: str
    amount_allocated_untied_st: str
    amount_allocated_untied_general: str
    amount_allocated_untied_total: str

    amount_planned_outlay_tied_sc: str
    amount_planned_outlay_tied_st: str
    amount_planned_outlay_tied_general: str
    amount_planned_outlay_tied_total: str

    amount_planned_outlay_untied_sc: str
    amount_planned_outlay_untied_st: str
    amount_planned_outlay_untied_general: str
    amount_planned_outlay_untied_total: str

    @classmethod
    def to_df(cls, views: list["SchemeView"]):
        data = [
            {
                'sno': view.sno,
                'scheme_name': view.scheme_name,
                'component_name': view.component_name,
                'amount_allocated_tied_sc': view.amount_allocated_tied_sc,
                'amount_allocated_tied_st': view.amount_allocated_tied_st,
                'amount_allocated_tied_general': view.amount_allocated_tied_general,
                'amount_allocated_tied_total': view.amount_allocated_tied_total,
                'amount_allocated_untied_sc': view.amount_allocated_untied_sc,
                'amount_allocated_untied_st': view.amount_allocated_untied_st,
                'amount_allocated_untied_general': view.amount_allocated_untied_general,
                'amount_allocated_untied_total': view.amount_allocated_untied_total,
                'amount_planned_outlay_tied_sc': view.amount_planned_outlay_tied_sc,
                'amount_planned_outlay_tied_st': view.amount_planned_outlay_tied_st,
                'amount_planned_outlay_tied_general': view.amount_planned_outlay_tied_general,
                'amount_planned_outlay_tied_total': view.amount_planned_outlay_tied_total,
                'amount_planned_outlay_untied_sc': view.amount_planned_outlay_untied_sc,
                'amount_planned_outlay_untied_st': view.amount_planned_outlay_untied_st,
                'amount_planned_outlay_untied_general': view.amount_planned_outlay_untied_general,
                'amount_planned_outlay_untied_total': view.amount_planned_outlay_untied_total
            }
            for view in views
        ]
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        return df


@dataclass
class ActivityDetails:
    sno: Optional[int]
    act_code: int
    activity_name: str
    activity_desc: str
    activity_for: str
    sector: str
    mgnrega_activity_cat: str
    location_of_asset: str
    estimated_cost: int
    total_duration: str
    scheme_name: str
    general_fund: int
    sc_fund: Optional[int]
    st_fund: Optional[int]

    @classmethod
    def to_df(cls, activities: list["ActivityDetails"]) -> pd.DataFrame:
        # Create a list of dictionaries from the list of ActivityDetails instances
        data = [
            {
                'sno': activity.sno,
                'act_code': activity.act_code,
                'activity_name': activity.activity_name,
                'activity_desc': activity.activity_desc,
                'activity_for': activity.activity_for,
                'sector': activity.sector,
                'mgnrega_activity_cat': activity.mgnrega_activity_cat,
                'location_of_asset': activity.location_of_asset,
                'estimated_cost': activity.estimated_cost,
                'total_duration': activity.total_duration,
                'scheme_name': activity.scheme_name,
                'general_fun': activity.general_fund,
                'sc_fund': activity.sc_fund,
                'st_fun': activity.st_fund

            }
            for activity in activities
        ]
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        return df


def get_html(link):
    # request for HTML document of given url
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_panchayat_stat(html) -> PanchayatStat:
    p_stats = html.find('tr', class_='tblRowB')
    data = []
    for th in p_stats.find_all('th'):
        data.append(th.getText())

    return PanchayatStat(
        year=data[0],
        state=data[1],
        district_panchayat=data[2],
        block_panchayat=data[3],
        village_panchayat=data[4]
    )


def get_section1(html) -> PlanSummary:
    plan_sum = html.find('div', class_="col-12").find_next("div", class_="card").find_next("tbody").find_next("tr")
    row = plan_sum.text.split('\n')
    numbers = [int(cell) for cell in row if cell.isnumeric()]

    assert len(numbers) == 16

    return PlanSummary(
        total_amount_tied_sc=numbers[0],
        total_amount_tied_st=numbers[1],
        total_amount_tied_general=numbers[2],
        total_amount_tied_total=numbers[3],

        total_amount_untied_sc=numbers[4],
        total_amount_untied_st=numbers[5],
        total_amount_untied_general=numbers[6],
        total_amount_untied_total=numbers[7],

        total_planned_tied_sc=numbers[8],
        total_planned_tied_st=numbers[9],
        total_planned_tied_general=numbers[10],
        total_planned_tied_total=numbers[11],

        total_planned_untied_sc=numbers[12],
        total_planned_untied_st=numbers[13],
        total_planned_untied_general=numbers[14],
        total_planned_untied_total=numbers[15],
    )


def get_section2(html) -> list[SectoralView]:
    sectoral_views = []

    sec_view = html.find("div", id="collapseTwo", class_="collapse").find_next('tbody').find_all('tr')
    for row in sec_view:

        cells = row.find_all('th') + row.find_all('td')

        if len(cells) == 10:
            sectoral_views.append(
                SectoralView(
                    sno=cells[0].text,
                    sector=cells[1].text,
                    planned_outlay_scheme_tied_sc=cells[2].text,
                    planned_outlay_scheme_tied_st=cells[3].text,
                    planned_outlay_scheme_tied_general=cells[4].text,
                    planned_outlay_scheme_tied_total=cells[5].text,

                    planned_outlay_scheme_untied_sc=cells[6].text,
                    planned_outlay_scheme_untied_st=cells[7].text,
                    planned_outlay_scheme_untied_general=cells[8].text,
                    planned_outlay_scheme_untied_total=cells[9].text,
                )
            )

    return sectoral_views


def get_section3(html) -> list[SchemeView]:
    scheme_views = []

    sec_view = html.find("div", id="collapseThree", class_="collapse").find_next('tbody').find_all('tr')
    for row in sec_view:

        cells = row.find_all('td')

        if len(cells) == 19:
            scheme_views.append(
                SchemeView(
                    sno=cells[0].text,
                    scheme_name=cells[1].text,
                    component_name=cells[2].text,

                    amount_allocated_tied_sc=cells[3].text,
                    amount_allocated_tied_st=cells[4].text,
                    amount_allocated_tied_general=cells[5].text,
                    amount_allocated_tied_total=cells[6].text,

                    amount_allocated_untied_sc=cells[7].text,
                    amount_allocated_untied_st=cells[8].text,
                    amount_allocated_untied_general=cells[9].text,
                    amount_allocated_untied_total=cells[10].text,

                    amount_planned_outlay_tied_sc=cells[11].text,
                    amount_planned_outlay_tied_st=cells[12].text,
                    amount_planned_outlay_tied_general=cells[13].text,
                    amount_planned_outlay_tied_total=cells[14].text,

                    amount_planned_outlay_untied_sc=cells[15].text,
                    amount_planned_outlay_untied_st=cells[16].text,
                    amount_planned_outlay_untied_general=cells[17].text,
                    amount_planned_outlay_untied_total=cells[18].text,
                )
            )
        elif len(cells) == 17:
            scheme_views.append(
                SchemeView(
                    sno="",
                    scheme_name=cells[0].text,
                    component_name="",

                    amount_allocated_tied_sc=cells[3].text,
                    amount_allocated_tied_st=cells[4].text,
                    amount_allocated_tied_general=cells[5].text,
                    amount_allocated_tied_total=cells[6].text,

                    amount_allocated_untied_sc=cells[7].text,
                    amount_allocated_untied_st=cells[8].text,
                    amount_allocated_untied_general=cells[9].text,
                    amount_allocated_untied_total=cells[10].text,

                    amount_planned_outlay_tied_sc=cells[11].text,
                    amount_planned_outlay_tied_st=cells[12].text,
                    amount_planned_outlay_tied_general=cells[13].text,
                    amount_planned_outlay_tied_total=cells[14].text,

                    amount_planned_outlay_untied_sc=cells[15].text,
                    amount_planned_outlay_untied_st=cells[16].text,
                    amount_planned_outlay_untied_general=cells[17].text,
                    amount_planned_outlay_untied_total=cells[18].text,
                )
            )

    return scheme_views


def get_section4(html) -> list[ActivityDetails]:
    activity_details = []

    act_view = html.find("div", id="collapseFour", class_="collapse").find_next('tbody').find_all('tr')
    for row in act_view:

        cells = row.find_all('td')

        print(len(cells))

        if len(cells) == 14:
            activity_details.append(
                ActivityDetails(
                    sno=int(cells[0].text),
                    act_code=int(cells[1].text),
                    activity_name=cells[2].text,
                    activity_desc=cells[3].text,
                    activity_for=cells[4].text.strip(),
                    sector=cells[5].text,
                    mgnrega_activity_cat=cells[6].text,
                    location_of_asset=cells[7].text,
                    estimated_cost=int(cells[8].text),
                    total_duration=cells[9].text,
                    scheme_name=cells[10].text,
                    general_fund=cells[11].text,
                    sc_fund=int(cells[12].text),
                    st_fund=int(cells[13].text)
                )
            )

        elif len(cells) == 8:
            activity_details.append(
                ActivityDetails(
                    sno=None,
                    act_code=cells[1].text,
                    activity_name="",
                    activity_desc="",
                    activity_for="",
                    sector="",
                    mgnrega_activity_cat="",
                    location_of_asset="",
                    estimated_cost=int(cells[2].text),
                    total_duration="",
                    scheme_name="",
                    general_fund=int(cells[5].text),
                    sc_fund=None,
                    st_fund=None
                )
            )

    return activity_details


def make_xls(writer, p_stat: PanchayatStat, section1: PlanSummary, section2: list[SectoralView],
             section3: list[SchemeView], section4: list[ActivityDetails]):
    worksheet = writer.book.add_worksheet(p_stat.village_panchayat)
    writer.sheets[p_stat.village_panchayat] = worksheet

    heading = writer.book.add_format({'bold': True, 'font_size': 20, 'font_color': 'red'})
    heading1 = writer.book.add_format({'bold': True, 'font_size': 15})


    worksheet.write(0, 0, "Approved Action Plan", heading)
    p_stat.to_df().to_excel(writer, sheet_name=p_stat.village_panchayat, startrow=2, startcol=0)

    worksheet.write(5, 0, "Plan Summary", heading1)
    section1.to_df().to_excel(writer, sheet_name=p_stat.village_panchayat, startrow=7, startcol=0)

    worksheet.write(10, 0, "Sectoral View", heading1)
    SectoralView.to_df(section2).to_excel(writer, sheet_name=p_stat.village_panchayat, startrow=12, startcol=0)

    worksheet.write(14 + len(section2), 0, "Scheme View", heading1)
    SchemeView.to_df(section3).to_excel(writer, sheet_name=p_stat.village_panchayat, startrow=16 + len(section2),
                                        startcol=0)

    worksheet.write(18 + len(section2) + len(section3), 0, "Activity Details", heading1)
    ActivityDetails.to_df(section4).to_excel(writer, sheet_name=p_stat.village_panchayat,
                                             startrow=20 + len(section2) + len(section3), startcol=0)


def main():
    writer = pd.ExcelWriter("panchayat.xlsx", engine='xlsxwriter')

    for pc in panchayat_codes:
        pc_link = link.format(pc)

        html = get_html(pc_link)

        p_stat = get_panchayat_stat(html)
        section1 = get_section1(html)
        section2 = get_section2(html)
        section3 = get_section3(html)
        section4 = get_section4(html)

        make_xls(writer, p_stat, section1, section2, section3, section4)

    writer.close()


if __name__ == '__main__':
    main()
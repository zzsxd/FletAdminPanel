#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
from flet import *
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from flet_navigator import PageData
from UI.sidebar import SideBar
#################################################


class Med_profile:
    def __init__(self, vault, config, db):
        super(Med_profile, self).__init__()
        self.__vault = vault
        self.__config = config

    def med_profile(self, pg: PageData):
        pg.page.title = "Мед. профили"
        pg.page.theme_mode = 'dark'
        pg.page.add(
            Row(
                [
                Container(
                    content=SideBar(self.__vault, pg),
                    ),
                VerticalDivider(width=1),
            ],
                expand=True,
            )
        )
        pg.page.update()
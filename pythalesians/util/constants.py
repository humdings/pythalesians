__author__ = 'saeedamen' # Saeed Amen / saeed@pythalesians.com

#
# Copyright 2015 Thalesians Ltd. - http//www.pythalesians.com / @pythalesians
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and limitations under the License.
#

"""
Constants

Has various constants required for the project. Before running the project, you will need to modify
root_pythalesians_folder, for logging and also chart stylesheets amongst other things.

"""

import os

class Constants:
    def __init__(self):

        ###### CHANGE THIS TO REFER TO YOUR OWN ROOT FOLDER
        self.root_pythalesians_folder = "D:/Remote/pythalesians/pythalesians/"
        self.temp_pythalesians_folder = self.root_pythalesians_folder + "temp"

        ###### FOR FUTURE VERSIONS (which include caching) - DO NOT REMOVE!
        # folders for holding market data
        self.folder_time_series_data = "D:/timeseriesdata"
        self.folder_historic_CSV = "D:/tickdata/historicCSV"

        # config file for time series categories
        self.time_series_categories_fields = \
             self.root_pythalesians_folder + "conf/time_series_categories_fields.csv"

        # we can have multiple tickers files (separated by ";")
        self.time_series_tickers_list = self.root_pythalesians_folder + "conf/time_series_tickers_list.csv;" + \
                                         self.root_pythalesians_folder + "conf/g10_vol_tickers.csv"

        self.time_series_fields_list = self.root_pythalesians_folder + "conf/time_series_fields_list.csv"

        # for events filtering
        self.events_category = 'events'
        self.events_category_dt = 'events_dt'

        ###### FOR CURRENT VERSION

        # which timeseriesfactory type to use?
        # note: lighttimeseriesfactory currently implemented
        #       cachedtimeseriesfactory will be added in due course
        self.default_time_series_factory = "lighttimeseriesfactory"

        # log config file
        self.logging_conf = self.root_pythalesians_folder + "conf/logging.conf"

        # Bloomberg settings
        self.bbg_default_api = 'open-api'   # allowed values 'open-api' (newer & recommended) and 'com-api' (older style API)
        self.bbg_server = "localhost"       # needs changing if you use Bloomberg Server API
        self.bbg_server_port = 8194

        # Dukascopy settings
        self.dukascopy_base_url = "http://www.dukascopy.com/datafeed/"
        self.dukascopy_write_temp_tick_disk = False

        # for plots
        self.plotfactory_default_adapter = "pythalesians"
        self.plotfactory_source = "Thalesians/BBG (created with PyThalesians Python library)"
        self.plotfactory_brand_label = "@thalesians"
        self.plotfactory_display_source_label = True
        self.plotfactory_display_brand_label = True
        self.plotfactory_brand_colour = "#5B9BD5"

        self.plotfactory_default_stylesheet = "pythalesians"

        self.plotfactory_pythalesians_style_sheet = {"pythalesians" : self.root_pythalesians_folder + "conf/stylesheets/pythalesians.mplstyle",
                                                     "538-pythalesians" : self.root_pythalesians_folder + "conf/stylesheets/538-pythalesians.mplstyle",
                                                     "miletus-pythalesians" : self.root_pythalesians_folder + "conf/stylesheets/miletus-pythalesians.mplstyle",
                                                     "ggplot-pythalesians" : self.root_pythalesians_folder + "conf/stylesheets/ggplot-pythalesians.mplstyle",
                                                     "ggplot-traditional" : self.root_pythalesians_folder + "conf/stylesheets/ggplot-traditional.mplstyle"}

        self.plotfactory_scale_factor = 1
        self.plotfactory_dpi = 100
        self.plotfactory_width = 543
        self.plotfactory_height = 381

        ########## BOKEH SETTINGS
        self.bokeh_font       = 'calibri'
        self.bokeh_font_style = "normal"
        self.bokeh_palette = [  '#E24A33',
                                '#348ABD',
                                '#988ED5',
                                '#777777',
                                '#FBC15E',
                                '#8EBA42',
                                '#FFB5B8']

        ########## PLOTLY SETTINGS
        self.plotly_world_readable = False

        ########## API KEYS

        # Plotly default username
        self.plotly_default_username = 'argonautae'

        # Plotly settings (username : api_key)
        self.plotly_creds = {"x" : "x",
                             "x1" : "x1"
                             }

        self.plotly_streaming_key = "x2"

        # Quandl settings
        self.quandl_api_key = "x"

        # Twitter settings (you need to set these up on Twitter)
        self.APP_KEY             = "x"
        self.APP_SECRET          = "x"
        self.OAUTH_TOKEN	     = "x"
        self.OAUTH_TOKEN_SECRET	 = "x"

        ##### Colors for plotting
         # 'red'   :   '#E24A33',
            # 'blue'  :   '#348ABD',
            # 'purple':   '#988ED5',
            # 'gray'  :   '#777777',
            # 'yellow':   '#FBC15E',
            # 'green' :   '#8EBA42',
            # 'pink'  :   '#FFB5B8'

        # nicer than the default colors of matplotlib (fully editable!)
        # list of colors from http://www.github.com/santosjorge/cufflinks project
        # where I've overwritten some of the primary colours (with the above)
        self.plotfactory_color_overwrites = {
            'aliceblue':         '#F0F8FF',
            'antiquewhite':	     '#FAEBD7',
            'aqua':			     '#00FFFF',
            'aquamarine':		 '#7FFFD4',
            'azure':			 '#F0FFFF',
            'beige':			 '#F5F5DC',
            'bisque':			 '#FFE4C4',
            'black':			 '#000000',
            'blanchedalmond':	 '#FFEBCD',
            'blue':			     '#348ABD', # '#3780bf',
            'bluegray':		     '#565656',
            'bluepurple':		 '#6432AB',
            'blueviolet':		 '#8A2BE2',
            'brick':			 '#E24A33',
            'brightblue':		 '#0000FF',
            'brightred':		 '#FF0000',
            'brown':			 '#A52A2A',
            'burlywood':		 '#DEB887',
            'cadetblue':		 '#5F9EA0',
            'charcoal':		     '#151516',
            'chartreuse':		 '#7FFF00',
            'chocolate':		 '#D2691E',
            'coral':			 '#FF7F50',
            'cornflowerblue':	 '#6495ED',
            'cornsilk':		     '#FFF8DC',
            'crimson':			 '#DC143C',
            'cyan':			     '#00FFFF',
            'darkblue':		     '#00008B',
            'darkcyan':		     '#008B8B',
            'darkgoldenrod':	 '#B8860B',
            'darkgray':		     '#A9A9A9',
            'darkgreen':		 '#006400',
            'darkgrey':		     '#A9A9A9',
            'darkkhaki':		 '#BDB76B',
            'darkmagenta':		 '#8B008B',
            'darkolivegreen':	 '#556B2F',
            'darkorange':		 '#FF8C00',
            'darkorchid':		 '#9932CC',
            'darkred':			 '#8B0000',
            'darksalmon':		 '#E9967A',
            'darkseagreen':	     '#8FBC8F',
            'darkslateblue':	 '#483D8B',
            'darkslategray':	 '#2F4F4F',
            'darkslategrey':	 '#2F4F4F',
            'darkturquoise':	 '#00CED1',
            'darkviolet':		 '#9400D3',
            'deeppink':		     '#FF1493',
            'deepskyblue':		 '#00BFFF',
            'dimgray':			 '#696969',
            'dimgrey':			 '#696969',
            'dodgerblue':		 '#1E90FF',
            'firebrick':		 '#B22222',
            'floralwhite':		 '#FFFAF0',
            'forestgreen':		 '#228B22',
            'fuchsia':			 '#FF00FF',
            'gainsboro':		 '#DCDCDC',
            'ghostwhite':		 '#F8F8FF',
            'gold':			     '#FFD700',
            'goldenrod':		 '#DAA520',
            'grassgreen':		 '#32ab60',
            'gray':			     '#777777', # '#808080',
            'green':			 '#8EBA42', # '#008000',
            'greenyellow':		 '#ADFF2F',
            'grey':			     '#808080',
            'grey01':			 '#0A0A0A',
            'grey02':			 '#151516',
            'grey03':			 '#1A1A1C',
            'grey04':			 '#1E1E21',
            'grey05':			 '#252529',
            'grey06':			 '#36363C',
            'grey07':			 '#3C3C42',
            'grey08':			 '#434343',
            'grey09':			 '#666570',
            'grey10':			 '#666666',
            'grey11':			 '#8C8C8C',
            'grey12':			 '#C2C2C2',
            'grey13':			 '#E2E2E2',
            'honeydew':		     '#F0FFF0',
            'hotpink':			 '#FF69B4',
            'indianred':		 '#CD5C5C',
            'indigo':			 '#4B0082',
            'ivory':			 '#FFFFF0',
            'khaki':			 '#F0E68C',
            'lavender':		     '#E6E6FA',
            'lavenderblush':	 '#FFF0F5',
            'lawngreen':		 '#7CFC00',
            'lemonchiffon':	     '#FFFACD',
            'lightpink2':		 '#fccde5',
            'lightpurple':		 '#bc80bd',
            'lightblue':		 '#ADD8E6',
            'lightcoral':		 '#F08080',
            'lightcyan':		 '#E0FFFF',
            'lightgoldenrodyellow':	 '#FAFAD2',
            'lightgray':		 '#D3D3D3',
            'lightgreen':		 '#90EE90',
            'lightgrey':		 '#D3D3D3',
            'lightpink':		 '#FFB6C1',
            'lightsalmon':		 '#FFA07A',
            'lightseagreen':	 '#20B2AA',
            'lightskyblue':	     '#87CEFA',
            'lightslategray':	 '#778899',
            'lightslategrey':	 '#778899',
            'lightsteelblue':	 '#B0C4DE',
            'lightteal':		 '#8dd3c7',
            'lightyellow':		 '#FFFFE0',
            'lightblue2':		 '#80b1d3',
            'lightviolet':		 '#8476CA',
            'lime':			     '#00FF00',
            'lime2':			 '#8EBA42',
            'limegreen':		 '#32CD32',
            'linen':			 '#FAF0E6',
            'magenta':			 '#FF00FF',
            'maroon':			 '#800000',
            'mediumaquamarine':  '#66CDAA',
            'mediumblue':		 '#0000CD',
            'mediumgray' : 	     '#656565',
            'mediumorchid':	     '#BA55D3',
            'mediumpurple':	     '#9370DB',
            'mediumseagreen':	 '#3CB371',
            'mediumslateblue':	 '#7B68EE',
            'mediumspringgreen': '#00FA9A',
            'mediumturquoise':	 '#48D1CC',
            'mediumvioletred':	 '#C71585',
            'midnightblue':	     '#191970',
            'mintcream':		 '#F5FFFA',
            'mistyrose':		 '#FFE4E1',
            'moccasin':		     '#FFE4B5',
            'mustard':			 '#FBC15E',
            'navajowhite':		 '#FFDEAD',
            'navy':			     '#000080',
            'oldlace':			 '#FDF5E6',
            'olive':			 '#808000',
            'olivedrab':		 '#6B8E23',
            'orange':			 '#FF9900', # '#ff9933',
            'orangered':		 '#FF4500',
            'orchid':			 '#DA70D6',
            'palegoldenrod':	 '#EEE8AA',
            'palegreen':		 '#98FB98',
            'paleolive':		 '#b3de69',
            'paleturquoise':	 '#AFEEEE',
            'palevioletred':	 '#DB7093',
            'papayawhip':		 '#FFEFD5',
            'peachpuff':		 '#FFDAB9',
            'pearl':			 '#D9D9D9',
            'pearl02':			 '#F5F6F9',
            'pearl03':			 '#E1E5ED',
            'pearl04':			 '#9499A3',
            'pearl05':			 '#6F7B8B',
            'pearl06':			 '#4D5663',
            'peru':			     '#CD853F',
            'pink':			     '#FFB5B8', #'#ff0088',
            'pinksalmon':		 '#FFB5B8',
            'plum':			     '#DDA0DD',
            'powderblue':		 '#B0E0E6',
            'purple':			 '#988ED5', #'#800080',
            'red':				 '#E24A33', #'#db4052',
            'rose':			     '#FFC0CB',
            'rosybrown':		 '#BC8F8F',
            'royalblue':		 '#4169E1',
            'saddlebrown':		 '#8B4513',
            'salmon':			 '#fb8072',
            'sandybrown':		 '#FAA460',
            'seaborn':			 '#EAE7E4',
            'seagreen':		     '#2E8B57',
            'seashell':		     '#FFF5EE',
            'sienna':			 '#A0522D',
            'silver':			 '#C0C0C0',
            'skyblue':			 '#87CEEB',
            'slateblue':		 '#6A5ACD',
            'slategray':		 '#708090',
            'slategrey':		 '#708090',
            'smurf':			 '#3E6FB0',
            'snow':			     '#FFFAFA',
            'springgreen':		 '#00FF7F',
            'steelblue':		 '#4682B4',
            'tan':				 '#D2B48C',
            'teal':			     '#008080',
            'thistle':			 '#D8BFD8',
            'tomato':			 '#FF6347',
            'turquoise':		 '#40E0D0',
            'violet':			 '#EE82EE',
            'wheat':			 '#F5DEB3',
            'white':			 '#FFFFFF',
            'whitesmoke':		 '#F5F5F5',
            'yellow':			 '#FBC15E', #'#ffff33',
            'yellowgreen':		 '#9ACD32'
        }

        # plot Bokeh settings
        self.plotfactory_bokeh_palette =    ['#E24A33',
                                             '#348ABD',
                                             '#988ED5',
                                             '#777777',
                                             '#FBC15E',
                                             '#8EBA42',
                                             '#FFB5B8']
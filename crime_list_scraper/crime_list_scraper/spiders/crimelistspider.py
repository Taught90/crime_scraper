import scrapy


class CrimelistspiderSpider(scrapy.Spider):
    name = "crimelistspider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate"]

    def parse(self, response):
        content = response.css('table.wikitable tbody tr')

        for column in content:
            column = content.css('td')

            state = column[0].css('a::text').get(default=column[0].css('::text').get(default='')).strip()
            city = column[1].css('::text').get(default='').strip()
            population = column[2].css('::text').get(default='').strip()
            total_crimes = column[3].css('::text').get(default='').strip()
            murder = column[4].css('::text').get(default='').strip()
            rape = column[5].css('::text').get(default='').strip()
            robbery = column[6].css('::text').get(default='').strip()
            assault = column[7].css('::text').get(default='').strip()
            total_violent_crime = column[8].css('::text').get(default='').strip()
            arson = column[9].css('::text').get(default='').strip()
            burglary = column[10].css('::text').get(default='').strip()
            theft = column[11].css('::text').get(default='').strip()
            total_property_crime = column[12].css('::text').get(default='').strip()

            yield{
                "State": state,
                "City": city,
                "Population": population,
                "Murder": murder,
                "Robbery": robbery,
                "Assault": assault,
                "Arson": arson,
                "Burlgary": burglary,
                "Theft": theft,
                "Total_number_of_crimes": total_crimes
            }

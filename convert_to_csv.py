import csv
import covid


def convert_to_csv(filename):
    report = covid.get_report()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # headers
        writer.writerow(['Day', 'Month', 'Year', 'Cases', 'Deaths', 'Population', 'Rate', 'Country', 'Code', 'Continent'])

        # write data
        for item in report:
            row = [
                item['Date']['Day'],
                item['Date']['Month'],
                item['Date']['Year'],
                item['Data']['Cases'],
                item['Data']['Deaths'],
                item['Data']['Population'],
                item['Data']['Rate'],
                item['Location']['Country'],
                item['Location']['Code'],
                item['Location']['Continent']
            ]
            writer.writerow(row)


convert_to_csv('covid_data.csv')

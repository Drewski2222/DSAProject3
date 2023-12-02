#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;

struct data {
    int day, month, year;
    int cases, deaths, population;
    double rate;
    string country, code, continent;
};

// load CSV file into vector of data
vector<data> read_csv(const string& filename) {
    vector<data> full_data;
    ifstream file(filename);
    string line, token;
    getline(file, line);

    while (getline(file, line)) {
        istringstream ss(line);
        data record;
        getline(ss, token, ','); record.day = stoi(token);
        getline(ss, token, ','); record.month = stoi(token);
        getline(ss, token, ','); record.year = stoi(token);
        getline(ss, token, ','); record.cases = stoi(token);
        getline(ss, token, ','); record.deaths = stoi(token);
        getline(ss, token, ','); record.population = stoi(token);
        getline(ss, token, ','); record.rate = stod(token);
        getline(ss, token, ','); record.country = token;
        getline(ss, token, ','); record.code = token;
        getline(ss, token, ','); record.continent = token;

        full_data.push_back(record);
    }
    return full_data;
}

int main() {
    string filename = R"(H:\Coding\Project3_Python\covid_data.csv)";
    auto full_data = read_csv(filename);
    int choice;
    cout << "Key to sort data by? (1 = cases, 2 = deaths, 3 = rate)" << endl;
    cin >> choice;

    if (choice == 1) {
        auto time1 = chrono::high_resolution_clock::now();
        sort(full_data.begin(), full_data.end(), [](data& a, data& b) {
            return a.cases < b.cases;
        });
    } else if (choice == 2) {
        auto time1 = chrono::high_resolution_clock::now();
        sort(full_data.begin(), full_data.end(), [](data& a, data& b) {
            return a.deaths < b.deaths;
        });
    } else if (choice == 3) {
        auto time1 = chrono::high_resolution_clock::now();
        sort(full_data.begin(), full_data.end(), [](data& a, data& b) {
            return a.rate < b.rate;
        });
    }

    // stop timer
    auto time2 = chrono::high_resolution_clock::now();

    // calculate duration
    auto duration = chrono::duration<double>(time2 - time1).count();
    cout << "Sorting completed in " << duration << " seconds." << endl;

    // output first 10 sorted items
    for (int i = 0; i < 10 && i < full_data.size(); ++i) {
        auto& item = full_data[i];
        cout << "Date: " << item.month << "/" << item.day << "/" << item.year << ", Cases: " << item.cases
        << ", Deaths: " << item.deaths << ", Population: " << item.population << ", Rate: " << item.rate << ", Country: " << item.country << endl;
    }

    return 0;
}

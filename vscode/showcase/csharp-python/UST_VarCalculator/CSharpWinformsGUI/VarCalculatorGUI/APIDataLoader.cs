using System.Text;
using System.Net.Http;
using System.Threading.Tasks;
using System.Configuration;
using Newtonsoft.Json;

namespace VarCalculatorGUI
{
    internal class APIDataLoader
    {
        private readonly HttpClient _client;
        private readonly string apiBaseUrl = ConfigurationManager.AppSettings["ApiBaseUrl"]; 

        public APIDataLoader()
        {
            _client = new HttpClient();
        }

        public async Task<string> GetInstrumentList()
        {
            var response = await _client.GetAsync($"{apiBaseUrl}/GetInstrumentList");
            return await response.Content.ReadAsStringAsync();
        }

        public async Task<string> CalculatePortfolioYield(Weights weights)
        {
            var json = JsonConvert.SerializeObject(weights);
            var data = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await _client.PostAsync($"{apiBaseUrl}/CalculatePortfolioYield", data);
            return await response.Content.ReadAsStringAsync();
        }

        public async Task<string> CalculateVar_HistoricalSimulation(float confidenceLevel, Weights weights)
        {
            var json = JsonConvert.SerializeObject(weights);
            var data = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await _client.PostAsync($"{apiBaseUrl}/CalculateVar_HistoricalSimulation/{confidenceLevel}", data);
            return await response.Content.ReadAsStringAsync();
        }

        public async Task<string> CalculateVar_Parametric(float confidenceLevel, Weights weights)
        {
            var json = JsonConvert.SerializeObject(weights);
            var data = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await _client.PostAsync($"{apiBaseUrl}/CalculateVar_Parametric/{confidenceLevel}", data);
            return await response.Content.ReadAsStringAsync();
        }

        public async Task<string> CalculateDV01()
        {
            var response = await _client.GetAsync($"{apiBaseUrl}/CalculateDV01");
            return await response.Content.ReadAsStringAsync();
        }
    }
   
}

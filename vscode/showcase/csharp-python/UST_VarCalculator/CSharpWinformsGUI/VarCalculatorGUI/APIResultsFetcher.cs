using Newtonsoft.Json;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace VarCalculatorGUI
{
    internal class APIResultsFetcher
    {
        public List<string> InstrumentList { get; set; }
        public YieldData PortfolioYield { get; set; }
        public float Var_HistoricalSimulation95 { get; set; }
        public float Var_HistoricalSimulation99 { get; set; }
        public float Var_Parametric95 { get; set; }
        public float Var_Parametric99 { get; set; }
        public YieldData DV01 { get; set; }

        public async Task FetchAPIResults(Weights weights)
        {
            var dataLoader = new APIDataLoader();
            var confidenceLevel95 = 0.05f;
            var confidenceLevel99 = 0.01f;

            //takes care of the custom json deserializer registration
            var settings = new JsonSerializerSettings();
            settings.Converters.Add(new YieldDataConverter());

            InstrumentList = JsonConvert.DeserializeObject<List<string>>(await dataLoader.GetInstrumentList());
            PortfolioYield = JsonConvert.DeserializeObject<YieldData>(await dataLoader.CalculatePortfolioYield(weights), settings);

            Var_HistoricalSimulation95 = JsonConvert.DeserializeObject<float>(await dataLoader.CalculateVar_HistoricalSimulation(confidenceLevel95, weights)) * 100;
            Var_HistoricalSimulation99 = JsonConvert.DeserializeObject<float>(await dataLoader.CalculateVar_HistoricalSimulation(confidenceLevel99, weights)) * 100;
            Var_Parametric95 = JsonConvert.DeserializeObject<float>(await dataLoader.CalculateVar_Parametric(confidenceLevel95, weights)) * 100;
            Var_Parametric99 = JsonConvert.DeserializeObject<float>(await dataLoader.CalculateVar_Parametric(confidenceLevel99, weights)) * 100;
            DV01 = JsonConvert.DeserializeObject<YieldData>(await dataLoader.CalculateDV01(), settings);
        }
    }
}

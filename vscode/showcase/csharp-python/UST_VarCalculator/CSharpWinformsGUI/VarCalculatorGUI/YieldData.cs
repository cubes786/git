using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;

namespace VarCalculatorGUI
{
    public class YieldData
    {       
        public Dictionary<string, List<Tuple<DateTime, float>>> Data { get; set; }
    }

    public class YieldDataConverter : JsonConverter
    {
        public override bool CanConvert(Type objectType)
        {
            return (objectType == typeof(YieldData));
        }

        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            var jObject = JObject.Load(reader);
            var yieldData = new YieldData();
            yieldData.Data = new Dictionary<string, List<Tuple<DateTime, float>>>();

            foreach (var property in jObject.Properties())
            {
                var innerDictionary = new List<Tuple<DateTime, float>>();
                foreach (var dateValue in (JObject)property.Value)
                {
                    innerDictionary.Add(new Tuple<DateTime, float>(DateTime.Parse(dateValue.Key), dateValue.Value.Value<float>()));
                }
                yieldData.Data.Add(property.Name, innerDictionary);
            }

            return yieldData;
        }

        public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
        {
            throw new NotImplementedException();
        }
    }
}

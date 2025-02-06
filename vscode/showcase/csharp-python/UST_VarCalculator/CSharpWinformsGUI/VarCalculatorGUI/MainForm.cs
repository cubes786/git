using System;
using System.Collections.Generic;
using System.Configuration;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;

namespace VarCalculatorGUI
{
    public partial class MainForm : Form
    {
        APIResultsFetcher apiFetcher = new APIResultsFetcher();
        public MainForm()
        {
            InitializeComponent();         
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dateTimePicker1.Format = DateTimePickerFormat.Custom;
            dateTimePicker1.CustomFormat = "MM-dd-yyyy";

            dateTimePicker2.Format = DateTimePickerFormat.Custom;
            dateTimePicker2.CustomFormat = "MM-dd-yyyy";

            // Read startdate and enddate from App.config
            string startdate = ConfigurationManager.AppSettings["startdate"];
            string enddate = ConfigurationManager.AppSettings["enddate"];

            // Parse the dates and set the Value property of the DateTimePickers
            dateTimePicker1.Value = DateTime.ParseExact(startdate, "MM-dd-yyyy", CultureInfo.InvariantCulture);
            dateTimePicker2.Value = DateTime.ParseExact(enddate, "MM-dd-yyyy", CultureInfo.InvariantCulture);

            //initialize the initial weights to various FI instruments
            tb4W.Text = ConfigurationManager.AppSettings["4W_Weight"];
            tb8W.Text = ConfigurationManager.AppSettings["8W_Weight"];
            tb13W.Text = ConfigurationManager.AppSettings["13W_Weight"];
            tb26W.Text = ConfigurationManager.AppSettings["26W_Weight"];
            tb52W.Text = ConfigurationManager.AppSettings["52W_Weight"];
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            // Parse TextBox values
            decimal weight4W = decimal.Parse(tb4W.Text);
            decimal weight8W = decimal.Parse(tb8W.Text);
            decimal weight13W = decimal.Parse(tb13W.Text);
            decimal weight26W = decimal.Parse(tb26W.Text);
            decimal weight52W = decimal.Parse(tb52W.Text);

            // Calculate total weight
            decimal totalWeight = weight4W + weight8W + weight13W + weight26W + weight52W;

            // Validate total weight
            if (totalWeight != 1.0m)
            {
                MessageBox.Show("Invalid weights. The total should be 1.0. Please check.", "Error in Portfolio Weights");
                return;
            }

            Weights weights = new Weights();
            weights.weights = new Dictionary<string, decimal>() { { "4W", weight4W },
                                                                  { "8W", weight8W },
                                                                  { "13W", weight13W },
                                                                  { "26W", weight26W },
                                                                  { "52W", weight52W }
                                                                };
            
            await apiFetcher.FetchAPIResults(weights);

            //set the results on GUI
            tbHS95.Text = apiFetcher.Var_HistoricalSimulation95.ToString("F2");
            tbHS99.Text = apiFetcher.Var_HistoricalSimulation99.ToString("F2");
            tbPM95.Text = apiFetcher.Var_Parametric95.ToString("F2");
            tbPM99.Text = apiFetcher.Var_Parametric99.ToString("F2");

            //plot the charts
            // Assuming chartYield is your Chart control
            chartYield.Series.Clear();

            // Set the title of the chart
            chartYield.Titles.Clear();
            var title = new System.Windows.Forms.DataVisualization.Charting.Title
            {
                Text = "Yield vs DV01 Analysis",
                Font = new Font("Arial", 16, FontStyle.Bold)
            };
            chartYield.Titles.Add(title);

            // Make the axis titles bold and bigger
            var chartArea = chartYield.ChartAreas[0];           
            chartArea.AxisY.Title = "Yield";
            chartArea.AxisY.TitleFont = new Font("Arial", 12, FontStyle.Bold);
            chartArea.AxisY2.Title = "USD";
            chartArea.AxisY2.TitleFont = new Font("Arial", 12, FontStyle.Bold);

            foreach (var kvp in apiFetcher.PortfolioYield.Data)
            {
                var series = chartYield.Series.Add(kvp.Key);
                series.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
                if (series.Name == "Portfolio_Yield" || series.Name == "Portfolio_Delta_Yield")
                {
                    series.BorderWidth = 2;
                }

                foreach (var tuple in kvp.Value)
                {
                    series.Points.AddXY(tuple.Item1, tuple.Item2);
                }
            }

            //Plot DV01 on secondary Y-axis
            foreach (var kvp in apiFetcher.DV01.Data)
            {
                if (kvp.Key.EndsWith("_Yield"))
                    continue; 
                
                var series = chartYield.Series.Add(kvp.Key);
                series.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
                series.YAxisType = System.Windows.Forms.DataVisualization.Charting.AxisType.Secondary; // Use the secondary Y-axis

                foreach (var tuple in kvp.Value)
                {
                    series.Points.AddXY(tuple.Item1, tuple.Item2);
                }
            }

            // Configure the secondary Y-axis
            var yAxis = chartYield.ChartAreas[0].AxisY2;
            yAxis.Enabled = System.Windows.Forms.DataVisualization.Charting.AxisEnabled.True;
            yAxis.LabelStyle.Format = "{0:C4}"; // Format as currency


            //enable all CBs
            cbDV26W.Checked = true;
            cbY26W.Checked = true;
            cbDV52W.Checked = true;
            cbY52W.Checked = true;
            cbDV13W.Checked = true;
            cbY13W.Checked = true;
            cbDV8W.Checked = true;
            cbY8W.Checked = true;
            cbDV4W.Checked = true;
            cbY4W.Checked = true;
            cbPFDeltaYield.Checked = true;

        }

        private void ToggleCurve(string curve, bool enable)
        {
            // Assuming chartYield is your Chart control
            var series = chartYield.Series.FindByName(curve);
            if (series != null)
            {
                series.Enabled = enable;
            }
            else
            {
                Console.WriteLine($"Curve {curve} not found.");
            }
        }

        private void cbY4W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbY4W.Checked)
            {
                ToggleCurve("4W_Yield", true);
            }
            else
            {
                ToggleCurve("4W_Yield", false);
            }
        }

        private void cbY8W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbY8W.Checked)
            {
                ToggleCurve("8W_Yield", true);
            }
            else
            {
                ToggleCurve("8W_Yield", false);
            }
        }

        private void cbY13W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbY13W.Checked)
            {
                ToggleCurve("13W_Yield", true);
            }
            else
            {
                ToggleCurve("13W_Yield", false);
            }
        }

        private void cbY26W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbY26W.Checked)
            {
                ToggleCurve("26W_Yield", true);
            }
            else
            {
                ToggleCurve("26W_Yield", false);
            }
        }

        private void cbY52W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbY52W.Checked)
            {
                ToggleCurve("52W_Yield", true);
            }
            else
            {
                ToggleCurve("52W_Yield", false);
            }
        }

        private void cbDV4W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbDV4W.Checked)
            {
                ToggleCurve("4W_DV01", true);
            }
            else
            {
                ToggleCurve("4W_DV01", false);
            }
        }

        private void cbDV8W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbDV8W.Checked)
            {
                ToggleCurve("8W_DV01", true);
            }
            else
            {
                ToggleCurve("8W_DV01", false);
            }
        }

        private void cbDV13W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbDV13W.Checked)
            {
                ToggleCurve("13W_DV01", true);
            }
            else
            {
                ToggleCurve("13W_DV01", false);
            }
        }

        private void cbDV26W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbDV26W.Checked)
            {
                ToggleCurve("26W_DV01", true);
            }
            else
            {
                ToggleCurve("26W_DV01", false);
            }
        }

        private void cbDV52W_CheckedChanged(object sender, EventArgs e)
        {
            if (cbDV52W.Checked)
            {
                ToggleCurve("52W_DV01", true);
            }
            else
            {
                ToggleCurve("52W_DV01", false);
            }
        }

        private void cbPFDeltaYield_CheckedChanged(object sender, EventArgs e)
        {
            if (cbPFDeltaYield.Checked)
            {
                ToggleCurve("Portfolio_Yield", true);
                ToggleCurve("Portfolio_Delta_Yield", true);
            }
            else
            {
                ToggleCurve("Portfolio_Yield", false);
                ToggleCurve("Portfolio_Delta_Yield", false);
            }
        }
    }
}

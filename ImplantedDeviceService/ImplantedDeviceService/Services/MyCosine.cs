namespace ImplantedDeviceService.Services
{
    //I can probably extract functionality from this class into an interface
    //and make it more generic for extensibility
    public class MyCosine
    {
        public MyCosine() { }
        private double coefficient_a;
        private double coefficient_b;
        private double coefficient_c;
        private double coefficient_d;
        public double SampleRate { get; set; }
        public int SampleCount { get; set; }
        public double Amplitude
        {
            get
            {
                return coefficient_a;
            }
            set => coefficient_a = value;
        }
        public double PhaseShift
        {
            get
            {
                return -1 * coefficient_c;
            }
            set
            {
                coefficient_c = value * -1;
            }
        }
        public double Frequency
        {
            get
            {
                return (coefficient_b / 2 * Math.PI);
            }
            set
            {
                coefficient_b = value * 2 * Math.PI;
            }
        }
        public double VerticalShift
        {
            get
            {
                return coefficient_d;
            }
            set => coefficient_d = value;
        }

        private double GetYCoordinate(double x_coordinate)
        {
            return (coefficient_a * Math.Cos(coefficient_b * (x_coordinate + coefficient_c))) + coefficient_d;
        }
        public List<MyPoint> GetSamples()
        {
            //we need 1/samplerate, starting at time = 0
            //maybe change the graph start point eventually
            List<MyPoint> samples = new List<MyPoint>();
            for(int i = 0; i < SampleCount; i++)
            {
                double x = i * (1 / SampleRate);
                samples.Add(new MyPoint(x,GetYCoordinate(x)));
            }
            return samples;
        }
    }
}

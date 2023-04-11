namespace ImplantedDeviceService.Services
{
    public class MyPoint
    {
        public MyPoint () { }
        public MyPoint (double x, double y)
        {
            X = x;
            Y = y;
        }
        public double X { get; set; }
        public double Y { get; set; }
    }
}

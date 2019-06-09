
def class GregorianCalendarDemo {

    private GregorianCalendar cal;

    public GregorianCalendarDemo() {
        cal = new GregorianCalendar(TimeZone.getDefault(), Locale.getDefault());
        // discard time of day so we only have the date
        cal.set(Calendar.HOUR_OF_DAY, cal.getActualMinimum(Calendar.HOUR_OF_DAY));
        cal.set(Calendar.MINUTE, cal.getActualMinimum(Calendar.MINUTE));
        cal.set(Calendar.SECOND, cal.getActualMinimum(Calendar.SECOND));
        cal.set(Calendar.MILLISECOND, cal.getActualMinimum(Calendar.MILLISECOND));
    }

    protected GregorianCalendar getCal() {
        return cal;
    }

    public String getFormattedCal() {
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        return format.format(getCal().getTime());
    }
}
"""
Date and time utility functions.
"""

from datetime import datetime, timedelta, date
from typing import Optional, Tuple
import calendar


def current_timestamp() -> str:
    """
    Get current timestamp as string.
    
    Returns:
        str: Current timestamp in ISO format
        
    Example:
        >>> current_timestamp()
        '2025-08-10T14:30:45.123456'
    """
    return datetime.now().isoformat()


def format_datetime(dt: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format datetime object to string.
    
    Args:
        dt (datetime): Datetime object to format
        format_string (str): Format string (default: "%Y-%m-%d %H:%M:%S")
        
    Returns:
        str: Formatted datetime string
        
    Example:
        >>> dt = datetime(2025, 8, 10, 14, 30, 45)
        >>> format_datetime(dt)
        '2025-08-10 14:30:45'
    """
    return dt.strftime(format_string)


def parse_datetime(date_string: str, format_string: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse string to datetime object.
    
    Args:
        date_string (str): Date string to parse
        format_string (str): Format string (default: "%Y-%m-%d %H:%M:%S")
        
    Returns:
        datetime: Parsed datetime object
        
    Example:
        >>> parse_datetime('2025-08-10 14:30:45')
        datetime.datetime(2025, 8, 10, 14, 30, 45)
    """
    return datetime.strptime(date_string, format_string)


def add_days(dt: datetime, days: int) -> datetime:
    """
    Add days to a datetime object.
    
    Args:
        dt (datetime): Base datetime
        days (int): Number of days to add (can be negative)
        
    Returns:
        datetime: New datetime with days added
        
    Example:
        >>> dt = datetime(2025, 8, 10)
        >>> add_days(dt, 5)
        datetime.datetime(2025, 8, 15, 0, 0)
    """
    return dt + timedelta(days=days)


def add_hours(dt: datetime, hours: int) -> datetime:
    """
    Add hours to a datetime object.
    
    Args:
        dt (datetime): Base datetime
        hours (int): Number of hours to add (can be negative)
        
    Returns:
        datetime: New datetime with hours added
        
    Example:
        >>> dt = datetime(2025, 8, 10, 12, 0)
        >>> add_hours(dt, 6)
        datetime.datetime(2025, 8, 10, 18, 0)
    """
    return dt + timedelta(hours=hours)


def days_between(date1: datetime, date2: datetime) -> int:
    """
    Calculate number of days between two dates.
    
    Args:
        date1 (datetime): First date
        date2 (datetime): Second date
        
    Returns:
        int: Number of days between dates (positive if date2 > date1)
        
    Example:
        >>> date1 = datetime(2025, 8, 10)
        >>> date2 = datetime(2025, 8, 15)
        >>> days_between(date1, date2)
        5
    """
    return (date2 - date1).days


def is_weekend(dt: datetime) -> bool:
    """
    Check if a date falls on weekend (Saturday or Sunday).
    
    Args:
        dt (datetime): Date to check
        
    Returns:
        bool: True if weekend, False otherwise
        
    Example:
        >>> dt = datetime(2025, 8, 10)  # Sunday
        >>> is_weekend(dt)
        True
    """
    return dt.weekday() >= 5


def get_weekday_name(dt: datetime) -> str:
    """
    Get the name of the weekday.
    
    Args:
        dt (datetime): Date to get weekday for
        
    Returns:
        str: Weekday name
        
    Example:
        >>> dt = datetime(2025, 8, 10)  # Sunday
        >>> get_weekday_name(dt)
        'Sunday'
    """
    return dt.strftime('%A')


def get_month_name(dt: datetime) -> str:
    """
    Get the name of the month.
    
    Args:
        dt (datetime): Date to get month for
        
    Returns:
        str: Month name
        
    Example:
        >>> dt = datetime(2025, 8, 10)
        >>> get_month_name(dt)
        'August'
    """
    return dt.strftime('%B')


def get_quarter(dt: datetime) -> int:
    """
    Get the quarter of the year (1-4).
    
    Args:
        dt (datetime): Date to get quarter for
        
    Returns:
        int: Quarter number (1-4)
        
    Example:
        >>> dt = datetime(2025, 8, 10)
        >>> get_quarter(dt)
        3
    """
    return (dt.month - 1) // 3 + 1


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    
    Args:
        year (int): Year to check
        
    Returns:
        bool: True if leap year, False otherwise
        
    Example:
        >>> is_leap_year(2024)
        True
    """
    return calendar.isleap(year)


def get_days_in_month(year: int, month: int) -> int:
    """
    Get number of days in a specific month and year.
    
    Args:
        year (int): Year
        month (int): Month (1-12)
        
    Returns:
        int: Number of days in the month
        
    Example:
        >>> get_days_in_month(2025, 2)
        28
    """
    return calendar.monthrange(year, month)[1]


def age_in_years(birth_date: date, reference_date: Optional[date] = None) -> int:
    """
    Calculate age in years from birth date.
    
    Args:
        birth_date (date): Birth date
        reference_date (Optional[date]): Reference date (default: today)
        
    Returns:
        int: Age in years
        
    Example:
        >>> birth = date(1990, 8, 10)
        >>> age_in_years(birth)
        35
    """
    if reference_date is None:
        reference_date = date.today()
    
    age = reference_date.year - birth_date.year
    if reference_date.month < birth_date.month or \
       (reference_date.month == birth_date.month and reference_date.day < birth_date.day):
        age -= 1
    return age


def time_until(target_datetime: datetime) -> Tuple[int, int, int, int]:
    """
    Calculate time remaining until target datetime.
    
    Args:
        target_datetime (datetime): Target datetime
        
    Returns:
        Tuple[int, int, int, int]: (days, hours, minutes, seconds) remaining
        
    Example:
        >>> target = datetime.now() + timedelta(days=1, hours=2, minutes=30)
        >>> time_until(target)
        (1, 2, 30, 0)
    """
    now = datetime.now()
    if target_datetime <= now:
        return (0, 0, 0, 0)
    
    diff = target_datetime - now
    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return (days, hours, minutes, seconds)
